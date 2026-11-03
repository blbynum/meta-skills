# Sources — skill-author

Provenance ledger for the skill-author skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

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
- Last verified: 2026-11-02 (fetched in full for the versioning pass; the
  same six fields, and no version field). Previous: 2026-10-30 (fetched in
  full for the skill-author config pass; byte-for-byte the same six fields
  and no configuration mechanism); 2026-10-24 (fetched in full). No version
  or date shown on the page.
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

## Tier 3: community (corroborated or labeled)

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
