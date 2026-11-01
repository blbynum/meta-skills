#!/usr/bin/env python3
"""Mechanical checks over ab_eval.py run outputs for the /goal evals.

Usage: python3 -I check_goal_outputs.py <eval-run dir>
Prints one row per run: eval, arm, run, cost, and the observable signals.
Judgment calls (faithfulness, invented requirements) stay with the grader.
"""
import json, re, sys
from pathlib import Path

FENCE_RE = re.compile(r"^(`{3,4})[^\n]*\n(.*?)^\1\s*$", re.S | re.M)

def fenced_blocks(text):
    return [m.group(2) for m in FENCE_RE.finditer(text)]

def first_line(block):
    for line in block.splitlines():
        if line.strip():
            return line.strip()
    return ""

def signals(text):
    blocks = fenced_blocks(text)
    goal_blocks = [b for b in blocks if first_line(b).startswith("/goal")]
    prompt_words = len(blocks[0].split()) if blocks else 0
    low = text.lower()
    return {
        "blocks": len(blocks),
        "goal_led": len(goal_blocks),
        "goal_mentions": len(re.findall(r"/goal", text)),
        "auto_mode": bool(re.search(r"auto mode|auto-mode|permission mode|permission-mode|permission settings|permissions", low)),
        "bound": bool(re.search(r"stop after \d+|after \d+ (turns?|minutes|hours)|within \d+ (turns?|minutes|hours)|(turn|time) (limit|bound|clause|cap)|\d+ turns", low)),
        "first_cmd": bool(re.search(r"first slash|only the first|only one slash|one slash command|as (its |the )?argument|argument text|treated .{0,40}as (its |the )?argument", low)),
        "poor_fit": bool(re.search(r"(poor|bad|not a good|isn.t a good|is not a good|wrong) fit|does not fit|doesn.t fit|not (well )?suited|cannot wait|can.t wait|won.t wait|instead of waiting|rather than wait", low)),
        "split": bool(re.search(r"split|two (prompts|steps|messages|parts|phases)|then (set|run|start) (a |the )?/?goal|after (the |your )?approval|once (you|the draft)", low)),
        "research_skill_prose": bool(re.search(r"(use|using|load|invoke|run) the (/?research|research) skill", low)),
        "second_slash": bool(re.search(r"/goal[^\n]{0,40}/research", text)),
        "first_block_words": prompt_words,
    }

def main(root):
    root = Path(root)
    rows = []
    for metrics in sorted(root.glob("*/*/run-*/metrics.json")):
        run_dir = metrics.parent
        out = run_dir / "output.md"
        text = out.read_text(encoding="utf-8") if out.exists() else ""
        m = json.loads(metrics.read_text())
        row = {"eval": run_dir.parts[-3], "arm": run_dir.parts[-2], "run": run_dir.name,
               "cost": m.get("cost_usd"), "turns": m.get("num_turns"),
               "loaded": m.get("artifact_loaded"), "err": m.get("is_error")}
        row.update(signals(text))
        rows.append(row)
    keys = ["eval", "arm", "run", "cost", "turns", "loaded", "err", "blocks", "goal_led",
            "goal_mentions", "auto_mode", "bound", "first_cmd", "poor_fit", "split",
            "research_skill_prose", "second_slash", "first_block_words"]
    print("\t".join(keys))
    for r in rows:
        print("\t".join(str(r.get(k, "")) for k in keys))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    main(sys.argv[1])
