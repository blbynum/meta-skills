# Skill configuration

How a skill carries the values that differ between machines or projects
without writing them into its body and without a rule file. Read this at
step 4 when a draft names a path, a companion skill, a vendor, an account,
or another value the author's machine supplies; at Updating step 2 when an
existing skill carries such a value; and for every Migrate request.

## Contents

- Decide what varies
- The Config table
- The values file
- The read instruction
- Set-up and failure wording
- Migrating an existing skill
- The portability check

## Decide what varies

A key earns its place only when its value differs between two real
environments the skill will run in. Ask for each candidate: would a second
machine, a second project, or a second user need a different value? If
yes, it is a key. If no, write the value into the skill and move on.

Candidates that usually vary:

- A path outside the skill directory and outside the project: a notes
  vault, an archive share, a guides directory.
- A companion skill the skill hands work to: the skill that records
  findings, the skill that runs research.
- A vendor, account, host, or product the user chose: which cloud, which
  registry, which tracker.

Candidates that usually do not vary, so they get no key:

- A tool that differs by operating system. Detect the OS at run time and
  choose the tool in the skill. A key here makes the user record a fact
  the machine already knows.
- A path inside the project the skill runs in. Use a relative path.
- A value the skill can read from the repository, such as the package
  manager or the test command.
- A preference nobody has asked to change. Choose a default and name it in
  the body. Add a key when a second environment needs another value.
- A secret. A key may name where a credential lives, a file or a keychain
  item; the value is never a token or a password.

Each value has one owner. When a skill needs a value another skill owns,
such as the notes vault, it hands that work to the owning skill instead of
holding a copy of the path, and the owning skill's name is itself a key.

Do not add a key to show that configuration was considered. A skill with
no Config section is the normal case. When nothing varies, the report to
the user says "no config keys" in one line.

## The Config table

A skill with keys declares them in a `## Config` section, the first
section after the title. The section is the spec and the example: there is
no shipped values file. One row per key:

```markdown
## Config

| Key | Required | Default | Purpose |
|---|---|---|---|
| archive-dir | yes | | directory that receives finished downloads |
| notes-skill | no | | skill that records durable findings; when unset, record nothing |
```

Rules for the table:

- Key names are lowercase words joined by hyphens.
- A required key has an empty Default. An optional key's Default is the
  value the skill uses when the values file does not set it.
- Purpose says what the value is for in one clause. A key with a fixed set
  of options lists them there: "copy or move".
- A value never appears in the description. The description loads before
  any file is read, so it names the kind of value, "the configured archive
  directory", not the value.

## The values file

The user's values live in `config.local.yaml` in the skill directory: one
flat file of `key: value` lines, nothing else. Quote a value that contains
`: ` or `#`.

```yaml
archive-dir: /Volumes/media/archive
```

The skill ships a `.gitignore` beside it with the single line
`config.local.yaml`, so the ignore travels with the skill and a `git pull`
of the skills repository never touches the user's values. The `.local.`
infix follows the convention of other local-override files: the name says
"mine, never committed" even outside git.

No project scope. A key differs per project only when the skill itself is
a project skill, and then its `config.local.yaml` lives in the project with
it.

## The read instruction

The last paragraph of the Config section tells the agent what to do, in
these words:

```
Read `config.local.yaml` in this skill's directory before anything else.
A key missing there takes its Default from the table. If a required key is
missing or empty, stop: name the key and its purpose, and offer to write
`config.local.yaml` with the values the user gives. If a configured
directory does not exist, stop and say so; do not create it.
```

Two reasons behind the two stops. A skill that fills a required path with
a plausible default writes to the wrong place on the one machine where the
default is wrong, and the user finds out later. And creating a missing
directory is unsafe where the path is a mount point: on a Mac, creating
`/Volumes/Archive` while the drive is unmounted makes a folder on
the boot disk, and the skill writes there happily. A skill that needs a
different rule for one directory states it in its own step.

## Set-up and failure wording

Offer the whole file at set-up time, not one key per turn: "This skill
needs `archive-dir`, the directory that receives finished downloads. Give
me the value and I will write `config.local.yaml` in the skill
directory." A harness may refuse a write under its own configuration
directory; then print the finished file and its path for the user to
save. After the first successful read, use the values without comment.

## Migrating an existing skill

A Migrate request ("migrate <skill>", "make <skill> shareable", or a path
to a skill in any repository) decides the skill's kind, moves its
machine-specific values into config, and, for a portable skill, moves its
harness facts into harness references. "Make shareable" means the portable
kind. Steps:

1. Read the whole skill: SKILL.md, references, scripts. Decide the kind as
   step 3 of the workflow does, and write it into `metadata.harness`
   before anything else. Then list every machine-specific value: an
   absolute path outside the skill, a hostname, an account, a user name, a
   vendor or product name, and every companion skill named in prose.
   Decide each one by "Decide what varies" above.
   A copy of a value another skill owns, held beside an existing hand-off
   to that skill, is a value move, not a hand-off: drop the copy and name
   the owning skill through its key.
   For each value that will move, search the skills directory for copies
   in other skills and list each holder in the report as a hand-off
   candidate.
2. Add the Config table with one row per key, and the read instruction
   under it.
3. Write the values the skill carried today into `config.local.yaml`, so
   the author's machine keeps working, and add the `.gitignore`.
4. Replace each value in the body and the description with the kind of
   value and the key's name: "the configured archive directory
   (`archive-dir`)".
5. Companion skills named in prose: for each, propose the hand-off rewrite
   in the report, one line per skill, and apply it only on the user's yes.
   A hand-off changes behavior; a moved value does not. A skill named in
   the description only to say where a near-miss request goes stays as a
   name: the description decides loading before any file is read, so a key
   cannot route there, and a missing skill on another machine only means
   the request is handled without it. List those names in the report and
   leave them.
6. For a portable skill: move every harness fact in the body and
   references into `references/<harness-id>.md`, one file per harness;
   rewrite the body to name actions instead of tools and mechanisms
   instead of a harness's names for them ("a lifecycle hook, where the
   harness has them"); drop harness-only frontmatter and syntax. Keep
   every step the skill needs; a step that only one harness can do stays,
   worded as "where the harness supports it", with the specifics in that
   harness's reference. For a harness-specific skill, change nothing here.
7. Check: desk-check the table against the body; read `config.local.yaml`
   and confirm it holds every value that left the body (a `grep` wrapper
   that honors `.gitignore` never sees the file); for a portable skill,
   run the portability check below and paste its result into the pass
   record; run the trigger eval where a runner exists if the
   description changed; run the skill once and confirm it used a value
   from the file. Run the A/B only when step 5 rewrote behavior. When step
   1 finds nothing to move, report "no config keys", still do step 6, and
   record in the pass record that the trigger eval and the run were skipped
   because nothing changed. If step 6 changed the frontmatter or the body,
   run the skill once to confirm it still loads. Write the pass record as
   step 6 of SKILL.md says.

## The portability check

A portable skill passes this check; a reading of the text does not
replace it. Search SKILL.md and every file under `references/` except the
harness references themselves (`references/<harness-id>.md` and any
`references/<harness-id>-*.md` companion, such as a long field table) for
these,
and paste the result into the pass record:

- a harness's command-line tool or its flags: `claude -p`, `claude --`,
  `codex `, `agy `
- its configuration paths: `~/.claude`, `.claude/`, `~/.codex`,
  `~/.cursor`, `~/.gemini`, `.agents/`, `.cursor/`, `.github/copilot`
- its substitution or injection syntax: `${CLAUDE_`, `$ARGUMENTS`,
  `` !` ``, `@path` imports
- its frontmatter extensions: `argument-hint`, `when_to_use`,
  `disable-model-invocation`, `context: fork`, `user-invocable`
- its settings and mechanisms by name: `settings.json`, `skillOverrides`,
  `permissions.deny`, `PreToolUse`, `auto memory` (also spelled
  `auto-memory`)
- its tool names used as tools: `Read tool`, `Bash tool`, `Skill tool`,
  `Agent tool`, `Task tool`, `WebFetch`, `WebSearch`, `AskUserQuestion`,
  `TodoWrite`
- its instruction files as a dependency: `CLAUDE.md`, `CLAUDE.local.md`,
  `AGENTS.md`, `GEMINI.md`

In a shell, from the skill directory. The file list is piped through
`xargs` so it works in bash and zsh alike, and `--exclude` is not used
because not every grep honors it by bare name:

```
{ echo SKILL.md; find references -maxdepth 1 -name '*.md' | grep -vE '/(claude-code|cursor|codex|copilot|antigravity|gemini-cli)[^/]*\.md$'; } | xargs grep -nE 'claude -p|claude --|\$\{CLAUDE_|\$ARGUMENTS|~/\.claude|\.claude/|~/\.codex|~/\.cursor|~/\.gemini|\.agents/|\.cursor/|\.github/copilot|argument-hint|when_to_use|disable-model-invocation|context: fork|user-invocable|settings\.json|skillOverrides|permissions\.deny|PreToolUse|[Aa]uto[- ]memory|(Read|Bash|Skill|Agent|Task) tool|WebFetch|WebSearch|AskUserQuestion|TodoWrite|CLAUDE\.md|CLAUDE\.local\.md|AGENTS\.md|GEMINI\.md|!`'
```

Zero hits passes. A hit that is subject matter rather than dependence (a
documentation skill that lists `AGENTS.md` among document kinds, the
description's trigger vocabulary, this check's own text) is named in the
pass record with that reason. Anything else is a dependence, and the skill
is not portable until it is gone. A harness's product name in a sentence
such as "when you run in Claude Code, read its reference" is not a hit.
