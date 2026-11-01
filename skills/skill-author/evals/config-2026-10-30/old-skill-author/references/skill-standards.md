# Skill standards

Format rules and quality bars for the skills the skill-author skill
produces. Apply them to every skill, including this skill's own files. Read
this with [guidance-style.md](../../skill-rule-shared/guidance-style.md) in
the shared directory, which holds the prose style and old-patterns guidance
that applies to skills and rules alike.

## Contents

- Writing skills: frontmatter
- Writing skills: body
- Writing skills: scripts

## Writing skills: frontmatter

- `name`: 64 characters maximum; lowercase letters, numbers, and hyphens
  only; no reserved words "anthropic" or "claude". Prefer gerund form
  (`processing-pdfs`) or a clear noun phrase. In Claude Code the slash
  command comes from the directory name, so name the directory what the user
  should type.
- `description`: 1,024 characters maximum, non-empty, always third person —
  it is injected into the system prompt, where first person breaks
  discovery. State what the skill does and when to use it, with the concrete
  trigger phrases users actually type. On how forceful to be, Anthropic's
  guidance is split: its skill-creator says Claude tends to under-trigger
  skills and descriptions should be "a little bit pushy"; its prompting page
  reports over-triggering from aggressive language on Opus 4.5 and 4.6.
  Neither direction is measured on current models. Write plain conditions
  and concrete phrases, run the trigger eval, and adjust in the direction the
  numbers show. Put the key use case first: long descriptions are truncated
  in skill listings.
- Optional fields worth using:
  - `disable-model-invocation: true` for workflows only the user should
    time. The skill then acts as a pure slash command: its description
    leaves Claude's context, so a prose request naming the skill cannot
    load it — only `/name` can. When the user wants prose requests to work
    but nothing else to trigger, gate by description instead: lead with the
    tool's own name, keep shared vocabulary (the domain nouns near-misses
    would use) out of the opening clause, name where the near-miss requests
    go instead, and repeat the restriction in the body. When the description
    names a path the model could explore on its own, read the trigger-eval
    transcripts for runs that explore the path instead of loading the body.
  - `when_to_use` for extra trigger phrases; it is appended to the
    description in the listing, and the two together are cut at 1,536
    characters, so the key use case still goes first in `description`.
  - `argument-hint` when the skill takes arguments.
  - `allowed-tools` pre-approves tools for the invoking turn, but on Claude
    Code 2.1.220 and 2.1.287 any value makes a model-invoked Skill call a
    permission prompt ("Execute skill: <name>"): in a non-interactive
    `claude -p` session under `acceptEdits` the call is denied and the
    body never loads (measured 2026-08-19 and 2026-10-24, 3 of 3 runs
    each; the same skill loaded on every run with the field removed). A
    user-typed `/name` is not affected: the body renders with the field
    set (4 of 4 runs, 2026-10-24). Leave the field off a skill that must
    load unattended — in evals, cron, or `-p` pipelines — and let the
    user's permission settings govern the tools instead.
  - A body that injects shell output with `` !`command` `` is the one case
    that needs `allowed-tools`: outside auto mode an injected command that
    no allow rule matches aborts the whole invocation, silently in `-p`
    (zero turns, empty result), while `disableSkillShellExecution`
    replaces it with a placeholder and the body still loads. Inject a
    bundled script, `` !`${CLAUDE_SKILL_DIR}/scripts/x.sh` ``, pre-approve
    it with `allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/x.sh *)`, make
    the script exit 0 on every path, and write the surrounding prose so it
    still reads correctly when the placeholder appears (measured
    2026-10-24 on 2.1.287; works through a symlinked skill directory).
    Accept the model-invocation cost above, or keep the config out of the
    body and have the prose point at a file the model reads instead.
  - `metadata: {last-verified: "YYYY-MM-DD"}` — a free-form map for your own
    tooling; Claude Code does not act on its contents. This skill uses it to
    track verification dates and config-export uses it for catalog tags.
- A skill that must also upload to claude.ai should restrict frontmatter to
  the Agent Skills spec fields: `name`, `description`, `license`,
  `compatibility`, `metadata`, `allowed-tools`.

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
- No citations or source URLs inside the skill. Provenance lives in the
  shared [sources.md](../../skill-rule-shared/sources.md).

## Writing skills: scripts

- Scripts solve errors rather than defer them to the model: handle missing
  files, bad input, and permissions inside the script with useful messages.
- No unexplained constants — if the author can't justify a value, the model
  can't either.
- State whether the model should execute a script or read it as reference.
- For batch or destructive operations, use plan-validate-execute: write a
  machine-checkable plan file, validate it with a script, only then apply.
