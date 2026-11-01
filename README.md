# meta-skills

Six Agent Skills for working on an AI harness's own configuration — the
skills, rules, prompts, and sessions — plus the shared directory the two
authoring skills read. Each skill is a directory with a `SKILL.md` under
the [Agent Skills standard](https://agentskills.io/). The repository is
not installed into a harness; it is linked into one with `link.sh`.

## Contents

- [Install](#install)
- [What is here](#what-is-here)
- [Per-machine configuration](#per-machine-configuration)
- [Portability](#portability)
- [The provenance ledger](#the-provenance-ledger)
- [Requirements](#requirements)
- [Changelogs](#changelogs)
- [Versioning](#versioning)

## Install

1. Clone the repository anywhere.
2. From the clone, run the linker. With no argument it targets Claude
   Code's personal skills directory, `~/.claude/skills`:

   ```sh
   ./link.sh
   ```

   Output on a machine with none of the links yet:

   ```text
   linked ai-retrospective
   linked prompt-author
   linked research
   linked rule-author
   linked skill-author
   linked skill-rule-shared
   linked study-credibility
   ```

3. Run it again after every `git pull`. It prints nothing when nothing
   changed.

`link.sh` creates one symlink per top-level directory of this repository
inside the target directory, so `~/.claude/skills/research` points at
`<clone>/research`. Claude Code reads a skill through a symlinked folder
and loads it once. On a later run the script relinks a link that points
elsewhere, skips a name that exists as a real directory, and removes a
link into this repository whose source directory no longer exists — so a
skill added or removed upstream appears or disappears after the next
`git pull` and `./link.sh`. It never links `tools/`, `.git`, or any other
dot-directory.

A directory without a `SKILL.md` (`skill-rule-shared`) is linked too. The
harness ignores it as a skill; the two authoring skills find it next to
their own directories by the relative path `../skill-rule-shared/`.

For a harness that reads another directory, pass it:

```sh
./link.sh ~/.agents/skills
```

Cursor reads `~/.claude/skills` directly, so the default run serves it
too. Codex reads `~/.agents/skills`. Both facts come from those
harnesses' documentation as read on 2026-10-25; re-check them before you
rely on them.

To unlink, delete the symlinks in the target directory. The clone is
untouched.

## What is here

| Directory | What it does | Config keys |
|---|---|---|
| `skill-author/` | Creates, evaluates, migrates, and updates skills. | `skills-dir` (required), `rule-skill` |
| `rule-author/` | Creates, evaluates, and updates always-loaded rules (CLAUDE.md, AGENTS.md, GEMINI.md, `.cursor/rules`, and the like). | none |
| `prompt-author/` | Writes, rewrites, and reviews prompts; packages a conversation into a hand-off prompt. | none |
| `ai-retrospective/` | Audits how the agent worked in one session from its raw transcript, then proposes changes. | `prompt-skill`, `rule-skill`, `skills-skill`, `settings-skill` |
| `research/` | Desk research: finds, weighs, and synthesizes sources, with stated confidence. | `notes-skill`, `appraisal-skill` |
| `study-credibility/` | Appraises whether a study or research-backed claim is trustworthy. | none |
| `skill-rule-shared/` | Not a skill. The ledger, evaluation method, eval scripts, prose standards, and the skill-versus-rule decision framework that `skill-author` and `rule-author` share. | — |
| `link.sh` | The linker described above. | — |

Every key without "(required)" is optional and defaults to none. A skill
with an unset optional key does the work itself or says what it left out;
it never guesses a value.

## Per-machine configuration

A skill that needs a value that differs between machines — a directory,
or the name of a companion skill — declares it in a `## Config` table at
the top of its `SKILL.md` and reads the value from `config.local.yaml` in
its own directory: one flat file of `key: value` lines.

```yaml
skills-dir: ~/.claude/skills
rule-skill: rule-author
```

`config.local.yaml` is listed in `.gitignore`, so each machine keeps its
own values and a pull never overwrites them. The file lives inside the
clone, reached through the symlink, which is why the symlink points at
the clone rather than copying it. A skill whose required key is missing
stops and offers to write the file with the values you give it.

Companion-skill keys name a skill the harness can load by name; the
companion does not have to live in this repository. On this machine, for
example, `research` names a `notes` skill that lives elsewhere.

## Portability

Each `SKILL.md` declares its kind in `metadata.harness`. All six skills
here are `portable`: the body uses only the fields the Agent Skills
standard defines, names actions rather than one harness's tools, refers to
its own files by paths relative to the skill root, and keeps every
harness-specific fact in `references/<harness-id>.md`. Five skills have a
`references/claude-code.md`; `study-credibility` has no harness-specific
step and needs none. `rule-author` also has references for Cursor, Codex,
Copilot, Antigravity, and Gemini CLI, because rule files differ per
harness.

What that claim rests on, as of 2026-10-31:

- Each skill passes a text check for harness-only syntax, paths, tool
  names, and frontmatter fields (the check is in
  `skill-author/references/skill-config.md`).
- The layout matches what the Cursor and Codex documentation describe,
  as read on 2026-10-25.
- The skills have run in Claude Code. No run in another harness has
  happened yet.

Two limits. The measurement step of `skill-author` and `rule-author`
(trigger evals and A/B evals) uses the shared scripts, which drive Claude
Code's `claude -p`; in another harness the skills record "not measured"
instead. And `ai-retrospective` needs to read the session transcript; its
Claude Code reference says where that lives, and in a harness without a
reference it reads that harness's documentation first and otherwise
audits from the conversation in context and says so.

## The provenance ledger

The skills carry no citations. Provenance lives in
`skill-rule-shared/sources.md`: every source behind the authoring
guidance (skill and rule best practices, the Agent Skills specification,
harness documentation, prompting guidance, research papers) and the
subject-matter sources of the six skills here, each with the date it was
last verified and the models or vintage a finding was measured on.

A skill outside this repository keeps its own `sources.md` in its
directory, never linked from its `SKILL.md`. The authoring skills read
whichever ledger holds the skill they are working on.

## Requirements

- A harness that reads the Agent Skills standard.
- Python 3.10 or later, for the eval scripts in `skill-rule-shared/scripts/`
  and for `ai-retrospective/scripts/session_facts.py`.
- The `claude` command-line tool, only for measurement in Claude Code.
- `curl`, for the verification examples in `study-credibility`.

## Changelogs

Each skill keeps a dated `CHANGELOG.md` in its directory, one entry per
pass, including "checked, no change" entries. `skill-rule-shared/CHANGELOG.md`
is the closed history of the single skill the two authoring skills were
split from in August 2026.

## Versioning

The file `VERSION` holds the version of the repository as
`major.minor.snapshot`. `master` is the development branch.

Every change that merges into `master` gets a new version. Most changes
increase the snapshot number. The effect of the change on a person who
already has the repository linked into a harness sets the level:

| Level | The change | Examples |
|---|---|---|
| Major | breaks the install, or needs more than `git pull` and a new run of the link script | a skill or rule removed or renamed; a config key removed, renamed, or made required; a link script command that worked before now fails |
| Minor | adds something the install can use, and breaks nothing | a new skill or rule; a new optional config key; a new link script option; a skill that does a new kind of task |
| Snapshot | all other changes | guidance edits, fixes, references, evals, documentation |

If more than one level fits, use the highest. A minor increase sets the
snapshot to 0. A major increase sets the minor and the snapshot to 0.

Each version has a branch with the version as its name:

- When a new version is cut, a branch named after the old version stays
  at the last state of `master` before the new version. For example, the
  branch `1.4.2` marks the last commit of `master` at version 1.4.2.
- Snapshot branches are kept only for the current minor version. When a
  new minor version is cut, the branch `1.4` marks the last state of the
  old minor version, and its snapshot branches are deleted. No commit is
  lost, because each snapshot branch is an ancestor of `1.4`.
- When a new major version is cut, the branch `1` also marks the last
  state of the old major version.
- Major and minor branches are kept indefinitely for now.

To use an earlier version, check out its branch in the clone, for
example `git checkout 1.4`. The links point into the clone, so the
harness then reads that version.

`AGENTS.md` holds the same policy as steps for agents, with the version
check to do immediately before a merge.
