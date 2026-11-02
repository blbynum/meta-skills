---
name: ai-repo-author
description: >-
  Moves skills and rules into a git repository that people clone and link
  into an AI harness, or audits an existing skills repository: traces and
  cleans dependencies, keeps data stores out, scrubs personal identifiers
  and the user's research subjects, migrates each skill, lays out skills/
  and rules/, copies in a link script, and sets up versioning, an agents
  rule, and a README. Use it before any skill files move, when
  the user asks to move skills or rules out of the harness's skills
  directory into a repo, put a set of skills in git, share several skills
  as a repository to clone, set up versioning or a link script for a
  skills repository, or check whether one is ready to
  share. Triggers include "make a repo out of these skills",
  "move these skills into a git repo", "set up a skills repo like the last
  one", "turn my rules into a repo", and "is this skills repo ready to
  publish". Not for writing, fixing, or migrating one skill or rule, for
  adding a license, or for a code repository with no skills or rules.
compatibility: Needs git, a POSIX shell, and Python 3.9 or later for the bundled scripts.
metadata:
  harness: portable
  last-verified: "2026-11-01"
---

# AI repository author

This skill makes a git repository out of skills and rules, in the shape
that `link.sh` links into a harness: `skills/<name>/` and
`rules/<name>.md` at the root, with a first version, a README, an agents
rule, and links into the user's harness. Every step below
exists because a setup done by hand got it wrong: a README with a false
claim, a stale copy of the link script, real research records shipped as
examples, scripts that crashed on the system Python, and a scan for
personal data that scanned no file and reported nothing.

## Config

| Key | Required | Default | Purpose |
|---|---|---|---|
| link-script-source | yes | | local clone, or raw-file URL, of the repository that publishes `link.sh`; the copy comes from its default branch as committed |
| migrate-skill | no | | skill that migrates one skill to its kind and to config, and runs its checks and trigger evals; when unset, migrate nothing and claim no portability |
| rule-skill | no | | skill that writes always-loaded rules; when unset, write the agents rule from the template in [references/repository.md](references/repository.md) and say that the rule checks did not run |
| doc-skill | no | | skill that writes READMEs; when unset, write the README from the outline in [references/readme.md](references/readme.md) and say that no README contract was applied |

Read `config.local.yaml` in this skill's directory before anything else.
A key missing there takes its Default from the table. If a required key is
missing or empty, stop: name the key and its purpose, and offer to write
`config.local.yaml` with the values the user gives. If a configured
directory does not exist, stop and say so; do not create it.

The bundled scripts are in `scripts/`. Paths in the commands below are
relative to this skill's directory; give the full path when you run a
script from elsewhere. Each script prints its usage with `--help`.

## Inputs

Name the input kind before step 1:

- **Loose skills and rules**, the main case: skill directories in the
  harness's skills directory, rule files in its rules directory, or a
  list the user gives. `./link.sh --list` in the link script source prints
  each harness's directories. Run the whole workflow into a new
  repository directory that the user names.
- **A directory that is not a repository** but holds skills or rules: run
  the whole workflow in place, as an audit first (see "Existing
  directories and repositories").
- **An existing repository** with skills or rules: audit it against the
  treatment and apply only the missing parts.

## Boundaries

- Ask before any push, before any deletion outside the new repository, and
  before any change to a skill's behavior: a hand-off to another skill
  added or removed, or a required config key added.
- Never write research data, a notes vault, or any other data store into
  the repository, and never commit a `config.local.yaml`.
- Never commit in the harness's own configuration directory, even when it
  is a git repository. The old location of the moved skills is the user's
  to commit.
- Never rewrite the history of an existing repository. Report what the
  history holds and let the user decide.
- Leave licenses to the user: they are out of scope for this skill. Add,
  change, or remove no license file or README license section, and report
  no missing license. If the user asks for a license, say that this skill
  does not do that work, and continue with the rest. The MIT notice in the
  header of `link.sh` belongs to that file and stays in each copy; it does
  not license the repository.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 1. Scope: trace dependencies, compute the closure, ask what goes in and which kind
- [ ] 2. Clean the dependencies; dependency check with zero errors
- [ ] 3. Separate data from code; split provenance by owner
- [ ] 4. Launder; rerun the scan
- [ ] 5. Migrate each skill; delete changelogs
- [ ] 6. Move, copy link.sh, link, and check the links
- [ ] 7. Versioning and the agents rule
- [ ] 8. README
- [ ] 9. Commit, final checks, report
```

### 1. Scope

Read [references/dependencies.md](references/dependencies.md) first.

1. List the candidates: each skill directory and rule file in the input,
   and the shared directories (directories with no `SKILL.md`) beside
   them.
2. Trace what each candidate depends on: run `scripts/dep_check.py` over
   the candidates, with the harness's skills and rules directories as
   `--outside`, then read each candidate's `SKILL.md` and
   `config.local.yaml` for what the script cannot see.
3. Compute the closure. A shared directory that a chosen skill reads must
   move with it. A companion skill reached through a config key with an
   empty default stays where it is. A data directory never moves.
4. Show the user one table: each candidate, what it depends on, what must
   come along, what stays, and what is data rather than code. Then ask,
   in one message: which skills and rules go in; for each skill, portable
   or harness-specific, with your recommendation from its subject; the
   path of the new repository and its remote URL, if it has one; any word
   that identifies the user beyond their name, such as an employer or a
   city, for the scan in step 4; and the files the treatment will delete,
   such as `CHANGELOG.md` files. The user's yes covers those deletions and
   the move.

### 2. Clean the dependencies

Apply the cleaning rules in
[references/dependencies.md](references/dependencies.md): no skill names
another skill in its description; a skill reaches another skill only
through a config key with an empty default and says what it does when the
key is unset; a shared directory names no consumer; a reference to another
directory is a relative path (`../<dir>/`); harness facts go to
`references/<harness-id>.md` or stay in a skill the user declared
harness-specific; `compatibility` declares every command-line tool and
interpreter a skill runs. Run every bundled script once under the oldest
interpreter version that its `compatibility` names.

Dependencies point one way, down the layers rule > skill > shared
directory, with no cycle and no two-way pair. Rerun the dependency check
until it reports zero errors and you can name the reason for each review
item.

### 3. Separate data from code

Follow [references/data-and-provenance.md](references/data-and-provenance.md).
Data never enters the repository: a skill names it through a required
config key. The data's contract, its scripts, and an init script that
creates an empty copy live in a shared directory in the repository, and
every script takes the data path as an argument. Split each provenance
ledger by owner before the move.

### 4. Launder

Follow [references/launder.md](references/launder.md). First delete each
`evals/` directory among the inputs and list them in the report: eval files
stay out of the repository. Then scan everything
that will be committed with `scripts/launder_scan.py`: the user's name,
emails, accounts, hostnames, IP addresses, home paths, and the user's own
research subjects, taken from the user's data stores and searched as whole
words. Replace a path with `~` or `<user>` so the line still works.
Replace a real record used as an example with a fictional one of the same
shape. Keep public subject matter that a skill teaches from, with its source.
Rerun the scan after the edits and show its counts.

Do not search with a hand-written shell loop instead of the script. The
script exits with status 2 when it reads no file; a loop that reads no
file reports a clean result.

### 5. Migrate

Hand each skill to the configured migrate skill (`migrate-skill`), with
the kind the user chose in step 1. Its pass must leave:

- the kind declared in `metadata`;
- the portability check run from the skill directory, with zero hits or a
  reason for each hit;
- frontmatter that parses as strict YAML, with `compatibility` present;
- one fresh-session run that read a configured value;
- a trigger eval when a description changed, with its eval files kept
  outside the repository.

When no migrate skill is configured, migrate nothing: keep each skill as
it is, make no portability claim in the README, and list the migration as
left for the user.

No changelog file. Version control is the record: the pass record goes
into the report and the commit message. Delete each `CHANGELOG.md` among
the inputs. Remove agent-written observations from shared files and
references, such as dated eval incidents and claims from one run or one
harness version, and keep what can be checked against a source or the
code.

### 6. Move and link

Follow [references/repository.md](references/repository.md), sections
"Move", "Copy link.sh", and "Link and check":

1. Create the repository directory and run `git init -b master` in it, so
   that `link.sh` can run and git's ignore rules apply from the start.
   Make no commit yet. In place, run `git init` only if it is not a
   repository yet.
2. Move each skill to `skills/<name>/` and each rule to `rules/<name>.md`
   with `mv`, so that `config.local.yaml` and per-skill `.gitignore`
   files travel with them. In place, move only what is not in that shape.
3. Copy `link.sh` unchanged from the default branch of the configured
   source (`link-script-source`), never from its working tree, and
   compare the copy with the source.
4. Add the root `.gitignore`: `config.local.yaml`, `.DS_Store`,
   `__pycache__/`, and `skills/*/evals/`.
5. Run `./link.sh --harness <id>` for the user's harness, run it again,
   and confirm that it reports no changes and skipped no name. Run `scripts/dep_check.py`
   with `--linked` to confirm that the links resolve and that relative
   paths between skills and shared directories resolve through them.
6. If the old location is a git repository, tell the user that it now
   shows deletions and new links for them to commit.

### 7. Versioning and the agents rule

Follow [references/repository.md](references/repository.md), sections
"Versions and branches", "Commits and merges", and "The agents rule".
`VERSION` holds `major.minor.snapshot`; a new repository starts at
`1.0.0`; `master` is the development branch. Hand the agents rule to the
configured rule skill (`rule-skill`) with the template text: `AGENTS.md`
at the root carries the version procedure as steps, with the version
check immediately before a merge, and `CLAUDE.md` and `GEMINI.md` each
import it.

### 8. README

Follow [references/readme.md](references/readme.md). Hand the README to
the configured doc skill (`doc-skill`) with the outline, the install
output captured from a scratch home directory, and the facts it needs,
and tell it to read its README contract and style rules before it writes.
Then run `scripts/readme_check.py` on the repository and check each claim
about a skill against that skill's files.

### 9. Commit and report

1. Rerun the dependency check and the launder scan. Paste both counts
   into the report.
2. Commit as the user's identity (see "Initialize git and the identity"
   in [references/repository.md](references/repository.md)), with the
   message format in "Commits and merges". Add the remote only with the
   URL the user gives. Push `master` and the version branches only when
   the user says to.
3. Report the pass record: what moved and from where; what changed in
   each skill; the checks run, with their numbers; what the old location
   now shows; and what is left for the user. The same record goes into
   the commit message.

## Existing directories and repositories

For a directory or repository that already holds skills or rules, run
each step as a check before you change anything: the dependency check,
the launder scan (with `--history` in a repository), the migrate skill's
checks, `link.sh` compared with its source, `VERSION`, the version
branches, `AGENTS.md`, and the README check. Report what
matches and what is missing, then apply only the missing parts. Do not
reorganize what already matches.

A change that moves or renames a skill, or removes or renames a config
key, breaks the install of a person who already linked the repository.
It is a major version: ask before you make it. An existing repository
with no `VERSION` gets `1.0.0` in the change that adds versioning, and it
keeps its own default branch name, such as `main`.
