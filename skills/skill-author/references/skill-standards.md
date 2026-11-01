# Skill standards

Format rules and quality bars for the skills the skill-author skill
produces. Apply them to every skill, including this skill's own files. Read
this with [guidance-style.md](../../skill-rule-shared/guidance-style.md) in
the shared directory, which holds the prose style and old-patterns guidance
that applies to skills and rules alike. Harness-specific fields and
behavior live in the harness reference, [claude-code.md](claude-code.md)
for Claude Code.

## Contents

- Writing skills: frontmatter
- Writing skills: body
- Writing skills: scripts
- Writing skills: configuration
- Writing skills: portability

## Writing skills: frontmatter

- `name`: 64 characters maximum; lowercase letters, numbers, and hyphens
  only; no reserved words "anthropic" or "claude"; it matches the directory
  name, which is also the slash command where the harness has one. Prefer
  gerund form (`processing-pdfs`) or a clear noun phrase.
- `description`: 1,024 characters maximum, non-empty, always third person —
  it is injected into the system prompt, where first person breaks
  discovery. State what the skill does and when to use it, with the concrete
  trigger phrases users actually type. On how forceful to be, Anthropic's
  guidance is split: its skill-creator says Claude tends to under-trigger
  skills and descriptions should be "a little bit pushy"; its prompting page
  reports over-triggering from aggressive language on Opus 4.5 and 4.6.
  Neither direction is measured on current models. Write plain conditions
  and concrete phrases, run the trigger eval where a runner exists, and
  adjust in the direction the numbers show. Put the key use case first:
  long descriptions are truncated in skill listings.
- The Agent Skills spec allows six fields: `name`, `description`,
  `license`, `compatibility`, `metadata`, and the experimental
  `allowed-tools`. A portable skill uses no others. Harness extensions and
  their measured behavior are in the harness reference.
- `metadata` is a map of string values for your own tooling; harnesses do
  not act on it. Every skill carries two keys: `last-verified: "YYYY-MM-DD"`
  and `harness`, which is `portable` or a harness id (`claude-code`,
  `cursor`, `codex`, `copilot`, `antigravity`, `gemini-cli`). A missing
  `harness` key is a defect, not a default.

## Writing skills: body

- Keep SKILL.md under 500 lines. Split overflow into reference files linked
  one level deep from SKILL.md — nested references cause partial reads.
  Start any reference file longer than 100 lines with a table of contents.
- The context window is a public good. Assume the model is already smart:
  challenge every paragraph to justify its token cost, and cut anything the
  model already knows.
- Give one default approach with an escape hatch, never a menu of options:
  "Use X. For edge case Y, use Z instead."
- Match degrees of freedom to task fragility: heuristics for
  context-dependent work (high freedom), a parameterized template or
  pseudocode when a preferred pattern exists (medium), an exact
  do-not-modify command sequence for fragile operations (low).
- Give complex tasks a numbered workflow with a copyable checklist. Build
  feedback loops for quality-critical steps: validate, fix, repeat until
  clean.
- Use one term per concept, consistently, throughout the skill.
- For format-sensitive output, show 3–5 concrete input→output examples
  rather than describing the format in prose.
- Avoid time-sensitive instructions ("before August 2025, use..."). Keep
  current guidance in the main body and move superseded practices to an "Old
  patterns" section. Naming the model or the date a finding was measured on
  is not time-sensitive phrasing; it is the qualifier every claim carries.
- No citations or source URLs inside SKILL.md or the files it links.
  Provenance lives in a ledger: the skill's own `sources.md` beside its
  SKILL.md, never linked from it, or the shared
  [sources.md](../../skill-rule-shared/sources.md) for a skill that lives
  beside the authoring skills.

## Writing skills: scripts

- Scripts solve errors rather than defer them to the model: handle missing
  files, bad input, and permissions inside the script with useful messages.
- No unexplained constants — if the author can't justify a value, the model
  can't either.
- State whether the model should execute a script or read it as reference.
- For batch or destructive operations, use plan-validate-execute: write a
  machine-checkable plan file, validate it with a script, only then apply.
- A portable skill whose workflow needs a script names the interpreter in
  `compatibility` and says what to do when it is missing. Windows runs
  PowerShell unless Git Bash is installed, and Python is not a given, so
  the skill's core path does not depend on either.

## Writing skills: configuration

- A value that differs between machines or projects — a path outside the
  skill and the project, a companion skill, a vendor or account choice —
  is a config key: declared in a `## Config` table at the top of SKILL.md,
  with the user's values in `config.local.yaml` beside it, never in the
  body and never in a rule file. [skill-config.md](skill-config.md) has
  the table, the read instruction, the set-up wording, and the migration
  procedure.
- A key exists only when a second environment needs a different value. An
  operating-system tool choice is detected at run time, a project-internal
  path is relative, and a preference nobody asked to change is a named
  default. A skill with no Config section is the normal case; the report to
  the user says "no config keys" rather than inventing one.
- Each value has one owner: a skill that needs another skill's value hands
  the work to that skill. A key never holds a secret, only where one lives.

## Writing skills: kind

- Every skill is one of two kinds, decided at step 3 and declared in
  `metadata.harness`. Portable: runs as written in any harness that reads
  the Agent Skills standard. Harness-specific: written for one harness and
  free to use everything it offers. The subject decides; the user can
  override.
- Priority is unchanged by kind. A skill of either kind is written to do
  its job and produce the best output the standards and the ledger support.
  Portability moves harness facts out of the body; it never removes a step
  the skill needs. If doing the job well needs one harness's feature, say
  so and let the user choose the kind.
- A portable skill uses the six spec fields, names actions instead of
  tools ("read the file", "run the command", "search the web"), refers to
  its own files by paths relative to the skill root, uses no harness
  substitution, injection, or import syntax, and keeps every harness fact
  in `references/<harness-id>.md`, one file per harness, Claude Code
  included. The body points at them once: "read the reference for the
  harness you run in". Verified for this layout: Claude Code, Cursor,
  Codex. Best effort: Gemini CLI, Copilot, Antigravity. macOS and Windows.
- A portable skill is portable only when it passes the portability check in
  [skill-config.md](skill-config.md), with zero hits or every hit named
  with its reason in the pass record. A pass never claims "portable" from a
  reading of the text alone.
- A harness-specific skill names its tools, uses its fields and syntax, and
  states the harness in `compatibility` as well when it needs that
  harness's command-line tool.
