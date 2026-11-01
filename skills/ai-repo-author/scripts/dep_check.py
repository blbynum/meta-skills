#!/usr/bin/env python3
"""Trace the dependencies between skills, rules, and shared directories.

Usage:
  python3 dep_check.py [--outside DIR]... [--linked DIR] [--json] PATH...

PATH is a repository root (it holds skills/ or rules/), a directory of
skill directories, one skill directory (it holds SKILL.md), one shared
directory (no SKILL.md), a rules directory (named rules or instructions),
or one rule file (.md). The
entries found in the PATHs are the inside nodes; the script reads their
files and reports what each one depends on.

--outside DIR   A skills or rules directory whose entries count as outside
                targets, for example the harness's skills directory before
                a move. Their names are found in the inside files; their own
                files are not read. Repeatable.
--linked DIR    The harness skills directory after link.sh ran. Checks that
                each inside skill and shared directory has a link there that
                resolves, and that each relative path (../<dir>/...) in a
                skill resolves through its link.
--json          Print the result as JSON instead of text.

Layers, top to bottom: rule > skill > shared directory. An edge may point
down, or sideways from skill to skill, never up.

Errors (exit 1): a cycle, a two-way pair, an upward edge, frontmatter
(the description included) that names another skill or rule, a Config default that names a skill, a
relative path whose target does not exist, a link that does not resolve.
Review items (exit 0): another skill or rule named in a body, a path under
a home directory, CLIs, Python imports, and MCP tool names. A review item
is a candidate, not a verdict: read the line before you act on it.
Files skipped: evals/, retired/, sources.md, CHANGELOG.md, __pycache__,
binaries.
Runs on Python 3.9 or later; stdlib only.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
import sysconfig

SKIP_DIRS = {"evals", "retired", "__pycache__", ".git", "node_modules"}
# A directory with these names and .md files in it is a rules directory;
# any other directory without SKILL.md is a shared directory.
RULES_DIR_NAMES = {"rules", "instructions"}
SKIP_FILES = {"sources.md", "CHANGELOG.md", ".DS_Store"}
SHELL_LANGS = {"sh", "bash", "zsh", "shell", "console"}
SHELL_WORDS = {
    "cd", "echo", "export", "set", "unset", "if", "then", "else", "elif",
    "fi", "for", "in", "do", "done", "while", "until", "case", "esac",
    "test", "[", "[[", "printf", "read", "local", "return", "exit", "true",
    "false", "shift", "eval", "exec", "source", ".", "trap", "wait", "{",
    "}", "(", ")", "time", "env", "sudo", "!", "function",
}
# Built from parts so that this file does not match its own pattern.
HOME_PATH = re.compile("(" + "|".join([
    "/" + r"Users/[^/\s`'\")]+", "/" + r"home/[^/\s`'\")]+",
    r"[A-Za-z]:\\" + r"Users\\[^\\\s]+", "~" + "/", r"\$" + "HOME/"]) + ")")
REL_PATH = re.compile(r"(?<![\w./])((?:\.\./)+)([A-Za-z0-9][\w.-]*)(/[^\s`'\")\]|]*)?")
MCP_TOOL = re.compile(r"\bmcp__[A-Za-z0-9_-]+")


def die(msg: str) -> None:
    print(f"dep_check: {msg}", file=sys.stderr)
    sys.exit(2)


def read_text(path: str) -> str | None:
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        print(f"dep_check: skip {path}: {e.strerror}", file=sys.stderr)
        return None
    if b"\0" in data[:8192]:
        return None
    return data.decode("utf-8", errors="replace")


class Node:
    def __init__(self, name: str, kind: str, path: str):
        self.name = name      # skill or shared: directory name; rule: rule:<name>
        self.kind = kind      # "rule", "skill", or "shared"
        self.path = path

    @property
    def layer(self) -> int:
        return {"rule": 2, "skill": 1, "shared": 0}[self.kind]


def classify_dir(path: str) -> str:
    return "skill" if os.path.isfile(os.path.join(path, "SKILL.md")) else "shared"


def collect(path: str) -> list[Node]:
    """Expand one PATH argument into nodes."""
    path = os.path.abspath(os.path.expanduser(path))
    if os.path.isfile(path):
        if not path.endswith(".md"):
            die(f"{path}: a file argument must be a rule file (.md)")
        return [Node("rule:" + os.path.basename(path)[:-3], "rule", path)]
    if not os.path.isdir(path):
        die(f"{path}: no such file or directory")
    if os.path.isfile(os.path.join(path, "SKILL.md")):
        return [Node(os.path.basename(path), "skill", path)]
    nodes: list[Node] = []
    subs = [d for d in ("skills", "rules") if os.path.isdir(os.path.join(path, d))]
    if subs:  # a repository root
        for d in subs:
            nodes += collect(os.path.join(path, d))
        return nodes
    entries = sorted(os.listdir(path))
    mds = [e for e in entries if e.endswith(".md") and os.path.isfile(os.path.join(path, e))]
    dirs = [e for e in entries if os.path.isdir(os.path.join(path, e)) and not e.startswith(".")]
    if any(os.path.isfile(os.path.join(path, d, "SKILL.md")) for d in dirs):
        for d in dirs:  # a directory of skill directories
            p = os.path.join(path, d)
            nodes.append(Node(d, classify_dir(p), p))
        return nodes
    if mds and os.path.basename(path) in RULES_DIR_NAMES:  # a rules directory
        return [Node("rule:" + m[:-3], "rule", os.path.join(path, m)) for m in mds]
    return [Node(os.path.basename(path), "shared", path)]  # one shared directory


def node_files(node: Node) -> list[str]:
    if node.kind == "rule":
        return [node.path]
    out = []
    for dp, dns, fns in os.walk(node.path, followlinks=True):
        dns[:] = sorted(d for d in dns if d not in SKIP_DIRS and not d.startswith("."))
        for f in sorted(fns):
            if f in SKIP_FILES or f.endswith((".pyc", ".png", ".jpg", ".svg", ".pdf", ".zip")):
                continue
            if f.startswith(".") and f != ".gitignore":
                continue
            out.append(os.path.join(dp, f))
    return out


def frontmatter(text: str) -> tuple[dict[str, str], int]:
    """Return the top-level frontmatter values as raw text, and its last line."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, 0
    values: dict[str, str] = {}
    key = None
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return values, i + 1
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if m:
            key = m.group(1)
            values[key] = m.group(2).strip()
        elif key:
            values[key] += " " + line.strip()
    return values, 0


def config_rows(text: str) -> list[dict[str, str]]:
    """Rows of the ## Config table: key, required, default, purpose."""
    m = re.search(r"^## Config\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return []
    rows = []
    for line in m.group(1).split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "key" or set(cells[0]) <= {"-", ":", " "}:
            continue
        rows.append({"key": cells[0].strip("`"), "required": cells[1],
                     "default": cells[2].strip("`"), "purpose": cells[3]})
    return rows


def local_config(node: Node) -> dict[str, str]:
    p = os.path.join(node.path, "config.local.yaml") if node.kind != "rule" else ""
    out: dict[str, str] = {}
    if p and os.path.isfile(p):
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r"^([\w-]+):\s*(.*?)\s*$", line)
            if m:
                out[m.group(1)] = m.group(2).strip("'\"")
    return out


def name_pattern(name: str) -> re.Pattern:
    """A hyphenated name matches as a whole word anywhere. A one-word name
    is often an ordinary word, so it matches only where it reads as a skill:
    in backticks, as a slash command, before the word "skill", after
    skills/, before /SKILL.md, or as a relative path to it."""
    n = re.escape(name)
    if "-" in name:
        return re.compile(rf"(?<![\w-]){n}(?![\w-])")
    return re.compile(
        rf"(`/?{n}`|(?<![\w/.-])/{n}\b|\b{n} skill\b|skills/{n}\b|\b{n}/SKILL\.md|\.\./{n}/)",
        re.I)


def shell_commands(text: str, is_script: bool) -> set[str]:
    """First words of command lines in shell fences, or of a shell script."""
    cmds: set[str] = set()
    lines = text.split("\n")
    in_fence, lang = False, ""
    for line in lines:
        s = line.strip()
        fence = re.match(r"^(`{3,}|~{3,})\s*([\w+-]*)", s)
        if fence and not is_script:
            if in_fence:
                in_fence = False
            else:
                in_fence, lang = True, fence.group(2).lower()
            continue
        if not (is_script or (in_fence and lang in SHELL_LANGS)):
            continue
        if not s or s.startswith("#"):
            continue
        s = re.sub(r"^\$\s+", "", s)
        for part in re.split(r"\|\|?|&&|;|\$\(|`", s):
            words = part.strip().split()
            while words and (re.match(r"^\w+=", words[0]) or words[0] in SHELL_WORDS):
                words = words[1:]
            if words:
                w = words[0].strip("\"'()")
                if re.match(r"^[a-z][\w.+-]+$", w) and w not in SHELL_WORDS:
                    cmds.add(os.path.basename(w))
    return cmds


def python_imports(path: str, text: str) -> dict[str, str]:
    """Top-level imports of a Python script, each graded stdlib, local, or other."""
    here = os.path.dirname(path)
    stdlib = sysconfig.get_paths()["stdlib"]
    out: dict[str, str] = {}
    for m in re.finditer(r"^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w., ]+))", text, re.M):
        names = [m.group(1)] if m.group(1) else [n.strip().split(" ")[0] for n in m.group(2).split(",")]
        for n in names:
            top = n.split(".")[0]
            if not top or top == "__future__":
                continue
            if os.path.exists(os.path.join(here, top + ".py")) or os.path.isdir(os.path.join(here, top)):
                out[top] = "local"
                continue
            try:
                spec = importlib.util.find_spec(top)
            except (ImportError, ValueError):
                spec = None
            origin = getattr(spec, "origin", None) or ""
            if top in sys.builtin_module_names or origin in ("built-in", "frozen") or (
                    origin.startswith(stdlib) and "site-packages" not in origin):
                out[top] = "stdlib"
            else:
                out[top] = "other"
    return out


def scan(inside: list[Node], outside: list[Node]) -> dict:
    by_name = {n.name: n for n in outside}
    by_name.update({n.name: n for n in inside})
    targets = [(n, name_pattern(n.name.split(":", 1)[-1])) for n in by_name.values()]
    edges: dict[tuple[str, str], set[str]] = {}
    errors: list[str] = []
    review: list[str] = []
    inventory: dict[str, dict] = {}

    siblings: dict[str, str] = {}

    def edge(src: str, dst: str, how: str) -> None:
        edges.setdefault((src, dst), set()).add(how)

    for node in inside:
        inv = {"kind": node.kind, "clis": set(), "imports": {}, "mcp": set(), "config": []}
        inventory[node.name] = inv
        if node.kind == "skill":
            rows = config_rows(read_text(os.path.join(node.path, "SKILL.md")) or "")
            inv["config"] = [r["key"] for r in rows]
            values = local_config(node)
            for r in rows:
                for t, _ in targets:
                    if t.name == node.name:
                        continue
                    bare = t.name.split(":", 1)[-1]
                    if r["default"] and re.search(rf"(?<![\w-]){re.escape(bare)}(?![\w-])", r["default"]):
                        errors.append(f"default names a skill: {node.name} key {r['key']} defaults to {r['default']}")
                    if values.get(r["key"], "") == bare:
                        edge(node.name, t.name, f"config:{r['key']}")
        for path in node_files(node):
            text = read_text(path)
            if text is None:
                continue
            rel = os.path.relpath(path, node.path) if node.kind != "rule" else os.path.basename(path)
            is_skill_md = node.kind == "skill" and rel == "SKILL.md"
            fm, fm_end = frontmatter(text) if (is_skill_md or node.kind == "rule") else ({}, 0)
            is_script = path.endswith((".py", ".sh")) or text.startswith("#!")
            if rel == "config.local.yaml":
                continue  # read above; it holds this machine's values by design
            lines = text.split("\n")
            in_config = False
            for i, line in enumerate(lines, 1):
                where = f"{node.name}/{rel}:{i}" if node.kind != "rule" else f"{rel}:{i}"
                if is_skill_md and re.match(r"^## ", line):
                    in_config = line.strip() == "## Config"
                bare_line = REL_PATH.sub(" ", line)  # a relative path is its own edge kind
                for t, pat in targets:
                    if t.name == node.name or not pat.search(bare_line):
                        continue
                    if fm_end and i <= fm_end:
                        errors.append(f"frontmatter names {t.name}: {where}")
                        edge(node.name, t.name, "frontmatter")
                    elif in_config:
                        edge(node.name, t.name, "config-table")
                    else:
                        review.append(f"names {t.name}: {where}: {line.strip()[:140]}")
                        edge(node.name, t.name, "mention")
                for m in REL_PATH.finditer(line):
                    if "<" in m.group(0) or node.kind == "rule":
                        continue
                    first = os.path.normpath(os.path.join(os.path.dirname(path), m.group(1), m.group(2)))
                    if os.path.dirname(first) == os.path.dirname(node.path) and m.group(2) != node.name:
                        edge(node.name, m.group(2), "relative-path")
                        siblings[m.group(2)] = first
                    elif not first.startswith(node.path + os.sep):
                        review.append(f"relative path leaves the sibling set: {where}: {m.group(0)}")
                    # The OS resolves ".." after it follows a link; so does this check.
                    if not os.path.exists(os.path.join(os.path.dirname(path), m.group(0))):
                        errors.append(f"relative path does not resolve: {where}: {m.group(0)}")
                for m in HOME_PATH.finditer(line):
                    review.append(f"home path {m.group(0)}: {where}")
                for m in MCP_TOOL.finditer(line):
                    inv["mcp"].add(m.group(0))
            inv["clis"] |= shell_commands(text, is_script and not path.endswith(".py"))
            if path.endswith(".py"):
                inv["imports"].update(python_imports(path, text))
                for m in re.finditer(r"""\[\s*["']([A-Za-z][\w.+-]*)["']\s*,""", text):
                    inv["clis"].add(m.group(1))

    # Layers, two-way pairs, cycles.
    kind = {n.name: n.kind for n in by_name.values()}
    graph: dict[str, set[str]] = {}
    for (s, d), hows in edges.items():
        if d not in kind:
            kind[d] = classify_dir(siblings[d]) if d in siblings and os.path.isdir(siblings[d]) else "shared"
        graph.setdefault(s, set()).add(d)
        graph.setdefault(d, set())
        layer = {"rule": 2, "skill": 1, "shared": 0}
        if layer[kind[d]] > layer[kind[s]]:
            errors.append(f"upward edge: {s} ({kind[s]}) -> {d} ({kind[d]}) via {', '.join(sorted(hows))}")
    for s in graph:
        for d in graph[s]:
            if s < d and s in graph.get(d, set()):
                errors.append(f"two-way pair: {s} <-> {d}")
    for cyc in cycles(graph):
        if len(cyc) > 2:
            errors.append("cycle: " + " -> ".join(cyc + [cyc[0]]))

    inside_names = {n.name for n in inside}
    closure = sorted({d for (s, d), hows in edges.items()
                      if s in inside_names and d not in inside_names and "relative-path" in hows})
    return {
        "inside": sorted(inside_names),
        "edges": [{"from": s, "to": d, "via": sorted(h)} for (s, d), h in sorted(edges.items())],
        "must_come_along": closure,
        "errors": sorted(set(errors)),
        "review": review,
        "inventory": {k: {"kind": v["kind"], "config_keys": v["config"],
                          "clis": sorted(v["clis"]), "imports": dict(sorted(v["imports"].items())),
                          "mcp_tools": sorted(v["mcp"])} for k, v in sorted(inventory.items())},
    }


def cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    """Strongly connected components with more than one node (Tarjan)."""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on: set[str] = set()
    out: list[list[str]] = []
    counter = [0]

    def visit(v: str) -> None:
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on.add(v)
        for w in sorted(graph.get(v, ())):
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                on.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                out.append(sorted(comp))

    for v in sorted(graph):
        if v not in index:
            visit(v)
    return out


def check_links(inside: list[Node], linked: str) -> list[str]:
    errors = []
    linked = os.path.abspath(os.path.expanduser(linked))
    if not os.path.isdir(linked):
        return [f"linked directory does not exist: {linked}"]
    for node in inside:
        if node.kind == "rule":
            continue
        link = os.path.join(linked, node.name)
        if not os.path.lexists(link):
            errors.append(f"no link for {node.name} in {linked}")
            continue
        if os.path.realpath(link) != os.path.realpath(node.path):
            errors.append(f"link {link} resolves to {os.path.realpath(link)}, not {node.path}")
            continue
        for path in node_files(node):
            text = read_text(path) or ""
            sub = os.path.relpath(os.path.dirname(path), node.path)
            for m in REL_PATH.finditer(text):
                if "<" in m.group(0):
                    continue
                # The OS follows the link first, then applies "..", as an agent's read does.
                through = os.path.join(link, sub, m.group(0))
                if not os.path.exists(through):
                    errors.append(f"through the link, {node.name}/{os.path.relpath(path, node.path)} "
                                  f"cannot reach {m.group(0)}")
    return sorted(set(errors))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--outside", action="append", default=[])
    ap.add_argument("--linked")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    inside: list[Node] = []
    for p in a.paths:
        inside += collect(p)
    if not inside:
        die("no skills, rules, or shared directories found in the PATHs")
    names = {n.name for n in inside}
    outside = [n for d in a.outside for n in collect(d) if n.name not in names]
    result = scan(inside, outside)
    if a.linked:
        result["errors"] += check_links(inside, a.linked)
    if a.json:
        print(json.dumps(result, indent=1))
    else:
        print(f"inside: {len(result['inside'])} ({', '.join(result['inside'])}); "
              f"outside names: {len(outside)}")
        print("\nEDGES")
        for e in result["edges"]:
            print(f"  {e['from']} -> {e['to']}  [{', '.join(e['via'])}]")
        print("\nMUST COME ALONG (read by relative path, not inside)")
        for d in result["must_come_along"] or ["none"]:
            print(f"  {d}")
        print("\nINVENTORY")
        for k, v in result["inventory"].items():
            other = [m for m, g in v["imports"].items() if g == "other"]
            print(f"  {k} ({v['kind']}): config {v['config_keys'] or '-'}; clis {v['clis'] or '-'}; "
                  f"non-stdlib imports {other or '-'}; mcp {v['mcp_tools'] or '-'}")
        print(f"\nREVIEW ({len(result['review'])})")
        for r in result["review"]:
            print(f"  {r}")
        print(f"\nERRORS ({len(result['errors'])})")
        for r in result["errors"]:
            print(f"  {r}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
