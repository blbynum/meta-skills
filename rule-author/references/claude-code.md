# Claude Code

What differs when rule-author runs in Claude Code: where rules live, how
they load and scope, the mechanisms the body names generically, and the
measurement runner. Read this when you run in Claude Code, before step 1
and again before step 5. The memory doc and the permissions doc are the
sources, with dates in the shared ledger.

## Contents

- Where rules live and how they load
- Scoping, imports, and comments
- Mechanisms the body names generically
- Measurement: the runner and its approximation
- Sources to re-check

## Where rules live and how they load

| Scope | File | Notes |
|---|---|---|
| Managed policy | a `CLAUDE.md` in the managed settings directory | organization-wide, loads first |
| User | `~/.claude/CLAUDE.md`, `~/.claude/rules/*.md` | every project on the machine |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md`, `.claude/rules/*.md` | shared through source control |
| Local | `./CLAUDE.local.md` | personal, add to `.gitignore`; appended after the project file |

Files in the working directory and every directory above it load at
launch, concatenated from the root down; a subdirectory's file loads when
Claude first reads, writes, or edits a file there. Content arrives as a
user message after the system prompt and is context, not enforcement.
The project-root file is re-read and re-injected after compaction;
subdirectory files and path-scoped rules are not. `AGENTS.md` is read in
place of `CLAUDE.md` only when no `CLAUDE.md` or `CLAUDE.local.md` exists
in or above the working directory (v2.1.277 or later), and
`AGENTS.override.md`, `AGENTS.local.md`, and `.agents/` are never read.
`claudeMdExcludes` skips files by pattern. The vendor's size guidance:
under 200 lines per file; longer files reduce adherence, and splitting or
importing reorganizes the cost without reducing it.

## Scoping, imports, and comments

- A rules file with `paths:` frontmatter loads only when Claude reads,
  writes, or edits a matching file. Patterns are relative to the rule's
  base directory. This is the scoping mechanism the body means.
- `@path` imports expand inline, relative to the file that contains them,
  up to four hops. An import in a project file that resolves outside the
  working directory is "external" and needs a one-time approval dialog;
  user-scope files load their imports without it. The vendor states that
  a sentence telling Claude to read a file is weaker than an import.
- Block-level HTML comments are stripped before injection, so the
  `<!-- last-verified -->` marker costs no context here. Comments inside
  code blocks are kept.
- `/doctor prompt-audit` reports outdated and contradictory instruction
  files (v2.1.283 or later), a mechanical version of the contradiction
  check. An `InstructionsLoaded` hook can log which files loaded and why.

## Mechanisms the body names generically

- Enforcement at a lifecycle point: a hook in `settings.json`, for example
  `PreToolUse` to block an action regardless of what Claude decides.
- A tool ban: a bare tool name in `permissions.deny` (`"AskUserQuestion"`,
  `"mcp__<server>__<tool>"`). Claude Code removes the tool from context,
  enforces the ban itself, charges no context, and applies it to a running
  session.
- A remembered personal fact: auto memory, which Claude writes itself and
  loads every session (first 200 lines or 25 KB).
- A file that must be in context in every session of a directory: an
  `@path` import in that directory's `CLAUDE.md`.

## Measurement: the runner and its approximation

`claude -p` is the non-interactive runner. The shared script runs rule
A/Bs:

- `ab_eval.py --mode rule --rule-file <path>` starts both arms from
  `--safe-mode`, which loads no `CLAUDE.md`, skills, plugins, or hooks,
  and injects the rule into the with arm through `--append-system-prompt`
  with frontmatter and HTML comments stripped. A real rule arrives as a
  user-turn reminder beside every other loaded rule, so a rule that
  competes with others looks better here than in practice. Phrase queries
  as the bare task, not as a slash command.
- `--old` and `--new` compare two versions of a rule the same way.
- There is no trigger eval for a rule. A `paths:` rule has a loading
  condition the script cannot see; check it by hand once per `paths:`
  edit, as the shared `evaluating.md` describes, and read that file's
  preflight checks (Python 3.10 or later, login state, output directory
  outside `~/.claude`) before a suite.

## Sources to re-check

The memory doc is the source for everything above the measurement
section; the permissions doc for hooks and `permissions.deny`; the skills
doc when the shared decision framework changes. All three are in the
shared ledger with last-verified dates.
