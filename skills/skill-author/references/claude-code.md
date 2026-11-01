# Claude Code

What differs when skill-author runs in Claude Code, and what Claude Code
adds to the Agent Skills standard. Read this when you run in Claude Code,
before step 0 and again before step 5. Nothing here goes into a portable
skill's body; it applies to this skill's own work and to skills declared
`metadata: {harness: claude-code}`.

## Contents

- Where skills and transcripts live
- Frontmatter extensions and measured quirks
- Dynamic context injection
- Writes under the configuration directory
- Measurement: the runner and the scripts
- Sources to re-check

## Where skills and transcripts live

- Personal skills: `~/.claude/skills/<name>/SKILL.md`, the usual value of
  `skills-dir` here. Project skills: `.claude/skills/<name>/SKILL.md`, also
  under subdirectories and directories passed with `--add-dir`. Plugin
  skills: `<plugin>/skills/<name>/`. Enterprise skills come from managed
  settings, and claude.ai account skills sync in.
- Only the name and description, plus `when_to_use` if set, load at
  startup. The body loads when a task matches or the user types `/<name>`;
  the command comes from the directory name.
- Raw session transcripts: `~/.claude/projects/<cwd-slug>/<session>.jsonl`.
  In the desktop app, `list_events` renders user turns, assistant text, and
  tool-call names only; tool arguments and results are in the raw
  transcript. Use them for step 0.
- `/doctor prompt-audit` checks instruction files, skills included, for
  outdated or contradictory content (v2.1.283 or later). `/skills` writes
  `skillOverrides` to `.claude/settings.local.json` to hide a skill without
  editing it.

## Frontmatter extensions and measured quirks

Claude Code reads these beyond the spec's six fields. A portable skill
does not use them; a Claude-only skill may.

- `when_to_use`: extra trigger phrases appended to the description in the
  listing. The two together are cut at 1,536 characters, so the key use
  case still goes first in `description`.
- `argument-hint`, `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N`, and named
  arguments from an `arguments` list; `${CLAUDE_SESSION_ID}`,
  `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, and
  the plugin variables are substituted in the body.
- `disable-model-invocation: true` makes the skill a pure slash command:
  its description leaves Claude's context, so a prose request naming it
  cannot load it. When the user wants prose requests to work but nothing
  else to trigger, gate by description instead: lead with the tool's own
  name, keep shared vocabulary out of the opening clause, name where
  near-miss requests go, and repeat the restriction in the body. When the
  description names a path the model could explore on its own, read the
  trigger-eval transcripts for runs that explore the path instead of
  loading the body.
- `allowed-tools` pre-approves tools for the invoking turn, but on Claude
  Code 2.1.220 and 2.1.287 any value makes a model-invoked Skill call a
  permission prompt ("Execute skill: <name>"): in a non-interactive
  `claude -p` session under `acceptEdits` the call is denied and the body
  never loads (measured 2026-08-19 and 2026-10-24, 3 of 3 runs each; the
  same skill loaded on every run with the field removed). A user-typed
  `/name` is not affected (4 of 4 runs, 2026-10-24). Leave the field off a
  skill that must load unattended and let the user's permission settings
  govern the tools. Workspace trust does not gate the field, so review
  `allowed-tools` in skills checked into a repository before running
  there.
- `context: fork` runs the skill in a subagent and only makes sense for a
  skill with explicit instructions.
- A skill that must also upload to claude.ai is limited to the spec
  fields; any other field fails packaging with a hard error.

## Dynamic context injection

A body line `` !`command` `` runs the command before the body is sent and
replaces the placeholder with its output. Outside auto mode an injected
command that no allow rule matches aborts the whole invocation, silently
in `-p` (zero turns, empty result), while `disableSkillShellExecution`
replaces it with a placeholder and the body still loads. If a Claude-only
skill injects, inject a bundled script,
`` !`${CLAUDE_SKILL_DIR}/scripts/x.sh` ``, pre-approve it with
`allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/x.sh *)`, make the script
exit 0 on every path, and write the surrounding prose so it still reads
correctly when the placeholder appears (measured 2026-10-24 on 2.1.287;
works through a symlinked skill directory). `@path` references in a skill
body do not import the file. Injection never belongs in a portable skill.

## Writes under the configuration directory

Claude Code treats files under `~/.claude` as sensitive: a non-interactive
run denies edits there, and an interactive session prompts. A skill's
offer to write `config.local.yaml` for a personal skill may therefore be
refused, which is why the set-up wording has a print fallback, and eval
output directories go outside `~/.claude`.

Reads there are gated the same way: under `--permission-mode dontAsk` a
read under `~/.claude` is denied unless an allow rule names the path. A
`claude -p` smoke run of a skill whose body links to the shared directory
needs `--allowedTools "Read(//Users/<user>/.claude/skills/skill-rule-shared/**)"`,
the rule the A/B command already passes (2.1.287, 2026-10-31).

## Measurement: the runner and the scripts

`claude -p` is the non-interactive runner the two scripts in the shared
directory use:

- `scripts/trigger_eval.py` measures how often the skill loads across
  should-trigger prompts and near-misses. Run it for every description
  change.
- `scripts/ab_eval.py --mode skill` runs task prompts with and without the
  skill, or `--old` and `--new` for two versions, three runs per arm, and
  saves outputs, transcripts, cost, the Claude Code version, and the
  resolved model.

The shared `evaluating.md` holds the method, the eval set formats, the
preflight checks, and the confounds to record. Two preflights fail most
often: run the scripts with Python 3.10 or later, and check login with a
one-word `claude -p` before a suite, because `claude auth status` can say
logged in on a token the run cannot refresh.

## Sources to re-check

The Claude Code skills doc is the harness source for this file, and the
memory doc covers rules and the skill-versus-rule boundary. Both are in
the shared ledger with their last-verified dates.
