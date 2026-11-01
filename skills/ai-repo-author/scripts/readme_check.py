#!/usr/bin/env python3
"""Check a skills repository's README against the files.

Usage:
  python3 readme_check.py REPO [--readme README.md]

Checks, each against the repository REPO:
  anchors   every [text](#anchor) matches a heading, by GitHub's rule
  fences    every code fence is closed, and every opening fence names a
            language
  links     every relative [text](path) points at a file or directory
  paths     every backticked path whose first part is a top-level entry
            of REPO (skills/..., rules/..., link.sh, ...) exists; a path
            with a <placeholder> is skipped
  table     every skills/<name>/ and rules/<name>.md has a row in the
            README table whose first cell is that path; in a table with a
            column whose header contains "config", the keys in that cell
            match the skill's ## Config table ("none" or a dash: no keys)

Exit status: 0 when every check passes, 1 when one fails, 2 when the
README cannot be read.
Runs on Python 3.9 or later; stdlib only.
"""
from __future__ import annotations

import argparse
import os
import re
import sys


def slug(heading: str, seen: dict[str, int]) -> str:
    s = re.sub(r"[`*_]|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", heading.strip().lower())
    s = re.sub(r"[^\w\- ]", "", s).replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def config_keys(skill_md: str) -> set[str]:
    try:
        text = open(skill_md, encoding="utf-8").read()
    except OSError:
        return set()
    m = re.search(r"^## Config\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    keys = set()
    for line in (m.group(1).split("\n") if m else []):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0].lower() != "key" and not set(cells[0]) <= {"-", ":", " "}:
            keys.add(cells[0].strip("`"))
    return keys


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("repo")
    ap.add_argument("--readme", default="README.md")
    a = ap.parse_args(argv)
    repo = os.path.abspath(os.path.expanduser(a.repo))
    path = os.path.join(repo, a.readme)
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"readme_check: {path}: {e.strerror}", file=sys.stderr)
        return 2
    lines = text.split("\n")
    problems: list[str] = []
    top = set(os.listdir(repo))

    # Headings and fences in one pass, so a "#" inside a fence is not a heading.
    seen: dict[str, int] = {}
    anchors = set()
    fence = ""
    fence_line = 0
    body: list[tuple[int, str]] = []  # lines outside fences
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if m:
            mark = m.group(1)
            if not fence:
                fence, fence_line = mark, i
                if not m.group(2).strip():
                    problems.append(f"fence: line {i} opens a code block with no language")
                continue
            if mark[0] == fence[0] and len(mark) >= len(fence) and not m.group(2).strip():
                fence = ""
                continue
        if fence:
            continue
        body.append((i, line))
        h = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if h:
            anchors.add(slug(h.group(2), seen))
    if fence:
        problems.append(f"fence: the code block opened on line {fence_line} is never closed")

    for i, line in body:
        for m in re.finditer(r"\]\(#([^)\s]+)\)", line):
            if m.group(1) not in anchors:
                problems.append(f"anchor: line {i}: #{m.group(1)} matches no heading")
        for m in re.finditer(r"\]\(([^)\s#]+)(?:#[^)\s]*)?\)", line):
            target = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue  # a URL
            if not os.path.exists(os.path.join(os.path.dirname(path), target)):
                problems.append(f"link: line {i}: {target} does not exist")
        for m in re.finditer(r"`([^`\s]+)`", line):
            tok = m.group(1).rstrip(".,:;")
            if "<" in tok or tok.startswith(("/", "~", "$", "-", "http")):
                continue
            if tok.endswith("config.local.yaml"):
                continue  # per-machine and ignored by git: absent from a clone by design
            tok = tok[2:] if tok.startswith("./") else tok
            first = tok.split("/")[0]
            if first in top and first not in (".git",) and ("/" in tok or os.path.exists(os.path.join(repo, first))):
                if not os.path.exists(os.path.join(repo, tok.rstrip("/"))):
                    problems.append(f"path: line {i}: {tok} does not exist")

    # The table of what is here.
    rows: dict[str, tuple[int, list[str], int]] = {}
    header: list[str] = []
    for i, line in body:
        if not line.strip().startswith("|"):
            header = []
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not header:
            header = cells
            continue
        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue
        first = cells[0].strip("`").rstrip("/")
        cfg = next((j for j, h in enumerate(header) if "config" in h.lower()), -1)
        rows[first] = (i, cells, cfg)
    entries = []
    for d, kind in (("skills", "dir"), ("rules", "md")):
        p = os.path.join(repo, d)
        if not os.path.isdir(p):
            continue
        for e in sorted(os.listdir(p)):
            if e.startswith("."):
                continue
            if kind == "dir" and os.path.isdir(os.path.join(p, e)):
                entries.append(f"{d}/{e}")
            elif kind == "md" and e.endswith(".md"):
                entries.append(f"{d}/{e}")
    for e in entries:
        if e not in rows:
            problems.append(f"table: {e} has no row whose first cell is `{e}{'/' if e.startswith('skills/') else ''}`")
            continue
        i, cells, cfg = rows[e]
        skill_md = os.path.join(repo, e, "SKILL.md")
        if cfg < 0 or cfg >= len(cells) or not os.path.isfile(skill_md):
            continue
        listed = set(re.findall(r"`([\w-]+)`", cells[cfg]))
        actual = config_keys(skill_md)
        if listed != actual:
            problems.append(f"table: line {i}: {e} lists keys {sorted(listed) or 'none'}, "
                            f"its SKILL.md declares {sorted(actual) or 'none'}")

    print(f"readme_check: {path}: {len(anchors)} headings, {len(entries)} skills and rules, "
          f"{len(problems)} problems")
    for p in problems:
        print(f"  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
