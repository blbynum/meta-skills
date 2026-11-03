# Sources — rule-author

Provenance ledger for the rule-author skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

## Tier 1: Anthropic official

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

### Anthropic engineering: effective context engineering
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Last verified: 2026-08-15 (fetched)
- Supports: smallest set of high-signal tokens as the goal; right-altitude
  instructions (start minimal, add on observed failure); curated canonical
  examples over exhaustive edge cases; just-in-time retrieval; finite
  attention budget and context rot (recall degrades as loaded context
  grows) — grounds the aggregate always-loaded budget rule.

## Tier 1: other vendor documentation

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

## Tier 2: research

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

## Tier 3: community (corroborated or labeled)

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
