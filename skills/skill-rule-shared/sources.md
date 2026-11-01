# Sources

Provenance for every claim the two authoring skills make, one for skills
and one for rules, and for the subject-matter claims of the skills that
live in this repository with them. This file lives in the shared directory
beside the two authoring skills. Seeded 2026-08-15 from the user's research
notes. On each research pass, refresh the "Last verified" date of any
source actually re-checked; if a source moved or its guidance changed,
update the skill files and name the change in the pass record of the skill
that ran the pass. The skills kept per-skill changelogs until version
2.0.1; that history is in version control.

Renamed 2026-08-18, all in one day: skill-rule-creator → skill-author +
rule-author (via skill-creator + rule-creator for a few hours);
agent-creator → agent-author; persona-creator → persona-author;
mcp-servers → mcp-author; refine-prompt → prompt-author. Entries keep the
name in use when they were written; section headings carry both names.

Verification method notes: "fetched" means the page was retrieved and read
directly on that date; "via vault" means the claim was verified through the
user's own sourced notes on that date. A fetch tool that returns a model's
answer to an extraction prompt rather than the page makes a "fetched"
negative ("the page does not say X") hold only for what the prompt asked;
re-fetch with a narrower prompt or read the raw page before recording that
a source lacks a claim.

Every other skill keeps its own `sources.md` in its directory, never
linked from its SKILL.md. Split that way on 2026-10-31; before that, this
file held every skill's provenance.

## Contents

- Tier 1: Anthropic official
- Tier 1: other vendor documentation
- Tier 2: research
- Artifact tooling
- Tier 3: community (corroborated or labeled)
- Artifact subject-matter sources
- prompt-author skill subject-matter sources
- skill-author skill subject-matter sources
- ai-repo-author skill subject-matter sources

Every entry names the models or vintage a finding was measured on. A claim
that drops that qualifier when it is copied into an artifact is the most
common error this file has recorded (audit of 2026-08-18: eight findings in
five artifacts traced to one dropped qualifier).

Artifacts these skills maintain carry no citations of their own, so
provenance for their subject-matter claims is recorded in a ledger: the
sections below for the skills that share this repository, each other
skill's own `sources.md` otherwise.

## Tier 1: Anthropic official

### Skill authoring best practices
- URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Last verified: 2026-10-30 (re-fetched in full for the tea-guide pass;
  every section the standards cite read unchanged: limits, third person,
  500-line body, one-level references, TOC for 100+-line files, degrees of
  freedom, scripts that solve rather than defer, no voodoo constants,
  eval-first). Previous: 2026-10-28 (re-fetched in full for the doc-author pass:
  name/description limits and the no-XML rule, third person, 500-line
  body, one-level references, TOC for 100+-line files, degrees of freedom,
  eval-first steps, and the "Claude models understand the Skill format"
  tip all read unchanged; the naming section lists `writing-documentation`
  among its good gerund examples). Previous: 2026-08-27 (re-fetched in full for the github-cli pass;
  every section the standards cite read unchanged — name/description limits
  and no-XML validation, third person, 500-line body, one-level references,
  TOC for 100+-line files, degrees of freedom, eval-first, "Claude models
  understand the Skill format and structure natively"). Previous:
  2026-08-25 (re-fetched for the info-design pass:
  name/description limits, no-XML-tags rule, third person, 500-line body,
  one-level references, TOC-for-100+-line files, and the eval-first section
  all read unchanged). Previous: 2026-08-19 (re-fetched as raw markdown for the sleuth pass:
  still 1,185 lines; the name/description limits, "no XML tags", third
  person, 500-line body, and one-level-deep references lines read
  unchanged). Previous: 2026-08-18 (re-fetched as raw markdown, `best-practices.md`,
  1,185 lines, for the split pass; every section cited below read
  unchanged, including the "writing skills skill" tip at line 792, the
  three-eval / baseline steps, and "Keep references one level deep from
  SKILL.md". Naming section, verbatim: avoid "Inconsistent patterns within
  your skill collection" — the reason the split keeps the `<kind>-creator`
  pattern of `agent-creator` and `persona-creator` — the whole set was
  renamed to `-author` the same day to avoid the identical last segment
  with `anthropic-skills:skill-creator`. Pattern 2 ("Domain-
  specific organization": one SKILL.md navigating per-domain reference
  files) is the page's own alternative to splitting a skill; recorded so the
  split decision names what it chose against. Also read: both `name` and
  `description` "Cannot contain XML tags" — a validation rule
  skill-standards.md does not state.)
- Supports: name/description limits (64 and 1,024 chars, third person,
  lowercase-hyphen names, reserved words); 500-line body guidance;
  references one level deep; table of contents for reference files over 100
  lines; degrees of freedom; one default plus escape hatch; workflow
  checklists and feedback loops; consistent terminology; old-patterns
  section instead of dates; evaluation-first development (three evals,
  baseline, iterate); script standards (solve don't defer, no unexplained
  constants, execute vs reference, plan-validate-execute).
- Re-fetched 2026-08-15 for the evaluating.md pass, reading the full
  "Evaluation and iteration" section. Verbatim: "Create evaluations BEFORE
  writing extensive documentation." The five steps are identify gaps, create
  evaluations, "Establish baseline: Measure Claude's performance without the
  Skill", write minimal instructions, "Iterate: Execute evaluations, compare
  against baseline, and refine". The Claude A / Claude B pattern: Claude A
  refines the skill while Claude B, "a fresh instance with the Skill loaded",
  runs real tasks, and the author observes Claude B's behavior. The page
  still says (re-read 2026-08-18, line 774 of the cached copy): "There is
  not currently a built-in way to run these evaluations. Users can create
  their own evaluation system. Evaluations are your source of truth for
  measuring Skill effectiveness". That sentence is stale on the page and
  was mis-recorded here as the reason this skill ships its own scripts. See
  the "skill-creator plugin eval harness" entry under Artifact tooling for
  the vendor runner that does exist and the real reason the in-house
  scripts were written. The eval JSON shape (`skills`, `query`, `files`,
  `expected_behavior`) grounds the format in evaluating.md. The checklist
  requires at least three evaluations and testing with Haiku, Sonnet, and
  Opus. Grounds workflow step 5b in full.
- Also verbatim (line 15): "The context window is a public good. Your Skill
  shares the context window with everything else Claude needs to know" —
  this page, not the equipping-agents engineering post, is the source of
  the "public good" framing. And (line 792): "Claude models understand the
  Skill format and structure natively. You don't need special system
  prompts or a 'writing skills' skill to get Claude to help create Skills."
  What this skill adds over that native ability is the ledger, the evidence
  bar, and the measurement scripts — not the SKILL.md format.
- Contradiction recorded 2026-08-15, corrected 2026-08-18: this page's
  iteration example says Claude A "might suggest ... using stronger language
  such as 'MUST filter' instead of 'always filter'". The claim that ALL-CAPS
  and MUST over-trigger comes from one passage of the prompting
  best-practices page and is scoped there to two models: "Claude Opus 4.5
  and Claude Opus 4.6 are also more responsive to the system prompt than
  previous models. If your prompts were designed to reduce undertriggering
  on tools or skills, these models may now overtrigger. The fix is to dial
  back any aggressive language." The Fable 5, Opus 5, and Sonnet 5
  prompting pages carry no guidance on caps, MUST, emphasis, or skill
  over-triggering (all three grepped 2026-08-18), and the same
  best-practices page recommends a sample prompt containing "you MUST read
  the file before answering". Anthropic's own skill-creator SKILL.md says
  the opposite direction: "currently Claude has a tendency to 'undertrigger'
  skills ... please make the skill descriptions a little bit 'pushy'".
  Anthropic guidance is therefore split, and neither side is measured on
  the current model generation. authoring-standards.md keeps plain
  conditions as the default and tells the author to measure the direction
  with the trigger eval rather than assert it.

### Claude Code memory and rules documentation
- URL: https://code.claude.com/docs/en/memory
- Last verified: 2026-11-01 (re-fetched as raw markdown, `memory.md`, 664
  lines, saved and grepped, for the ai-repo-author follow-up; the AGENTS.md
  section read in full. What that pass used is at the end of Supports.)
- Re-fetched 2026-08-18 as raw markdown (`memory.md`, 462 lines) for the
  split pass; everything cited below held then. Read on this pass and not
  yet used by any artifact: rules files "are discovered
  recursively, so you can organize rules into subdirectories"; "The
  `.claude/rules/` directory supports symlinks"; path-scoped rules "are not
  re-injected automatically" after compaction; "CLAUDE.md content is
  delivered as a user message after the system prompt, not as part of the
  system prompt itself" (corroborates the ab_eval rule-mode caveat); and an
  `InstructionsLoaded` hook exists "to log exactly which instruction files
  are loaded, when they load, and why" — a mechanical alternative to
  evaluating.md's by-hand check of a `paths:` rule, not yet tried here. On
  the framing the split rests on, verbatim: "If an entry is a multi-step
  procedure or only matters for one part of the codebase, move it to a skill
  or a path-scoped rule instead." Two more for rule-standards' next pass:
  the locations table lists `./CLAUDE.local.md` ("Personal project-specific
  preferences; add to `.gitignore`"), which the framework's list omits; and
  the `/doctor` trim check states a content test the standards lack — "it
  cuts content Claude can derive from the codebase, such as directory
  layouts, dependency lists, and architecture overviews, and keeps pitfalls,
  rationale, and conventions that differ from tool defaults".
- Supports: CLAUDE.md locations and load order; under-200-lines-per-file
  guidance; `.claude/rules/` and `~/.claude/rules/` with `paths:`
  frontmatter scoping; rules-vs-skills framing (facts vs procedures); rules
  are context not enforcement, hooks for lifecycle enforcement; HTML
  comments stripped before context injection; imports syntax; specificity
  and consistency guidance for instructions; splitting into files or
  imports reorganizes loaded context without reducing it, with
  path-scoping and demotion to skills as the named remediations. Since
  2026-11-01, also the one-line `CLAUDE.md` that imports `AGENTS.md`
  (ai-repo-author `references/repository.md`, "The agents rule").
  Verbatim: "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or
  later"; by default Claude reads it "only when you have no `CLAUDE.md` in
  your working directory or above it"; and, for a `CLAUDE.md` containing
  `@AGENTS.md`, "Keeping the import never makes Claude read `AGENTS.md`
  twice". The same item says to remove such a `CLAUDE.md` if it holds
  nothing else, or keep it if some sessions cannot read `AGENTS.md`
  directly. The 2026-08-18 quote below, "Claude Code reads `CLAUDE.md`,
  not `AGENTS.md`", is no longer on the page.
- Re-read 2026-08-18 (byte-identical to the 2026-08-15 copy). Verbatim:
  "Size: target under 200 lines per CLAUDE.md file. Longer files consume
  more context and reduce adherence." And on AGENTS.md: "Claude Code reads
  `CLAUDE.md`, not `AGENTS.md`. If your repository already uses `AGENTS.md`
  for other coding agents, create a `CLAUDE.md` that imports it" — so
  AGENTS.md is not an always-loaded file for Claude Code; it loads only
  through an `@AGENTS.md` import or a symlink.
- Re-fetched 2026-10-13 (project-author pass; page now also covers direct
  AGENTS.md reading, v2.1.277+). New facts used: "Relative paths resolve
  relative to the file containing the import, not the working directory";
  "CLAUDE.md and CLAUDE.local.md files in the directory hierarchy above the
  working directory are loaded at launch. Files in subdirectories load on
  demand"; and, on telling Claude in words to read a file, "Claude sees
  `AGENTS.md` only if it decides to open the file ... replace the sentence
  with an `@AGENTS.md` import" — the vendor's own statement that an import
  is stronger than an instruction to read, which the shared framework now
  records. Compaction: "Project-root CLAUDE.md survives compaction: after
  `/compact`, Claude re-reads it from disk and re-injects it"; nested
  CLAUDE.md and `paths:` rules reload on demand.
- Re-fetched 2026-10-14 (wrap_up deny pass, core-source check; targeted
  extraction, not the raw file). Everything the standards cite still holds:
  "target under 200 lines per CLAUDE.md file"; block-level HTML comments
  "are stripped before the content is injected"; "Claude treats them as
  context, not enforced configuration. To block an action regardless of
  what Claude decides, use a PreToolUse hook instead". New since 2026-10-13:
  `/doctor prompt-audit` checks instruction files for "instructions written
  for older models, references to files or commands that don't exist, and
  files that contradict each other" (a mechanical contradiction check the
  rule-author step 4 could call in a terminal session, untried); user-scope
  files (`~/.claude/CLAUDE.md`, `~/.claude/rules/`) load their imports
  without the external-import dialog except in Cowork sessions.
- Re-fetched 2026-10-24 (research-skill decoupling pass; targeted
  extraction, saved to disk and grepped). `CLAUDE.local.md`, verbatim from
  the locations table: "Personal project-specific preferences; add to
  `.gitignore`", and from the body: "Add `CLAUDE.local.md` to your
  `.gitignore` so it isn't committed. With `CLAUDE_CODE_NEW_INIT=1` set,
  running `/init` and choosing the personal option does this for you" —
  so the memory system's own local-override file is hand-gitignored,
  unlike `settings.local.json` (see the settings page entry). Worktree
  caveat: "a gitignored `CLAUDE.local.md` only exists in the worktree
  where you created it. To share personal instructions across worktrees,
  import a file from your home directory instead" (`@~/.claude/...`).
  Within a directory "`CLAUDE.local.md` is appended after `CLAUDE.md`".
  Grounds the comparison of local-override conventions in the research
  skill's decoupling design.
- Re-fetched 2026-10-30 (full page, saved and grepped; skill-author
  config pass). New since 2026-10-24, the AGENTS.md section: "Reading
  `AGENTS.md` directly requires Claude Code v2.1.277 or later"; by default
  Claude reads `AGENTS.md` "only when you have no `CLAUDE.md` in your
  working directory or above it", where a `CLAUDE.md`, `.claude/CLAUDE.md`,
  or `CLAUDE.local.md` counts and `~/.claude/CLAUDE.md`, managed
  `CLAUDE.md`, and `.claude/rules/` do not; "Not read: `AGENTS.local.md`,
  `AGENTS.override.md`, or anything under a `.agents/` directory"; the
  **Project instructions** setting takes `claude-md-or-agents-md`
  (default), `claude-md-and-agents-md`, `claude-md`, `managed-only`.
  Trust, verbatim: "Claude Code shows the dialog to protect you from files
  other people commit to a shared project. User-scope memory files, such
  as `~/.claude/CLAUDE.md` and `~/.claude/rules/`, are files you wrote
  yourself." Content rule unchanged: "Keep it to facts Claude should hold
  in every session: build commands, conventions, project layout". Grounds
  skill-config.md's project-scope-is-untrusted rule and the framework's
  config bullet (rule files have no common cross-harness location).

### Claude Code permissions and permission modes
- URLs: https://code.claude.com/docs/en/permissions ,
  https://code.claude.com/docs/en/permission-modes
- Last verified: 2026-10-14 (permissions page re-fetched, with the settings
  page, for the wrap_up deny pass). Previous: 2026-08-22.
- Supports: permission rules are enforced by Claude Code, not the model, so
  they are the enforcement layer to pair with a rule; a bare tool name in
  `permissions.deny` (for example `"AskUserQuestion"`) removes the tool from
  Claude's context entirely, while a scoped rule such as `Bash(rm *)` only
  blocks matching calls; deny beats ask beats allow; `dontAsk` mode denies
  `AskUserQuestion` and every other call that would prompt, so it suits CI
  rather than interactive sessions.
- Re-fetched 2026-08-15 for the scope-discipline rule pass, reading the "Read
  and Edit" section. Read and Edit rules use gitignore pattern syntax with
  four anchors: `//path` is absolute from the filesystem root, `~/path` from
  the home directory, `/path` from the settings source, and `path` or
  `./path` from the current directory. Verbatim warning: "A pattern like
  `/Users/alice/file` isn't an absolute path. The single leading slash
  anchors at the settings source, not the filesystem root." A user-settings
  rule that must apply inside every project therefore needs `//` or `~/`.
  Scope limit, verbatim: Read and Edit deny rules "apply to Claude's built-in
  file tools and to file commands Claude Code recognizes in Bash, such as
  `cat`, `head`, `tail`, and `sed`. They don't apply to arbitrary subprocesses
  that read or write files indirectly, like a Python or Node script that opens
  files itself" — full process-level blocking needs the sandbox. Also: path
  rules are consulted for `Read` and `Edit` only; a `Write`, `NotebookEdit`,
  or `Glob` path rule is accepted, never consulted, and warned about at
  startup.
- Re-fetched 2026-08-22 for the data-uploads rule pass, reading the rule
  format and the ask semantics. Verbatim: "Permission rules follow the format
  `Tool` or `Tool(specifier)`." A bare name matches every use of the tool.
  Bare-name removal from context is a *deny*-only effect; a bare-name **ask**
  rule leaves the tool in place and prompts on every call, which is the
  enforcement layer for a rule of the form "do X only when the user asks".
  Ask beats allow: "a matching ask rule prompts even when a more specific
  allow rule also matches the same call", and a matching ask rule still
  prompts when a PreToolUse hook returned `"allow"`. Deny and ask rules can
  also match one top-level input parameter with `Tool(param:value)` (exact
  scalar value; allow rules cannot). Two traps: rules match the canonical
  tool name, not the label shown in the transcript (`TaskStop`, not `Stop
  Task`), and a deny or ask rule naming no known tool produces a startup
  warning — except names containing `_` or `*`, which are exempt from the
  check. `EndConversation` is the one tool a deny or ask rule cannot reach
  while any other tool remains.
- Re-fetched 2026-10-14 for the wrap_up deny pass (rule-author), reading the
  MCP rule syntax, tool-name wildcards, and the manage-permissions section;
  the settings page's "When edits take effect" read the same day. Verbatim:
  "`mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool
  provided by the `puppeteer` server"; "A bare tool name like `Bash` removes
  the tool from Claude's context entirely, so Claude never sees it. If you
  add such a rule mid-session, Claude can't call the tool from its next tool
  call on"; "Permission rules are enforced by Claude Code, not by the model.
  Instructions in your prompt or `CLAUDE.md` shape what Claude tries to do,
  but they don't change what Claude Code allows." Settings page, verbatim:
  "Claude Code watches your settings files and reloads them when they
  change, so it applies most edits to the running session without a restart,
  including edits to `permissions`, `hooks`, and credential helpers"; the
  terminal, the IDE extensions, and the desktop app "all read the same
  settings files". Three more facts for deny work: app-internal
  tools of the desktop Code tab are MCP tools (`mcp__ccd_turn__*`,
  `mcp__ccd_session__*`) and a deny reaches them like any server's; "When
  Claude Code loads a settings file, it skips any `mcp__` rule that has
  parentheses", so an MCP parameter rule goes through `--disallowedTools`
  only; and deny/ask globs match the full name (`"mcp__*"` denies every MCP
  tool) while allow globs need a literal `mcp__<server>__` prefix. The
  startup warning for an unknown tool name exempts names containing `_`, so
  an MCP deny is silent in sessions where that server is not attached.
  Also new on the page: Cowork's `mcp__workspace__bash` inherits a bare
  `Bash` deny but not a `Bash` allow.

### Claude Code skills documentation
- URL: https://code.claude.com/docs/en/skills
- Last verified: 2026-10-30 (one WebFetch extraction for the tea-guide
  pass: the frontmatter table, personal and project locations, the
  invocation table, `$ARGUMENTS`, `${CLAUDE_SKILL_DIR}` "in bash injection
  commands", the 1,536-character listing cap and 500-line tip; all read
  unchanged; the page shows no date). Same day, skill-author config pass
  (targeted extraction of the first 100k characters): the substitution
  table lists `$ARGUMENTS[N]`, `$N`, `$name` (from an `arguments`
  frontmatter list), `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`,
  `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_PLUGIN_ROOT}`,
  `${CLAUDE_PLUGIN_DATA}`; `skillOverrides` has four states and the
  `/skills` menu writes it to `.claude/settings.local.json`; verbatim
  "Claude Code skills follow the Agent Skills open standard ... Claude
  Code extends the standard with additional features like invocation
  control, subagent execution, and dynamic context injection", "Outside
  Claude Code, you can use only the fields in the Agent Skills spec", "If
  you include any field the spec doesn't allow, packaging or upload fails
  with a hard error"; security: "Workspace trust doesn't gate this field"
  (`allowed-tools`) and "review the `allowed-tools` of skills checked into
  a repository before you run Claude Code there". Grounds skill-config.md's
  portability section. Previous: 2026-10-29 (partial: raw `skills.md` fetched in full for
  the prompt-author /goal pass, 1,258 lines; only "Stack several skills
  in one message" and "Restrict Claude's skill access" read, quoted under
  the prompt-author subject section; nothing else re-read). Previous:
  2026-10-28 (one WebFetch extraction for the doc-author
  pass: 20 frontmatter fields, personal `~/.claude/skills/<name>/SKILL.md`
  and project `.claude/skills/<name>/SKILL.md` locations, the description
  as the trigger, `disable-model-invocation`, `when_to_use` appended and
  the combined 1,536-character cap all read unchanged). Previous:
  2026-10-24 (three targeted WebFetch extractions for the
  research-skill decoupling pass, not the raw file; local Claude Code
  2.1.287). Read in full for the first time here: the "Inject dynamic
  context" section. Verbatim: "The `` !`<command>` `` syntax runs shell
  commands before the skill content is sent to Claude. The command output
  replaces the placeholder"; "Substitution runs once over the original
  file"; the inline form is recognized only when `!` starts a line or
  follows whitespace; "A failed command aborts the entire skill
  invocation, not just its own placeholder. Claude never sees the skill
  content for that invocation"; "any non-zero exit code counts as a
  failure ... append `|| true` to any other command you expect to exit
  non-zero"; "Injected commands never prompt for permission while the
  skill renders. Claude Code checks each one against your permission
  rules first"; "Outside auto mode, when a command's permission check
  returns anything other than allow, Claude Code aborts the invocation
  with the same error. This includes a rule that would normally ask you.
  To keep an unmatched command from aborting here, pre-approve it with
  `allowed-tools`"; "In auto mode, a command that would otherwise need
  your approval doesn't abort the invocation. The skill loads with an
  instruction telling Claude to run the command first"; each command runs
  under the Bash tool's 2-minute timeout; with `disableSkillShellExecution`
  "Each command is replaced with `[shell command execution disabled by
  policy]` instead of being run. Bundled and managed skills are not
  affected"; commands in skills synced from claude.ai never run locally
  (v2.1.228+). `${CLAUDE_SKILL_DIR}` row verbatim: "The directory
  containing the skill's `SKILL.md` file. For plugin skills, this is the
  skill's subdirectory within the plugin, not the plugin root"; it and
  `${CLAUDE_PROJECT_DIR}` are substituted "in two places: the skill's
  markdown content, and Bash rules in the `allowed-tools` frontmatter";
  `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` only in plugin
  skills. The frontmatter table now lists 20 fields (adds `hooks`,
  `shell`, `license`, `compatibility` since the 2026-08-19 read); outside
  Claude Code only the six Agent Skills spec fields are allowed and "If
  you include any field the spec doesn't allow, packaging or upload fails
  with a hard error". "Share skills": commit `.claude/skills/`, a plugin
  `skills/` directory, or managed settings. Negative, limited to what the
  three prompts asked: the page has no section on a skill depending on,
  configuring, or invoking another skill; the closest is stacking
  `/a /b` in one message and preloading skills into a subagent. Roster
  visibility, verbatim from troubleshooting: "Verify the skill appears in
  `What skills are available?`" and "Claude Code loads a listing of skill
  names and descriptions into context so Claude knows what's available".
  Previous: 2026-08-27 (re-fetched for the github-cli pass as a 93.9KB
  persisted markdown copy; spot-checked by grep for the facts the standards
  state, not read in full — the locations table (`~/.claude/skills/`,
  `.claude/skills/`), the precedence rules, the synced-folder reservation,
  and the `allowed-tools` permission-flow line all read unchanged; the
  1,536-char listing cap did not surface in the grep and was not
  re-verified on this pass. New facts recorded this pass: live change
  detection — "When you add, edit, or remove a skill under
  `~/.claude/skills/` ... Claude Code picks up the change within the
  current session, without a restart"; custom commands are merged into skills, a `.claude/commands/` file and a
  skill directory create the same command; nested `.claude/skills/` below
  the working directory load lazily when a file there is first touched).
  Previous: 2026-08-19 (re-fetched as `skills.md`, 1,070 lines, for the
  sleuth pass; read the frontmatter table in full — `allowed-tools`
  "Tools Claude can use without asking permission during the turn that
  invokes this skill. The grant clears when you send your next message";
  "Claude Code honors the frontmatter in every kind of session, so an
  `allowed-tools` grant goes through the normal permission flow";
  `${CLAUDE_SKILL_DIR}` is substituted "in two places: the skill's markdown
  content, and Bash rules in the `allowed-tools` frontmatter"; `effort`,
  `context: fork`, `agent`, `background`, `disallowed-tools`, `model`
  fields present; 1,536-char listing cap; `skillListingBudgetFraction`).
  Previous: 2026-08-18 (re-fetched as `skills.md`; invocation-control
  table, frontmatter reference, and troubleshooting sections read; re-read
  the same day as raw markdown, 1,068 lines, for the split pass)
- Read 2026-08-18 for the split. Name resolution, verbatim: "Plugin skills
  use a `plugin-name:skill-name` namespace, so they can't conflict with
  other levels" and "The bare `/fancy` also invokes the skill unless another
  command already uses that name" — so a personal `skill-creator` and the
  desktop's `anthropic-skills:skill-creator` would both load, the bare name
  resolves to the personal one, and the model sees both in the listing (the
  collision is a description contest, not a name override). The user's decision
  the same day: rename every `-creator` skill to `-author`
  (`skill-author`, `rule-author`, `agent-author`, `persona-author`) so no
  personal skill shares a last segment with an anthropic-skills entry, and
  the collection stays on one pattern. Also: "A
  `<skill-name>` entry in the enterprise, personal, or project locations can
  be a symlink to a directory elsewhere on disk"; a `paths` frontmatter field
  now exists for skills ("Glob patterns that limit when this skill is
  activated ... Uses the same format as path-specific rules") — not yet
  reflected in the skill-vs-rule framework, which names `paths:` rules as the
  only path-scoped middle ground; and on body cost: "Keep the body itself
  concise. Once a skill loads, its content stays in context across turns, so
  every line is a recurring token cost", with the lifecycle detail that
  invoked content "stays there for the rest of the session" and that
  auto-compaction re-attaches "the first 5,000 tokens of each" invoked skill
  within "a combined budget of 25,000 tokens". The body-cost line is the
  tier-1 ground for loading only the artifact kind a request needs. Two
  more lines read on this pass, for evaluating.md's next pass: "If the
  frontmatter YAML is malformed, Claude Code loads the skill body with empty
  metadata, so `/skill-name` still works but Claude has no `description` to
  match against" (a zero trigger rate with a working `/name` is that
  signature); and "Plugin skills are not affected by `skillOverrides`.
  Manage those through `/plugin` instead" (so `ab_eval.py --mode skill`
  cannot build a baseline for a plugin skill).
- Read 2026-08-18 for the insights-v2 skill. The invocation-control table,
  verbatim for `disable-model-invocation: true`: "You can invoke: Yes.
  Claude can invoke: No. Description not in context, full skill loads when
  you invoke." So the flag does more than block auto-invocation: the
  description leaves Claude's context, and a prose request naming the skill
  cannot load it — only `/name` can. This is why an "only when the user
  asks" skill that must still answer prose requests gates by description
  instead. The troubleshooting order for a skill that "triggers too often"
  is "1. Make the description more specific 2. Add
  `disable-model-invocation: true` if you only want manual invocation".
  Also new on this read: a `when_to_use` frontmatter field ("Additional
  context for when Claude should invoke the skill, such as trigger phrases
  or example requests. Appended to `description` in the skill listing"); the
  combined `description` + `when_to_use` text "is truncated at 1,536
  characters in the skill listing" (configurable via
  `skillListingMaxDescChars`); the listing budget "scales at 1% of the
  model's context window" (`skillListingBudgetFraction`,
  `SLASH_COMMAND_TOOL_CHAR_BUDGET`) and drops descriptions "starting with
  the skills you invoke least"; `skillOverrides` in settings with states
  `on`, `off`, `user-invocable-only`, `name-only` for skills whose file you
  do not want to edit; and `allowed-tools` grants last only "the turn that
  invokes the skill".
- Re-read 2026-08-18 for the meta-tooling review. The page has an
  "Evaluate and iterate on a skill" section: "measure two things separately:
  whether Claude invokes it on the prompts it should, and whether the output
  matches what you expect when it does", by running "each one in a fresh
  session with the skill available and again with it disabled". Its
  subsection "Run evals with skill-creator" documents the vendor harness:
  "The `skill-creator` plugin automates the comparison loop inside Claude
  Code" (`/plugin install skill-creator@claude-plugins-official`), with
  test cases in `evals/evals.json`, one subagent per test case, grading to
  `grading.json`, a with-versus-without benchmark to `benchmark.json`, "a
  blind A/B between two versions of the skill", and description tuning that
  "generates should-trigger and should-not-trigger prompts, measures the hit
  rate". Also documented, contrary to an earlier entry here: "Claude Code
  downloads the skills you enable on claude.ai into `~/.claude/skills/synced/`
  when `CLAUDE_CODE_SYNC_SKILLS` is set in non-interactive mode" — the
  `synced` folder name is reserved. Listing budget, verbatim: "The budget
  scales at 1% of the model's context window. When the listing overflows,
  Claude Code drops descriptions starting with the skills you invoke least".
- Supports: personal (`~/.claude/skills/`) and project (`.claude/skills/`)
  locations; command name comes from directory name; frontmatter reference
  (`disable-model-invocation`, `argument-hint`, `arguments`,
  `allowed-tools`, `model`, `effort`, `context: fork`, free-form
  `metadata:` map); Agent Skills spec fields for claude.ai upload;
  description truncation in listings; `${CLAUDE_SKILL_DIR}` substitution.
- Refined 2026-08-16, replacing the earlier shorthand "`metadata:` map
  ignored by the runtime". Verbatim: `metadata` is a "Free-form YAML map for
  your own key-value data, such as entitlement or catalog fields, read by
  your own tooling from `SKILL.md`. Claude Code doesn't act on its contents,
  and drops a value that isn't a map. Don't reuse frontmatter field names
  such as `paths` as keys." Ignored-by-the-runtime and designated-for-your-
  own-tooling are different claims, and the second is what licenses catalog
  fields such as an export tag. Also read on this pass: `user-invocable:
  false` (Claude-only skills, hidden from the `/` menu) and
  `disallowed-tools`, neither previously recorded; `disable-model-invocation`
  is documented for "workflows with side effects or that you want to control
  timing, like `/commit`, `/deploy`", and also blocks preloading into
  subagents and firing from scheduled tasks (v2.1.196+); pairing
  `${CLAUDE_SKILL_DIR}` in both the body and an `allowed-tools` Bash rule
  lets a bundled script run without a permission prompt.

### Claude Code settings page (files, scopes, precedence)
- URL: https://code.claude.com/docs/en/settings
- Last verified: 2026-10-24 (fetched in full, research-skill decoupling
  pass).
- Supports: the four settings files and scopes; `.claude/settings.local.json`
  verbatim: "You, in this one project only. Claude Code keeps it out of git
  when it creates the file; if you create it by hand, add it to `.gitignore`
  yourself" and "The first time Claude Code writes the file in a git
  repository that doesn't already ignore it, it adds
  `**/.claude/settings.local.json` to your global git excludes file" — the
  vendor's own committed-plus-local pattern, and the precedent for a
  skill's `config.local.*`. Precedence, highest first: managed, `--settings`
  command line, project local, shared project, user; lists merge. "An
  `env` block inside a settings file is an ordinary key and follows the
  levels above." Cloud sessions read neither `~/.claude/settings.json` nor
  the local file. Settings files are strict JSON (no comments).

### Claude Code environment variables page (`env` block)
- URL: https://code.claude.com/docs/en/env-vars
- Last verified: 2026-10-24 (targeted extraction of the "Set variables in
  settings files" section; the page is 185k characters and the rest was
  not read).
- Supports: the `env` block, verbatim: "Add variables under the `env` key
  in a `settings.json` file ... Claude Code reads them directly from the
  file, so they take effect no matter how `claude` was launched"; "Claude
  Code writes each `env` entry into the process environment, replacing the
  value inherited from the shell"; "Subprocesses still inherit" values; the
  file-to-scope table repeats the settings page (local file "gitignored
  when Claude Code saves a setting to it; add it to your gitignore if you
  create it by hand"). Not stated on the portion read:
  whether `CLAUDE_SKILL_DIR` is exported to the Bash tool (the plugin
  manifest reference says the plugin path variables are not).

### Claude Code plugin manifest reference and plugin components (userConfig, data directory)
- URLs: https://code.claude.com/docs/en/plugins-reference (serves the
  manifest reference) ; https://code.claude.com/docs/en/plugins/components
- Last verified: 2026-10-24 (both fetched in full, research-skill
  decoupling pass).
- Supports: `userConfig` — "declares values Claude Code prompts the user for
  when the plugin is enabled, so users don't edit `settings.json`
  themselves"; option fields `type` (`string`, `number`, `boolean`,
  `directory`, `file`), `title`, `description`, `required`, `default`,
  `options` (v2.1.271+), `multiple`, `sensitive`, `min`/`max`; "Non-sensitive
  values are saved under `pluginConfigs` in the user's `settings.json`.
  Sensitive values go to the platform's secure credential store"; reference
  forms "`${user_config.KEY}`: substituted in MCP server config, LSP server
  config, exec-form hook `args`, and skill and agent content. In skill and
  agent content, only non-sensitive values are substituted" and
  `CLAUDE_PLUGIN_OPTION_<KEY>` exported to hook processes; shell-form hook
  commands and monitor commands reject `${user_config.*}`. The dialog
  opens from `/plugin` install or enable, and "The `claude plugin install`
  shell command never prompts for `userConfig` values. To set values from
  the shell, pass each one as `--config KEY=VALUE` when you install, or
  pipe a JSON object to `claude plugin configure --values-stdin`".
  Path variables: "`${CLAUDE_PLUGIN_ROOT}` changes when the plugin
  updates, so don't write state there"; "`${CLAUDE_PLUGIN_DATA}` |
  `~/.claude/plugins/data/<id>/`, created on first reference and kept
  across plugin updates"; deleted on uninstall from the last place unless
  `--keep-data`; "The variables aren't present in the environment of
  commands Claude runs through the Bash tool ... write the `${...}`
  reference in the Markdown body instead". `dependencies`: "Plugins that
  must be enabled for this one to work". "A `CLAUDE.md` at the plugin root
  isn't loaded as context". Plugin skills are `/<plugin>:<skill>`; the
  manifest `skills` key adds to the default `skills/` scan. This is the
  only vendor-sanctioned per-user configuration mechanism for a skill, and
  it exists only for plugin-distributed skills; the `${user_config.KEY}`
  substitution in skill content was read, not exercised, on this pass.

### Agent Skills specification (agentskills.io)
- URL: https://agentskills.io/specification
- Last verified: 2026-10-30 (fetched in full for the skill-author config
  pass; byte-for-byte the same six fields and no configuration mechanism).
  Previous: 2026-10-24 (fetched in full). No version or date shown on
  the page.
- Supports: the six frontmatter fields and their constraints (`name` 1–64,
  must match the parent directory name, no consecutive hyphens;
  `description` 1–1024; `license`; `compatibility` 1–500 characters,
  "Should only be included if your skill has specific environment
  requirements"; `metadata` "A map from string keys to string values ...
  We recommend making your key names reasonably unique"; `allowed-tools`
  experimental); `scripts/`, `references/`, `assets/` conventions;
  progressive disclosure (metadata ~100 tokens, body under 5,000 tokens
  recommended, 500 lines); "Keep file references one level deep". Negative,
  for what the prompt asked: the spec defines no configuration, settings,
  environment-variable, or per-user customization mechanism and nothing on
  one skill referencing another; `compatibility` is the only field that can
  state an environment requirement. So a skill's optional companion and its
  local config are portable only as prose plus files the skill reads.

### Cursor and Codex skills documentation (cross-harness skill support)
- URLs: https://cursor.com/docs/context/skills ; https://learn.chatgpt.com/docs/build-skills
  (the Codex skills page; developers.openai.com/codex/skills redirects
  there) ; https://agentskills.io/ (overview; a client showcase exists at
  /clients and was not opened)
- Last verified: 2026-10-25 (targeted WebFetch extractions for the
  research-skill cross-harness design question).
- Supports: Cursor loads skills from `.agents/skills/`, `.cursor/skills/`,
  `~/.agents/skills/`, `~/.cursor/skills/`, and "For compatibility, Cursor
  also loads skills from Claude and Codex directories" — `.claude/skills/`,
  `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`; frontmatter
  read: `name`, `description`, `paths`, `disable-model-invocation`, `icon`,
  `color`, `metadata` (`globs` legacy); "Reference scripts in your
  `SKILL.md` using relative paths from the skill root". Codex reads skills
  from `$CWD/.agents/skills` up to `$REPO_ROOT/.agents/skills`,
  `$HOME/.agents/skills`, `/etc/codex/skills`, and bundled system skills;
  invocation by `$` or `/skills` in the CLI, `@` in ChatGPT; host-side
  `[[skills.config]]` in `~/.codex/config.toml` enables or disables a
  skill; "Skills build on the open agent skills standard". Negative, for
  what the prompts asked: neither page describes dynamic content, shell
  substitution, variables, file imports, or skill-declared configuration.
  A Cursor forum feature request (2026-06-20, forum.cursor.com thread
  163688) asks Cursor to "Add dynamic context injection to Agent Skills
  (`SKILL.md`)", citing Claude Code as prior art, with no staff reply in
  the fetched content. Grounds the design conclusion that only Claude Code
  can inject a config file into a skill body, that `~/.agents/skills` is
  the directory Cursor and Codex share, and that a relative `scripts/`
  path is the one file reference all three harnesses document. Symlinked
  skill directories and handling of non-spec frontmatter in Cursor and
  Codex: not stated, not tested.

### Claude prompting best practices
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Last verified: 2026-10-30 (re-fetched in full for the skill-author config
  pass, saved and grepped: the over-triggering text still names Opus 4.5
  and 4.6 and "Claude 4.6 models" only; the Fable 5.1 "formats less" and
  "fewer user-facing updates" lines unchanged; nothing on configuration
  files or reading values from files). Previous: 2026-10-28 (re-fetched in full, 1,172 lines, for the
  doc-author pass). Structure change since 2026-08-15: the page now covers
  Claude Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5.5, Opus 5, Opus
  4.8/4.7/4.6, Sonnet 5.5, Sonnet 5, Sonnet 4.6, Haiku 5.5 and 4.5, and
  links a separate "Prompting Claude Fable 5.1" page (effort levels,
  finishing long tasks, user-facing progress updates, thinking blocks
  passed back unchanged, tool-call batching, writing density). Unchanged:
  the over-triggering passage is still scoped to "Claude Opus 4.5 and
  Claude Opus 4.6" ("The fix is to soften any aggressive language"); "If in
  doubt, use [tool]" still "cause[s] overtriggering"; "Tell Claude what to
  do instead of what not to do"; motivation ("explaining to Claude why such
  behavior is important") still recommended; examples should be "Diverse".
  New model-specific lines worth knowing for skill prose: "Claude Fable 5.1
  has the opposite tendency during agentic work: it writes fewer
  user-facing updates between tool calls" and "Claude Fable 5.1 already
  formats less than earlier models, so on that model a block like this can
  suppress structure the content needs" (about a formatting-restriction
  block). Previous: 2026-08-15 (fetched twice; second fetch read the full page)
- Structure note: the page now leads with model-specific guidance and links
  a separate prompting page per model (Fable 5, Sonnet 5, Opus 5, Opus 4.8),
  then techniques for all current models, then migration. Model-conditional
  statements in the shared body cover verbosity (Opus 5 is the exception:
  effort does not reliably shorten visible responses), thinking defaults per
  model, self-check, manual chain-of-thought as a fallback, subagent overuse,
  and context awareness (Sonnet and Haiku only) — grounds refine-prompt's
  Target model section, in particular the split between durable
  capability-tier advice and volatile per-release behavior.
- Supports: clarity and directness; motivation ("explain why") improves
  generalization; 3–5 diverse examples for format-sensitive tasks; positive
  instructions over prohibitions; XML only for complex prompts on current
  models; long-context ordering (documents top, query last, up to 30
  percent) and quote-grounding; action verbs for agentic action ("Change"
  not "Can you suggest"); prefills removed from the API (4.6+).
  Deprecations, each with the scope the page gives it (re-read
  2026-08-18): aggressive language such as "CRITICAL: You MUST use this
  tool" may over-trigger tools and skills on "Claude Opus 4.5 and Claude
  Opus 4.6", which "are also more responsive to the system prompt than
  previous models"; anti-laziness prompting ("If in doubt, use [tool]")
  "will cause overtriggering" on Claude Opus 4.6 and, in the migration
  list, on "Claude 4.6 models"; manual chain-of-thought is kept as a
  fallback — verbatim, "Manual chain-of-thought (CoT) prompting as a
  fallback. When thinking is off, you can still encourage step-by-step
  reasoning" — and "Prefer general instructions over prescriptive steps. A
  prompt like 'think thoroughly' often produces better reasoning than a
  hand-written step-by-step plan." None of the deprecations is stated for
  Fable 5, Opus 5, or Sonnet 5, and the page's own recommended sample for
  agentic coding reads "If the user references a specific file, you MUST
  read the file before answering."
  Self-check, verbatim: "Ask Claude to self-check. Append something like
  'Before you finish, verify your answer against [test criteria].' This
  catches errors reliably, especially for coding and math. Claude Opus 5 is
  the exception: it verifies its own work well without explicit
  instruction, and verification instructions carried over from prompts
  tuned for earlier models can cause over-verification". Only Opus 5 is
  named; Fable 5 does not appear in that bullet, and its own page says the
  opposite for long runs (see the Fable 5 entry). An earlier version of
  this entry added Fable 5 to the exception in a parenthesis; that
  parenthesis was this file's error, copied into refine-prompt and
  authoring-standards until 2026-08-18. Re-fetched 2026-08-15
  for the research skill: the page also carries a "Research and information
  gathering" section (clear success criteria; verify across multiple
  sources; a sample prompt with competing hypotheses, confidence tracking,
  self-critique, and a research notes file) and a "Subagent orchestration"
  section with a damping prompt for subagent overuse.
- Re-fetched 2026-08-17 for the refine-prompt scope pass. The "Overeagerness"
  section carries a sample prompt against overengineering whose method is to
  name the categories of addition rather than ask for restraint in general:
  "Scope: Don't add features, refactor code, or make 'improvements' beyond
  what was asked", "Don't design for hypothetical future requirements", "The
  right amount of complexity is the minimum needed for the current task."
  Grounds writing a scope clamp as named categories with a stated source for
  each kind of material. Also verbatim on line 39: "If you want 'above and
  beyond' behavior, explicitly request it rather than relying on the model to
  infer this from vague prompts" — advice to the person writing the prompt,
  which is why refine-prompt reports it in the rationale instead of adding a
  quality bar the user never asked for.

### Prompting Claude Fable 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Last verified: 2026-08-18 (re-fetched; byte-identical to the 2026-08-15
  copy; full page read)
- Supports: give the reason behind the request ("I'm working on X for Y...");
  state assess-vs-act boundaries; brief brevity instructions outperform
  enumerating verbosity patterns; ground progress claims in tool results;
  reasoning-echo instructions can trigger reasoning-extraction refusals;
  skills written for prior models are often too prescriptive and can degrade
  Fable 5 output.
- Self-verification, verbatim (section "Recommended scaffolding changes"):
  "Make self-verification explicit in long-run prompts. Separate,
  fresh-context verifier subagents tend to outperform self-critique. For
  long-running tasks, instruct: `Establish a method for checking your own
  work at an interval of [X] as you build. Run this every [X interval],
  verifying your work with subagents against the specification.`" This is
  the reverse of the Opus 5 guidance to remove verification instructions,
  and it is why refine-prompt must not strip self-checks from a Fable 5
  long-run prompt. Also verbatim: "Skills developed for prior models are
  often too prescriptive for Claude Fable 5 and can degrade output quality.
  Review and consider removing older instructions if default performance
  is better." The page has no guidance on caps, MUST, emphasis, or skill
  over-triggering, and does not mention Opus 4.5 or 4.6.

### Prompting Claude Opus 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Last verified: 2026-08-17 (re-fetched, full page read)
- Supports: default responses run longer than prior Opus models and effort
  does not control visible length, so prompt for conciseness; readier
  narration during agentic work; longer written deliverables; removal of
  verification instructions because the model verifies its own work
  ("removing them reduces wasted tokens with no loss in quality"); scope
  expansion on narrow tasks; readier subagent delegation; more correction
  narration; artifacts when thinking is disabled. Also: literal compliance
  with "only report high-severity issues" in review prompts reduces reported
  findings.
- Read in full 2026-08-17 for the refine-prompt scope pass. The "Task scope
  and over-verification" section states, verbatim: "Claude Opus 5 can also
  expand the scope of a task, adding steps that weren't requested or applying
  its own judgment about what the task should be. For narrow tasks, constrain
  scope explicitly", followed by a sample clamp whose operative lines are
  "Deliver what was asked, at the scope intended" and "stop short of actions
  that are clearly beyond what was asked". Two things follow. First, scope
  expansion is a documented model behavior, not an artifact defect, so an
  artifact that produces text on the user's behalf needs its own clamp.
  Second, the documented remedy is an explicit clamp in the prompt, which is
  the design refine-prompt's Scope section adopts.
- Re-read 2026-08-18: the "Self-correction" section adds "Claude Opus 5
  catches and fixes its own mistakes well without prompting. Avoid
  instructing re-checks it already performs". The page has no guidance on
  caps, MUST, emphasis, or skill over-triggering, and never mentions Opus
  4.5 or 4.6 (comparisons are against Opus 4.8 only). "Positive examples of
  the communication style you want tend to be more effective than
  instructions about what not to do" is the page's positive-framing line.

### Prompting Claude Sonnet 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- Last verified: 2026-08-15 (fetched)
- Supports: length calibrated to task complexity rather than a fixed
  verbosity; adaptive thinking on by default (a change from Sonnet 4.6);
  `temperature`, `top_p`, and `top_k` return 400; manual extended thinking
  removed; readier tool use and self-verification loops; more literal
  instruction following, so state scope explicitly; code-review harnesses
  tuned for earlier models lose recall. Read together with the Opus 5 page,
  this is the evidence that two models in one generation need different
  prompt changes.
- Re-read 2026-08-18: no guidance on caps, MUST, emphasis, or skill
  over-triggering; the "Tool use triggering" section frames the risk as
  under-triggering with thinking off ("add an explicit nudge in the system
  prompt"). The page's one ALL-CAPS "NEVER" sits inside a recommended
  frontend sample prompt. Comparisons are against Sonnet 4.6 only.

### Console prompting tools (prompt generator and improver)
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools
- Last verified: 2026-08-15 (fetch redirects to the consolidated
  best-practices page; improver behavior per the 2024 announcement at
  https://www.anthropic.com/news/prompt-improver and search summaries)
- Supports: the improver's classic transformations (chain-of-thought
  enrichment, prefill addition) target older model generations and are now
  deprecated techniques on current models — grounds refine-prompt's rule to
  strip what automated improvers added rather than emulate them.

### Anthropic engineering: equipping agents with skills
- URL: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Last verified: 2026-08-18 (fetched; full post read)
- Supports: skills design rationale; progressive disclosure architecture —
  verbatim, "Progressive disclosure is the core design principle that makes
  Agent Skills flexible and scalable", and "At startup, the agent pre-loads
  the name and description of every installed skill into its system prompt.
  This metadata is the first level of progressive disclosure". The phrase
  "public good" does not appear in this post (grep 2026-08-18); it belongs
  to the skill authoring best-practices page above, where an earlier
  version of this entry had misplaced it. Post dated 2025-10-16.

### Anthropic engineering: effective context engineering
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Last verified: 2026-08-15 (fetched)
- Supports: smallest set of high-signal tokens as the goal; right-altitude
  instructions (start minimal, add on observed failure); curated canonical
  examples over exhaustive edge cases; just-in-time retrieval; finite
  attention budget and context rot (recall degrades as loaded context
  grows) — grounds the aggregate always-loaded budget rule.

### Claude's Constitution (January 2026)
- URL: https://www.anthropic.com/constitution
- Last verified: 2026-08-15 (fetched)
- Supports: value priority order (safety, ethics including honesty,
  guidelines, helpfulness) — honesty outranks helpfulness; "Claude should be
  diplomatically honest rather than dishonestly diplomatic"; "Epistemic
  cowardice—giving deliberately vague or noncommittal answers to avoid
  controversy or to placate people—violates honesty norms"; Claude should
  "disagree with experts when it has good reason to, point out things people
  might not want to hear"; helpfulness as an intrinsic value risks
  obsequiousness; autonomy-preserving communication.

### Claude Sonnet 5 system card (June 2026)
- URL: https://www.anthropic.com/claude-sonnet-5-system-card
- Last verified: 2026-08-18 (PDF text extracted and read; 146 pages, dated
  June 30, 2026)
- Supports: sycophancy and hallucination "markedly improved" over Sonnet
  4.6 (p.4); "Claude Sonnet 5 is the strongest tested Claude model on the
  MASK measure of sycophantic dishonesty" (p.68), lowest MASK lying rate at
  3.1% against Sonnet 4.6 at 13.3% (p.90, public split, n=904); "wet
  blanket" responses ("Excessively discouraging, dismissive, or moralizing
  tone toward the user", p.88) "slightly increased" (p.4). The link is
  hedged, verbatim (p.86): "Sonnet 5 appears to be actively worse on the
  broader 'wet blanket' metric for dismissive or discouraging output. This
  is potentially linked to its improvement on sycophancy." An earlier
  version of this entry, written from a search summary, said the card
  "links" the two; the card says "potentially linked", and authoring-
  standards.md carried "ties" until 2026-08-18. Tier-1 evidence that
  anti-sycophancy pressure can overcorrect, stated at the strength the
  card gives it.
## Tier 1: other vendor documentation

Primary documentation for models other than Claude. Rank it as tier 1 for
claims about its own models only.

### OpenAI GPT-5.1 and GPT-5.2 prompting guides
- URLs: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide ,
  https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide
- Last verified: 2026-08-15 (fetched)
- Supports: GPT-5.1 errs toward excessive concision, so prompt for
  persistence and completeness; new `none` reasoning mode; tool-eagerness
  guidance; a metaprompting section that uses the model on its own prompts.
  GPT-5.2 is lower-verbosity with stronger instruction adherence, and the
  guide adds explicit length clamps, scope constraints ("EXACTLY and ONLY
  what the user requests"), and a `minimal → none` effort migration.
  Corroborates that per-release deltas are real outside Anthropic, and that
  each release ships its own prompt changes.

### Gemini 3 developer guide
- URL: https://ai.google.dev/gemini-api/docs/gemini-3
- Last verified: 2026-08-15 (fetched)
- Supports: verbatim, Gemini 3 "may over-analyze verbose or overly complex
  prompt engineering techniques used for older models"; replace
  chain-of-thought scaffolding with `thinking_level: "high"` and simplified
  prompts; remove explicit `temperature` and use the 1.0 default, since low
  values cause "looping or performance degradation on complex tasks"; less
  verbose by default; put the question after the data. Third independent
  vendor stating that prompts tuned for older models over-steer newer ones.
## Tier 2: research

### Wharton GAIL chain-of-thought tech report (Meincke et al., 2025)
- URL: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/
- Last verified: 2026-08-18 (re-fetched; report dated June 8, 2025;
  GPQA Diamond, 198 questions, 25 trials per condition)
- Supports: on the three reasoning models tested, explicit CoT prompting
  gave "Small average improvements for o3-mini (2.9%) and o4-mini (3.1%)"
  and a "Performance decrease for Gemini Flash 2.5 (-3.3%)", at "20-80%
  (10-20 seconds) more time"; on the five non-reasoning models (Sonnet 3.5,
  Gemini 2.0 Flash, GPT-4o-mini, GPT-4o, Gemini Pro 1.5) average gains were
  4.4–13.5% with mixed results at the perfect-accuracy threshold and 35–600%
  more time. Verbatim conclusion: "For reasoning models, the minimal
  accuracy gains rarely justify the increased response time." Grounds the
  old-patterns entry on CoT scaffolding for reasoning targets; the range
  is −3.3% to +3.1%, not "2.9–3.1%", and the models are mid-2025 vintage.

### To CoT or not to CoT (Sprague et al., arXiv 2409.12183, ICLR 2025)
- URL: https://arxiv.org/abs/2409.12183
- Last verified: 2026-08-18 (abstract and full text fetched and read; v3 of
  7 May 2025)
- Models: 14 instruction-tuned models of 2023–2024 vintage (Llama 2 7B,
  Mistral 7B, Llama 3.1 8B/70B, Gemma 2 9B, Phi-3, Qwen 7B/72B, gpt-4o-mini
  and gpt-4o 2024 releases, Gemini 1.5 Flash/Pro, claude-3-haiku,
  claude-3-5-sonnet-20240620) over 20 datasets, plus "a quantitative
  meta-analysis covering over 100 papers using CoT".
- Supports, verbatim: "CoT gives strong performance benefits primarily on
  tasks involving math or logic, with much smaller gains on other types of
  tasks"; "On MMLU, directly generating the answer without CoT leads to
  almost identical accuracy as CoT unless the question or model's response
  contains an equals sign". The finding is about prompt-based CoT on
  pre-reasoning-era models; the vault note that paraphrased it as "minimal
  or negative" overstated it. Cited by the vault's CoT note; not a basis
  for any artifact claim beyond "CoT gains concentrate in math and
  symbolic tasks".

### The Prompt Report (Schulhoff et al., arXiv 2406.06608)
- URL: https://arxiv.org/abs/2406.06608
- Last verified: 2026-08-15 (via vault)
- Supports: standard vocabulary and taxonomy of prompting techniques.

### Which Prompting Technique Should I Use? (arXiv 2506.05614)
- URL: https://arxiv.org/abs/2506.05614
- Last verified: 2026-08-15 (via vault)
- Supports: technique effectiveness depends on task type — grounds matching
  degrees of freedom and guidance style to the task.

### Prompt underspecification (Yang et al., arXiv 2505.13360, ACL Findings 2026)
- URL: https://arxiv.org/abs/2505.13360
- Last verified: 2026-08-18 (abstract re-fetched, v3 of 24 Apr 2026; full
  HTML text read for the model list)
- Models tested (Sec 3.2): Llama-3.3-70B-Instruct, gpt-4o-2024-08-06, and
  o3-mini; the model-update study adds gpt-4o 05-13/11-20 and Llama-3/3.1
  70B; the optimizer study runs on Llama3.3-70b-instruct only; Appendix D
  reports the pattern also holds on gemini-2.5-flash. No Claude model is
  tested. Treat every percentage below as a 2024–2025 open-weight and
  GPT-4o-era measurement.
- Supports: the both-sided constraint on any anti-addition guidance. Models
  infer unstated requirements correctly about 41.1% of the time, so gaps are
  real and consequential: under-specified prompts are "2x as likely to
  regress across model or prompt changes, sometimes with accuracy drops
  exceeding 20%". But the paper also finds that "simply specifying all
  requirements does not consistently help, as models have limited
  instruction-following ability and requirements can conflict. Standard
  prompt optimizers likewise provide little benefit." Its remedy is
  requirements discovery, evaluation, and monitoring with the human in the
  loop — requirements-aware optimization "improve[s] performance by 4.8% on
  average over baselines". Also: "stronger LLMs are more likely to guess
  requirements: o3-mini can guess 44.7% of unspecified requirements, a
  20.2% increase compared to Llama3.3-70b-instruct". Grounds refine-prompt's
  design: surface the gap to the user as an offer rather than filling it
  silently, and do not overcorrect into stripping. Tasks studied are code
  explanation, trip advisory, and product description, so treat the
  percentages as directional outside those domains.

### PromptBridge: cross-model prompt transfer (arXiv 2512.01420)
- URL: https://arxiv.org/html/2512.01420
- Last verified: 2026-08-15 (fetched)
- Supports: "model drifting" — a prompt tuned for one model transfers badly
  to another, measured across GPT-4o, o3, o4-mini, GPT-5, Llama-3.1-70B,
  Qwen3-32B, and Gemma3-27B (December 2025). A GPT-5-optimized prompt scored
  99.39 percent on GPT-5 and 68.70 percent on Llama-3.1-70B; cross-model
  adaptation beat direct transfer by 27.39 percent relative on SWE-Bench
  Verified and 39.44 percent on Terminal-Bench. Caveat: single-group
  preprint, not replicated. Grounds refine-prompt's re-check-on-target-change
  line. Note what it does not show: the gains come from optimizing against
  the target with measurements, not from the refiner sharing the target's
  identity.

### Prompt sensitivity does not track scale (JudgeSense, arXiv 2604.23478)
- URL: https://arxiv.org/html/2604.23478v2
- Last verified: 2026-08-18 (abstract and full v2 text fetched and read;
  v2 dated 7 May 2026; 13 judge models run April 2026: GPT-5.5, GPT-4o,
  GPT-4o-mini, Claude Opus 4.7, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini
  2.5 Flash, Llama-3.1-70B, Mistral small, Qwen-2.5-72B, DeepSeek-R1, Qwen
  3.6 Flash, DeepSeek-V4 Flash)
- Supports: the paper's stated finding, verbatim from the abstract:
  "Crucially, we find that model scale is not a reliable proxy for
  consistency; notably, as an interesting result in our analysis, the
  largest and newest models are not the most consistent." Within-vendor
  inversions: "Claude Opus 4.7 below Claude Haiku 4.5; GPT-5.5 below
  GPT-4o" on coherence-judgment stability (Opus–Haiku directional with
  overlapping CIs; GPT-5.5–GPT-4o statistically separated). The 8.5%
  (GPT-4o) and 61.3% (gemini-2.5-flash) flip rates are the introduction's
  motivating example, not a capability ordering. Correction recorded
  2026-08-18: an earlier version of this entry, written from a search
  summary, cited these two numbers as corroboration that "weaker models ...
  are more sensitive to wording"; the paper says the opposite, and its
  authors add that reasoning-tuned judges ran at a different token budget
  ("an uncontrolled confound"). What survives for refine-prompt: prompt
  sensitivity is model-specific and must be measured on the target, not
  inferred from its tier. Judge setting only.

### Model-specific prompting strategies (VMware, arXiv 2402.10949)
- URL: https://arxiv.org/pdf/2402.10949.pdf
- Last verified: 2026-08-18 (abstract and full text fetched and read; v2
  of 20 Feb 2024; Battle & Gollapudi, VMware NLP Lab)
- Models: Mistral-7B-Instruct-v0.1, Llama-2-13b-chat-hf, Llama-2-70b-chat-hf
  on GSM8K; 60 system-message combinations with and without CoT; DSPy as
  the optimizer. Commercial models were named as not tested ("financially
  prohibitive").
- Supports, verbatim: "results do not universally generalize across models"
  and "employing an automated prompt optimizer emerges as the most effective
  method for enhancing performance, even when working with smaller
  open-source models"; conclusion: "the automatically generated prompts
  perform better and generalize better than hand-tuned 'positive thinking'
  prompts", with the caveat that "Mistral-7B struggled to optimize its own
  prompt until it had 100 questions to work with". Grounds the model-and-
  dataset specificity of prompts. Caveat: 2023–2024 open-weight models of
  7–70B, so directional for current models rather than current evidence.

### Context Rot study (Chroma, 2025)
- URL: https://www.trychroma.com/research/context-rot
- Last verified: 2026-08-18 (page fetched and read; report dated July 14,
  2025; 18 models: Claude Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5, Haiku
  3.5; o3, GPT-4.1 family, GPT-4o, GPT-4 Turbo, GPT-3.5 Turbo; Gemini 2.5
  Pro/Flash, 2.0 Flash; Qwen3-235B/32B/8B)
- Supports, verbatim: "We observe that model performance varies
  significantly as input length changes, even on simple tasks" and "their
  performance grows increasingly unreliable as input length grows"; "Even a
  single distractor reduces performance relative to the baseline"; on
  LongMemEval, "Across all models, we see significantly higher performance
  on focused prompts compared to full prompts" (about 300 versus 113k
  tokens). No single headline percentage is given; results are per-
  experiment curves. Corroborates the aggregate always-loaded budget rule.
  Vintage: mid-2025 models; no Claude 4.5+ or GPT-5 tested.

### GEPA / automatic prompt optimization (Agrawal et al., ICLR 2026)
- URLs: https://github.com/gepa-ai/gepa , https://arxiv.org/abs/2507.19457
- Last verified: 2026-08-18 (arXiv abstract and full text fetched and read;
  v2 of 14 Feb 2026, "Accepted to ICLR 2026 (Oral)"; repo fetched
  2026-08-15)
- Paper numbers, verbatim: "Across six tasks, GEPA outperforms GRPO by 6%
  on average and by up to 20%, while using up to 35x fewer rollouts" and
  "GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10%
  (e.g., +12% accuracy on AIME-2025)". Models: Qwen3 8B and GPT-4.1 mini
  (openai/gpt-4.1-mini-2025-04-14); tasks HotpotQA, AIME, LiveBench-Math,
  IFBench, PUPA, HoVer. The comparison is against RL (GRPO) and against
  another optimizer, not against a human iterating on wording by hand.
- Supports: with an eval set, an automated optimizer improves on RL and on
  MIPROv2 at far lower rollout cost — grounds the evaluation-scenarios-
  before-polish emphasis. Repo confirms: works from as few as 3 graded
  examples. The claim "automated optimizers beat manual wording iteration"
  rests on VMware 2402.10949 (7–70B models, 2024) and this paper's
  optimizer-versus-optimizer results, while arXiv 2505.13360 finds
  "Standard prompt optimizers likewise provide little benefit" on its
  tasks; state it as "can beat" with a graded set, not as a general law.
  Also: the reflection model is deliberately separate from the model being
  optimized, and DSPy's guidance is to use a larger model as the reflection
  model when optimizing a smaller one. Evidence gap recorded 2026-08-15: no
  study found measures whether a prompt is refined better by the model that
  will run it than by a different model told which model it targets. Existing
  self-optimization work has each model optimize its own prompts with no
  cross-model arm, and self-preference bias means a same-model refiner may
  favor its own output without it being better.

### Sycophancy: origin in preference training (Sharma et al., arXiv 2310.13548)
- URL: https://arxiv.org/abs/2310.13548
- Last verified: 2026-08-18 (abstract re-fetched; v4 PDF text read for the
  model list; ICLR 2024)
- Models (Sec 3): "claude-1.3, claude-2.0, gpt-3.5-turbo, gpt-4, and
  llama-2-70b-chat" — all 2023 assistants. The arXiv listing abstract calls
  them "five state-of-the-art AI assistants"; the v4 PDF abstract says
  "five AI assistants".
- Supports, verbatim: the five "consistently exhibit sycophancy across four
  varied free-form text-generation tasks", and "sycophancy is a general
  behavior of AI assistants, likely driven in part by human preference
  judgments favoring sycophantic responses" — grounds treating sycophancy
  as a training-induced default rather than an occasional slip. Effect
  sizes were 2023-era ("Claude 1.3 wrongly admits mistakes on 98% of
  questions"; "GPT-4 being the most robust"); the tag-question study below
  shows the direction has since reversed on current models, so cite this
  paper for the mechanism, not for current rates.

### Ask Don't Tell (Dubois et al., arXiv 2602.23971)
- URL: https://arxiv.org/html/2602.23971v1
- Last verified: 2026-08-15 (fetched)
- Supports: the ranked measured effect of prompt-level mitigations on GPT-4o,
  GPT-5, and Sonnet-4.5 (lower beta = less sycophancy). No mitigation
  β=1.13; explicit "respond without being sycophantic" β=0.51; 1-step
  question reframing (same model restates the input as a question, then
  answers it) β=0.16; 2-step reframing by a separate model β=−0.55. Rewrite
  of the user's first person into third person failed (β=1.19 vs 1.42
  unmitigated) — "user reframing is not an effective mitigation strategy".
  Grounds the anti-sycophancy rule's restate-as-a-question line, and the
  choice to keep a plain anti-sycophancy statement alongside it.

### BrokenMath (arXiv 2510.04721, NeurIPS 2025)
- URL: https://arxiv.org/html/2510.04721v1
- Last verified: 2026-08-15 (fetched)
- Supports: sycophancy on false theorems is widespread (GPT-5 29%,
  Gemini-2.5-Pro 37.5%, DeepSeek-V3.1 70.2%); an instruction to validate the
  problem before the model solves it reduces but does not remove it (34.1%
  absolute gain for DeepSeek-V3.1); confidence-score filters largely fail;
  self-sycophancy is worse — models endorse false claims they believe they
  produced, up to 15.6% higher.

### Pushback and answer flipping: FlipFlop, TRUTH DECAY, unfaithful capitulation
- URLs: https://arxiv.org/abs/2311.08596 (FlipFlop, Laban et al., Salesforce,
  v2 Feb 2024) , https://arxiv.org/abs/2503.11656 (TRUTH DECAY, Algoverse,
  Feb 2025) , https://arxiv.org/abs/2605.29087 (unfaithful capitulation, Li,
  Krishnan & Padman, CMU, May 2026)
- Last verified: 2026-08-18 (all three abstracts and full HTML texts fetched
  and read). An earlier version of this entry, written from a search
  summary, attributed all three findings below to TRUTH DECAY; they come
  from three papers on three model vintages.
- FlipFlop — ten 2023 models (Llama2-7b/13b-chat, Mistral-7b, Command-XL,
  Claude V1.3, Claude V2, PaLM2-Bison, Gemini-Pro, GPT3.5-Turbo, GPT-4) on
  seven classification tasks. Verbatim: "models flip their answers on
  average 46% of the time and that all models see a deterioration of
  accuracy between their first and final prediction, with an average drop
  of 17%". Per-model drop ranged from −1.3 (Command-XL) to −35.1 (Claude
  V1.3). This is the source of the 46%/17% figures.
- TRUTH DECAY — three models, "Claude Haiku" (Claude 3 family, 2024),
  GPT-4o-mini, Llama 3.1 8B Instruct, over TruthfulQA and MMLU-Pro with 1,
  3, and 7 follow-up turns. Verbatim: "sycophantic behaviors can cause
  accuracy drops of up to 47%, with models progressively drifting away from
  factual correctness under persistent user influence"; the authors state
  they did not test "GPT o1, Claude 3.5 Sonnet, or Deepseek R1". Grounds
  the claim that sustained multi-turn pressure moves models off correct
  answers, on small 2024 models.
- Unfaithful capitulation — Qwen3-32B, GPT-OSS-20B, Gemma-4-31B-it, 2026,
  under a 9-round adversarial protocol. Verbatim: "the chain-of-thought
  stays factually correct from first turn to last while the emitted answer
  flips wrong. We call this unfaithful capitulation (UC)"; the latent-
  correct rate at the flip "clusters near 50% in think mode and collapses
  to 11-15% under no_think". No Claude model tested.
- Together these ground the hold-a-position section as a mechanism that
  recurs across generations; none of the three measures a current Claude
  model, and the tag-question study below finds Claude Fable 5 the most
  resistant of 45 models to one form of pushback. Cite the mechanism, not
  the rates, for current models.

### Tag questions and the generational reversal (arXiv 2607.23976)
- URL: https://arxiv.org/html/2607.23976
- Last verified: 2026-08-18 (abstract and full HTML text re-fetched and
  read; arXiv v1 of 27 Jul 2026; single author, Tapan Parikh, Cornell Tech;
  no venue — treat as an unreviewed preprint)
- Design: 20 frozen, ground-truth-free decision items between two
  defensible options, counterbalanced, "Reply with only Yes or No", four
  samples per cell, 45 models from nine vendors served via OpenRouter in
  one window (mid-2023 to mid-2026 releases). The author writes: "We treat
  the data as a dated characterization of served model behavior, not a
  timeless property."
- Supports: across 45 models the confirmation-tag effect spans 64 points,
  from MythoMax-L2-13B at +32% to "Claude Fable 5 at −32% [−45,−19], which
  endorses the user's pick a third less often"; the field drifts at "a
  descriptive −5.9 points per year", with the inference resting on
  within-family sign flips ("Claude +7%→−32%"). How the resisters resist,
  verbatim: "across the 17, the mean reject share rises from 33% (ask) to
  48% (tag) ... fifteen of the seventeen resist by saying No more. The two
  exceptions decline the frame instead: Claude Fable 5's rejects fall under
  the tag (5% → 2%) while its hedge share jumps from 44% to 79%". So Fable
  5 does not contradict more; it declines the forced yes/no and names the
  unstated alternative. Correction recorded 2026-08-18: an earlier version
  of this entry placed the 33%→48% rejection rise next to Fable 5's −32% as
  if it described Fable 5; it is the mean of the other resisters. The
  resistance is grammar-keyed: all 45 models fold for a tentative
  "…maybe?" (+19.6 points mean; Fable 5 at +14) and every resister affirms
  a bare commitment such as "I've settled on X" (+6 to +49). Grounds the
  judge-the-claim-the-same-way line and the overcorrection section, with
  the caveat that Fable 5's overcorrection takes the form of hedging.

### Sycophancy taxonomy and expert survey (arXiv 2605.21778)
- URL: https://arxiv.org/html/2605.21778v1
- Last verified: 2026-08-15 (fetched)
- Supports: sycophancy splits by referent (the user's position vs the user as
  a person) and explicitness. Among 106 experts, explicit praise of the user
  is the highest-consensus case (M=1.74) while implicit deference rates near
  neutral (M=0.21) — grounds targeting praise openers directly. Also: warmth
  training raises sycophancy, different cells need different mitigations, and
  one-size-fits-all suppression risks manufactured disagreement.

### ELEPHANT social sycophancy (Cheng et al., arXiv 2505.13995)
- URL: https://arxiv.org/abs/2505.13995
- Last verified: 2026-08-18 (abstract and full v2 HTML text fetched and
  read; v2 of 29 Sep 2025; evaluations run March–September 2025)
- Models (11): GPT-5, GPT-4o (2024-11-20), Gemini-1.5-Flash, Claude Sonnet
  3.7, Llama-3-8B, Llama-4-Scout, Llama-3.3-70B, Mistral-7B-v0.3, Mistral-
  Small-24B, DeepSeek-V3, Qwen2.5-7B. No Claude 4-era model.
- Supports: defines social sycophancy as "excessive preservation of a
  user's face (their desired self-image)" and names four dimensions
  (verbatim): "(1) Validation sycophancy: validating the users' emotions
  and perspectives ... (2) Indirectness sycophancy: providing indirect
  responses rather than clear guidance ... (3) Framing sycophancy:
  unquestioningly adopting the user's framing ... (4) Moral sycophancy:
  affirming whichever stance the user takes". Headline, verbatim: "they
  preserve user's face 45 percentage points more than humans in general
  advice queries"; and "There is no consistent pattern with model size ...
  suggesting that social sycophancy is invariant to model size". An earlier
  version of this entry listed three types; v2 names four (v1 named five
  behaviors). Grounds the correct-the-premise line and the no-hedging line.
## Artifact tooling

### skill-rule-shared scripts (formerly under skill-rule-creator) — Claude Code CLI surface
- Source: `claude --help` and a probe run of `claude -p --output-format json`
  (Claude Code 2.1.229)
- Last verified: 2026-08-15 (inspected)
- Supports: the flags the eval scripts depend on — `--disable-slash-commands`
  ("Disable all skills"), `--safe-mode` (disables CLAUDE.md, skills, plugins,
  hooks, and other customizations while auth, tools, and permissions still
  work), `--append-system-prompt`, `--max-budget-usd` (print mode only),
  `--permission-mode` with choices acceptEdits, auto, bypassPermissions,
  manual, dontAsk, plan, and `--output-format stream-json` requiring
  `--verbose`. The `result` event carries `total_cost_usd`, `duration_ms`,
  `num_turns`, `is_error`, `result`, and a `usage` map with `input_tokens`,
  `output_tokens`, and the cache token counts — these are the metric field
  names ab_eval.py reads. The `system`/`init` event carries
  `claude_code_version`, `model` (the resolved id), `skills` (the roster of
  loaded skill names), `slash_commands`, `plugins`, and `tools` — the
  fields the scripts record per run. `ab_eval.py --mode skill` builds its
  targeted baseline with `--settings '{"skillOverrides":{"<name>":"off"}}'`
  and `--disallowed-tools "Skill(<name>)"` as a second guard.
- Caveat: CLI flags and the result schema are internal to Claude Code and can
  change between releases. When a script's output looks wrong, suspect a
  flag or field rename before suspecting the model.

### skill-creator plugin eval harness — vendor runner and why the in-house scripts exist
- Sources: https://code.claude.com/docs/en/skills (section "Run evals with
  skill-creator") ; https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
  (March 3, 2026) ; https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md
  and its `scripts/run_eval.py`, `scripts/run_loop.py`,
  `scripts/aggregate_benchmark.py`, `eval-viewer/generate_review.py`,
  `agents/comparator.md`
- Last verified: 2026-08-18 (doc, blog, and SKILL.md fetched and read)
- What exists: a vendor harness that "automates the comparison loop inside
  Claude Code": eval cases in `evals/evals.json`, one subagent per case,
  grading to `grading.json`, a with-versus-without benchmark
  (`benchmark.json`, pass rate, time, tokens, mean ± stddev), a blind A/B
  comparator between two skill versions, and a description-tuning loop
  (`run_loop.py`: 60/40 train/test split, three runs per query, up to five
  iterations, best description chosen by test score). The blog reports
  "improved triggering on 5 out of 6 public skills". `run_eval.py` writes
  a temporary command file into `.claude/commands/`, runs `claude -p`, and
  detects a trigger from stream events.
- What the in-house scripts add over the vendor harness: a rule A/B mode
  (`--mode rule`), near-miss trigger sets graded by the author, cost and
  transcript capture per run, and a stable path under this skill. What the
  vendor harness has that they lack: the blind comparator agent, the
  train/test description optimizer, and the HTML review viewer. Neither is
  a reason to drop the other; when a description needs tuning rather than
  measuring, the vendor loop is the tool.

### Claude Code dynamic workflows
- URLs: https://code.claude.com/docs/en/workflows (fetched as `workflows.md`)
- Last verified: 2026-08-18 (fetched)
- Supports: a workflow needs a user opt-in, and "Claude treats a direct
  request as the same opt-in" as the `ultracode` keyword — so a skill whose
  body launches a saved workflow is itself only ever run on the user's
  request. Launch prompting by permission mode, verbatim for the row that
  matters to evals: "Bypass permissions, `claude -p`, Agent SDK — Never. The
  run starts immediately." A trigger or A/B eval of a skill that launches a
  workflow must therefore run with `CLAUDE_CODE_DISABLE_WORKFLOWS=1`
  ("Read at startup, so it applies wherever you set it"), or the eval can
  start the real run. Also: "Every run writes its script to a file under
  your session's directory in `~/.claude/projects/`" — the doc names the
  script, not the result. Resume "works within the same Claude Code
  session"; a `Large workflow` warning appears past 25 agents or a
  projected 1.5 million tokens. Saved workflows live in
  `~/.claude/workflows/` or `.claude/workflows/` and run as `/<name>` with
  an `args` global.

## Tier 3: community (corroborated or labeled)

### SkillsBench (skillsbench.ai and arXiv 2602.12670)
- URLs: https://www.skillsbench.ai/ , https://arxiv.org/abs/2602.12670
- Last verified: 2026-08-18 (site cache read; paper v4 abstract and full
  HTML text fetched and read; v4 dated 14 Jun 2026)
- Supports (labeled as a benchmark preprint plus its vendor site, not peer
  reviewed): 87 tasks across eight domains; the paper's aggregate covers 18
  model–harness configurations (GPT-5.5, Claude Opus 4.8/4.7, Sonnet 4.6,
  Gemini 3.1 Pro / 3.5 Flash, GLM 5.1, DeepSeek V4, and others, on
  OpenHands, Codex, Claude Code, Gemini CLI); the site leaderboard extends
  it to 25 configurations, 24 paired, up to 3 trials per task. Verbatim
  headline: "Curated Skills raise the average pass rate from 33.9% to
  50.5% (+16.6 percentage points; 25.5% normalized gain), with
  configuration-level gains ranging from +4.1 to +25.7 pp." Correction
  recorded 2026-08-18: an earlier version of this entry gave "about 15.8
  percentage points" as the average; 15.8 is the OpenHands + GPT-5.5 row
  (51.5 → 67.3), not the mean. Directly relevant to authoring, verbatim:
  "Focused Skills with at most three modules outperform larger or
  exhaustive bundles, and smaller models with Skills can match larger
  models without them"; body: "compact and standard-length Skills (+19.0
  and +21.5 pp) outperform detailed (+14.5 pp) and comprehensive
  documentation (+0.7 pp)"; and "Self-generated Skills land below the
  no-Skills baseline on all three configurations". Grounds evaluating.md's
  point that published averages do not transfer to a specific artifact
  ("Skill efficacy is therefore an empirical property of a specific agent
  stack rather than a universal constant"), corroborates the paired
  with/without design, and adds tier-2 support for keeping skills compact.

### Simon Willison on skills (2025-10-16)
- URL: https://simonwillison.net/2025/Oct/16/claude-skills/
- Last verified: 2026-08-15 (via vault)
- Supports: skills' startup cost is a few dozen tokens versus heavyweight
  alternatives; corroborates the loading-model framing of the decision
  framework.

### obra/superpowers skill library
- URL: https://github.com/obra/superpowers
- Last verified: 2026-10-24 (README fetched for the research-skill
  decoupling pass: it has no configuration, settings, or local-override
  mechanism; the only environment variables are telemetry opt-outs
  (`SUPERPOWERS_DISABLE_TELEMETRY`); "Installation differs by harness. If
  you use more than one, install Superpowers separately for each one";
  skills "trigger automatically"). Previous: 2026-08-15 (via vault).
- Supports: evaluation scenarios before documentation; common authoring
  mistakes (inconsistent terminology, vague descriptions). Corroborates
  tier 1. Negative evidence for the research skill's design: the largest
  community skill library ships no per-user config at all.

### anthropics/skills repository README
- URL: https://github.com/anthropics/skills
- Last verified: 2026-10-24 (README fetched).
- Supports: "Each skill is self-contained in its own folder with a
  `SKILL.md` file"; distribution is through the plugin marketplace
  (`/plugin marketplace add anthropics/skills`, then `document-skills` or
  `example-skills`), claude.ai, and the Skills API; "These skills are
  provided for demonstration and educational purposes only". Nothing on
  user-specific configuration, paths, or inter-skill dependencies.

### Community skills that ship a local config file (glebis/claude-skills disk-cleanup; EveryInc compound-engineering ce-debug; devcodex load-profile)
- URLs: https://github.com/glebis/claude-skills (skills/disk-cleanup/SKILL.md) ;
  https://github.com/EveryInc/compound-engineering-plugin (skills/ce-debug/SKILL.md) ;
  https://github.com/devcodex-labs/devcodex (content/skills/load-profile/SKILL.md)
- Last verified: 2026-10-24. Found with `gh search code 'config.local
  filename:SKILL.md'` (15 hits; these three read as raw files; the other
  twelve not opened). Tier 3, unverified beyond the SKILL.md text; none
  was run.
- Supports: the committed-example-plus-gitignored-real pattern exists in
  the wild for skills. disk-cleanup, verbatim: "`config.json` ships
  **generic, public-safe defaults**. Anything personal ... or
  machine-specific goes in **`config.local.json`** (gitignored).
  `load_config()` deep-merges it over `config.json`: **lists are unioned**
  ..., scalars override. See `config.local.example.json` for the shape";
  it also has a "Setup mode" that offers to build the local file by asking
  the user, then "Confirm what was saved. Never commit it." Its directory
  holds `config.json`, `config.local.example.json`, `targets.json`,
  `scripts/`, and its own `.gitignore` (not read). ce-debug reads a
  project-level `.compound-engineering/config.yaml` and says "Do not read
  it from `config.local.yaml`" for one key — a local overlay exists there
  but is excluded for that setting. load-profile (Chinese-language) layers
  `config.local.json` over `config.json` as a "local overlay" read only
  when the user or project names it. Common to all three: the merge is done
  by a bundled script or by instructing the model to read the file; none
  uses `!` dynamic context injection, so each costs a tool call per
  invocation and depends on the model following the instruction.

### Datadog Security Labs — malicious skills and dynamic context (2026-05-11)
- URL: https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/
- Last verified: 2026-10-24 (fetched, targeted extraction).
- Supports: the risk side of `!` injection in a shared skill. "These shell
  commands run before the rendered skill content is sent to Claude";
  "Instructions shipped with a codebase can influence what happens on a
  developer machine"; advice to "Review them before use, restrict shell
  execution where you can, require review for `.claude/` changes", and
  that organizations can disable it for user, project, plugin, and
  additional-directory skills. A public skill that relies on injection
  should therefore keep the injected command to a bundled, readable script
  and degrade when the placeholder is replaced by policy. Tier 3 (vendor
  security blog), consistent with the Claude Code skills doc.

### Community prompt-refinement skills (prompt-architect, prompt-improver)
- URLs: https://github.com/ckelsoe/prompt-architect ,
  https://github.com/wagnersza/prompt-improver
- Last verified: 2026-08-15 (fetched)
- Supports (unverified community practice): delivery shape of diagnosis +
  improved prompt + model-settings note (adopted in refine-prompt);
  prompt-architect's 31-framework menu and progressive questioning were
  reviewed and rejected as conflicting with tier-1 minimum-necessary-
  structure and one-default-with-escape-hatch guidance.

### Community CLAUDE.md guides (agentlint, dev.to, iwoszapar, hackernoon)
- URLs: https://www.agentlint.app/blog/claude-md-best-practices-2026/ ,
  https://dev.to/nishilbhave/claudemd-best-practices-the-complete-2026-guide-435j ,
  https://www.iwoszapar.com/p/claude-code-best-practices ,
  https://hackernoon.com/navigating-claude-code-skills-that-actually-fire
- Last verified: 2026-08-15 (via vault)
- Supports (unverified community practice unless noted): lead CLAUDE.md
  with exact commands; pair each rule with enforcement or mark it advisory
  (now corroborated by tier 1 hooks guidance); under-triggering as the
  dominant skill failure with pushy descriptions as the fix — corroborated
  only by Anthropic's skill-creator SKILL.md ("Claude has a tendency to
  'undertrigger' skills ... make the skill descriptions a little bit
  'pushy'"); the Claude Code skills doc treats "Skill not triggering" and
  "Skill triggers too often" symmetrically with no frequency claim, and
  the prompting best-practices page warns of over-triggering on Opus
  4.5/4.6, so the direction is unmeasured on current models and
  authoring-standards.md says to measure it; ~200-line CLAUDE.md ceiling
  (now corroborated by tier 1 memory docs: "target under 200 lines per
  CLAUDE.md file").
## Artifact subject-matter sources
### notes skill, ste100 rule — ASD-STE100 official site (About, FAQ, Issue 9 PDF)
- URLs: https://www.asd-ste100.org/about_STE.html ,
  https://www.asd-ste100.org/STE_faq.html ,
  https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf
- Last verified: 2026-08-15 (FAQ re-fetched for the ste100 rule pass;
  About and Issue 9 counts via fetched search summary)
- Supports: current issue is Issue 9 (January 2025), an international
  standard as of Issue 9; Issue 10 scheduled January 2028; 53 writing rules
  in 9 sections; ~900 approved words, one meaning and one part of speech
  each; ~1,200 non-approved words with suggested replacements; 20-word
  maximum sentences in procedures and 25-word in descriptive text;
  imperative, active-voice procedural language; scope is procedural and
  descriptive maintenance text; the FAQ quote "not intended for
  general-purpose writing" is verbatim; the FAQ also says many STE
  principles can be adopted in other writing contexts, which grounds the
  ste100 rule's user-chosen scope (documentation plus technical
  explanations in chat, but not casual conversation or code).
### ai-retrospective skill — runtime guidance entry points
- URLs: https://code.claude.com/docs/llms.txt ,
  https://www.anthropic.com/engineering ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Last verified: 2026-08-15 (all three fetched)
- Supports: `llms.txt` is a compact index of every Claude Code doc page, and
  those pages accept a `.md` suffix for clean markdown — fetching the rendered
  `/docs/en/overview` page instead costs thousands of tokens on install
  instructions. The engineering index lists posts with dates, so it works as a
  freshness check rather than a fixed post list. Page URLs confirmed present:
  `best-practices`, `sub-agents`, `skills`, `memory`, `hooks-guide`,
  `settings`, `permissions`, `mcp`, `workflows`, `costs`, `output-styles`.
  The tool-use overview supports steerable tool-calling boundaries via the
  system prompt and links a dedicated parallel-tool-use page.
### ai-retrospective skill — session analysis and compaction
- URLs: https://code.claude.com/docs/en/costs.md ,
  https://code.claude.com/docs/en/best-practices.md
- Last verified: 2026-08-15 (both fetched)
- Supports: `/insights` analyzes up to 200 recent local sessions and writes an
  HTML report on how the user works, including friction points — adjacent to
  ai-retrospective from the other direction (many sessions, user patterns,
  versus one session, agent execution), so the skill points at it rather than
  duplicating it. Auto-compaction "summarizes older history to free space"
  and `/compact` "reads the conversation it summarizes". Recorded evidence
  gap: neither page states whether the on-disk transcript keeps the
  pre-compaction turns, and none of 92 local transcripts had ever compacted,
  so the ai-retrospective skill now instructs the agent to verify this on the
  first compacted session it meets rather than assert it. Also grounds the
  context-window-as-binding-constraint framing used to rank findings by cost.
### research skill — tier 1: Anthropic and Claude Code
- URLs: https://www.anthropic.com/engineering/multi-agent-research-system ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool ,
  https://code.claude.com/docs/en/tools-reference (WebFetch and WebSearch
  behavior sections) , https://code.claude.com/docs/en/sub-agents ,
  https://code.claude.com/docs/en/workflows , and the "Research and
  information gathering" and "Subagent orchestration" sections of the
  prompting best-practices page listed under Tier 1 above
- Last verified: 2026-08-15 (all fetched)
- Supports: orchestrator-worker research with parallel subagents; effort
  scaling by query complexity ("Simple fact-finding requires just 1 agent
  with 3-10 tool calls, direct comparisons might need 2-4 subagents with
  10-15 calls each, and complex research might use more than 10 subagents");
  "start wide, then narrow" because agents "default to overly long, specific
  queries that return few results"; each subagent brief needs "an objective,
  an output format, guidance on the tools and sources to use, and clear task
  boundaries"; early agents "consistently chose SEO-optimized content farms
  over authoritative but less highly-ranked sources" until source-quality
  heuristics were added; observed failure modes (excess subagents for simple
  queries, endless search for nonexistent sources, duplicated subagent work,
  research continuing past sufficiency); "instilling good heuristics rather
  than rigid rules"; a citation pass after research; token usage explains
  80% of BrowseComp variance (the depth side of the depth-vs-breadth
  tension). Web search docs: citations always on with `cited_text` up to
  150 characters and `page_age`; "Simple factual queries typically use 1–3
  searches; comparative or multientity research can use 10 or more". Web
  fetch docs: fetches only URLs already seen in the conversation or in
  prior search/fetch results; explicit exfiltration warning; citations
  optional; PDF sizes (~125k tokens for a 500 kB paper). Claude Code tools
  reference: WebSearch returns titles and URLs only and "may issue up to
  eight backend searches per call"; WebFetch "is lossy by design" — a small
  model answers the extraction prompt, so "a result that says a page doesn't
  mention something may only mean the prompt didn't ask about it", with
  re-fetch or `curl` as the remedy; 15-minute cache; cross-host redirects
  returned rather than followed; a 200-call session search cap "counted
  across the main conversation and every subagent". Sub-agents doc: use
  subagents for self-contained work returning a summary and for parallel
  independent investigations; a subagent "doesn't see your conversation
  history"; concurrency 20, nesting depth 3. Workflows doc: `/deep-research`
  is a bundled workflow that "runs only when you invoke it" (the version
  anchor is in the Claude Code CHANGELOG, not this doc: 2.1.218 "Changed
  `/deep-research` to start only when invoked manually; Claude no longer
  launches it on its own"), fans out searches, cross-checks
  and votes on claims, and lists unverifiable claims as unverified; the
  "stop once two rounds in a row find nothing new" example. Prompting page:
  "Provide clear success criteria", "verify information across multiple
  sources", "develop several competing hypotheses. Track your confidence
  levels ... research notes file", and the subagent-overuse damping prompt.
### research skill — tier 1: other vendors' deep-research documentation
- URLs: https://developers.openai.com/api/docs/guides/deep-research ,
  https://ai.google.dev/gemini-api/docs/deep-research
- Last verified: 2026-08-15 (fetched)
- Supports (for their own products only): OpenAI recommends a clarification
  step before research, steering toward primary sources ("the original paper
  or official journal publication" over aggregators), `max_tool_calls` as
  the cost lever, and warns of prompt injection through web content with a
  worked exfiltration example. Google's loop is "Plan -> Search -> Read ->
  Iterate -> Output"; it recommends stating output structure, telling the
  agent how to handle missing data ("explicitly state they are projections
  or unavailable rather than estimating"), and "reviewing the citations
  provided in the response to verify the sources". Neither addresses
  contradictory sources or stopping.
### research skill — tier 2: agent benchmarks and audits
- URLs: https://arxiv.org/html/2506.06287 (Deep Research Bench, FutureSearch,
  May 2025) , https://arxiv.org/html/2504.12516 (BrowseComp, OpenAI, April
  2025) , https://arxiv.org/abs/2311.12983 (GAIA, 2023) ,
  https://arxiv.org/html/2509.04499 (DeepTRACE, Sept 2025) ,
  https://arxiv.org/html/2605.06635 (Cited but Not Verified, May 2026) ,
  https://arxiv.org/html/2604.03173v1 (reference hallucination in
  commercial LLMs and deep research agents, April 2026) ,
  https://arxiv.org/html/2404.10198v2 (ClashEval, NeurIPS 2024; via fetched
  search summary) , https://arxiv.org/html/2605.14473v4 (Does RAG Know When
  Retrieval Is Wrong?, July 2026) , https://arxiv.org/pdf/2504.18575
  (WASP, 2025; via fetched search summary) ,
  https://arxiv.org/abs/2506.18096 (Deep Research Agents roadmap survey)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports: Deep Research Bench — "forgetting information" is the strongest
  predictor of task failure (coefficient −0.843); repeated searches common;
  hallucination "not the central issue"; "a tendency towards satisficement
  rather than optimization" with minimum-effort answers; search terms
  "overly influenced" by task phrasing; best agent 0.51 against a ~0.8 noise
  ceiling. BrowseComp — humans solved 29.2% and gave up on 70.8% within two
  hours; accuracy scales with browsing effort and parallel sampling; models
  with browsing showed higher calibration error, "access to web tools may
  increase the model's confidence in incorrect answers"; success needs
  "strategic perseverance, flexible search reformulation, and ability to
  assemble fragmented clues". GAIA — questions "conceptually simple for
  humans yet challenging for most advanced AIs" (92% vs 15%). DeepTRACE —
  deep research agents 54.7–94.8% one-sided on debate queries, 53.6–97.5%
  unsupported statements, citation accuracy 50.3–79.1%; "more sources and
  longer answers do not translate into reliability". Cited but Not Verified
  — 14 models: link works >94%, content relevant >80%, but factual accuracy
  of the cited claim only 39–77%; raising tool calls from 2 to 150 dropped
  GPT-5.4's fact-check accuracy from 78.6% to 16.7% and Claude Opus 4.6's
  from 80% to 57.9% ("information overload effect"); recommends "depth of
  source understanding over breadth of source coverage" (the breadth side
  of the depth-vs-breadth tension). Reference hallucination — 3–13% of
  cited URLs fabricated even with web search, 5–18% non-resolving, deep
  research agents highest; a URL-check tool cut non-resolving citations to
  under 1% when the model acted on it. ClashEval — models adopt incorrect
  retrieved content over a correct prior over 60% of the time, more so when
  the wrong content is realistic and the model's prior confidence is low.
  Does RAG Know — standard RAG at 15% accuracy under adversarial
  misconception injection; conflict-aware decomposition helps. WASP —
  partial injection success up to 86%, "security by incompetence" rather
  than robust defense. Roadmap survey — definition and taxonomy of deep
  research agents; open challenges include sequential inefficiency and
  metric misalignment.
- Contradiction recorded 2026-08-15: Anthropic's post ties research quality
  to token spend (more effort → better on BrowseComp) while the 2026 audits
  find more retrieval into one context lowers citation factual accuracy.
  They measure different things (finding hard facts vs faithful synthesis);
  the research skill resolves it as fan-out into fresh contexts with a lean
  synthesizing context, and labels this a judgment call.
### research skill — tier 2: research methodology (academic and standards)
- URLs: https://www.ala.org/acrl/standards/ilframework (ACRL Framework,
  2016; revision draft out for comment through May 2026) ,
  https://wp.comminfo.rutgers.edu/ckuhlthau/information-search-process/
  (Kuhlthau ISP; via fetched search summary) ,
  https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html (Bates 1989)
  , Ellis 1989/1993 (via fetched search summary) ,
  https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
  (Cochrane Handbook 6.5.1, chapter 4, March 2025) ,
  https://www.prisma-statement.org/prisma-2020 (PRISMA 2020) ,
  https://arxiv.org/abs/2307.02612 (Wohlin et al., hybrid database search
  plus snowballing) and Wohlin 2014 snowballing guidelines (via search) ,
  https://gdt.gradepro.org/app/handbook/handbook.html (GRADE handbook) ,
  https://journals.sagepub.com/doi/10.1177/016146811912101102 (Wineburg &
  McGrew 2019, via fetched search summary) and
  https://www.scienceofboosting.org/project/lateral-reading/ (evidence
  base for lateral reading) , SIFT (Caulfield; library guides and Brodsky
  et al. 2021 via search) , Lord, Lepper & Preston 1984 and Mussweiler et
  al. 2000 (consider-the-opposite; via fetched search summary) , Nickerson
  1998 (confirmation bias; via search) ,
  https://aisel.aisnet.org/misq/vol31/iss1/7/ (Browne, Pitts & Wetherbe
  2007, MIS Quarterly) plus the AMCIS 2016 and TRR replications , Ilani et
  al. 2024 systematic review of stopping behavior (abstract) , capture–
  mark–recapture as a stopping rule (Kastner et al. 2009) and Booth 2010
  "How much searching is enough?" (via search) , Tetlock's Good Judgment
  Project findings (via fetched search summaries)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports: ACRL — "Authority Is Constructed and Contextual", "Research as
  Inquiry" (formulate questions from gaps and conflicting information;
  monitor for gaps), "Searching as Strategic Exploration" ("first attempts
  at searching do not always produce adequate results"; refine strategy
  from results), skeptical stance with self-awareness of bias. Kuhlthau —
  six stages with exploration before focus formulation; the uncertainty
  principle ("information commonly increases uncertainty in the early
  stages"). Bates — the evolving query, "bit-at-a-time" retrieval, and six
  techniques (footnote chasing, citation searching, journal run, area
  scanning, subject searches, author searching), which ground the chaining
  moves table. Ellis — starting, chaining, browsing, differentiating,
  monitoring, extracting, verifying, ending. Cochrane — "aim for high
  sensitivity, which may result in relatively low precision"; search
  multiple sources including grey literature, reference lists, and
  contacting experts; text words plus controlled vocabulary; avoid too many
  concepts; peer-review the search; document and report the search
  (PRISMA-S); "balance the thoroughness of the search with efficiency in
  the use of time and funds" (section 4.4.11 on stopping was not
  retrievable through the fetch). PRISMA 2020 — transparent, replicable
  reporting of sources, strategies, selection, and certainty. Wohlin — the
  hybrid strategy "identified 30 percent more primary studies" than either
  alone. GRADE — four certainty levels with their verbatim meanings; RCTs
  start high, observational low; rate down for risk of bias, inconsistency,
  indirectness, imprecision, publication bias; rate up for large effect,
  dose-response, residual confounding; certainty applies to the body of
  evidence per outcome, not per study — adapted in source-weighing.md.
  Wineburg & McGrew — fact-checkers "read laterally, leaving a site after a
  quick scan and opening up new browser tabs" while historians and students
  "read vertically" and fell for surface features; interventions of hours
  produce measurable gains. SIFT — Stop, Investigate the source, Find
  better coverage, Trace claims to the original. Lord et al. — a
  consider-the-opposite instruction "had greater corrective effect than more
  demand-laden alternative instructions to be as fair and unbiased as
  possible"; Mussweiler — considering the opposite reduces anchoring.
  Browne et al. — "people utilize a number of stopping rules to terminate
  search, and that the stopping rule used depends on the type of task";
  replications confirm for structured tasks and find drift for poorly
  structured ones. The five named rules (mental list, representational
  stability, difference threshold, magnitude threshold, single criterion)
  are trained knowledge verified only at abstract level on this pass. Ilani
  2024 — "the lack of a comprehensive model of factors affecting search
  stopping behavior" (the evidence-is-thin statement). Capture–recapture and
  Booth — empirical stopping estimates exist for systematic reviews but
  not for desk research. Tetlock — granular probabilities, frequent small
  updates, base rates and the outside view.
### research skill — tier 3: community
- URLs: https://paddo.dev/blog/three-ways-deep-research-claude/ ,
  https://github.com/Weizhena/Deep-Research-skills ,
  https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
  (Tow Center, March 2025; via fetched search summary)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports (corroboration or labeled unverified): the practitioner account
  that led to the `/deep-research` workflow (confirmed against the Claude
  Code docs); community research skills converge on outline → parallel
  per-item search → report with a human checkpoint after the outline
  (adopted only as "ask one question when it changes the work"); the Tow
  Center test of eight AI search engines found over 60% of source-
  identification answers wrong and most wrong answers given confidently
  (corroborates the tier-2 audits, tier 3 because it is journalism rather
  than peer review).
### study-credibility skill — tier 2: meta-research primary sources
- URLs (all resolved through the Europe PMC REST API rather than the
  publisher, which is the technique the skill itself documents):
  https://doi.org/10.1002/14651858.MR000033.pub3 (Lundh 2017, Cochrane) ,
  https://doi.org/10.1056/NEJMsa065779 (Turner 2008) ,
  Barnes & Bero, JAMA 1998, "Why review articles on the health effects of
  passive smoking reach different conclusions" ,
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1885451/ (Bero 2007,
  PLoS Medicine, statin drug-drug comparisons) ,
  Nuijten et al., "The prevalence of statistical reporting errors in
  psychology (1985-2013)" (statcheck) ,
  https://www.science.org/doi/10.1126/science.aac4716 (OSC 2015) ,
  https://www.nature.com/articles/nrn3475 (Button et al. 2013) ,
  Boutron et al., JAMA 2010 (spin) ,
  Schroter et al., J R Soc Med 2008 (inserted-error detection)
- Last verified: 2026-08-15 (Lundh, Turner, Barnes & Bero, and Bero 2007
  abstracts and full text retrieved directly from Europe PMC; statcheck
  abstract retrieved directly; OSC 2015, Button 2013, Boutron 2010, and
  Schroter via fetched search summaries)
- Supports: Lundh — favorable efficacy RR 1.27 (1.17–1.37, 25 papers,
  moderate quality); favorable conclusions RR 1.34 (1.19–1.51, 29 papers,
  low quality); harms RR 1.37 (0.64–2.93, four papers, very low quality —
  interval spans null); no difference between industry and non-industry on
  sequence generation, allocation concealment, follow-up, or selective
  outcome reporting; industry studies more often low risk of bias from
  blinding RR 1.25 (1.05–1.50); results-to-conclusions agreement RR 0.83
  (0.70–0.98); verbatim authors' conclusion that the effect "cannot be
  explained by standard 'Risk of bias' assessments". Turner — 74
  FDA-registered antidepressant studies, 31% unpublished; 37 of 38 positive
  published; 22 negative unpublished and 11 published conveying a positive
  outcome; literature appeared 94% positive vs. FDA's 51%; pooled effect
  inflation 32%. Barnes & Bero — 106 reviews, 37% (39/106) concluded passive
  smoking not harmful, 74% of those industry-affiliated, adjusted OR 88.4
  (16.4–476.5). Bero 2007 — 192 statin comparison RCTs, 98% surrogate
  outcomes only; test-drug-company funding associated with favorable results
  OR 20.2 and favorable conclusions OR 34.6 in multivariate analysis of
  industry-funded trials; adequately blinded trials less likely to favor the
  test drug. statcheck — >250,000 p-values, ~half of NHST papers contain a
  p-value inconsistent with its test statistic, ~1 in 8 a gross
  inconsistency. OSC 2015 — 36 of 100 replications significant in the same
  direction, down from 97% in the originals, effect sizes about half. Button
  2013 — median power 8–31% across 49 meta-analyses. Boutron 2010 — 72 RCTs
  with nonsignificant primary outcomes, spin in 58.3% of abstract
  conclusions, 18.0% of titles. Schroter — nine major errors inserted, mean
  2.6 detected at baseline.
- Corrections recorded 2026-08-15: the skill previously stated a Lundh harms
  RR of 1.87 (no such figure; the real one spans null), a Lundh claim that
  restricting to low-risk-of-bias studies strengthened the association (not
  in the review), Barnes & Bero rates of 6% vs. 87% (not in the paper), Bero
  2007 rates of 66%/79%/10% (not in the paper), and a Schroter figure of
  8 errors with "none caught more than 5" (9 major errors; the second clause
  unverified). Five of seven checked numeric claims were wrong — treat
  unsourced meta-research figures in any artifact as suspect until pulled
  from the primary source.
### study-credibility skill — tier 2: figures added to the ledger 2026-08-18
- Sources and how read (all 2026-08-18): Bekelman, Li & Gross, JAMA 2003
  (PMID 12533125; abstract via Europe PMC) ; Jia et al., "Association
  between switching of primary outcomes and reported trial findings among
  randomized drug trials from China", J Clin Epidemiol 2021;132:10-17 (PMID
  33309887; abstract via Europe PMC — full text paywalled, methods not read)
  ; Brown & Heathers, "The GRIM Test", SPPS 2017 (DOI
  10.1177/1948550616673876; abstract via Crossref, preprint abstract via
  Europe PMC) ; Janda et al., "Comparison of Clinical Study Results Reported
  in medRxiv Preprints vs Peer-reviewed Journal Articles", JAMA Netw Open
  2022;5(12):e2245847 (PMID 36484989; abstract via Europe PMC) and the same
  group's Peer Review Congress 2022 abstract (interim data) ; Higgins et al.,
  "Measuring inconsistency in meta-analyses", BMJ 2003;327:557 (PMC192859;
  full text) ; Cochrane Handbook v6.5 ch. 10 §10.10.2 and ch. 13 §13.3.4.4
  (fetched) ; Sterne et al., BMJ 2011;343:d4002 (LSHTM repository PDF).
- Supports, verbatim: Bekelman — "Eight articles, which together evaluated
  1140 original studies ... pooled Mantel-Haenszel odds ratio, 3.60; 95%
  confidence interval, 2.63-4.91" and "Approximately one fourth of
  investigators have industry affiliations" (the artifact had said "about a
  third"; corrected). Jia — a retrospective cohort of "294 RCTs" from
  mainland China: "Among RCTs registered before they started, the odds of
  switching primary outcomes with negative findings were 2.64 (95% CI:
  1.16-6.02) times the odds of switching those with positive findings. Among
  RCTs registered when they were ongoing, the odds ... were 8.84 (95% CI:
  3.62-25.93)"; the artifact had stated the 2.6 without population or
  interval; corrected. GRIM — "Of the articles that we could test with the
  GRIM technique (N = 71), around half (N = 36) appeared to contain at least
  one inconsistent mean, and more than 20% (N = 16) contained multiple";
  matches. Janda 2022 (version of record, 547 pairs) — sample size concordant
  86.4%, primary end-point results 81.1%, interpretation 96.2%; the "~89%"
  the artifact carried is the interim conference figure (290/325 = 89.2%);
  corrected to the version of record with the interim noted. Higgins 2003 —
  "we would tentatively assign adjectives of low, moderate, and high to I2
  values of 25%, 50%, and 75%"; Cochrane ch. 10 — "0% to 40%: might not be
  important; 30% to 60%: may represent moderate heterogeneity; 50% to 90%:
  may represent substantial heterogeneity; 75% to 100%: considerable
  heterogeneity" with "Thresholds for the interpretation of the I2 statistic
  can be misleading"; the artifact's non-overlapping 0–25/25–50/50–75/75–100
  bands matched neither and now quote Cochrane. Cochrane ch. 13 / Sterne
  2011 — "As a rule of thumb, tests for funnel plot asymmetry should be used
  only when there are at least 10 studies included in the meta-analysis"
  and "should not be used if the standard errors ... are all similar";
  matches the artifact, which now carries both conditions.
### study-credibility skill — tier 1: appraisal instruments and reporting guidelines
- URLs: https://www.equator-network.org/reporting-guidelines/consort/ ,
  https://www.nature.com/articles/s41591-025-03635-5 (CONSORT 2025) ,
  https://www.riskofbias.info/welcome/robins-i-v2 ,
  https://methods.cochrane.org/bias/resources/rob-2-revised-cochrane-risk-bias-tool-randomized-trials
- Last verified: 2026-08-15 (fetched search summaries)
- Supports: CONSORT 2025 published April 2025 across multiple journals,
  30-item checklist plus flow diagram, superseding CONSORT 2010; SPIRIT 2025
  as the protocol counterpart; ROBINS-I V2 first released November 2024 with
  a revision posted November 2025, adding signalling-question algorithms,
  six bias domains, judgements from Low to Critical, currently scoped to
  follow-up (cohort) studies with other designs in development, and
  preferred over V1 for non-randomized studies in Cochrane reviews.
- Note: reporting guidelines describe required disclosure, not validity.
  The skill states this explicitly because conflating the two is a common
  reader error.
### study-credibility skill — tier 3: research-integrity landscape
- URLs: https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/ ,
  https://retractionwatch.com/ ,
  https://dbrech.irit.fr/pls/apex/f?p=9999:1 (Problematic Paper Screener) ,
  https://www.chemistryworld.com/features/ai-tools-tackle-paper-mill-fraud-overwhelming-peer-review/4022253.article
- Last verified: 2026-08-15 (Problematic Paper Screener URL confirmed live
  with a 200 and page-title match; the rest via fetched search summaries)
- Supports (labeled approximate in the artifact): Crossref acquired the
  Retraction Watch database in September 2023 and publishes it openly, daily
  updated; database past 60,000 entries; five-figure annual retraction counts
  since 2023 driven mainly by mass retractions; roughly 1.5–2% of 2022
  publications closely resembling paper-mill output; the Wiley/Hindawi event
  retracting ~8,000 papers and closing 19 journals; paper-mill detection
  signals (mismatched affiliations, coauthor patterns, fabricated citations,
  tortured phrases, image duplication). Figures are journalism and vendor
  estimates rather than peer-reviewed measurement, so the skill states them
  as approximate trends and never as precise rates.
## prompt-author skill subject-matter sources

### Claude Code `/goal` (2026-10-29)
- URLs: https://code.claude.com/docs/en/goal (fetched in full as raw
  markdown, `goal.md`, 2026-10-29) ; https://code.claude.com/docs/en/commands
  (`commands.md`, the `/goal` row and the table preamble) ;
  https://code.claude.com/docs/en/skills (`skills.md`, "Stack several
  skills in one message" and "Restrict Claude's skill access") ;
  https://code.claude.com/docs/en/desktop (`desktop.md`, grep only, no
  `/goal` mention).
- Last verified: 2026-10-29 (first entry; local CLI 2.1.287).
- Supports (verbatim where quoted), goal page: "The `/goal` command sets a
  completion condition and Claude keeps working toward it without you
  prompting each step. After each turn, a model checks whether the
  condition holds. If the model judges it not yet met, Claude starts
  another turn instead of returning control to you. The goal clears
  automatically once the condition is met, if the model judges the
  condition impossible to satisfy, or if a turn fails on an error you have
  to fix"; "Setting a goal starts a turn immediately, with the condition
  itself as the directive. You don't need to send a separate prompt"; "The
  evaluator judges your condition against what Claude has surfaced in the
  conversation. It doesn't run commands or read files independently, so
  write the condition as something Claude's own output can demonstrate";
  a durable condition has "One measurable end state", "A stated check",
  and "Constraints that matter"; "The condition can be up to 4,000
  characters"; "To bound how long a goal runs, include a turn or time
  clause in the condition, such as `or stop after 20 turns`"; "A goal
  doesn't change your permission mode. To let goal turns run unattended,
  run `/goal` in auto mode"; "If Claude keeps answering the evaluator
  without making progress (no tool use for several turns in a row),
  Claude Code stops the loop, prints a warning, and returns control to you
  with the goal still set"; the evaluator is "a wrapper around a
  session-scoped prompt-based Stop hook" on "your configured small fast
  model" and "does not call tools"; `claude -p "/goal <condition>"` "runs
  the loop to completion in a single invocation". Fit examples on the
  page: migrate a module until call sites compile and tests pass,
  implement a design doc until acceptance criteria hold, split a file
  until each piece is under a size budget, drain a labeled issue backlog.
  Version notes on the page, not carried into the skill: check-ins
  v2.1.234+, idle check-ins v2.1.236+, retry/pause notices v2.1.269+,
  restore on every resume route v2.1.239+.
- Built-in, not a skill: commands.md lists `/goal [condition|clear]`
  without the **Skill** marker in a table whose preamble says "Most are
  built-in commands whose behavior is coded into the CLI"; `/loop` in the
  same table is marked **Skill**. skills.md: "A few built-in commands are
  also available through the Skill tool, including `/init` and
  `/security-review`. Other built-in commands such as `/compact` are
  not."
- Placement, skills.md verbatim: "When you type at the Claude Code prompt
  in your terminal, you can stack several skills at the start of one
  message. Through the Agent SDK or `claude -p`, Claude Code loads only
  the first skill, with the rest of the line as its arguments"; "Expansion
  stops at the first token that isn't an inline user-invocable skill. If
  you stack a skill that runs as a forked subagent ... or one whose
  arguments may start with another command, such as `/loop`, expansion
  ends there. That token and everything after it become the argument text
  for every expanded skill." `/goal` is not a skill, so a `/goal` after a
  skill ends expansion and becomes argument text in every mode.
- Inference carried into the skill, not stated on the page: a run with a
  user gate (an approval, rounds of questions) is a poor fit because the
  evaluator starts another turn rather than waiting, and the
  no-tool-use stop then halts the loop. Mechanism-level inference from the
  quoted text; not measured.

## skill-author skill subject-matter sources

Provenance for `references/skill-config.md` (added 2026-10-30) and the
framework's config bullet. Session 4b9d2382-e133-42cd-9deb-18f9093fcab0.

### skill-author — config design decided by the user (2026-10-30)
- Decisions taken by the user 2026-10-30 in this session: no rule file
  carries skill config; the plain read is the default and `!` injection is
  out; the config block is a flat key list with one documenting header.
- Superseded 2026-10-31 by a grilling session (same session id) that
  settled the design the user confirmed: keys declared in a `## Config`
  table in SKILL.md; values in `config.local.yaml` beside it, ignored by a
  `.gitignore` shipped in the skill; no shipped or example values file; no
  project scope (a project skill's local file is project-scoped by
  location); no script of any language (Python rejected as a setup
  dependency; with no untrusted file left there was nothing for a script
  to check); one owner per value with hand-offs between skills; "stop and
  say so" for a configured directory that does not exist, never create
  (mount-point hazard); portable by default with
  `metadata: {harness: <name>}` as the opt-out; a Migrate mode; rule-author
  and the export skills deferred. Verified targets Claude Code, Cursor,
  Codex; best effort Gemini CLI, Copilot, Antigravity; macOS and Windows.

### Config file format (2026-10-31)
- Supports: INI was proposed and rejected by the user as dated; with no
  script in the design the choice fell to readability and honesty, and a
  flat `key: value` file is valid YAML, the syntax every skill's
  frontmatter already uses. JSON allows no comments. Author rule recorded
  in skill-config.md: quote a value that contains `: ` or `#`.

### Antigravity documentation (skills, rules, sandbox, permissions)
- URLs: https://antigravity.google/docs/skills ;
  https://antigravity.google/docs/migration/workflows-to-skills ;
  https://antigravity.google/docs/rules ;
  https://antigravity.google/docs/customization-discovery ;
  https://antigravity.google/docs/permissions ;
  https://antigravity.google/docs/sandbox ;
  https://antigravity.google/docs/agent-settings ;
  https://antigravity.google/docs/changelog ;
  https://codelabs.developers.google.com/getting-started-with-antigravity-skills
- Last verified: 2026-10-31 (fetched by a subagent, quotes relayed; the
  lead did not open the pages). Docs pages show no date; dates come from
  the changelog.
- Supports: Agent Skills adopted "In May 2026"; workspace skills in
  `<workspace-root>/.agents/skills/<skill-folder>/` ("defaults to
  .agents/skills, but still maintains backward compatibility for
  .agent/skills"), global in `~/.gemini/config/skills/`; the folder tree
  lists "scripts/ # Optional executable scripts" and the codelab runs a
  bundled Python script with `run_command`; rules per directory in
  `AGENTS.md` or `GEMINI.md` (always on, no frontmatter) and
  `.agents/rules/*.md` (a rule without `trigger:` frontmatter is silently
  discarded), global under `~/.gemini/`; "By default, the agent only has
  access to the folders inside your project and the application's local
  app data directory ~/.gemini/antigravity/", `allowNonWorkspaceAccess`
  "Set to off by default for safety", and the CLI "asks before editing"
  files under `~/.gemini/config` (v1.2.15, 2026-10-02); terminal commands
  run in a sandbox "with access restricted to your workspace and temp
  directories and no network access"; Windows shell: changelog v1.0.10
  "defaulted shell resolution to PowerShell", v1.3.3 "falls back to Windows
  PowerShell"; no official statement on reviewing repository rules or
  skills. Conflict noted: the codelab (2026-09-08) says `~/.agents/skills`
  is read by the IDE but not the CLI, which the reference page does not
  state; unverified. Grounds: Antigravity listed as best effort; the
  set-up write may prompt there; portable skills avoid bash-only scripts.

### Cursor rules documentation
- URL: https://cursor.com/docs/context/rules
- Last verified: 2026-10-30 (targeted WebFetch extraction). No date on the
  page.
- Supports: "Project rules live in `.cursor/rules` as `.mdc` files and are
  version-controlled"; a plain `.md` there is ignored for lack of
  frontmatter; `alwaysApply: true` puts a rule in every chat session and
  then `globs` and `description` are ignored; "User Rules are global
  preferences defined in **Customize → Rules**" (the app, not a file);
  Team Rules from the dashboard; precedence "Team Rules → Project Rules →
  User Rules"; "Cursor supports AGENTS.md in the project root and
  subdirectories"; no mention of `CLAUDE.md`; "AI guidance should not be
  your only security control". Grounds: rule files have no common
  user-level location across harnesses.

### Codex AGENTS.md documentation
- URL: https://learn.chatgpt.com/docs/agent-configuration/agents-md
  (developers.openai.com/codex/guides/agents-md redirects here)
- Last verified: 2026-10-30 (targeted WebFetch extraction). No date on the
  page.
- Supports: global level "Codex reads `AGENTS.override.md` if it exists.
  Otherwise, Codex reads `AGENTS.md`"; per project directory
  "`AGENTS.override.md`, then `AGENTS.md`, then any fallback names in
  `project_doc_fallback_filenames`", "at most one file per directory";
  concatenated root-down, "Files closer to your current directory override
  earlier guidance"; `project_doc_max_bytes` (32 KiB default); no trust or
  security statement. Same grounds as the Cursor entry.

### GitHub Copilot repository custom instructions
- URL: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- Last verified: 2026-10-30 (targeted WebFetch extraction). No date on the
  page.
- Supports: `.github/copilot-instructions.md`; `NAME.instructions.md`
  under `.github/instructions` with an `applyTo` glob, "only supported for
  Copilot cloud agent and Copilot code review"; `AGENTS.md` "stored
  anywhere within the repository", nearest wins; "Alternatively, you can
  use a single `CLAUDE.md` or `GEMINI.md` file stored in the root of the
  repository"; precedence personal > repository > organization, personal
  instructions live in the UI; no security statement. Same grounds.

### Gemini CLI context files
- URL: https://geminicli.com/docs/cli/gemini-md
- Last verified: 2026-11-01 (WebFetch extraction; first fetch, the
  2026-10-30 entry was from a search summary only).
- Supports: default context file `GEMINI.md`; global
  `~/.gemini/GEMINI.md`; project files found "in your configured
  workspace directories and their parent directories", and
  subdirectory files loaded just in time when a tool touches the
  directory; `context.fileName` in `settings.json` takes a name or a
  list, for example `["AGENTS.md", "CONTEXT.md", "GEMINI.md"]`; imports
  with `@file.md`, "both relative and absolute paths". Import depth and
  size limits are not stated on the page; it points to the Memory Import
  Processor page, not opened. Grounds `rule-author/references/gemini-cli.md`
  and the root `GEMINI.md` of this repository.

### Claude Code setup page (Windows shell)
- URL: https://code.claude.com/docs/en/setup
- Last verified: 2026-10-30 (fetched in full).
- Supports, verbatim: "[Git for Windows] is recommended on native Windows
  so Claude Code can use the Bash tool. If Git for Windows is not
  installed, Claude Code uses PowerShell as the shell tool instead. WSL
  setups do not need Git for Windows." Grounds skill-config.md's choice of
  Python over bash for an optional config script.

### Pillar Security — Rules File Backdoor (tier 3, vendor security blog)
- URL: https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents
- Last verified: 2026-10-30 (targeted WebFetch extraction). Published
  2025-03-18.
- Supports: hidden instructions in rules files ("typically stored in a
  .cursor/rules directory") "Using zero-width joiners, bidirectional text
  markers, and other invisible characters"; the demo payload added "a
  malicious script sourced from an attacker-controlled site" and told the
  AI "not to mention the code changes"; "Cursor maintained their initial
  position, stating it is not a vulnerability on their side"; GitHub later
  added a hidden-Unicode warning on github.com; mitigation: treat rules
  files "with the same scrutiny as executable code". Grounds
  skill-config.md's control-character check and the "instruction file"
  framing. The fetch tool noted invisible Unicode in the page's own
  reference section; ignored.

### Malicious Agent Skills in the Wild (Liu et al., arXiv 2602.06547, USENIX Security 2026)
- URL: https://arxiv.org/abs/2602.06547
- Last verified: 2026-10-30 (abstract page fetched; paper body not read).
  v1 2026-02-06, v4 2026-06-10.
- Supports: 98,380 skills from two community registries; 157 confirmed
  malicious with 632 vulnerabilities across 13 techniques (4.03 per
  skill); over half from one actor's templated brand impersonation; two
  dominant strategies, credential theft via remote code execution and
  "agent manipulation through adversarial instructions embedded in
  documentation"; all 157 removed after disclosure. Tier 2 for the counts;
  the taxonomy of techniques was not read.

### OWASP Agentic Skills Top 10 (v1.0, 2026 edition)
- URL: https://owasp.github.io/www-project-agentic-skills-top-10/
  (owasp.org project page holds no list)
- Last verified: 2026-10-30 (targeted WebFetch extraction). "Last
  updated: March 2026".
- Supports: AST01 Malicious Skills, AST02 Supply Chain Compromise, AST03
  Over-Privileged Skills, AST04 Insecure Metadata, AST05 Untrusted
  External Instructions, AST06 Weak Isolation, AST07 Update Drift, AST08
  Poor Scanning, AST09 No Governance, AST10 Cross-Platform Reuse;
  verbatim "repository-level configuration files now function as part of
  the execution layer"; `AGENTS.md` named only as a file to protect from
  writes. A draft from a standards body; grounds the obedience-channel
  argument in skill-config.md together with the two entries above.

### Snyk ToxicSkills (not opened)
- URL: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub
  — seen in a WebSearch summary only, 2026-10-30.
- At summary grade: 3,984 skills scanned on ClawHub and skills.sh, 76 with
  malicious payloads in their instructions. Not relied on by any artifact.

## ai-repo-author skill subject-matter sources

Provenance for the skill created 2026-11-01. Its procedure comes from the
user's own practice, not from vendor guidance; its few harness facts are
grounded in entries above.

### ai-repo-author — the treatment, from two repository setups (2026-11-01)
- Sources: the transcripts of the sessions that set up this repository
  (2026-10-31 to 2026-11-01) and a second skills repository of three
  research skills (2026-11-01), session
  69abbd20-032e-4c0c-9880-3d4c6ea3e444 and its forks, read for step 0 of
  the create pass; the user's request that specified the treatment. This
  repository's `AGENTS.md` at version 2.1.0 is the reference text for the
  agents-rule template; the step for a copied `link.sh` comes from the
  second repository's `AGENTS.md`.
- Last verified: 2026-11-01.
- Supports: each failure the skill names: a README written without the
  writing skill's README contract that carried a false claim; `link.sh`
  copied from a working tree that predated the license notice; changelog
  entries appended after the changelogs were removed; scripts that crashed
  under the system Python 3.9 on `dict | None` annotations; a usage line
  written from memory without the data-path argument; contract examples
  that were real records; eval prompts that named real organizations; a
  scan whose directory list zsh did not split, so it read no file and
  reported nothing; a config key that held a value that differs by
  harness; a portable claim made before the portability check existed; a
  first commit under the account name because git had no user name set;
  `git merge -F -` failing with "could not read file '-'".

### ai-repo-author — instruction-file imports
- Grounded in "Claude Code memory and rules documentation" (an
  `@AGENTS.md` import in `CLAUDE.md`; re-fetched 2026-10-13) and "Gemini
  CLI context files" (imports with `@file.md`; verified 2026-11-01).
- Supports: the one-line `CLAUDE.md` and `GEMINI.md` in
  `references/repository.md`, "The agents rule".

### ai-repo-author — link.sh 1.0.0 interface
- Source: `./link.sh --help` and `--list`, and two runs from a scratch home
  directory, 2026-11-01 (link.sh 1.0.0, this repository at 2.1.0).
- Supports: the repository shape; that the script links only from inside
  a git repository; `--harness`; the second run printing `no changes`; the
  MIT notice in the header, from which the skill builds `LICENSE` (the
  result matched this repository's `LICENSE` byte for byte).
