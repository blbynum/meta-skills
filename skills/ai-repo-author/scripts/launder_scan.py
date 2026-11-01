#!/usr/bin/env python3
"""Scan the files that will be committed for personal identifiers and the
user's own research subjects.

Usage:
  python3 launder_scan.py ROOT... [--term T]... [--terms-file F]...
      [--jsonl FILE:FIELD[,FIELD]]... [--names-from DIR]...
      [--allow T]... [--allow-line REGEX]... [--min-length N]
      [--no-builtin] [--no-identity] [--history]

ROOT is a directory to scan. In a git work tree the scan reads what git
would commit (tracked files plus untracked files that are not ignored).
Outside a work tree it walks the directory and skips the names that a
.gitignore on the way lists, a simple subset of the gitignore rules.

Terms are matched case-insensitively as whole words; the words of a
multi-word term may be split by spaces, line breaks, hyphens, or
underscores, so "Pat Example" also finds "pat-example".

--term T            One term. Repeatable.
--terms-file F      One term per line; lines starting with # are skipped.
--jsonl FILE:FIELDS Terms from a JSON Lines data file: the named fields of
                    each record, a string or a list of strings. A value such
                    as "person:pat-example" also adds "pat-example".
--names-from DIR    Each entry name in DIR, without its extension, as a
                    term: case slugs, assessment names. Repeatable.
--allow T           Drop hits whose matched text is T: public subject matter
                    that a skill teaches from. Repeatable.
--allow-line REGEX  Drop hits on lines that match REGEX, for example the
                    copyright line of a license. Repeatable.
--min-length N      Skip terms shorter than N characters (default 3). The
                    skipped terms are listed so you can check them by hand.
--no-builtin        Do not add the built-in patterns: home directory paths,
                    email addresses, IPv4 addresses, private host names,
                    ssh remotes.
--no-identity       Do not add git's user.name and user.email and the name
                    of the home directory as terms.
--history           Also scan every line that any commit added, in every
                    branch (git work trees only). A scrub of the files does
                    not remove a term from history.

Exit status: 0 when nothing is found, 1 when there are hits, 2 when the
scan could not run or read no file. A scan that read no file is a failed
scan, not a clean one.
Runs on Python 3.9 or later; stdlib only.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

MAX_BYTES = 5 * 1024 * 1024
SEP = r"[\s_-]+"
# Built from parts so that this file does not match its own patterns.
# The ssh remote comes first: at one position the first pattern wins, and
# the scp-like remote form (user, at sign, host, colon, path) is not an email.
BUILTIN = {
    "ssh remote": "ssh" + r"://[^\s`'\")]+|\bgit" + "@" + r"[A-Za-z0-9.-]+:[^\s`'\")]+",
    # Also the slug form -Users-<name>- that some tools build from a path.
    "home path": "(?:[/-]" + "Users[/-]|/" + "home/|[A-Za-z]:\\\\" + "Users\\\\)[A-Za-z0-9._]+",
    "email": r"[A-Za-z0-9._%+-]+" + "@" + r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}",
    "ipv4": r"(?<![\d.§v])(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)(?![\d.])",
    "private host": r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.(?:home\.arpa|local|lan|internal|localdomain)(?![\w.*-])",
}
# Values that identify no one: loopback and broadcast addresses, example
# domains and the reserved test domains, and the /Users/you placeholder that READMEs use for a home path.
HARMLESS = re.compile(r"^(?:0\.0\.0\.0|127\.0\.0\.1|255\.255\.255\.255|.*@example\.(?:com|org|net)"
                      r"|.*@(?:[\w-]+\.)*(?:invalid|example|test)"
                      r"|.*@users\.noreply\.github\.com|[/-]Users[/-]you|/home/you)$", re.I)


def die(msg: str) -> None:
    print(f"launder_scan: {msg}", file=sys.stderr)
    sys.exit(2)


def git(root: str, *args: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)
    except OSError:
        return None
    return r.stdout if r.returncode == 0 else None


def files_of(root: str) -> tuple[list[str], str]:
    if git(root, "rev-parse", "--is-inside-work-tree") is not None:
        out = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
        if out is None:
            die(f"{root}: git ls-files failed")
        paths = [os.path.join(root, p) for p in out.split("\0") if p]
        return [p for p in paths if os.path.isfile(p)], "git ls-files"
    found = []
    ignores: dict[str, list[str]] = {}
    for dp, dns, fns in os.walk(root):
        gi = os.path.join(dp, ".gitignore")
        pats = list(ignores.get(os.path.dirname(dp), []))
        if os.path.isfile(gi):
            pats += [l.strip().rstrip("/") for l in open(gi, encoding="utf-8", errors="replace")
                     if l.strip() and not l.startswith("#")]
        ignores[dp] = pats
        dns[:] = [d for d in dns if d != ".git" and not any(fnmatch.fnmatch(d, p) for p in pats)]
        found += [os.path.join(dp, f) for f in fns if not any(fnmatch.fnmatch(f, p) for p in pats)]
    return found, "directory walk with .gitignore names"


def term_regex(term: str) -> str:
    words = [re.escape(w) for w in re.split(SEP, term.strip()) if w]
    return r"(?<![\w])" + SEP.join(words) + r"(?![\w])"


def norm(s: str) -> str:
    return re.sub(SEP, " ", s.strip().lower())


def add_jsonl(spec: str, terms: set[str]) -> None:
    path, _, fields = spec.rpartition(":")
    if not path or not fields:
        die(f"--jsonl wants FILE:FIELD[,FIELD], got {spec}")
    path = os.path.expanduser(path)
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        die(f"{path}: {e.strerror}")
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except ValueError:
            die(f"{path}:{n}: not JSON")
        for f in fields.split(","):
            v = rec.get(f.strip())
            for x in v if isinstance(v, list) else [v]:
                if isinstance(x, str) and x.strip():
                    terms.add(x.strip())
                    if ":" in x and " " not in x:
                        terms.add(x.rsplit(":", 1)[1])


def identity_terms() -> set[str]:
    out = set()
    for key in ("user.name", "user.email"):
        v = git(os.getcwd(), "config", "--get", key)
        if v and v.strip():
            out.add(v.strip())
    home = os.path.basename(os.path.expanduser("~").rstrip("/"))
    if home:
        out.add(home)
    return out


def build(patterns: dict[str, str]) -> re.Pattern:
    return re.compile("|".join(f"(?P<p{i}>{p})" for i, p in enumerate(patterns.values())), re.I)


def scan_text(text: str, where_line, rx: re.Pattern, labels: list[str], terms_by_norm: dict[str, str],
              allow: set[str], allow_line: list[re.Pattern], hits: list, counts: dict[str, int]) -> None:
    line_starts = [0] + [m.end() for m in re.finditer("\n", text)]
    for m in rx.finditer(text):
        label = labels[int(m.lastgroup[1:])]
        found = m.group(0)
        if norm(found) in allow or (label != "term" and HARMLESS.match(found)):
            continue
        lo = text.rfind("\n", 0, m.start()) + 1
        hi = text.find("\n", m.end())
        line = text[lo:hi if hi >= 0 else len(text)]
        if any(a.search(line) for a in allow_line):
            continue
        key = terms_by_norm.get(norm(found), found) if label == "term" else f"{label}: {found}"
        counts[key] = counts.get(key, 0) + 1
        lineno = bisect_right(line_starts, m.start())
        hits.append(f"{where_line(lineno)}: [{key}] {line.strip()[:160]}")


def bisect_right(a: list[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--term", action="append", default=[])
    ap.add_argument("--terms-file", action="append", default=[])
    ap.add_argument("--jsonl", action="append", default=[])
    ap.add_argument("--names-from", action="append", default=[])
    ap.add_argument("--allow", action="append", default=[])
    ap.add_argument("--allow-line", action="append", default=[])
    ap.add_argument("--min-length", type=int, default=3)
    ap.add_argument("--no-builtin", action="store_true")
    ap.add_argument("--no-identity", action="store_true")
    ap.add_argument("--history", action="store_true")
    a = ap.parse_args(argv)

    terms: set[str] = set(t.strip() for t in a.term if t.strip())
    for f in a.terms_file:
        try:
            terms |= {l.strip() for l in open(os.path.expanduser(f), encoding="utf-8")
                      if l.strip() and not l.startswith("#")}
        except OSError as e:
            die(f"{f}: {e.strerror}")
    for spec in a.jsonl:
        add_jsonl(spec, terms)
    for d in a.names_from:
        d = os.path.expanduser(d)
        if not os.path.isdir(d):
            die(f"{d}: not a directory")
        terms |= {os.path.splitext(e)[0] for e in os.listdir(d) if not e.startswith(".")}
    if not a.no_identity:
        terms |= identity_terms()
    short = sorted(t for t in terms if len(t) < a.min_length)
    terms = {t for t in terms if len(t) >= a.min_length}
    terms_by_norm = {norm(t): t for t in terms}

    patterns: dict[str, str] = {}
    labels: list[str] = []
    if not a.no_builtin:
        for k, v in BUILTIN.items():
            patterns[k] = v
            labels.append(k)
    # One alternation for all terms, longest first, so "Pat Example" wins over "Pat".
    if terms:
        patterns["term"] = "|".join(term_regex(t) for t in sorted(terms, key=len, reverse=True))
        labels.append("term")
    if not patterns:
        die("nothing to search for: give terms, or drop --no-builtin")
    rx = build(patterns)
    allow = {norm(x) for x in a.allow}
    try:
        allow_line = [re.compile(x, re.I) for x in a.allow_line]
    except re.error as e:
        die(f"--allow-line: {e}")

    hits: list[str] = []
    counts: dict[str, int] = {}
    nfiles, skipped, sources = 0, [], []
    for root in a.roots:
        root = os.path.abspath(os.path.expanduser(root))
        if not os.path.isdir(root):
            die(f"{root}: not a directory")
        paths, how = files_of(root)
        sources.append(f"{root} ({how}, {len(paths)} files)")
        for p in sorted(paths):
            if os.path.basename(p) == "config.local.yaml":
                continue  # the machine's own values, ignored by git by design
            try:
                if os.path.getsize(p) > MAX_BYTES:
                    skipped.append(f"{p} (over {MAX_BYTES} bytes)")
                    continue
                data = open(p, "rb").read()
            except OSError as e:
                skipped.append(f"{p} ({e.strerror})")
                continue
            if b"\0" in data[:8192]:
                skipped.append(f"{p} (binary)")
                continue
            nfiles += 1
            rel = os.path.relpath(p, root)
            scan_text(data.decode("utf-8", errors="replace"), lambda n, r=rel: f"{r}:{n}", rx, labels,
                      terms_by_norm, allow, allow_line, hits, counts)
        if a.history:
            log = git(root, "log", "--all", "-p", "--no-color", "--no-ext-diff", "--format=commit %h")
            if log is None:
                die(f"{root}: --history needs a git work tree with commits")
            commit, path = "", ""
            for line in log.split("\n"):
                if line.startswith("commit "):
                    commit = line[7:]
                elif line.startswith("+++ "):
                    path = line[6:] if line.startswith("+++ b/") else line[4:]
                elif line.startswith("+") and not line.startswith("+++"):
                    scan_text(line[1:], lambda n, c=commit, q=path: f"history {c}:{q}", rx, labels,
                              terms_by_norm, allow, allow_line, hits, counts)

    print(f"launder_scan: {nfiles} files read; {len(terms)} terms; "
          f"{0 if a.no_builtin else len(BUILTIN)} built-in patterns")
    for s in sources:
        print(f"  source: {s}")
    if short:
        print(f"  terms shorter than {a.min_length} characters, not searched; check by hand: {', '.join(short)}")
    for s in skipped:
        print(f"  skipped: {s}")
    if nfiles == 0:
        die("no file was read; the scan did not run (check the ROOT paths)")
    print(f"\nCOUNTS ({sum(counts.values())} hits)")
    for k, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0].lower())):
        print(f"  {n:4d}  {k}")
    print("\nHITS")
    for h in hits:
        print(f"  {h}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
