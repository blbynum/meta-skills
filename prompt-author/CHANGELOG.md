# Changelog

## 2026-10-31 — migrated to the portable kind: Claude Code facts to a harness reference

This entry supersedes the entry below of the same day ("migrated: no
config keys; two portability edits"). That pass claimed portability
without the portability check and left the Claude Code `/goal` section in
the body. This pass follows "Migrating an existing skill" and "The
portability check" in skill-author/references/skill-config.md, as rebuilt
the same day, in a session started from Ben's review session (cwd
`~/projects/ai`).

Kind: portable, `metadata: {harness: portable}`, decided in the brief. The
subject is prompts for any model and harness; only the `/goal` facts and
the session-rename tool are Claude Code facts.

Changes:

- New `references/claude-code.md` (68 lines, with a contents list). The
  `## Claude Code /goal` section moved in full and is now `## /goal`. A
  word diff against the pre-edit body shows one change: "the three in
  Scope" became "the three in SKILL.md's Scope section", so the
  cross-reference resolves from the new file. A new "Session rename"
  section gives the "Session title" section its Claude Code tool again:
  `mcp__ccd_session_mgmt__set_session_title` with `session_id: "self"`
  and `title`, often deferred, absent in the terminal CLI, and unable to
  rename a subagent's own session. These facts come from the live tool
  schema, loaded in this session.
- SKILL.md: the 48-line `/goal` section became "## Harness references",
  4 lines: harness facts live in `references/<harness-id>.md`; when you
  run in Claude Code, or the prompt will run there, read
  references/claude-code.md for `/goal` and the session-rename tool. The
  clause "or the prompt will run there" keeps the old section's own
  condition ("A prompt that will run in Claude Code"). The `/goal` choice
  depends on where the produced prompt runs, not where this skill runs;
  the brief's pointer wording named only the second case. 335 lines
  became 292.
- Frontmatter: `metadata: {harness: portable, last-verified:
  "2026-10-31"}`. `export: portable` removed: a portable skill uses spec
  fields only, and config-export reads tags but never requires them, so
  an untagged skill goes through its interactive picks. Description
  unchanged: it names no harness dependence ("session" is generic).
- Not changed: every mode, the Scope section, "Session title", "Prompt
  craft", "Strip on sight", "Target model", and Delivery. The edit
  replaced only the block from the `/goal` heading to `## Delivery`, and
  the metadata line.

Config: no config keys. A scan of SKILL.md and references/ for absolute
paths, hosts, accounts, user names, and URLs found none. "The research
skill" in the `/goal` text is example wording for a condition, not a
hand-off. The comment in `evals/ab-evals.json` with this machine's paths
stays, as the earlier pass decided: the skill never reads it.

Portability check, run from `~/.claude/skills/prompt-author` with the
command in skill-config.md. Before the edit:

    SKILL.md:304:the prompt or passes it to `claude -p`; the Skill tool cannot run it, and

After the edit, files searched `SKILL.md` (references/claude-code.md is
the harness reference and is excluded by the command):

    (no output; grep exit 1)

Zero hits. The one product name left in the body is the pointer sentence,
which the check's own text exempts.

`last-verified` is set to 2026-10-31 as the brief asked. It records this
pass's portability check and the rename-tool schema check. No
prompting-guidance source was re-fetched (step 2 exempt: structural
pass). The guidance sources were last checked on 2026-10-29 (the Claude
Code goal, commands, and skills pages) and 2026-10-28 (the vendor
prompting pages, by the doc-author pass). The next guidance refresh
should search for changes since 2026-10-28, not since this date.

Checks:

- Desk-checked against 2 scenarios. (1) Refine in the Claude Code
  desktop app, mid-session: "fix this prompt: 'You are a world-class
  senior Python engineer with 20 years of experience. IMPORTANT: You MUST
  think step by step. Write a function that dedupes a list of dicts by
  the key {{key}}.'" The text is addressed to a model, so refine mode; no
  rename, because the session has prior conversation; strip the ALL-CAPS
  pressure, the manual chain-of-thought (frontier target), and the
  persona; keep `{{key}}`. The pointer applies because the skill runs in
  Claude Code, and the reference's one-turn bullet says no goal. No wrong
  path found. (2) Package in Claude Code: "wrap this up into a prompt so
  a fresh session can finish migrating the remaining skills unattended".
  Package mode; the prompt will run in Claude Code, so the pointer sends
  the model to the reference. The `/goal` section there decides: a long
  run, no user gate, and an end state the agent's output can show (the
  check output per skill), so the prompt leads with `/goal`; the
  condition carries the task, names skill-author in prose, states the
  proof, names what must not change, and has a turn bound; the rationale
  notes auto mode; the 4,000-character limit stated there caps the
  package. Wrong path looked for: a model in another harness that writes
  a prompt for Claude Code would skip the reference under run-only
  wording. The "or the prompt will run there" clause closes it.
- Trigger eval not run: the description did not change, so none is due.
- One run in this session (Claude Code 2.1.287, desktop app,
  claude-opus-5-5): `/prompt-author` with the scenario-1 refine request.
  The loaded body showed "## Harness references" and no `/goal` section.
  Output: a one-sentence prompt with `{{key}}` kept, a rationale that
  names the three removed patterns and the target dependence, and three
  offers. No rename attempt, no `/goal`.
- No A/B: behavior not rewritten.

Watch items: (1) The `/goal` guidance now reaches the model only when it
opens the reference. The research migration of the same day saw one run
that did not open a harness reference (n=1). The 2026-10-29 eval set
(`evals/ab-evals.json`: goal-fit-long-run, goal-unfit-user-gates)
measures this; run it against this body when budget allows. If the model
skips the reference, the fix is a stronger pointer, or the section back
in the body under `harness: claude-code`. (2) The rename-branch watch
item in the entry below still applies; the tool name is now in the
reference.

## 2026-10-31 — migrated: no config keys; two portability edits

Migrate pass under skill-author's "Migrating an existing skill"
(skill-author/references/skill-config.md), in a desktop session started
with `/skill-author migrate /prompt-author` (cwd `~/projects/ai`). Read
SKILL.md, CHANGELOG.md, and the three files under `evals/` for
machine-specific values. Found none in the skill: no absolute path outside
the skill, no hostname, user name, account, or vendor choice, and no
companion skill named in prose ("use the research skill" in the `/goal`
section is an example of a condition's wording, not a hand-off). Result:
no Config section, no `config.local.yaml`, no `.gitignore`. The comment in
`evals/ab-evals.json` holds this machine's Python and skills paths as the
author's run instructions; the skill never reads it, so it stays.

Portability rules (step 6) changed two things:

- Frontmatter: removed `argument-hint`, a Claude Code extension outside the
  spec's six fields. Cost: Claude Code's `/prompt-author` autocomplete no
  longer shows the hint; the description already names the inputs.
  `metadata.export: portable` stays because config-export reads it (the
  same decision as the notes and study-credibility migrations of
  2026-10-31).
- Session title: the sentence that named the desktop tool
  (`mcp__ccd_session_mgmt__set_session_title`, `session_id` `self`, "load
  it first if deferred") now names the action: rename where the
  environment provides a way to, search the available tools before
  concluding there is none, skip silently otherwise. The behavior the
  2026-08-30 feature asked for is unchanged; only the tool name left.

Nothing else in the body changed; the description is unchanged.

Checks:

- Desk-checked against 3 scenarios. (1) Desktop app, new session,
  `/prompt-author fix this prompt`: the rename sentence sends the model to
  search for a rename tool; in the migrating session a tool search for
  "rename session title" returned the desktop rename tool as its first
  hit, so the action wording finds it; then refine mode. (2) Terminal
  `claude -p`: no rename tool, silent skip (confirmed by the run below).
  (3) The skill copied into a Cursor or Codex project: spec-only
  frontmatter, no absolute paths, no harness syntax; the `/goal` section
  is conditional on the prompt's target and reads as subject matter there.
- Trigger eval not run: the description did not change.
- One headless run (`claude -p`, a prose write-mode ask about renaming
  `.jpeg` files, Claude Code 2.1.287, claude-opus-5-5[1m], `dontAsk`, cwd
  a scratch directory): the Skill tool loaded `prompt-author`, 3 turns,
  $0.22, 11 s; the output is a 3-line fenced prompt, a one-paragraph
  rationale, and four offers; no rename attempt and no mention of session
  titles. One sentence says `/goal` is not needed, consistent with the
  2026-10-29 watch item (still one sentence).
- No A/B: behavior not rewritten.

Step 2 research exempt: a structural pass that touched no guidance; the
portability rules came from skill-standards.md, whose sources were
verified 2026-10-30. `last-verified` unchanged at 2026-10-29; no guidance
source was checked this pass.

Watch item: the rename branch is desk-checked only (one tool search in the
migrating session). The first real new-session `/prompt-author` in the
desktop app should confirm the session is renamed. If the rename stops
firing, the fix is a stronger search instruction, or
`metadata: {harness: claude-code}` with the tool name restored.

## 2026-10-29 — added the Claude Code `/goal` section

Observed failure (step 0): in the desktop session "Teach prompt-author
when to use /goal" (cwd `~/projects/tea`), prompt-author was asked to
refine a prompt that runs `/skill-author` to build a tea-guide skill, and
had no text on `/goal` at all, so that session had to research the
command from the Claude Code docs before it could judge the fit. Earlier
the same day, in "White tea brewing guide" (transcript `1a9fc4d9-...`,
desktop 2.1.309), the user typed `/research /goal <condition>`; the
transcript stores `/research` as the command and the whole `/goal ...`
text as its arguments, and no goal was ever set. Ben's requirement: the
skill "should be able to write a prompt with it and determine if its
worth using".

Added one section, "Claude Code `/goal`", between Target model and
Delivery: what the command does (a completion condition; after each turn a
small model judges it from the conversation and starts the next turn while
it is unmet; clears on met, impossible, or an error the user has to fix);
the fit rule (lead with `/goal` for a long unattended run with an end
state the agent's output can show; an ordinary prompt when the run has a
user gate, because the evaluator starts another turn instead of waiting
and several turns without tool use halt the loop; nothing for a one-turn
task); what the condition carries, since it is the whole prompt (task,
skills named in prose, end state plus proof, what must not change, a turn
or time bound — the bound is a bounding addition allowed like the three in
Scope); the placement rule (built-in command, user-typed or `claude -p`,
not in the Skill tool, first in the message or it is argument text); and
the rationale note on auto mode. Nothing else in the body changed.
`last-verified` refreshed to 2026-10-29 for the sources checked this pass
(the goal, commands, and skills pages); the prompting pages were last
re-read by the 2026-10-28 doc-author pass and were not re-fetched here.

Step 2 research: the goal page fetched in full as raw markdown on
2026-10-29, plus the commands and skills pages for the built-in/stacking
facts and the two tea transcripts for the placement failure. Provenance in
the shared ledger under "prompt-author skill subject-matter sources". One
nuance the brief did not have: at the terminal prompt several skills can
stack at the start of one message, but expansion stops at the first token
that is not an inline user-invocable skill, and `/goal` is not one, so
`/goal` after a skill becomes argument text in every mode. The skill
states the safe rule (lead with `/goal`, name skills in prose) rather than
the stacking mechanics.

Desk-checked against 3 scenarios: (1) a prompt to run `/skill-author`
with grilling rounds and a draft approval, "as a /goal" → the user-gate
bullet refuses the goal, names the reason, and offers the split;
(2) an unattended layout-conformance run over a directory with a check
script → leads with `/goal`, condition carries the proof, the constraint,
and a bound, rationale notes auto mode; (3) refine of `/research /goal
...` → the placement paragraph explains the argument-text capture and the
rewrite names the research skill in prose. Wrong path looked for and not
found: the condition paragraph could read as licence to add requirements,
but it names the bound as the one allowed addition and defers to Scope.

Eval set created at `evals/ab-evals.json` (four prose queries with the
tea-session texture; the skill's own examples use the docs page's
domains, so no query identifier appears in the skill text — grepped).
Description unchanged, so no trigger eval. Watch item: a user who asks
for "a /goal condition" by that name has no matching phrase in the
description; if prompt-author fails to load on such an ask, add the phrase
and run the trigger eval.

Measured (A/B, `ab_eval.py --mode skill --old --new`, old body against new
body, 4 evals × 2 arms × 3 runs = 24 runs, $4.27; Claude Code 2.1.287 on
the CLI, model claude-opus-5-5[1m], builtin plugins agents-md,
plugin-authoring, telemetry, no user hooks, the user's rules loaded in
both arms; each body staged as a renamed project skill with the personal
copy off). Graded by the author against `expected_behavior`, with a
mechanical pass (`evals/check_goal_outputs.py`) for the observable
signals; `evals/ab-eval-2026-10-29-summary.md` holds the harness summary.

- goal-fit-long-run (skill loaded 3/3 in both arms): new 3/3 — every
  prompt leads with `/goal`, the condition asks for the per-guide exit
  codes to be shown in the conversation, keeps the headings-only
  constraint, carries a 30–40-turn bound, and the rationale notes auto
  mode; old 0/3 on the `/goal` discriminators (ordinary prompts with
  "don't stop to ask me" and acceptEdits advice, no bound). Cost new
  $0.218±0.005, old $0.243±0.003.
- goal-unfit-user-gates (new loaded 3/3, old 1/3): new 3/3 — refuses the
  single goal with the evaluator reason, splits into an ordinary
  `/skill-author` prompt and a `/goal` for the unattended remainder,
  keeps every step, names the turn bound as its one addition. Old: all
  three also refuse and split, "from memory" and saying so, but the two
  runs where the skill did not load invent requirements (six grilling
  topics, "at least 3 rounds", a skill path, eval cases), 0/3 bound the
  goal or ask for proof in the conversation, and one keeps "stop and ask
  me" inside the condition. Old 1/3 pass all four.
- goal-placement-refine: the skill loaded in 0/6 runs — "this is what i
  typed ... fix it:" plus a slash-command line matches the description in
  neither arm — so this eval measured the base model, not the artifact.
  All six runs explain the argument-text capture, lead with `/goal`, and
  name the research skill in prose; the old arm says it answered from
  memory. The placement paragraph is therefore desk-checked only.
- one-turn-no-goal (new loaded 3/3, old 0/3): new 3/3 — no `/goal`, at
  most one sentence saying one turn finishes the task, 28–52-word
  prompts; old 0/3 on the ask-only criteria (95–120-word prompts that
  merge with an existing Sources section and ask for a diff). That
  difference is the Scope section at work, not this pass; for this pass
  the eval shows no over-application of `/goal`.

Limits: three runs per arm; grading by the author, not blind; the old
copy loaded in 4/9 runs on the three triggerable evals against 9/9 for
the new copy with an identical description (watch item in skill-author's
changelog). Post-A/B wording edit, desk-checked only: "It has to open the
message" → "It has to come first in the message", rewrapped.

Watch items: (1) the refine phrasing above did not load the skill in
either arm — a user who pastes a slash-command line with "fix it" gets
the base model; a description phrase for a command line that did not do
what they expected, plus a trigger eval, is the fix if it recurs.
(2) Two of three one-turn outputs spend one sentence saying `/goal` is
not needed; acceptable, but if that grows into a paragraph the section's
one-turn bullet needs softening.

## 2026-08-30 — rename new sessions to "Refine Prompt: <subject>"

Feature request from Ben (this session): when the skill's invocation is
the first prompt of a new session, rename the session so refinement
sessions are findable in the session list. Added a `## Session title`
section between "Picking the mode" and "Mode specifics": rename to
`Refine Prompt: <subject>` via `mcp__ccd_session_mgmt__set_session_title`
(session_id `self`), silent skip where the tool does not exist, no rename
when the session has prior conversation. Description and frontmatter
unchanged; `last-verified` deliberately not refreshed — no guidance
sources were checked this pass.

Step 2 research skipped: feature exemption (adds capability, touches no
model/platform guidance). The one load-bearing fact — the tool's name and
parameters — was verified against the live tool schema in this session,
not recalled. Portability checked: cursor-export's conversion map already
maps `mcp__ccd_session_mgmt__*` sentences to deletion.

Desk-checked against 3 scenarios: (1) new desktop session with
`/prompt-author fix this prompt` → rename fires, then refine mode;
(2) mid-conversation package request → title kept, guarded by the
prior-conversation sentence; (3) new terminal-CLI session → silent skip.
Step 5b skipped, reason: description unchanged (no trigger eval), and the
rename depends on desktop-app-only MCP tools the ab_eval headless harness
does not expose, so an A/B run cannot exercise the behavior. The
silent-skip branch was additionally checked with one headless `claude -p`
run (claude-opus-5, 1 turn, $0.24): the skill loaded and produced a
write-mode prompt with no rename attempt and no mention of session
titles. The rename branch is desk-checked only until the next real
new-session invocation.

## 2026-08-18 — prompt-author — renamed from refine-prompt
Ben's decision, part of moving the collection to one `<subject>-author`
pattern (skill-author, rule-author, agent-author, persona-author,
prompt-author, mcp-author). Directory and `name:` renamed, so the slash
command is now `/prompt-author`; description and body unchanged. Live
pointers repointed: ai-retrospective (its description's "defer to the
refine-prompt skill", the intro, and the hand-off line) and the mc-computer
project's `CLAUDE.local.md` bullet ("Use `/prompt-author` to write or
rewrite prompt text"). The ledger's narrative mentions of refine-prompt are
historical and stay; its header now carries the rename map. Entries below
keep the name in use at the time.

## 2026-08-18 — scoped four strip-on-sight claims to the models they were measured on

A review of the meta-tooling found that the Strip on sight list and the
Target model section carried claims whose model qualifier had been dropped
when they entered the provenance ledger. Each is now stated at the scope its
source gives it, after the ledger entries were rewritten from the primary
pages:

- Self-checks: the vendor names only Opus 5 as the model that self-verifies
  without instruction. Fable 5's page asks for explicit self-verification at
  intervals in long runs. The bullet said "Opus 5, Fable 5" — for this user's
  default target that stripped exactly what the vendor says to keep. Now it
  says "a target whose vendor page says it self-verifies (Opus 5 today)" and
  names the Fable 5 exception.
- ALL-CAPS/MUST and anti-laziness nudges: documented to over-trigger on Opus
  4.5/4.6 (tools and skills) and on Claude 4.6 models respectively; not
  documented for later models, and the vendor's own samples still use
  "MUST". The bullets say so and keep the plain condition as the preferred
  form rather than calling emphasis an error.
- Manual chain-of-thought: still a documented fallback when thinking is
  off; the bullet now points at Target model like the self-check bullet.
- Capability tier: "scales inversely with capability" overstated the
  evidence (a 2026 judge-stability study found scale does not predict
  prompt sensitivity, and Fable 5 is a frontier exception on verification).
  Reworded as a default the target's page settles.

Also: the worked example labelled "check current sources" as craft when the
Scope section's own definitions make it an addition — it is now the first
offer under the prompt; "at most five" offers read as a target (five of six
A/B outputs carried exactly five), so it now says "only the ones worth
naming, up to five; zero is valid"; the optimizer line in Delivery says "can
beat" with mixed evidence rather than "beat"; the "format" overlap between
craft and the allowed additions is resolved by making the third addition a
length bound only. The 08-17 entry's "three of four" cost claim was two of
four and is corrected in place. Desk-checked below in the skill-rule-creator
CHANGELOG; no A/B on this pass (wording scoped, no requirement moved).

## 2026-08-17 — added the Scope section: prompts carry the user's requirements only

The skill added requirements the user never gave. Sixteen past sessions that
invoked it were read; six produced a prompt from a short ask, and the size of
the addition scaled inversely with the length of the ask — a 30-word ask
produced 458 words (15.3x), a 165-word ask produced 469 (2.8x). Counted on two
real cases: a four-question ask about self-hosted Confluence gained about 13
requirements (a deployment plan, a compose file, a reverse-proxy config, SSO,
backups, hardware sizing, an alternatives comparison), and a one-sentence
question gained about 7 (a shortlist cap, a rejected-candidates section, a
ranking criterion).

The cause was in the text. Write mode said to capture "any constraints they've
implied"; refine mode said to "infer the intent ... then rewrite the prompt to
achieve that intent"; two craft bullets said to set constraints and agent
boundaries. Nothing said where a requirement may come from, so every gap in an
ask read as an invitation.

Fixed by adding a Scope section that splits substance (from the user) from
craft (from the skill), gives a traceability test, sends additions to an offers
list under the prompt, and carries a worked example. Three constraining
additions stay allowed: permission to say the evidence is thin, a scope
sentence, and a length bound. Write, Refine, and Package were reworded, four
craft bullets changed, and Delivery now requires a ledger naming anything in
the prompt the user did not say.

Evidence: the Opus 5 prompting page documents scope expansion as model behavior
and prescribes an explicit clamp; the best-practices "Overeagerness" section
shows the clamp written as named categories; the GPT-5.2 guide reaches the same
remedy independently. The correction is bounded by arXiv 2505.13360, which
finds models infer unstated requirements correctly only about 41% of the time
and underspecified prompts twice as likely to regress — but also that
specifying every requirement does not consistently help. Hence offers to the
user rather than either silent filling or silent dropping.

Measured with `ab_eval.py --mode rule`, old body against new body, four evals
taken verbatim from real sessions, two runs per arm. Two evals were
informative. On the long detailed ask the old text produced 709 and 713 words
from a 132-word ask with about 12 invented requirements (a tag taxonomy, a
manifest schema, three named scrub passes, a default output directory); the new
text produced 202 and 188 words, kept every stated requirement including the
`<ISO-datetime>` token, added only permission to ask, and moved five
suggestions to offers. On the vague ask ("make my code better") the new text
refused to define "better" and said so, where the old text supplied a ranked
quality list. The Confluence eval is contaminated — its ask is the worked
example in the new text — and the meta-tooling eval measured nothing, because
in the clean-room harness both arms answered the question instead of writing a
prompt. Cost fell on two of four evals (with-arm means 0.226→0.154 and
0.272→0.206; the other two rose slightly, 0.209→0.216 and 0.148→0.154) —
corrected 2026-08-18 from "three of four" after a re-read of the two
`summary.json` files. The A/B also ran two runs per arm against the script's
own three-run default, so the direction on the long ask is warranted and the
rest is a smoke test.

Limits on record: two runs per arm is a small sample, and `--mode rule` is a
clean room without the user's own rules loaded. A skill is context, not
enforcement — no hook can check that a sentence traces to the user's words, so
the ledger exists to make drift visible to the user rather than to prevent it.

## 2026-08-15 — added the Target model section

Research pass on whether prompting advice diverges by model, and how to cover
that without bloat. Tier-1 evidence confirmed the divergence is real: the
Anthropic prompting reference now leads with model-specific guidance and keeps
separate pages for Fable 5, Sonnet 5, Opus 5, and Opus 4.8, with per-model
deltas on verbosity, over-verification, subagent delegation, literal
instruction following, and accepted sampling parameters. OpenAI (GPT-5.1 and
GPT-5.2 guides) and Google (Gemini 3 developer guide) publish comparable
per-release deltas, and all three say prompts written for older models
over-steer newer ones. Tier-2 work supports the capability-tier axis
(chain-of-thought gains and prompt sensitivity both shrink as capability
rises) and the non-transfer of tuned prompts across models.

Added one Target model section: default target is the running model, a
user-named target overrides it, reasoning scaffolding scales inversely with
capability, and release-specific behavior gets looked up in the vendor's page
rather than recalled. The section stores which axes differ and where to look,
never per-model facts, so it does not go stale on each release. Folded the old
Delivery bullet on model targeting into it and pointed the self-check entry in
"Strip on sight" at it.

Rejected: per-target sub-skills with a triage layer. The divergences number
about five axes, the per-model files would duplicate shared craft and expire
on each release, and no public benchmark shows that following a vendor's
per-model page beats generic good prompting. No evidence was found that a
prompt is refined better by the model that will run it; the measured lever is
evaluation against the target, not the refiner's identity.

## 2026-08-15 — created

Initial version. Four modes: write, refine, package, retrospective. Seeded
from the research vault (`~/ai/notes`, tags `prompting`/`research`) with
primary sources re-fetched the same day: the consolidated Anthropic prompting
best-practices page, the Prompting Claude Fable 5 page, the Wharton
chain-of-thought report, and the GEPA repository. Community prompt-refinement
skills (prompt-architect, wagnersza/prompt-improver) reviewed; adopted the
prompt-plus-rationale-plus-settings-note delivery shape, rejected framework
menus and progressive questioning as conflicting with the
minimum-necessary-structure principle. Provenance for all claims lives in
skill-rule-creator's references/sources.md.

## 2026-10-31 — dependency reduction: placeholder skill name in the Claude Code reference

Pass from `~/projects/ai/dependency-map/reduction-plan.md`. Research
exempt. `references/claude-code.md` uses "<name>" and "/<skill>" in its
`/goal` examples instead of the research skill. Description unchanged;
no trigger eval due.

## 2026-10-31 — moved to the meta-skills repository

Directory moved with its files to `/Users/ben/src/skills/meta-skills`
and symlinked into `~/.claude/skills` by the repository's `link.sh`. No
content change in this step; see skill-author's entry of this date.
