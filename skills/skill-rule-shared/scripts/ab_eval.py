#!/usr/bin/env python3
"""Run an A/B evaluation of a skill or a rule against a baseline.

Execute this script; do not read it as reference. It runs each task prompt
in two arms — with the artifact and without it, or old version and new
version — several times per arm, and saves the outputs, the full
transcripts, and the cost of each run. It does not grade: judging
expected_behavior needs judgment, so grading stays with the agent, which
reads the outputs this script leaves behind.

The baseline is what makes the numbers mean anything. Without it, an artifact
that changes nothing looks identical to one that works.

How each arm is built:

  --mode skill   with: the normal session. without: the same session with
                 only the skill under test removed — `skillOverrides` sets it
                 "off" through --settings, and --disallowed-tools blocks a
                 direct Skill(<name>) call. Every other skill, rule, plugin,
                 and hook stays loaded in both arms, so the comparison
                 isolates one artifact. (An older version disabled all skills
                 in the baseline, which measured "everything versus nothing".)
                 The with-arm transcript is checked for the skill actually
                 loading; a run where it did not is flagged, because a
                 with-arm that never loaded the artifact is a baseline run.
  --mode rule    both arms start from --safe-mode, which loads no CLAUDE.md,
                 skills, plugins, or hooks. The with arm adds the rule text
                 through --append-system-prompt, with the YAML frontmatter and
                 HTML comments stripped as Claude Code strips them. This is an
                 approximation: a real rule reaches the model as a
                 <system-reminder> block in the user turn, not as system-prompt
                 text, and a real session carries the user's other rules and
                 skills. A rule that competes with other loaded rules will
                 look better here than in practice.
  --old / --new  compare two versions of the same artifact instead of
                 artifact-versus-none. For a rule, each arm appends its
                 version's text (both from --safe-mode). For a skill, each arm
                 runs in a scratch project whose .claude/skills/<name>-<arm>/
                 holds that version (frontmatter `name` rewritten to match),
                 with the personal copy of <name> set "off" so it cannot
                 shadow the project copy — personal skills override project
                 skills of the same name, which is why the copies are
                 renamed. Write old/new queries as the bare task, not as
                 "/<name> ..." invocations.

Every run records the Claude Code version and the model the session resolved
to (both from the `init` event) and the plugins loaded, so results from
different days can be compared or told apart.

Evals file format:

  {
    "artifact": "my-skill",
    "evals": [
      {
        "id": "capture-a-fact",
        "query": "the prompt a user would type",
        "files": ["fixtures/input.md", "fixtures/some-dir"],
        "expected_behavior": ["what a correct run does", "..."]
      }
    ]
  }

Usage:

  python3 ab_eval.py --evals <eval-dir>/evals.json --out <eval-dir>/run --mode skill
  python3 ab_eval.py --evals <eval-dir>/evals.json --out <eval-dir>/run --mode rule \
      --rule-file ~/.claude/rules/<name>.md
  python3 ab_eval.py --evals <eval-dir>/evals.json --out <eval-dir>/run --mode rule \
      --old <eval-dir>/<name>.old.md --new ~/.claude/rules/<name>.md
  python3 ab_eval.py --evals <eval-dir>/evals.json --out <eval-dir>/run --mode skill \
      --old <eval-dir>/SKILL.old.md --new ~/.claude/skills/<name>/SKILL.md

<eval-dir> is a temporary directory outside the artifact's directory and the
repository. Delete it when the pass ends; evaluating.md says why.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from statistics import mean, stdev

# Three runs per arm is the smallest number that separates a real difference
# from run-to-run variance. Raise it when two arms land close together.
DEFAULT_RUNS = 3

# Real tasks are slower than trigger checks: this allows a full working
# session before the run is abandoned.
DEFAULT_TIMEOUT_S = 900

# Per run, not per suite. A suite of 3 evals x 2 arms x 3 runs is 18 runs, so
# the suite ceiling is 18x this number — check it before a large sweep.
DEFAULT_BUDGET_USD = 2.00

# acceptEdits lets the agent finish file-producing work without prompting,
# which a non-interactive run cannot answer. Each run works in its own
# throwaway directory, so the edits stay contained.
PERMISSION_MODE = "acceptEdits"

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->\s*", re.S)


def rule_text(path: Path) -> str:
    """Return the text Claude Code would inject for this rule file.

    Claude Code strips block HTML comments (the last-verified marker) before
    injection, and a rules file's YAML frontmatter (`paths:`) is metadata,
    not content. Injecting either verbatim would test text no session sees.
    """
    text = path.read_text()
    text = FRONTMATTER_RE.sub("", text, count=1)
    return HTML_COMMENT_RE.sub("", text).strip() + "\n"


def iter_events(stream: str):
    for line in stream.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def skill_md_pattern(skill: str) -> re.Pattern:
    return re.compile(
        rf"(?:^|[/\s\"'`=]){re.escape(skill)}/SKILL\.md(?:$|[\s\"'`|;)])")


def detect_loaded(events, skill: str) -> bool:
    """True when the transcript shows the named skill's body reaching context."""
    path_re = skill_md_pattern(skill)
    for event in events:
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if block.get("type") != "tool_use":
                continue
            payload = block.get("input", {}) or {}
            if block.get("name") == "Skill":
                requested = str(payload.get("skill", "")).strip()
                if requested == skill or requested.endswith(f":{skill}"):
                    return True
                continue
            for value in payload.values():
                if isinstance(value, str) and path_re.search(value):
                    return True
    return False


def stage_skill_version(run_dir: Path, name: str, version_file: Path) -> None:
    """Copy one version of a skill into the run's scratch project.

    The copy is a whole-directory copy of the version file's parent when that
    parent is a skill directory (so references/ and scripts/ travel with it),
    or a single SKILL.md otherwise. The frontmatter `name` is rewritten to the
    staged directory name so the listing and the directory agree.
    """
    target = run_dir / ".claude" / "skills" / name
    src_dir = version_file.parent
    if (src_dir / "SKILL.md").exists() and version_file.name == "SKILL.md":
        shutil.copytree(src_dir, target, dirs_exist_ok=True)
        skill_md = target / "SKILL.md"
    else:
        target.mkdir(parents=True, exist_ok=True)
        skill_md = target / "SKILL.md"
        shutil.copy2(version_file, skill_md)
    text = skill_md.read_text()
    text = re.sub(r"^name:\s*.*$", f"name: {name}", text, count=1,
                  flags=re.M)
    skill_md.write_text(text)


def skill_read_rules(skill: str) -> list[str]:
    """Return the Read rules that pre-allow the skill's own directory.

    A skill's reference files live in its own directory, outside the
    throwaway run directory, so reading them prompts for permission and a
    non-interactive run denies it — the with-arm then runs on SKILL.md
    alone (seen 2026-08-19: every reference read in the with-arm returned
    "Claude requested permissions to read"). The rules go to both arms; the
    without-arm never loads the skill, so the grant is inert there.

    A linked skill is read through its symlink path, which a rule for the
    resolved path does not match (seen 2026-11-02 on take-ticket), so a
    linked skill gets a rule for each path. Any other skill gets one rule.
    """
    for root in (Path.home() / ".claude" / "skills",
                 Path.cwd() / ".claude" / "skills"):
        skill_dir = root / skill
        if skill_dir.is_dir():
            # Rule syntax: "//" marks an absolute path, followed by the
            # path without its leading slash — Read(//Users/x/...).
            paths = dict.fromkeys((str(skill_dir), str(skill_dir.resolve())))
            return [f"Read(//{path.lstrip('/')}/**)" for path in paths]
    return []


def build_command(job: dict) -> list[str]:
    cmd = [
        "claude", "-p", job["query"],
        "--output-format", "stream-json",
        "--verbose",
        "--permission-mode", PERMISSION_MODE,
        "--max-budget-usd", str(job["budget"]),
    ]
    if job["model"]:
        cmd += ["--model", job["model"]]
    if job.get("effort"):
        cmd += ["--effort", job["effort"]]
    # Non-interactive runs cannot answer a permission prompt, so a tool that
    # would prompt (WebSearch, WebFetch, Bash) is silently denied. Pass the
    # tools the artifact needs so both arms can actually do the task.
    if job["allowed_tools"]:
        cmd += ["--allowed-tools", *job["allowed_tools"]]

    mode, arm, skill = job["mode"], job["arm"], job["skill"]
    if job["versions"]:
        if mode == "rule":
            cmd.append("--safe-mode")
            cmd += ["--append-system-prompt", rule_text(job["versions"][arm])]
        else:
            # Personal copy off; the arm's renamed project copy is the one
            # that can load. Both copies keep the same description text, so
            # triggering is unchanged; only the body differs between arms.
            overrides = json.dumps({"skillOverrides": {skill: "off"}})
            cmd += ["--settings", overrides]
    elif mode == "skill":
        if arm == "without":
            overrides = json.dumps({"skillOverrides": {skill: "off"}})
            cmd += ["--settings", overrides,
                    "--disallowed-tools", f"Skill({skill})"]
    else:
        cmd.append("--safe-mode")
        if arm == "with":
            cmd += ["--append-system-prompt", rule_text(job["rule_file"])]
    return cmd


def parse_stream(stream: str, loaded_name: str | None) -> dict:
    """Pull the final text, provenance, and cost out of the event stream."""
    metrics = {"result_text": "", "cost_usd": None, "duration_ms": None,
               "num_turns": None, "input_tokens": None, "output_tokens": None,
               "is_error": None, "claude_code_version": None, "model": None,
               "plugins": None, "artifact_loaded": None}
    events = list(iter_events(stream))
    for event in events:
        if event.get("type") == "system" and event.get("subtype") == "init":
            metrics["claude_code_version"] = event.get("claude_code_version")
            metrics["model"] = event.get("model")
            metrics["plugins"] = [p.get("source") or p.get("name")
                                  for p in event.get("plugins") or []]
        elif event.get("type") == "result":
            usage = event.get("usage", {})
            metrics.update({
                "result_text": event.get("result", ""),
                "cost_usd": event.get("total_cost_usd"),
                "duration_ms": event.get("duration_ms"),
                "num_turns": event.get("num_turns"),
                "input_tokens": usage.get("input_tokens"),
                "output_tokens": usage.get("output_tokens"),
                "is_error": event.get("is_error"),
            })
    if loaded_name:
        metrics["artifact_loaded"] = detect_loaded(events, loaded_name)
    return metrics


def run_once(job: dict) -> dict:
    """Run one eval, in one arm, once. Returns that run's metrics."""
    run_dir: Path = job["run_dir"]
    run_dir.mkdir(parents=True, exist_ok=True)

    # Input files are copied in so the agent works on a private copy and the
    # fixtures survive a destructive run. A directory is copied recursively
    # under its own name, so an eval can seed a nested tree (for example a
    # tracker directory an artifact discovers by relative path).
    for source in job["files"]:
        source = Path(source).expanduser()
        if source.is_dir():
            shutil.copytree(source, run_dir / source.name, dirs_exist_ok=True)
        elif source.exists():
            shutil.copy2(source, run_dir / source.name)
        else:
            print(f"  missing input file: {source}", file=sys.stderr)

    # Which skill name, if any, the loaded check should look for in this arm.
    loaded_name = None
    if job["mode"] == "skill":
        if job["versions"]:
            loaded_name = f"{job['skill']}-{job['arm']}"
            stage_skill_version(run_dir, loaded_name,
                                job["versions"][job["arm"]])
        elif job["arm"] == "with":
            loaded_name = job["skill"]

    cmd = build_command(job)
    try:
        done = subprocess.run(cmd, cwd=run_dir, capture_output=True,
                              text=True, timeout=job["timeout"],
                              stdin=subprocess.DEVNULL)
        stream = done.stdout
        timed_out = False
    except subprocess.TimeoutExpired as expired:
        stream = expired.stdout or ""
        if isinstance(stream, bytes):
            stream = stream.decode("utf-8", errors="replace")
        timed_out = True

    (run_dir / "transcript.jsonl").write_text(stream)
    metrics = parse_stream(stream, loaded_name)
    metrics.update({"eval_id": job["eval_id"], "arm": job["arm"],
                    "run": job["run"], "timed_out": timed_out})
    (run_dir / "output.md").write_text(metrics["result_text"])
    (run_dir / "metrics.json").write_text(json.dumps(metrics, indent=2))

    state = "timeout" if timed_out else f"${metrics['cost_usd'] or 0:.2f}"
    flag = ""
    if metrics["is_error"]:
        state = "API error"
        flag = f"  ({metrics['result_text'][:60]!r})"
    elif loaded_name and metrics["artifact_loaded"] is False:
        flag = f"  (WARNING: {loaded_name} did not load)"
    print(f"  {job['eval_id']} [{job['arm']}] run {job['run'] + 1}: {state}"
          f"{flag}", file=sys.stderr)
    return metrics


def summarize(values: list[float | None]) -> dict:
    usable = [v for v in values if v is not None]
    if not usable:
        return {"mean": None, "stdev": None, "n": 0}
    return {
        "mean": mean(usable),
        "stdev": stdev(usable) if len(usable) > 1 else 0.0,
        "n": len(usable),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evals", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--mode", choices=["skill", "rule"], required=True)
    parser.add_argument("--skill", default=None,
                        help="Skill name under test; defaults to the evals "
                             "file's 'artifact' field")
    parser.add_argument("--rule-file", type=Path, default=None,
                        help="Rule file under test; required for --mode rule "
                             "unless --old/--new are given")
    parser.add_argument("--old", type=Path, default=None,
                        help="Old version (rule file, or a SKILL.md) for an "
                             "old-vs-new comparison")
    parser.add_argument("--new", type=Path, default=None,
                        help="New version for an old-vs-new comparison")
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--model", default=None)
    parser.add_argument("--effort", default=None,
                        help="Effort level passed to claude -p "
                             "(low, medium, high, xhigh, max)")
    parser.add_argument("--allowed-tools", nargs="*", default=None,
                        help="Tools to pre-allow in every run, e.g. "
                             "WebSearch WebFetch 'Bash(curl *)'; a "
                             "non-interactive run denies any tool that "
                             "would prompt")
    parser.add_argument("--workers", type=int, default=3,
                        help="Runs in flight at once; each is a full session")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    parser.add_argument("--budget", type=float, default=DEFAULT_BUDGET_USD)
    args = parser.parse_args()

    spec = json.loads(args.evals.read_text())
    evals = spec["evals"]
    fixture_root = args.evals.parent
    skill = args.skill or spec.get("artifact")

    versions = None
    if args.old or args.new:
        if not (args.old and args.new):
            print("--old and --new go together", file=sys.stderr)
            return 1
        versions = {"old": args.old.expanduser(), "new": args.new.expanduser()}
        for label, path in versions.items():
            if not path.exists():
                print(f"--{label} file not found: {path}", file=sys.stderr)
                return 1
        arms = ("old", "new")
    else:
        arms = ("with", "without")
        if args.mode == "rule":
            if not args.rule_file or not args.rule_file.expanduser().exists():
                print("--mode rule needs --rule-file pointing at the rule "
                      "under test, or --old/--new", file=sys.stderr)
                return 1
            args.rule_file = args.rule_file.expanduser()
    if args.mode == "skill" and not skill:
        print("--mode skill needs --skill or an 'artifact' field in the "
              "evals file", file=sys.stderr)
        return 1

    allowed_tools = list(args.allowed_tools or [])
    if args.mode == "skill":
        allowed_tools += skill_read_rules(skill)

    jobs = []
    for item in evals:
        for arm in arms:
            for run in range(args.runs):
                jobs.append({
                    "eval_id": item["id"],
                    "query": item["query"],
                    "files": [fixture_root / f for f in item.get("files", [])],
                    "arm": arm,
                    "run": run,
                    "run_dir": args.out / item["id"] / arm / f"run-{run + 1}",
                    "mode": args.mode,
                    "skill": skill,
                    "rule_file": args.rule_file,
                    "versions": versions,
                    "model": args.model,
                    "effort": args.effort,
                    "allowed_tools": allowed_tools,
                    "timeout": args.timeout,
                    "budget": args.budget,
                })

    print(f"Running {len(jobs)} sessions "
          f"(ceiling ${len(jobs) * args.budget:.2f})...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(run_once, jobs))

    versions_seen = sorted({r["claude_code_version"] for r in results
                            if r["claude_code_version"]})
    models_seen = sorted({r["model"] for r in results if r["model"]})
    plugins_seen = sorted({p for r in results for p in (r["plugins"] or [])})
    summary = {
        "artifact": spec.get("artifact"), "mode": args.mode,
        "comparison": "old-vs-new" if versions else "with-vs-without",
        "model_requested": args.model or "default",
        "effort_requested": args.effort or "default",
        "allowed_tools": allowed_tools,
        "model": models_seen[0] if len(models_seen) == 1 else models_seen,
        "claude_code_version": (versions_seen[0] if len(versions_seen) == 1
                                else versions_seen),
        "plugins_loaded": plugins_seen,
        "runs_per_arm": args.runs, "evals": [],
    }
    for item in evals:
        entry = {"id": item["id"], "query": item["query"],
                 "expected_behavior": item.get("expected_behavior", []),
                 "arms": {}}
        for arm in arms:
            all_runs = [r for r in results
                        if r["eval_id"] == item["id"] and r["arm"] == arm]
            # API-error runs never reached the model; they are counted, not
            # averaged, so a 529 does not read as a cheap fast run.
            runs = [r for r in all_runs if not r["is_error"]]
            loaded = [r["artifact_loaded"] for r in runs
                      if r["artifact_loaded"] is not None]
            entry["arms"][arm] = {
                "cost_usd": summarize([r["cost_usd"] for r in runs]),
                "duration_ms": summarize([r["duration_ms"] for r in runs]),
                "output_tokens": summarize([r["output_tokens"] for r in runs]),
                "num_turns": summarize([r["num_turns"] for r in runs]),
                "timeouts": sum(1 for r in runs if r["timed_out"]),
                "api_errors": sum(1 for r in all_runs if r["is_error"]),
                "artifact_loaded": (f"{sum(loaded)}/{len(loaded)}"
                                    if loaded else None),
            }
        summary["evals"].append(entry)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2))

    lines = [f"# A/B eval: {summary['artifact']}", "",
             f"Mode: {args.mode} ({summary['comparison']}) | "
             f"Model: {summary['model']} | "
             f"Claude Code: {summary['claude_code_version']} | "
             f"Runs per arm: {args.runs}",
             f"Plugins loaded: {', '.join(plugins_seen) or 'none'}", ""]
    for entry in summary["evals"]:
        lines += [f"## {entry['id']}", "", f"> {entry['query']}", "",
                  "| arm | cost $ | duration s | turns ± sd | timeouts "
                  "| API errors | artifact loaded |",
                  "|---|---|---|---|---|---|---|"]
        for arm in arms:
            a = entry["arms"][arm]
            cost, dur, turns = a["cost_usd"], a["duration_ms"], a["num_turns"]
            loaded = a["artifact_loaded"] if a["artifact_loaded"] else "n/a"
            lines.append(
                f"| {arm} "
                f"| {cost['mean']:.3f} ± {cost['stdev']:.3f} "
                f"| {dur['mean'] / 1000:.0f} ± {dur['stdev'] / 1000:.0f} "
                f"| {turns['mean']:.1f} ± {turns['stdev']:.1f} "
                f"| {a['timeouts']} | {a['api_errors']} | {loaded} |"
                if cost["n"] else
                f"| {arm} | no usable runs | | | | {a['api_errors']} | |")
        lines += ["", "Expected behavior to grade against:", ""]
        lines += [f"- {b}" for b in entry["expected_behavior"]]
        lines.append("")
    (args.out / "summary.md").write_text("\n".join(lines))

    print(f"\nWrote {args.out / 'summary.md'} and per-run outputs under "
          f"{args.out}", file=sys.stderr)
    print("Grade the outputs against expected_behavior; the transcripts show "
          "how each run got there.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
