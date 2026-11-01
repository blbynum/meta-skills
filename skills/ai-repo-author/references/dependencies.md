# Dependencies

How to trace what each skill, rule, and shared directory depends on,
decide what moves together, and clean the dependencies so that each piece
stands on its own. Read this for steps 1 and 2.

## Contents

- What to trace
- Run the dependency check
- The closure
- The layers
- Clean the dependencies
- Scripts and interpreters

## What to trace

For each candidate, find:

- other skills and rules named in its description or its body;
- its config keys (the `## Config` table) and their values on this
  machine (`config.local.yaml`), which name companion skills and data
  directories;
- shared directories it reads by a relative path (`../<dir>/`);
- absolute paths: into another skill's directory, into a data directory,
  or under the user's home directory;
- data directories it reads or writes: a findings store, a notes vault,
  case files;
- command-line tools and interpreters it runs, and the packages its
  scripts import;
- MCP tools and harness tools named in its files.

## Run the dependency check

Find the harness's directories with `./link.sh --list` in the link script
source. Then run, with each candidate or its parent directory as an
argument:

```sh
python3 scripts/dep_check.py <candidate>... --outside <harness skills dir> --outside <harness rules dir>
```

An argument can be a repository root, a directory of skill directories,
one skill directory, one shared directory, a rules directory, or one rule
file. `--outside` names directories whose entries count as targets but are
not checked themselves. The output has five parts:

- **EDGES**: each dependency between two nodes, with how it was found:
  `config:<key>` (a value in `config.local.yaml`), `config-table`,
  `relative-path`, `frontmatter`, or `mention` (a name in the body).
- **MUST COME ALONG**: shared directories that a candidate reads by
  relative path and that are not among the candidates.
- **INVENTORY**: per node, its config keys, the commands in its shell
  fences and scripts, its non-standard Python imports, and its MCP tool
  names. Use it for `compatibility`.
- **REVIEW**: candidates to read, not verdicts: a skill or rule named in a
  body, and paths under a home directory. A one-word skill name such as
  `archive` is matched only where it reads as a skill, so a generic
  phrase such as "the configured archive skill" can still appear here.
- **ERRORS**: a cycle, a two-way pair, an upward edge, frontmatter that
  names another skill or rule, a Config default that names a skill, a
  relative path that does not resolve. The script exits with status 1.

Run it again with each directory under MUST COME ALONG added as an
argument: the directories that move are checked too, and a shared
directory that names a skill shows up only then.

The script skips `evals/`, `sources.md`, and `CHANGELOG.md`. It cannot see
a tool named only in prose, a hand-off phrased without a name, or a data
directory named only through a config value. Read each candidate's
`SKILL.md` and `config.local.yaml` for those.

## The closure

- A shared directory that a chosen skill reads by relative path moves
  with it. Without it, the skill breaks on the first read.
- A companion skill reached through a config key with an empty default
  stays where it is. This machine's `config.local.yaml` names it; another
  machine names its own companion or none.
- A companion named in the body, not through a key, either comes along or
  becomes a config key in step 2. A new key changes behavior on a machine
  without the value, so propose it and wait for the user's yes.
- A data directory never moves. Step 3 separates its code from its data.
- A shared directory that also serves a skill that stays behind can still
  move: `link.sh` links it back beside that skill, so its relative path
  resolves. Include that skill in the `--linked` check in step 6.

Show the user one table, then ask the step 1 questions in one message:

| Candidate | Kind | Depends on | Must come along | Stays | Data |
|---|---|---|---|---|---|
| example-skill | skill | `../<name>-shared/`; `archive-skill` key | the shared directory | the archive skill | the configured store directory |

## The layers

Layers, top to bottom: rule > skill > shared directory. A dependency
points down, or sideways from one skill to another through a config key.
It never points up:

- A shared directory names no skill or rule. It describes the skills that
  read it by role ("a skill that writes cases"), not by name.
- A skill names no rule. A rule loads in every session; a skill that
  needs it cannot know whether it is loaded on another machine.
- No cycle, and no two-way pair: if A hands work to B, B does not hand
  work to A, even through config keys.

Run the check before step 2 to see what to fix, after step 2, after the
move in step 6 with `--linked`, and in step 9. The result must have zero
errors and a reason for each review item.

## Clean the dependencies

- **Descriptions name no other skill.** The description loads before any
  config is read, so a name there is a dependency on a skill that another
  machine may not have. Say what the skill is not for in its own words:
  "Not for an always-loaded rule", not the name of the rule-writing skill.
- **Hand-offs go through a config key with an empty default.** The key's
  Purpose and the body say what the skill does when the key is unset: it
  does the work itself, or it leaves the work out and says so in its
  report. Adding or removing a hand-off changes behavior: propose it in
  the report and apply it on the user's yes.
- **A shared directory names no consumer.** Rewrite "used by the casework
  skill" as "used by the skills that read this directory".
- **References between directories are relative.** A skill reads a
  shared directory as `../<dir>/` from its own root. A path under the
  user's home into another directory breaks on every other machine. A path
  to data becomes a required config key (step 3).
- **Harness facts go to `references/<harness-id>.md`**, one file per
  harness, or stay in a skill that the user declared harness-specific in
  step 1. Frontmatter that only one harness reads, such as
  `argument-hint`, `when_to_use`, or that harness's substitution syntax,
  leaves a portable skill. The migrate skill checks this in step 5; fix
  what step 1 found now, so that its check passes on the first run.
- **`compatibility` declares what the skill runs**: each command-line tool
  and interpreter, with the oldest version it needs.
- **A config key holds a value that differs between machines.** A value
  that differs between harnesses on one machine, such as the harness's
  skills directory, cannot live in a per-machine file: the same file
  serves every harness that loads the skill. Such a value goes into the
  harness reference, or the skill reads it from the harness at run time.

## Scripts and interpreters

- Run each bundled script once under the oldest interpreter version that
  `compatibility` names. On macOS, `/usr/bin/python3` is the system
  Python, which can be older than the `python3` first on the path. Scripts
  that ran under the newer one crashed there on `dict | None`
  annotations; `from __future__ import annotations` fixes annotations,
  not other new syntax. Fix the script, or raise the declared version.
- If no interpreter of the declared version is on the machine, say so in
  the report, and do not claim that version as tested.
- Write each command and usage line in a skill, a reference, or a README
  from the script's `--help` or from a run, never from memory. A usage
  line written from memory left out the data-path argument, and the first
  fresh session that followed it failed.
