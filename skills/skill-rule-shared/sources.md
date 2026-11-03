# Sources

Provenance for the sources that both authoring skills use, one for skills
and one for rules. Seeded 2026-08-15 from the user's research notes. The
skills kept per-skill changelogs until version 2.0.1; that history is in
version control.

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

Every skill keeps its own `sources.md` in its directory, never linked from
its SKILL.md. Split that way on 2026-10-31; the entries of this
repository's other skills moved out on 2026-11-03.

## Contents

- Tier 1: Anthropic official
- Tier 1: other vendor documentation
- Tier 2: research
- Artifact tooling
- Tier 3: community (corroborated or labeled)

Every entry names the models or vintage a finding was measured on. A claim
that drops that qualifier when it is copied into an artifact is the most
common error this file has recorded (audit of 2026-08-18: eight findings in
five artifacts traced to one dropped qualifier).

## Tier 1: Anthropic official

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

### Which Prompting Technique Should I Use? (arXiv 2506.05614)
- URL: https://arxiv.org/abs/2506.05614
- Last verified: 2026-08-15 (via vault)
- Supports: technique effectiveness depends on task type — grounds matching
  degrees of freedom and guidance style to the task.

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
