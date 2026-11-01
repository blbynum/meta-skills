# Decision framework: skill vs rule

Shared by the two authoring skills, one for skills and one for rules.
Either applies it
at its "confirm the mechanism" step, and either can answer a pure choice
question ("should this be a skill or a rule?") from it without creating
anything. Both artifact kinds are defined by how they load:

- **Skill** — a directory `<name>/SKILL.md` plus optional `references/` and
  `scripts/`. Personal skills live in `~/.claude/skills/`, project skills in
  `.claude/skills/`. Only the name and description (plus `when_to_use`, if
  set) load at startup; the body loads when a task matches or the user types
  `/<name>` (the command comes from the directory name).
- **Rule** — an always-loaded instruction: an entry in CLAUDE.md
  (`~/.claude/CLAUDE.md` user-wide; `./CLAUDE.md` or `./.claude/CLAUDE.md`
  project) or a topic file in `.claude/rules/` (project) or `~/.claude/rules/`
  (user). A rules file with `paths:` frontmatter loads only when Claude works
  with matching files.

Decide on loading behavior, never on topic:

| Property | Rule | Skill |
|---|---|---|
| Loads | Every session, unconditionally | Metadata always; body on demand |
| Cost | Every line taxes every session, summed across all loaded files | Near zero until triggered |
| Fits | Short universal constraints: conventions, prohibitions, exact commands | Procedures: multi-step workflows, domain references, scripts, supporting files |
| Form | Imperative lines; under 200 per file | SKILL.md under 500 lines plus references |

Borderline calls:

- Prefer a **skill** when the content exceeds a few lines, applies to only
  some sessions, or has grown from a fact into a procedure.
- Prefer a **rule** when the guidance must hold even in sessions where nothing
  would trigger a skill. Prohibitions are the classic case: nothing "matches"
  a prohibition until it is already being violated.
- A rules file with `paths:` frontmatter is the middle ground for guidance
  tied to a file area rather than to a task.
- A skill with `disable-model-invocation: true` fits actions only the user
  should time (deploys, releases): it becomes a pure slash command.

Neither kind is the answer for:

- A tool that must never be called → a bare tool name in `permissions.deny`
  (`"AskUserQuestion"`, `"mcp__<server>__<tool>"` for an MCP or app-internal
  tool). Claude Code removes the tool from the model's context, enforces the
  ban itself, charges no context, and applies the edit to a running session.
  A rule beside it earns its lines only by saying what to do instead, when
  the surrounding prompts do not already say so.
- "Remember X" for a personal or one-project fact → auto memory already covers
  it; offer a rule only if the user wants a durable instruction.
- Behavior that must fire at a fixed lifecycle point (before every commit,
  after each edit) → that requires a hook in settings.json. A rule can state
  the policy but cannot enforce timing; say so and point to hook configuration.
- A file that must be in context in every session of a directory → an
  `@path` import in that directory's CLAUDE.md, not a sentence telling Claude
  to read it. The memory doc says Claude then sees the file "only if it
  decides to open the file"; an import loads it at launch and re-injects it
  after compaction. Relative import paths resolve against the CLAUDE.md that
  contains them, so a parent-directory CLAUDE.md cannot import a child's file.
- A value one skill needs that differs between machines or projects — a
  path, a companion skill, an account → a key in that skill's `## Config`
  table, with the machine's value in the skill's own `config.local.yaml`.
  A rule line for it taxes every
  session, and rule files have no common location across harnesses while
  skill directories do.
- A specialized worker with its own context → a subagent; an
  agent-authoring skill covers it, where one exists.
