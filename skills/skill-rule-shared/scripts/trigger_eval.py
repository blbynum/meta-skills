#!/usr/bin/env python3
"""Measure how often a skill actually loads for a set of queries.

Execute this script; do not read it as reference. A skill that never loads
delivers nothing, and the description is the only thing that decides. This
measures that decision instead of assuming it.

Each query runs `claude -p` in a scratch directory and watches the event
stream for the skill being invoked. Queries marked should_trigger:false are
near-misses: they measure the opposite failure, a description that steals
work from other skills.

What counts as a trigger: a Skill tool call whose `skill` field equals the
name under test exactly, or a tool call whose input names the path
`<skill>/SKILL.md` as a whole path segment. A query that merely mentions the
skill's name in its arguments does not count.

Every result carries the Claude Code version and the model the session
resolved to (both from the `init` event), the plugins that were loaded, and
the cost of each run — the confounds evaluating.md says to record.

Eval set format (JSON list):

  [{"query": "the prompt a user would type", "should_trigger": true}, ...]

Usage:

  python3 trigger_eval.py --skill <name> --eval-set queries.json
  python3 trigger_eval.py --skill <name> --eval-set queries.json --model haiku
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from statistics import mean

# Non-determinism means one run per query measures noise. Three runs is the
# smallest number that distinguishes "always", "sometimes", and "never".
DEFAULT_RUNS = 3

# A query passes when it triggers more often than not. Anything nearer the
# middle is a coin flip and should be reported as one, not rounded away.
DEFAULT_THRESHOLD = 0.5

# Trigger decisions happen in the first seconds. This ceiling stops a run
# that went on to do the whole task from costing minutes.
DEFAULT_TIMEOUT_S = 180

# Each run pays for a full system prompt, so cost is dominated by run count.
# This ceiling is per run and stops a runaway agent, not normal work.
DEFAULT_BUDGET_USD = 0.50

# dontAsk denies every call that would open a permission prompt, so the agent
# cannot edit anything, while the Skill tool itself still runs. Plan mode
# would also protect the filesystem but changes how the model opens a task,
# which is the behavior being measured.
PERMISSION_MODE = "dontAsk"


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
    """Match `<skill>/SKILL.md` as a whole path segment, not a substring.

    `foo/SKILL.md` must not match `barfoo/SKILL.md`; the character before
    the name has to be a path separator, whitespace, a quote, or the start of
    the string, and the path has to end at SKILL.md.
    """
    return re.compile(
        rf"(?:^|[/\s\"'`=]){re.escape(skill)}/SKILL\.md(?:$|[\s\"'`|;)])")


def detect_trigger(events, skill: str) -> bool:
    """Return True if the event stream shows the skill being loaded.

    Two paths count: the Skill tool invoked with exactly this skill name, and
    a tool call whose input names this skill's SKILL.md path. Both mean the
    skill's body reached the context.
    """
    path_re = skill_md_pattern(skill)
    for event in events:
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if block.get("type") != "tool_use":
                continue
            name = block.get("name", "")
            payload = block.get("input", {}) or {}
            if name == "Skill":
                requested = str(payload.get("skill", "")).strip()
                # Plugin skills are invoked as "plugin:name"; a personal skill
                # under test must match its bare name exactly.
                if requested == skill or requested.endswith(f":{skill}"):
                    return True
                continue
            for value in payload.values():
                if isinstance(value, str) and path_re.search(value):
                    return True
    return False


def parse_run(stream: str, skill: str) -> dict:
    """Extract the trigger verdict and the run's provenance and cost."""
    events = list(iter_events(stream))
    info = {"triggered": detect_trigger(events, skill), "cost_usd": None,
            "claude_code_version": None, "model": None, "plugins": None,
            "skill_listed": None, "is_error": None}
    for event in events:
        if event.get("type") == "system" and event.get("subtype") == "init":
            info["claude_code_version"] = event.get("claude_code_version")
            info["model"] = event.get("model")
            info["plugins"] = [p.get("source") or p.get("name")
                               for p in event.get("plugins") or []]
            listed = event.get("skills")
            if isinstance(listed, list):
                info["skill_listed"] = skill in listed
        elif event.get("type") == "result":
            info["cost_usd"] = event.get("total_cost_usd")
            info["is_error"] = event.get("is_error")
    return info


def other_skills_invoked(stream: str) -> list[str]:
    """Every Skill tool target the run invoked, for collision reporting."""
    names = []
    for event in iter_events(stream):
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if block.get("type") == "tool_use" and block.get("name") == "Skill":
                names.append(str((block.get("input") or {}).get("skill", "")))
    return names


def run_once(query: str, skill: str, model: str | None, timeout: int,
             budget: float, save_dir: Path | None = None,
             tag: str = "", effort: str | None = None) -> dict | None:
    """Run one query. Returns the parsed run; None when the run failed."""
    cmd = [
        "claude", "-p", query,
        "--output-format", "stream-json",
        "--verbose",
        "--permission-mode", PERMISSION_MODE,
        "--max-budget-usd", str(budget),
    ]
    if model:
        cmd += ["--model", model]
    if effort:
        cmd += ["--effort", effort]

    # A scratch cwd keeps project CLAUDE.md and project skills out of the
    # measurement, so the result describes the skill under test.
    with tempfile.TemporaryDirectory(prefix="trigger-eval-") as workdir:
        try:
            done = subprocess.run(
                cmd, cwd=workdir, capture_output=True, text=True,
                timeout=timeout, stdin=subprocess.DEVNULL,
            )
        except subprocess.TimeoutExpired as expired:
            partial = expired.stdout or ""
            if isinstance(partial, bytes):
                partial = partial.decode("utf-8", errors="replace")
            if save_dir:
                (save_dir / f"{tag}.jsonl").write_text(partial)
            info = parse_run(partial, skill)
            info["skills_invoked"] = other_skills_invoked(partial)
            # A run that hit the ceiling still counts if it already triggered.
            return info if info["triggered"] else None
        if save_dir:
            (save_dir / f"{tag}.jsonl").write_text(done.stdout)
        if done.returncode != 0 and not done.stdout:
            print(f"  run failed: {done.stderr.strip()[:200]}", file=sys.stderr)
            return None
        info = parse_run(done.stdout, skill)
        info["skills_invoked"] = other_skills_invoked(done.stdout)
        # An API error (for example 529 Overloaded) ends the run before the
        # model could decide anything; it is a failed run, not a non-trigger.
        if info["is_error"] and not info["triggered"]:
            print("  run failed: API error before a trigger decision",
                  file=sys.stderr)
            return None
        return info


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", required=True,
                        help="Skill directory name, as it appears in the path")
    parser.add_argument("--eval-set", required=True, type=Path)
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--effort", default=None,
                        help="Effort level passed to claude -p "
                             "(low, medium, high, xhigh, max)")
    parser.add_argument("--model", default=None,
                        help="Model alias or id; omit for the configured default")
    parser.add_argument("--workers", type=int, default=4,
                        help="Queries run concurrently; each is a full session")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    parser.add_argument("--budget", type=float, default=DEFAULT_BUDGET_USD)
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--json", type=Path, default=None,
                        help="Write full results here as well as stdout")
    parser.add_argument("--save-transcripts", type=Path, default=None,
                        help="Directory to keep every run's event stream, "
                             "for reading which skills competed for a query")
    args = parser.parse_args()
    if args.save_transcripts:
        args.save_transcripts.mkdir(parents=True, exist_ok=True)

    if not args.eval_set.exists():
        print(f"Eval set not found: {args.eval_set}", file=sys.stderr)
        return 1
    eval_set = json.loads(args.eval_set.read_text())
    for item in eval_set:
        if "query" not in item or "should_trigger" not in item:
            print("Every entry needs 'query' and 'should_trigger'", file=sys.stderr)
            return 1

    jobs = [(item, run, idx) for idx, item in enumerate(eval_set)
            for run in range(args.runs)]
    print(f"Running {len(jobs)} sessions "
          f"({len(eval_set)} queries x {args.runs} runs)...", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        outcomes = list(pool.map(
            lambda job: run_once(job[0]["query"], args.skill, args.model,
                                 args.timeout, args.budget,
                                 args.save_transcripts,
                                 f"q{job[2] + 1}-run{job[1] + 1}",
                                 args.effort),
            jobs,
        ))

    by_query: dict[str, list[dict | None]] = {}
    for (item, _, _), outcome in zip(jobs, outcomes):
        by_query.setdefault(item["query"], []).append(outcome)

    results = []
    for item in eval_set:
        outcomes = by_query[item["query"]]
        usable = [o for o in outcomes if o is not None]
        rate = mean(o["triggered"] for o in usable) if usable else 0.0
        passed = (rate >= args.threshold) if item["should_trigger"] \
            else (rate < args.threshold)
        costs = [o["cost_usd"] for o in usable if o["cost_usd"] is not None]
        competitors = sorted({s for o in usable
                              for s in o.get("skills_invoked", [])
                              if s and s != args.skill
                              and not s.endswith(f":{args.skill}")})
        results.append({
            "query": item["query"],
            "should_trigger": item["should_trigger"],
            "trigger_rate": rate,
            "runs": len(outcomes),
            "failed_runs": len(outcomes) - len(usable),
            "cost_usd_mean": mean(costs) if costs else None,
            "other_skills_invoked": competitors,
            "pass": passed,
        })

    usable_all = [o for o in outcomes if o is not None]
    versions = sorted({o["claude_code_version"] for o in usable_all
                       if o["claude_code_version"]})
    models = sorted({o["model"] for o in usable_all if o["model"]})
    plugins = sorted({p for o in usable_all for p in (o["plugins"] or [])})
    listed = [o["skill_listed"] for o in usable_all
              if o["skill_listed"] is not None]
    total_cost = sum(o["cost_usd"] for o in usable_all
                     if o["cost_usd"] is not None)

    wanted = [r for r in results if r["should_trigger"]]
    unwanted = [r for r in results if not r["should_trigger"]]
    summary = {
        "skill": args.skill,
        "model_requested": args.model or "default",
        "effort_requested": args.effort or "default",
        "model": models[0] if len(models) == 1 else models,
        "claude_code_version": versions[0] if len(versions) == 1 else versions,
        "plugins_loaded": plugins,
        "skill_listed_in_roster": (all(listed) if listed else None),
        "runs_per_query": args.runs,
        "passed": sum(1 for r in results if r["pass"]),
        "total": len(results),
        "recall": mean([r["trigger_rate"] for r in wanted]) if wanted else None,
        "false_positive_rate":
            mean([r["trigger_rate"] for r in unwanted]) if unwanted else None,
        "total_cost_usd": round(total_cost, 4),
    }

    for r in results:
        mark = "PASS" if r["pass"] else "FAIL"
        want = "should" if r["should_trigger"] else "should NOT"
        note = f" ({r['failed_runs']} runs failed)" if r["failed_runs"] else ""
        if r["other_skills_invoked"]:
            note += f" [also invoked: {', '.join(r['other_skills_invoked'])}]"
        print(f"[{mark}] rate={r['trigger_rate']:.2f} {want} trigger"
              f"{note}: {r['query'][:70]}")
    print(f"\n{summary['passed']}/{summary['total']} queries pass.")
    if summary["recall"] is not None:
        print(f"Trigger rate on should-trigger queries: {summary['recall']:.2f}")
    if summary["false_positive_rate"] is not None:
        print("Trigger rate on near-misses: "
              f"{summary['false_positive_rate']:.2f}")
    print(f"Claude Code {summary['claude_code_version']} | model "
          f"{summary['model']} | plugins {summary['plugins_loaded'] or 'none'}"
          f" | total cost ${summary['total_cost_usd']:.2f}")
    if summary["skill_listed_in_roster"] is False:
        print(f"WARNING: '{args.skill}' was not in the session's skill roster; "
              "the rates above measure nothing.", file=sys.stderr)

    if args.json:
        args.json.write_text(json.dumps(
            {"summary": summary, "results": results}, indent=2))
        print(f"Wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
