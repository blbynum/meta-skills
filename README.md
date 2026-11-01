# meta-skills

Six Agent Skills for working on an AI harness's own configuration — the
skills, rules, prompts, and sessions — plus the shared directory the two
authoring skills read. Each skill is a directory in `skills/` with a
`SKILL.md` under the [Agent Skills standard](https://agentskills.io/).
The repository is not installed into a harness; `link.sh` links it into
one. `link.sh` works for any repository with the same shape, so you can
copy it into your own skills or rules repository.

## Contents

- [Install](#install)
- [Update](#update)
- [Use link.sh in another repository](#use-linksh-in-another-repository)
- [What is here](#what-is-here)
- [Per-machine configuration](#per-machine-configuration)
- [Portability](#portability)
- [The provenance ledger](#the-provenance-ledger)
- [Requirements](#requirements)
- [Changelogs](#changelogs)
- [Versioning](#versioning)

## Install

1. Clone the repository to a location that stays. The links point into
   the clone, so they break if you move or delete it.

   ```sh
   git clone git@github.com:blbynum/meta-skills.git ~/src/meta-skills
   cd ~/src/meta-skills
   ```

2. Run the link script, then type the number of your harness:

   ```sh
   ./link.sh
   ```

   Output for a clone at `~/src/meta-skills` when you type `1`:

   ```text
   Repository: /Users/you/src/meta-skills
   Link the skills and rules into which harness?
     1) Claude Code
     2) Codex
     3) Cursor
     4) GitHub Copilot
     5) Gemini CLI
     6) Antigravity
     0) Custom: you type the directories
   Number (0-6): 1
   Harness:    Claude Code (claude-code)
   Skills:     /Users/you/.claude/skills
     linked ai-retrospective
     linked prompt-author
     linked research
     linked rule-author
     linked skill-author
     linked skill-rule-shared
     linked study-credibility

   The links point into /Users/you/src/meta-skills.
   The files stay there; the harness reads them through the links.
   To change a skill's settings on this machine, edit config.local.yaml in
   the skill's directory, /Users/you/src/meta-skills/skills/<name>/. Git ignores that file.
   To get updates, run "git pull" in /Users/you/src/meta-skills, then run this command again:
     /Users/you/src/meta-skills/link.sh --harness claude-code
   It links added skills and rules, and removes the links to deleted ones.
   ```

   Type `0` to give the skills directory yourself.

3. To link the skills into one more harness, run the script again and
   select that harness.

Some harnesses also read the skills directory of another harness. Cursor
also reads `~/.claude/skills` and `~/.agents/skills`. GitHub Copilot and
Gemini CLI also read `~/.agents/skills`, the Codex directory. If you link
the repository for two harnesses and one of them reads the directory of
the other, that harness sees each skill two times. For example, if you
link for Claude Code, do not also link for Cursor. These facts come from
the documentation of each harness as read on 2026-11-01.

To link without the menu, give the harness as an option. An agent or a
script must use this form: with no arguments and no terminal, `link.sh`
writes its usage to standard error and exits with status 2. It does not
wait for input.

```sh
./link.sh --harness claude-code
./link.sh --skills-dir ~/agent/skills
```

`--skills-dir` selects a custom skills directory. Run `./link.sh --list`
to see the harness ids and their directories:

```text
  ID           HARNESS         SKILLS                    RULES
  claude-code  Claude Code     ~/.claude/skills          ~/.claude/rules
  codex        Codex           ~/.agents/skills          none
  cursor       Cursor          ~/.cursor/skills          none
  copilot      GitHub Copilot  ~/.copilot/skills         ~/.copilot/instructions
  gemini-cli   Gemini CLI      ~/.gemini/skills          none
  antigravity  Antigravity     ~/.gemini/config/skills   ~/.gemini/config/rules
  custom       (you choose)    --skills-dir <dir>        --rules-dir <dir>
```

`./link.sh --help` is the full reference: every option, the repository
shape, how each harness handles rules, and the exit statuses.

`link.sh` makes one symlink for each directory in `skills/`, so
`~/.claude/skills/research` points at `<clone>/skills/research`. Claude
Code reads a skill through a symlinked folder and loads it once.
`skills/skill-rule-shared` has no `SKILL.md` and is linked too. Claude
Code ignores it as a skill; the two authoring skills find it next to
their own directories by the relative path `../skill-rule-shared/`.

To unlink, delete the symlinks in the harness's skills directory. The
clone is not changed.

## Update

1. Pull the changes in the clone:

   ```sh
   git -C ~/src/meta-skills pull
   ```

2. Run the command that the last run of `link.sh` printed, for example:

   ```sh
   ~/src/meta-skills/link.sh --harness claude-code
   ```

A pull changes the text of a linked skill immediately, because the links
point into the clone. The second step is necessary when a skill is added
or removed: the run links the new skill and removes the link to the
deleted one. When nothing changed, it writes `no changes`.

## Use link.sh in another repository

`link.sh` contains nothing specific to this repository. To link the
skills and rules of your own git repository the same way:

1. Put the skills and rules at the repository root in this shape. Either
   directory can be absent; `link.sh` links only the ones that exist.

   ```text
   skills/<name>/    one directory for each skill
   rules/<name>.md   one file for each rule
   ```

2. Copy `link.sh` from this repository to the root of your repository.
3. Add the line `config.local.yaml` to the `.gitignore` of your
   repository, so that the settings of one machine stay out of commits.
   `link.sh` warns when git does not ignore that file.
4. Commit `link.sh`. A person who clones your repository then runs
   `./link.sh`.

`link.sh` links each `rules/*.md` file into the user-level rules
directory of the harness. Codex, Cursor, and Gemini CLI have no such
directory, so `link.sh` says so and does not link the rules. For GitHub
Copilot, each link name ends in `.instructions.md`. Antigravity ignores
a rule without a `trigger:` line in its frontmatter, and `link.sh` warns
about each one.

## What is here

| Path | What it does | Config keys |
|---|---|---|
| `skills/skill-author/` | Creates, evaluates, migrates, and updates skills. | `skills-dir` (required), `rule-skill` |
| `skills/rule-author/` | Creates, evaluates, and updates always-loaded rules (CLAUDE.md, AGENTS.md, GEMINI.md, `.cursor/rules`, and the like). | none |
| `skills/prompt-author/` | Writes, rewrites, and reviews prompts; packages a conversation into a hand-off prompt. | none |
| `skills/ai-retrospective/` | Audits how the agent worked in one session from its raw transcript, then proposes changes. | `prompt-skill`, `rule-skill`, `skills-skill`, `settings-skill` |
| `skills/research/` | Desk research: finds, weighs, and synthesizes sources, with stated confidence. | `notes-skill`, `appraisal-skill` |
| `skills/study-credibility/` | Appraises whether a study or research-backed claim is trustworthy. | none |
| `skills/skill-rule-shared/` | Not a skill. The ledger, evaluation method, eval scripts, prose standards, and the skill-versus-rule decision framework that `skill-author` and `rule-author` share. | — |
| `link.sh` | The link script described above. | — |
| `AGENTS.md` | Instructions for agents that work on this repository: the version procedure. `link.sh` does not link it. `CLAUDE.md` and `GEMINI.md` import it for the harnesses that do not read `AGENTS.md`. | — |
| `VERSION` | The version of the repository; see [Versioning](#versioning). | — |

Every key without "(required)" is optional and defaults to none. A skill
with an unset optional key does the work itself or says what it left out;
it never guesses a value.

## Per-machine configuration

A skill that needs a value that differs between machines — a directory,
or the name of a companion skill — declares it in a `## Config` table at
the top of its `SKILL.md` and reads the value from `config.local.yaml` in
its own directory, for example `skills/skill-author/config.local.yaml`:
one flat file of `key: value` lines.

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
  `skills/skill-author/references/skill-config.md`).
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
`skills/skill-rule-shared/sources.md`: every source behind the authoring
guidance (skill and rule best practices, the Agent Skills specification,
harness documentation, prompting guidance, research papers) and the
subject-matter sources of the six skills here, each with the date it was
last verified and the models or vintage a finding was measured on.

A skill outside this repository keeps its own `sources.md` in its
directory, never linked from its `SKILL.md`. The authoring skills read
whichever ledger holds the skill they are working on.

## Requirements

- A harness that reads the Agent Skills standard.
- A POSIX shell (`sh`) and `git`, for `link.sh`.
- Python 3.10 or later, for the eval scripts in
  `skills/skill-rule-shared/scripts/` and for
  `skills/ai-retrospective/scripts/session_facts.py`.
- The `claude` command-line tool, only for measurement in Claude Code.
- `curl`, for the verification examples in `study-credibility`.

## Changelogs

Each skill keeps a dated `CHANGELOG.md` in its directory, one entry per
pass, including "checked, no change" entries.
`skills/skill-rule-shared/CHANGELOG.md` is the closed history of the
single skill the two authoring skills were split from in August 2026.

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
