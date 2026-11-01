# Rule standards

Format rules and quality bars for the rules the rule-author skill produces:
entries in the harness's always-loaded instruction files.
Read this with [guidance-style.md](../../skill-rule-shared/guidance-style.md)
in the shared directory, which holds the prose style and old-patterns
guidance that applies to rules and skills alike.

## Writing rules

- Imperative, concrete, verifiable: "Use 2-space indentation", "Run `npm
  test` before committing". Never hedged ("we generally prefer...") and
  never vague ("format code properly") — vague rules produce inconsistent
  compliance.
- One topic per rules file, with a descriptive filename (`testing.md`,
  `api-design.md`). Keep each always-loaded file under 200 lines; longer
  files reduce adherence and tax every session.
- Budget the total, not just the file. Everything the harness loads unconditionally loads every session, and
  adherence declines as that sum grows — attention is finite, so every
  always-loaded line competes with the task at hand. Check the aggregate
  before adding a rule; when the total creeps up, scope rules with the harness's file-scoping mechanism
  or demote procedures to skills. Splitting a large file into smaller files
  or `@path` imports reorganizes the cost without reducing it.
- When a rule concerns commands, lead with the exact commands.
- Scope with `paths:` frontmatter (glob patterns) when the rule only matters
  for part of the tree; unscoped rules load every session.
- Rules are context, not enforcement. When a violation is unacceptable, pair
  the rule with an enforcement layer — a lifecycle hook or a tool permission
  deny rule — or knowingly accept it as advisory.
- Before adding a rule, check for contradictions across everything already
  loaded (every file the harness reference lists).
  Conflicting rules get arbitrary compliance.
- Add the maintenance marker `<!-- last-verified: YYYY-MM-DD -->` at the top
  of the rule file or section. Block-level HTML comments are stripped before
  context injection, so the marker is free.
- No citations or source URLs inside the rule.
