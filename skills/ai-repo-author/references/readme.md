# README

How to get a README that is true about the repository. Read this for
step 8.

## Contents

- Hand-off
- Outline
- Capture the install output
- Check

## Hand-off

Hand the README to the configured doc skill (`doc-skill`). Give it the
outline below, the install output from "Capture the install output", the
list of skills and rules with their config keys and kinds, and the
results of the portability checks from step 5. Tell it to read its README
contract and its style rules before it writes. A README written without
them carried a false claim, that a skill had a harness reference it did
not have, which only a later check caught. Tell it also that licenses are
out of scope, so that it writes no license section and adds no license
file even when its contract asks for them. In a repository that already
has a license section, it keeps that section as it is.

When no doc skill is configured, write the README yourself from the
outline, and say in the report that no README contract was applied.

## Outline

Drop a section that has nothing to say.

1. **Title and summary.** The repository's name, then one or two
   sentences: what the skills and rules do, and that the repository is
   not installed into a harness but linked into one by `link.sh`.
2. **Contents**: links to the sections.
3. **Install.** Clone to a place that stays (the links point into the
   clone); run `./link.sh` with `--harness <id>`, with the captured
   output; how to link into one more harness; how to unlink (delete the
   links; the clone does not change).
4. **Set up the data**, only when the repository has a data contract: the
   init script command, then the config key to set, for example
   `findings-store: ~/data/store`.
5. **Update.** `git pull` in the clone, then the command that the last
   run of `link.sh` printed. A pull changes a linked skill at once; the
   second command links added skills and removes links to deleted ones.
6. **What is here**: a table with the columns Path, What it does, and
   Config keys. One row for each skill (`skills/<name>/`), each shared
   directory, each rule (`rules/<name>.md`), `link.sh`, `AGENTS.md`, and
   `VERSION`. Mark required keys "(required)"; write "none" for a skill
   with no keys.
7. **Per-machine configuration.** Each skill reads its values from
   `config.local.yaml` in its own directory, which git ignores; a skill
   whose required key is missing stops and offers to write the file.
8. **Portability.** Each skill's kind from its `metadata`. The evidence
   behind a portable claim: the portability check and its date, and the
   harnesses the skills have run in. Its limits: harnesses where nothing
   has run yet, and steps that need one harness's tools.
9. **The provenance ledger.** Where the sources behind each skill live.
10. **Requirements**: from each skill's `compatibility` and from
    `link.sh` (a POSIX shell and `git`).
11. **Versioning.** Short: `VERSION` holds `major.minor.snapshot`; the
    three levels, judged by the effect on a person who already linked
    the repository; a branch named after each version marks its last
    state; how to check out an earlier version (`git checkout 1.4`);
    `AGENTS.md` holds the procedure for agents. When `link.sh` is a copy,
    say that it has its own version (`./link.sh --version`) from its
    source, and that this repository replaces it whole and never edits it.

## Capture the install output

Run the install as a new user would, from a copy of what the commit will
hold, with a scratch home directory, so that the real harness directory
is not touched and the output shows no real path:

```sh
S=<scratch dir>; R=<repo>; N=<repo name>; H="$S/home"
mkdir -p "$H/src/$N"
(cd "$R" && git ls-files -z -co --exclude-standard | tar -cf - --null -T -) | tar -xf - -C "$H/src/$N"
git -C "$H/src/$N" init -q && git -C "$H/src/$N" add -A
git -C "$H/src/$N" -c user.name=scratch -c user.email=scratch@example.invalid commit -qm scratch
cd "$H/src/$N" && HOME="$H" ./link.sh --harness <id> > "$S/install.txt" 2>&1; echo "exit $?"
HOME="$H" ./link.sh --harness <id>
sed "s|$H|/Users/you|g" "$S/install.txt"
```

The first `link.sh` run must exit 0; the second must print `no changes`.
Paste the output of the last command into the README as it is: only the
scratch path changes, to `/Users/you`.

## Check

```sh
python3 scripts/readme_check.py <repo>
```

It checks that each anchor matches a heading, that each code fence is
closed and names a language, that each relative link and each backticked
repository path exists, and that each skill and rule has a row in the
table whose Config keys match its `## Config` table. It exits with status
1 when a check fails.

Then check by hand what the script cannot: each claim about a skill (its
kind, its references, its requirements, what it does) against that
skill's files, and each command against a run.
