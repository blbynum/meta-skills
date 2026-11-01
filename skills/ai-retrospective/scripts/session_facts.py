#!/usr/bin/env python3
"""Extract an evidence table from a Claude Code session transcript (JSONL).

Turns a multi-hundred-kilobyte transcript into a compact ledger the model can
read: user turns, per-message tool calls (which shows parallelism), repeats,
failures, subagent launches, and skill invocations.

Every printed line carries a turn index so findings can cite it.

Usage:
    session_facts.py --session-id UUID     # preferred: exact
    session_facts.py --contains "phrase"   # pick the transcript holding a phrase
    session_facts.py --session-file PATH
    session_facts.py                       # newest by mtime — unreliable when
                                           # several sessions run at once
    session_facts.py --cwd /some/project   # resolve by another project dir
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

PROJECTS_DIR = os.path.expanduser("~/.claude/projects")

# Truncation widths. Long enough to identify a call or a correction on sight,
# short enough that a 500-call session still fits in a few thousand tokens.
ARG_WIDTH = 110
USER_WIDTH = 300

# Tool inputs whose value identifies the call. First match wins.
IDENTIFYING_ARGS = (
    "file_path", "command", "url", "pattern", "path", "query",
    "notebook_path", "skill", "description", "prompt",
)


def resolve_transcript(args):
    """Return (path, note). Raise SystemExit with a usable message on failure."""
    if args.session_file:
        p = os.path.expanduser(args.session_file)
        if not os.path.isfile(p):
            sys.exit(f"No transcript at {p}")
        return p, "explicit --session-file"

    cwd = os.path.abspath(os.path.expanduser(args.cwd or os.getcwd()))
    slug = re.sub(r"[^a-zA-Z0-9]", "-", cwd)
    proj = os.path.join(PROJECTS_DIR, slug)

    if args.session_id:
        p = os.path.join(proj, f"{args.session_id}.jsonl")
        if os.path.isfile(p):
            return p, "matched --session-id"
        hits = []
        if os.path.isdir(PROJECTS_DIR):
            for d in os.listdir(PROJECTS_DIR):
                cand = os.path.join(PROJECTS_DIR, d, f"{args.session_id}.jsonl")
                if os.path.isfile(cand):
                    hits.append(cand)
        if len(hits) == 1:
            return hits[0], "matched --session-id in another project dir"
        sys.exit(
            f"No transcript {args.session_id}.jsonl under {proj}"
            + (f" or elsewhere in {PROJECTS_DIR}" if not hits else "")
        )

    if not os.path.isdir(proj):
        sys.exit(
            f"No transcript directory {proj}.\n"
            f"The working directory {cwd} may not match the session's cwd. "
            f"Pass --cwd or --session-file."
        )
    files = [os.path.join(proj, f) for f in os.listdir(proj) if f.endswith(".jsonl")]
    if not files:
        sys.exit(f"No .jsonl transcripts in {proj}")

    if args.contains:
        needle = args.contains.lower()
        hits = []
        for p in files:
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read().lower():
                    hits.append(p)
        if not hits:
            sys.exit(
                f"No transcript in {proj} contains {args.contains!r}. "
                f"Try a shorter, more distinctive phrase, or pass --session-id."
            )
        newest = max(hits, key=os.path.getmtime)
        note = f"contains {args.contains!r}"
        if len(hits) > 1:
            note += f" (in {len(hits)} transcripts; took the newest)"
        return newest, note

    newest = max(files, key=os.path.getmtime)
    return newest, (
        "WARNING newest by mtime. Another session writing concurrently would win "
        "this race. Confirm the session id below, or rerun with --session-id."
    )


def load(path):
    records, bad = [], 0
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                bad += 1
    return records, bad


def clip(text, width):
    text = " ".join(str(text).split())
    return text if len(text) <= width else text[: width - 1] + "…"


def blocks(rec):
    content = (rec.get("message") or {}).get("content")
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return []


def identifying_arg(tool_input):
    if not isinstance(tool_input, dict):
        return ""
    for key in IDENTIFYING_ARGS:
        if key in tool_input:
            return f"{key}={clip(tool_input[key], ARG_WIDTH)}"
    return clip(json.dumps(tool_input), ARG_WIDTH)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--session-id")
    ap.add_argument("--session-file")
    ap.add_argument("--cwd")
    ap.add_argument(
        "--contains",
        help="distinctive phrase from this session; picks the transcript holding it",
    )
    args = ap.parse_args()

    path, note = resolve_transcript(args)
    records, bad = load(path)
    if not records:
        sys.exit(f"{path} holds no readable records.")

    # --- header ------------------------------------------------------------
    meta = defaultdict(set)
    stamps = []
    for r in records:
        for key in ("sessionId", "cwd", "gitBranch", "version", "permissionMode", "effort"):
            if r.get(key):
                meta[key].add(str(r[key]))
        model = (r.get("message") or {}).get("model")
        if model:
            meta["model"].add(model)
        if r.get("timestamp"):
            stamps.append(r["timestamp"])

    print("=" * 72)
    print(f"transcript : {path}")
    print(f"resolved by: {note}")
    for key in ("sessionId", "model", "version", "cwd", "gitBranch", "permissionMode", "effort"):
        if meta.get(key):
            print(f"{key:11}: {', '.join(sorted(meta[key]))}")
    if stamps:
        print(f"span       : {min(stamps)} -> {max(stamps)}")
    print(f"records    : {len(records)}" + (f"  ({bad} unparseable lines)" if bad else ""))

    # --- context continuity ------------------------------------------------
    # A summarized session loses the raw early turns from context but usually
    # keeps them here. Report anything that looks like a summary boundary.
    marks = []
    for i, r in enumerate(records):
        raw = json.dumps(r).replace(" ", "")
        if r.get("type") == "summary" or '"isCompactSummary":true' in raw:
            marks.append((i, r.get("type", "summary"), clip(raw, 120)))
    print("\n-- context continuity --")
    if marks:
        for i, kind, sample in marks:
            print(f"  rec {i}: {kind} {sample}")
        print("  A summary boundary exists. The transcript below still holds the raw")
        print("  turns, but say so in the report: your in-context memory of the early")
        print("  session was replaced by a summary.")
    else:
        print("  No summary or compaction record found in this file.")
        print("  Cross-check: does the first user turn below match what you remember")
        print("  as the opening prompt? If not, context was summarized anyway.")

    sidechain = sum(1 for r in records if r.get("isSidechain"))
    print(f"  sidechain (subagent) records in this file: {sidechain}")

    # --- turns and tool calls ---------------------------------------------
    print("\n-- user turns --")
    print("  (idx = record index; use it to cite evidence)")
    for i, r in enumerate(records):
        if r.get("type") != "user" or r.get("isMeta") or r.get("isSidechain"):
            continue
        text = " ".join(
            b.get("text", "") for b in blocks(r) if b.get("type") == "text"
        ).strip()
        if not text:
            continue  # tool_result-only turn; covered by the tool ledger
        flag = " <== RETROSPECTIVE INVOCATION" if "ai-retrospective" in text else ""
        print(f"  [{i}] {r.get('timestamp','')} {clip(text, USER_WIDTH)}{flag}")

    tool_names = Counter()
    # One assistant message can span several JSONL records — the transcript
    # writes one record per content block. Group by message id so that tools
    # issued together are counted as the parallel batch they were.
    batches = {}              # msg id -> [idx, timestamp, [(name, arg)]]
    by_id = {}                # tool_use id -> (idx, name, arg)
    read_targets = Counter()
    bash_commands = Counter()
    agents, skills, failures = [], [], []

    for i, r in enumerate(records):
        if r.get("type") != "assistant":
            continue
        msg = r.get("message") or {}
        key = msg.get("id") or r.get("requestId") or f"rec{i}"
        entry = batches.setdefault(key, [i, r.get("timestamp", ""), []])
        calls = entry[2]
        for b in blocks(r):
            if b.get("type") != "tool_use":
                continue
            name = b.get("name", "?")
            arg = identifying_arg(b.get("input"))
            tool_names[name] += 1
            calls.append((name, arg))
            by_id[b.get("id")] = (i, name, arg)
            tin = b.get("input") if isinstance(b.get("input"), dict) else {}
            if name in ("Read", "Edit", "Write") and tin.get("file_path"):
                read_targets[(name, tin["file_path"])] += 1
            if name == "Bash" and tin.get("command"):
                bash_commands[clip(tin["command"], ARG_WIDTH)] += 1
            if name == "Agent":
                agents.append((i, tin.get("subagent_type", "general-purpose"),
                               tin.get("description", ""),
                               len(str(tin.get("prompt", ""))),
                               bool(tin.get("run_in_background"))))
            if name == "Skill":
                skills.append((i, tin.get("skill", "?"), clip(tin.get("args", ""), 60)))

    per_message = [tuple(v) for v in batches.values() if v[2]]

    for i, r in enumerate(records):
        for b in blocks(r):
            if b.get("type") == "tool_result" and b.get("is_error"):
                src = by_id.get(b.get("tool_use_id"), ("?", "?", ""))
                body = b.get("content")
                if isinstance(body, list):
                    body = " ".join(x.get("text", "") for x in body if isinstance(x, dict))
                failures.append((src[0], src[1], src[2], clip(body, ARG_WIDTH)))

    print("\n-- tool calls, in order --")
    print("  One line per assistant message. Several tools on one line ran in parallel.")
    for i, ts, calls in per_message:
        head = f"  [{i}] {ts[11:19] if len(ts) > 19 else ts}"
        if len(calls) == 1:
            print(f"{head} {calls[0][0]}({calls[0][1]})")
        else:
            print(f"{head} PARALLEL x{len(calls)}:")
            for name, arg in calls:
                print(f"        {name}({arg})")

    total_calls = sum(tool_names.values())
    solo = sum(1 for _, _, c in per_message if len(c) == 1)
    print("\n-- aggregates --")
    print(f"  tool calls: {total_calls} across {len(per_message)} assistant messages")
    print(f"  single-call messages: {solo}/{len(per_message)}")
    print("  A high single-call ratio is only a lead. Check whether those calls were")
    print("  actually independent — sequential calls that fed each other are correct.")
    print(f"  by tool: {', '.join(f'{n}={c}' for n, c in tool_names.most_common())}")

    repeats = [(k, c) for k, c in read_targets.items() if c > 1]
    print("\n-- repeated file access (same path, more than once) --")
    if repeats:
        for (name, p), c in sorted(repeats, key=lambda x: -x[1]):
            print(f"  {c}x {name} {p}")
    else:
        print("  none")

    dup_bash = [(k, c) for k, c in bash_commands.items() if c > 1]
    print("\n-- repeated identical shell commands --")
    if dup_bash:
        for cmd, c in sorted(dup_bash, key=lambda x: -x[1]):
            print(f"  {c}x {cmd}")
    else:
        print("  none")

    print("\n-- failed tool calls --")
    if failures:
        for idx, name, arg, err in failures:
            print(f"  [{idx}] {name}({arg}) -> {err}")
    else:
        print("  none")

    print("\n-- subagents --")
    if agents:
        for idx, kind, desc, plen, bg in agents:
            print(f"  [{idx}] {kind} bg={bg} prompt_chars={plen} desc={desc}")
        print("  Check each result was used: search the later transcript for its findings.")
    else:
        print("  none spawned")

    print("\n-- skill invocations --")
    if skills:
        for idx, name, sargs in skills:
            print(f"  [{idx}] {name} {sargs}")
    else:
        print("  none")
    print("=" * 72)


if __name__ == "__main__":
    main()
