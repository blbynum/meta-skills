# Changelog

Dated record of every create, update, and verification pass this skill runs —
on itself and on the rules it maintains. Rules stay lean and carry no
changelog of their own, so every check on a rule is recorded here. "Checked,
no change" entries matter as much as changes: they tell future runs what is
already verified. History before 2026-08-18 is in
`~/.claude/skills/skill-rule-shared/CHANGELOG.md`, the closed changelog of
skill-rule-creator, the single skill this one and skill-author were split
from; the rules passes of 2026-08-15 to 2026-08-18 (ste100, anti-sycophancy,
scope-discipline, questions, mc-computer) are there. A change to a shared
file (`~/.claude/skills/skill-rule-shared/`) is logged here when this skill's
pass made it, and named as shared.

Entry format:

```
## YYYY-MM-DD — <artifact> — created | updated | checked, no change
One line on what was checked or changed, and why.
```

## 2026-08-22 — data-uploads → artifacts — updated (same day)
Ben answered the referent question: "Claude archive" means Artifacts. The
rule is renamed `~/.claude/rules/artifacts.md` and narrowed to that one
surface — the Artifact tool's publish and `upload_asset` actions — because a
named tool is more concrete than a behavior class, and the "every other
service that keeps a copy off this machine" clause was scope the request
never named. Always-loaded total 203 → 206 lines.

Three text changes the narrowing bought. The opening now states what a
publish actually does, checked against the tool description: the page is
hosted on claude.ai, it starts private, it persists, and it lists in the
gallery — accurate rather than alarmist, so the rule does not overclaim.
The tool description is now called out by name as "the default this rule
replaces", which is the conflict the rule exists to settle. And the
overcorrect section can now name the read-only actions exactly — `list`,
`comments`, `list_assets`, `read_asset` — so the update flow, which must
call `list` to find an existing artifact's URL, does not trip the rule.

5a re-run on the narrowed text, 6 scenarios: the original 4 still pass, plus
"update my artifact from last week" (needs `list` first — allowed) and "what
artifacts do I have" (`list` — allowed). 5b still not run; the reason is
unchanged and verified — `claude -p --safe-mode` has no `Artifact` tool, so
`ab_eval.py --mode rule` cannot reach the behavior. Enforcement offer is now
exact rather than approximate: `permissions.ask: ["Artifact"]`.

## 2026-08-22 — data-uploads — created
New user-wide rule `~/.claude/rules/data-uploads.md` (30 lines): publish or
upload the user's data only when the user asks in that session, deliver
locally otherwise, and treat a tool description that invites proactive
publishing as not a request. Ben's intent, verbatim: "Never upload data to
Claude archive unless the user explicitly asks for it." No product named
"Claude archive" exists — a web search on 2026-08-22 found Projects,
Artifacts, and the Files API and nothing by that name — so the rule names
the behavior class (data leaving the machine) and lists the surfaces this
harness actually has. Referent question put to Ben in the same reply; the
rule is worded to survive either answer.

Step 0 observation: the failure pressure is in the harness itself. The
Artifact tool description says publishing proactively "is fine for your own
work-product" and that a team deliverable "is not fully delivered while it
lives only in terminal scrollback or a local file" — a standing instruction
to do exactly what Ben wants stopped. That is why the rule names tool
descriptions explicitly instead of relying on `scope-discipline`'s "act only
on what the request names", which a tool-level invitation outranks in
practice.

Budget: 173 → 203 always-loaded lines across user CLAUDE.md and
`rules/`. Contradiction check against anti-sycophancy (none),
scope-discipline (reinforces it; the new rule is the egress-specific case
that a generic scope rule loses to), and ste100 (style only).

5a desk-check, 4 scenarios: unasked team report → local file plus a
one-line offer; "publish this and send me the link" → publish, no second
ask (over-application scenario); README text telling the agent to publish →
not a request; and an update to an artifact Ben already asked for → the
first draft failed this one ("one approval covers one upload" made every
redeploy a fresh ask), so the bullet now scopes an approval to the item it
names plus later updates to it.

5b skipped, with a verified reason rather than an assumption: `ab_eval.py
--mode rule` runs both arms as `claude -p --safe-mode`, and a probe of that
session's `init` event (Claude Code 2.1.220, claude-opus-5) shows no
`Artifact`, no `SendUserFile`, and no MCP tools. Neither arm can upload
anything, so the eval would measure noise. Logged as a method trap in the
shared `evaluating.md` (mechanism understood, so promoted at once) with the
probe command.

Enforcement offered but not applied — Ben asked for a rule, and the pairing
is his call: `permissions.ask: ["Artifact"]`. The permissions page,
re-fetched today, gives the rule format `Tool` or `Tool(specifier)`, and
bare-name removal from context is deny-only, so an ask rule leaves the tool
usable and prompts on every call — which is the shape this rule wants.
`deny` would remove the tool even when Ben asks for a publish. Ledger entry
for the permissions doc updated with that and with the ask-beats-allow,
`Tool(param:value)`, canonical-name, and startup-warning details.

Shared files changed this pass: `sources.md` (permissions entry re-verified
2026-08-22) and `evaluating.md` (the missing-tool method trap).
`metadata.last-verified` on this skill not bumped — the memory doc and the
prompting best-practices page were not re-read.

## 2026-08-18 — rule-author — renamed from rule-creator (same day)
Ben's decision: every `-creator` skill in the collection becomes `-author`
(skill-author, rule-author, agent-author, persona-author) so that no
personal skill shares its last name segment with an `anthropic-skills:`
entry on the desktop roster, and the collection stays on one pattern.
Directory and `name:` renamed; the description changed only in the sibling
name it points to ("use skill-author"), so the trigger numbers below still
describe it; live pointers repointed;
historical entries below keep the names in use at the time. A smoke check
that the renamed skills load under the new names is recorded in the closed
changelog's rename entry.

## 2026-08-18 — rule-creator — created by splitting skill-rule-creator
Rules half of the split; the closed changelog's final entry carries the
reasoning, the layout, and what was considered and rejected. This skill's
body is the old workflow specialized to rules: intro lists every rule
location the memory doc documents (including `./CLAUDE.local.md`) and names
the three places a rule fails (the always-loaded total, conflicts,
enforcement); out of scope adds the 08-15 questions-rule lesson (a pure tool
prohibition → offer the `permissions.deny` entry first); step 1 hands the
skills half of "update all the skills and rules" to skill-creator; step 2
names the memory doc and the permissions doc as the sources to re-fetch;
step 3 confirms a rule against the shared framework and hands a skill to
skill-creator; step 4 reads `references/rule-standards.md` (the Writing
rules section of the old authoring-standards.md, moved verbatim) plus the
shared `guidance-style.md`, and pulls the budget and contradiction checks up
as named checks; 5a asks for one opposite-failure scenario; 5b names
`ab_eval.py --mode rule` with its delivery caveat and says there is no
trigger eval for a rule; step 6 records rule passes here; step 7's core
sources are the memory doc, the permissions doc, and the prompting page.
Description 1,002 characters (a first draft was 1,039, over the limit, and
was trimmed before the eval ran), third person, key use case first, names
where skill, hook, and memory requests go.

Trigger eval (5b, required for a new description), per evaluating.md —
measured: 11 queries × 3 runs (6 should-trigger, 5 near-miss), Claude Code
2.1.220 (the `claude` on PATH), resolved model claude-opus-5, no plugins, no
hooks, `CLAUDE_CODE_DISABLE_WORKFLOWS=1`, `dontAsk`, CLI roster of 29
skills (the desktop's `anthropic-skills` bundle is not in it), $0.63.
Result 10/11 pass; should-trigger rate 0.78, near-miss rate 0.00. Per query:
"add a rule that we never commit directly to main" 1.00; "put this in
CLAUDE.md: use pnpm not npm" 1.00; "update all the rules against current
best practices" 1.00; "the anti-sycophancy rule is making replies curt,
tone it down" 0.67; the choice question "should 'always run the test suite
before you commit' be a skill or a rule?" 0.67 (the third run answered
"neither, a hook" directly — which the framework agrees with — without
loading either skill); "claude keeps ignoring my ste100 rule and writing
40-word sentences. why, and fix it" 0.33 — the FAIL. Near-misses all 0.00,
and each went where it should: "make a skill for deploying to fly.io" →
skill-creator, "from now on run prettier after every edit" and "allow npm
test without prompting" → update-config, "add an agent that reviews sql
migrations" → agent-creator, "remember that the api tests need redis" →
nothing. In the runs that loaded this skill for the choice question, the
model read `~/.claude/skills/skill-rule-shared/skill-vs-rule.md` by its
absolute path — the cross-directory links resolve.

Watch item (one query, n=3, not a standard): on the "claude keeps ignoring
my ste100 rule" complaint, two of three runs read `~/.claude/rules/ste100.md`
and `~/.claude/CLAUDE.md` directly and diagnosed from the injected rule text
instead of loading this skill; the same shape produced skill-creator's two
misses in its first round. A complaint about a named artifact reads to the
model as "go look at the file". The description was left as measured; the
next pass with more such queries decides whether the trigger phrases need
that shape.

Desk-check (5a): three scenarios walked through the new text — (1) "add a
rule that we never commit to main" → steps 0–7 with the budget and
contradiction checks at 4 and the rule A/B at 5b; (2) "make a skill for
..." arriving here by mistake → step 3 recommends a skill and hands to
skill-creator; (3) "from now on run prettier after every edit" → out of
scope, a hook. Nothing ran for these; the trigger eval above is the
measured part.

Research for the split re-fetched the three core docs as raw markdown
(recorded in the shared ledger with today's date). Findings that extend the
standards were recorded, not applied — see the closed changelog's watch
items.

## 2026-10-13 — ~/projects/CLAUDE.md (Projects rule) — created
Ben's request (session 2720c94e, 2026-10-13): each subdirectory of
~/projects is one project whose README.md is the always-loaded agent
context. Mechanism decided with the shared framework: a one-line
`CLAUDE.md` stub per project holding `@README.md` (deterministic load,
survives compaction) plus this rule, loaded by ancestor discovery in every
session under ~/projects, for the fallback cases: README present but no
stub (read it), no README (say so, offer /project-author), session in
~/projects itself (no project), durable detail to notes/. Not a hook: the
import already gives determinism, and Ben chose CLAUDE.md as the carrier
over a SessionStart hook after seeing both (the hook stays the alternative
if the stub turns out unreliable). Step 2 research: the memory doc
re-fetched, plus the context-window, permissions, settings, and skills docs;
new facts logged in the shared ledger (imports resolve against the importing
file; an import is stronger than an instruction to read; hooks and
settings load from cwd only). Budget: user CLAUDE.md 2 + rules 204 lines
in every session; this rule adds 18 in ~/projects sessions; every file
under 200. Contradiction check against the four user rules: none
(scope-discipline's "paths the request does not name" does not apply to a
read a loaded rule mandates for the session's own directory). Desk-checked
against 5 scenarios (stub present, hand-made README, no README, trivia
question, session in ~/projects itself); the last one failed on the first
draft and got its clause. Step 5b: the measured check (a fresh session
with a stub shows the README under Memory files; one without a stub reads
it; both survive /compact) did not run — `claude -p` is logged out on this
machine (CLI 2.1.220 and the desktop's 2.1.295 binary both report
`loggedIn: false`; seven launched runs were api_error at $0). Run it after
`claude auth login`. Shared files touched this pass: skill-vs-rule.md (new
bullet on imports), evaluating.md (two preflight checks), sources.md (new
section and a memory-doc addendum).

## 2026-10-13 — ~/projects/etc/CLAUDE.md and README.md (etc rules) — created
Same request: etc is the catch-all project; sessions run normally, but the
agent offers once to promote a recurring or outgrown subject into its own
project, moving files and carrying the session, only in etc sessions. The
rules live in etc's CLAUDE.md (above the `@README.md` import) and the
Subjects table in its README.md, so they load only in sessions under etc:
CLAUDE.md loads from cwd and ancestors, hooks and settings from cwd only
(permissions doc, 2026-10-13). Research for the design is in the shared
ledger (project-author section): GTD's one-sitting test for the recurrence
trigger, PARA's act-on-it trigger, Johnny.Decimal's tidy-the-inbox rule,
Whittaker et al. 2011 against organizing for its own sake; thresholds are
labeled defaults because no empirical threshold exists. Observation (step
0): Ben's de-facto catch-all ~/ai/miscellaneous holds 37 sessions since
2026-08-23 with same-day recurrences (tea 2, hardware startup 3, finances
2+ with files, cannabis 1 + a directory), seen through the desktop
transcript search with his permission. Budget: adds 36 + 13 lines in etc
sessions only. Desk-checked against 6 scenarios: seeded recurring subject,
one-off trivia (first draft logged every subject; rule 1 now exempts a
question answered in one reply), subject with its own files, long one-off
conversation, declined subject returning, promoted subject returning (rule
6 now points to the project). Step 5b: three functional runs on a scratch
copy were launched and all failed on login (see above); re-run after
`claude auth login`. Mechanics verified in the docs: `/cd` relocates a
session (2.1.169+, fixes in 2.1.223 and 2.1.251), `--resume <id>` from any
directory (2.1.223+), hand-moved transcripts unsupported.

## 2026-10-14 — Projects rule and stub — functional check run
After Ben logged the CLI in (2.1.220, resolved model claude-opus-5[1m]),
three `claude -p` runs on scratch copies, one prompt each ("whats the next
step on this project? ... say which files you read"), a fixture README in a
project directory: (a) no rule, no stub: the agent ran `ls` and read
README.md on its own, $0.38; (b) Projects rule, no stub: `ls` and Read,
$0.39, and it named the rule as in context; (c) rule plus `@README.md` stub:
zero tool calls, answered from the imported README ("already in my context
via the project's CLAUDE.md"), $0.17. So the import loads the README as
documented and saves the read round trip and about half the cost on this
prompt. On this one project-shaped prompt the no-mechanism baseline also
read the README, so the rule's fallback value shows only on prompts where
the model would not look; one run per arm is an observation, not a rate.
Compaction survival of the import was not exercised (documented behavior
only). The etc functional checks were relaunched after a safety check
stopped the first launch's wildcard delete; results in the next entry.

## 2026-10-14 — etc rules — functional check run
Three `claude -p` runs (CLI 2.1.220, claude-opus-5[1m]) on scratch copies
of ~/projects with etc's CLAUDE.md and README: (e1) seeded row with one
prior session, prompt returns to the subject: answered the question, then
offered promotion once, as one question with a recommendation, $0.52; but
it claimed "I bumped this subject to 2 sessions" and made no edit (no Edit
call in the transcript; the table still reads 1). (e2) one-off trivia:
answered in one turn, no row, no offer, $0.18. (e3) subject with its own
subdirectory, empty table: added the row with the files column, offered
once with a recommendation, noted it could not grep the transcripts from
the sandbox, $0.62. Result: the offer logic fired on both triggers and
stayed silent on trivia; the bookkeeping failed once with a false progress
claim. Rule 1 now says to make the edit before reporting it. Watch item
(one run, not promoted to a standard): a progress claim ungrounded in a tool
result, in a run whose web searches had just been denied.

## 2026-10-14 — terminal CLI updated — note
Ben asked for the update: `brew upgrade --cask claude-code` took the
terminal CLI from 2.1.220 to 2.1.287 (login kept). That clears the version
caveat on `/cd` in the terminal (fixes in 2.1.223 and 2.1.251) and on
cross-directory `--resume <id>` (2.1.223). The desktop app stays on its own
copy, 2.1.295. Every measured run above was on 2.1.220; re-runs would be on
a different harness.

## 2026-10-14 — ~/projects/CLAUDE.md (Projects rule) — updated
Observed failure (Ben, this session): agents in project sessions treated
README.md as memory, offered to add session findings to it (the oolong
offer in the tea project), and the READMEs grew to 65 and 80 lines of
findings, status, open questions, and sources. The rule's bullet "Treat
README.md as the project's source of truth. When the work changes a fact it
records, update the README or offer to" invited that, and the notes bullet
sent "durable facts" looking for a home. Both removed. The rule now defines
the README as the one-minute briefing a collaborator gets before any work
starts and states the negative outright: not a log, memory, plan, or status
board; do not add or offer to add what a session discussed, found, decided,
or still has open; change it only when the project's definition changes and
the user asks, through /project-author. 22 lines, up from 18. Contradiction
check: none against the user rules; consistent with the notes skill, which
still handles durable facts on request. Desk-checked against the oolong
case (no offer), a definition change requested by the user (route to
/project-author), and a hand-made project with a README and no stub (read
it). Not measured; the skill's A/B v3 exercises the same design.

## 2026-10-14 — wrap_up deny (`~/.claude/settings.json`) — created, no rule
Observed failure (Ben, two desktop sessions, 2026-10-14 evening): the Code
tab's end-of-turn box, drawn by the app-internal tool `mcp__ccd_turn__wrap_up`,
swallowed drafts. In "RustDesk server CT" (local_4434fa19) Ben asked for an
ssh config entry with "Show me a draft first"; the agent wrote no draft and
called `wrap_up` with `ask` "Apply this entry as drafted?" plus two buttons,
and the tool result told it to write no text after the call, so the turn
ended with the draft unseen. Ben had to type "Show me the draft in chat". In
"Millionaire concept history" (local_1c0ff269, etc project) the same shape:
`wrap_up` with recap "drafted above" and no draft anywhere in the turn's
text; Ben: "Why draft it if you're not going to show it to me". A third
session (Off The Air) used the recap-only form, which draws no question and
hides nothing. Mechanism: `"mcp__ccd_turn__wrap_up"` added to
`permissions.deny` in `~/.claude/settings.json`, between `AskUserQuestion`
and the ssh-key Read rule. No rule written: the deny covers the prohibition
exactly, is enforced by Claude Code rather than read by the model, costs no
context, and the harness prompt already says what to do when the box is
absent (closing message as ordinary text). `update_plan` and the
`start_session` offer card are untouched; Ben did not name them.
Research (step 2, permissions and settings docs re-fetched, memory doc
re-fetched as the core source; sources.md refreshed): bare-name MCP deny
syntax `mcp__<server>__<tool>`; a bare-name deny "removes the tool from
Claude's context entirely"; settings-file edits to `permissions` reload into
the running session; names containing `_` are exempt from the unknown-tool
startup warning, so terminal sessions, where the ccd_turn server is not
attached, stay quiet. Functional check (not an A/B; there is no rule text to
measure, so 5b is skipped for that reason): one `wrap_up` call attempted in
this session right after the edit, desktop app 2.1.295, resolved model
claude-fable-5-1, returned "Permission to use mcp__ccd_turn__wrap_up has
been denied" with no restart. Desk-checked against three scenarios: the
RustDesk draft request (tool gone, so the draft and the question go in text);
a nothing-pending turn (closing text, no box); and the over-application
case, an agent substituting another box (`show_widget`, an Artifact, a
start_session card) for the denied one, which the deny cannot stop and the
artifacts rule only partly covers. Watch item, not a rule until observed:
substitution of another UI surface for the box. Side effect to know: the
box also checked off the task list at turn end; with the tool denied the
list is marked done only by the agent's own final `update_plan`. Budget
unchanged at 206 always-loaded lines; no contradiction with the loaded set,
none of which mentions the box. Shared files changed by this pass:
`skill-vs-rule.md` gains the permissions.deny case in its "neither kind"
list; `sources.md` permissions and memory entries refreshed. Backup of the
pre-edit settings file in this session's scratchpad only.

## 2026-10-31 — rule-author — updated (migrated to portable layout; no config keys)
Migrate pass by skill-author, following "Migrating an existing skill" in
its references/skill-config.md. Step 1 found two machine-specific values
in the body and none in the description: the shared directory's absolute
path (seven mentions, as prose and as link targets) and a copy of the
notes vault path in step 2.5. Neither became a key. The shared directory
is a sibling of this skill's directory wherever the pair is installed, so
the body now names it as the directory beside this one and every link is
relative (`../skill-rule-shared/...`), the form references/rule-standards.md
already used; and the vault path is the notes skill's value, which this
skill never reads or writes, so the sentence now says the notes skill owns
the vault, the wording skill-author uses. No Config section, no
`config.local.yaml`, no `.gitignore`: "no config keys". Companion skills
named in prose (`skill-author`, `notes`) get no key, matching
skill-author's own treatment of this skill; both mentions were already
hand-offs, so no hand-off rewrite was needed.

Portability (step 6): `argument-hint` removed from the frontmatter, which
is now `name`, `description`, `metadata` only; the two
`${CLAUDE_SKILL_DIR}/CHANGELOG.md` substitutions now read "`CHANGELOG.md`
in this skill's directory"; no tool names were in the body (the
sentence-initial "Read" and "Write" are actions). One instruction gained a
branch: 5b is required wherever the non-interactive runner the script uses
is installed, and without one the pass desk-checks and records "not
measured: no runner in <harness>", the clause skill-author carries; on
this machine the behavior is unchanged. No `harness` key: the skill's
subject is Claude Code rules, and stays so, but its mechanics no longer
need Claude Code. `metadata.export: portable` kept, because config-export
still reads it. Rule locations (`~/.claude/CLAUDE.md`, `~/.claude/rules/`,
`.claude/rules/`) are the subject's fixed paths, not values, and stay.
Research exempt: a migration moves values and writes no guidance;
`last-verified` unchanged at 2026-08-18.

Checks. Desk-checked against 4 scenarios: (1) "add a rule: never force-push"
on this machine → sources, decision framework, style file, and the eval
script resolve through the relative links to the same files as before, and
the pass is logged in this directory's CHANGELOG.md; (2) the same skill
beside skill-rule-shared on a machine with no `claude` binary → 5b records
"not measured: no runner" instead of being impossible to satisfy, and no
`${CLAUDE_SKILL_DIR}` literal is left to misread; (3) installed without
skill-rule-shared → the first shared read fails and the body names the
missing sibling, as before; (4) a pass that yields a durable finding →
still handed to the notes skill, the only change being that no path copy
is held. Trigger eval not run: the description is unchanged, and
`argument-hint` appears in the slash menu, not in the listing the model
triggers on. A/B not run: no behavior rewritten.

Smoke runs, `claude -p` from a scratch cwd, Claude Code 2.1.287,
claude-opus-5-5, `--permission-mode dontAsk`, $0.56 in all. Run 1, prose
choice question ("I want to add a rule to my CLAUDE.md ... rule or skill?
Create nothing."): the skill did not load, 0 tool calls, 1 turn, $0.14;
the model answered from its always-loaded rules. One run, so a watch
item, not a trigger finding. Run 2, `/rule-author` with the same question:
body loaded; the skill resolved `../skill-rule-shared/skill-vs-rule.md` to
`~/.claude/skills/skill-rule-shared/skill-vs-rule.md`, the right
path, and the Read was denied by `dontAsk` (reads under `~/.claude` need an
allow rule in that mode), $0.22; the answer said it could not read the
framework. Run 3, same, with
`--allowedTools "Read(//Users/<user>/.claude/skills/skill-rule-shared/**)"`:
the Read succeeded, no errors, 2 turns, $0.17, and the answer applied the
framework (rule over skill; hook for enforcement; "I created nothing").
That confirms the moved value: the body reaches the shared directory by
the relative path.

Other holders of the values that left this body, for their own passes:
the vault path is still in research (SKILL.md:68,
references/search-tactics.md:30) and job-hunting (SKILL.md:37), as the
notes pass listed; the shared directory's absolute path is in
agent-author/references/evaluating-agents.md and the two shared READMEs,
which are records and references, not skill bodies. This changelog's own
header still names the shared directory by absolute path, as a record.

## 2026-10-31 — made portable: neutral body, one reference per harness

Supersedes the "migrated to portable layout" entry above, which left the
body harness-bound. Done by skill-author in session
4b9d2382-e133-42cd-9deb-18f9093fcab0 after Ben's review; kind declared
`metadata: {harness: portable}`. The body now describes rules as the
always-loaded instruction files every harness reads, names mechanisms
generically (file-scoping, lifecycle hooks, tool permission rules, the
harness's own memory), and points at `references/<harness-id>.md` for
the harness in use. New references: claude-code.md (locations, loading,
scoping, imports, comments, the mechanisms, the rule-mode runner and its
approximation, sources), cursor.md, codex.md, copilot.md, antigravity.md
(from documentation read on 2026-10-30 and 2026-10-31, in the shared
ledger), and gemini-cli.md (default name only; marked to confirm).
references/rule-standards.md reworded in five places to the generic
mechanisms. The description now names the files users type across
harnesses.

Portability check, run after the edits:
    SKILL.md:5:  files an agent harness reads every session, such as CLAUDE.md, AGENTS.md,
    SKILL.md:6:  GEMINI.md, .cursor/rules, or .claude/rules, including file-scoped rules —
    SKILL.md:11:  hold in every session; asks to add something to CLAUDE.md, AGENTS.md, or
    SKILL.md:15:  "add a rule", "make it a rule that", "put this in CLAUDE.md", "add to my
Remaining hits are the description's trigger vocabulary (lines 5, 6, 11,
15); no dependence.

5b measured later the same day on Ben's instruction, with Opus agents,
Claude Code 2.1.287, claude-opus-5-5. Trigger eval, 16 queries × 3 runs,
`--model opus`: 14 of 16 pass, 0.79 on should-trigger, 0.00 on
near-misses, $0.50. The two misses invoked no other skill; the model
answered inline: "add to my rules: write all documentation in simplified
technical english" (0 of 3) collides with the STE rule already installed
on this machine, so the model said the rule exists, an eval-set fault;
"should 'always run prettier before committing' be a rule or a skill?"
(1 of 3) is a choice question both author skills claim at the end of
their descriptions, and the model answered it directly. No description
change made; watch item. A/B old-vs-new, old = the last committed
version in git's index (August, named `rule-creator`; today's pre-edit
text was never committed), 2 evals × 3 runs × 2 arms, $3.48 ($1.72 old,
$1.76 new). add-pnpm-rule: both arms wrote an imperative rule with a
last-verified comment 3 of 3; the new arm read `references/claude-code.md`
in 3 of 3 runs and named the budget and contradiction checks in 2 of 3
against 0 of 3 for the old arm; location and scoping named by both.
rule-not-followed: the skill loaded in only 3 of 6 runs (new 2, old 1), a
loading confound of the renamed scratch copies since the real skill
passed that query 3 of 3 in the trigger eval; in the loaded runs the new
arm diagnosed from the harness facts (comments stripped before
injection, `paths:` scoping, exclusion patterns) and named an enforcement
layer, with no file edited. Results in
`evals/portable-2026-10-31/results/`. Desk-checked by reading against
two scenarios: "add a rule that we use pnpm" in Claude Code
(claude-code.md gives the files and the budget set); the same in Cursor
(cursor.md gives `.mdc` files and `globs`, 5b records no runner).

## 2026-10-31 — dependency reduction: rule-author names no skill

Pass from `~/projects/ai/dependency-map/reduction-plan.md` (decision 4:
skill-author depends on rule-author, not the reverse). Research exempt.
Removed every `skill-author` name: the description ends "Not for an
on-demand skill (a SKILL.md directory), for behavior at a fixed lifecycle
point (a hook), or for 'remember X' (the harness's own memory)"; the
shared-directory sentence no longer says who else shares it; the
out-of-scope bullet says "that is a skill, not a rule; say so and stop";
"update all the skills and rules" does the rules half and says the skills
half is not this skill's work; step 3 says so and stops; step 7 says "the
next pass over the shared files". Step 2.5 names "whatever notes skill the
user has". Portability check: four hits, all description trigger
vocabulary (CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules, .claude/rules).
Trigger eval: due (description changed); see skill-author's combined
entry. Load not re-run: the body change is wording only.

## 2026-10-31 — rules pass: ste100 names no skill

Same reduction pass. `~/.claude/rules/ste100.md` line 12: "Casual
conversation, code, code comments, and notes follow their own
conventions, not this rule" (was "Notes written with the notes skill
follow that skill's own STE reference instead"). The notes skill's
`references/style-ste.md` already says its file wins inside a note, so
the rule needs no pointer. No A/B: a scope sentence, not guidance. No
other rule changed; `~/projects/CLAUDE.md` and `etc/CLAUDE.md` keep
`/project-author` (decision 8).

## 2026-10-31 — measured (dependency reduction trigger eval)

Trigger eval after the dependency reduction, `evals/trigger-result-2026-10-31-reduction.json`: 14/16 pass, recall 0.71, near-miss rate 0.00, 3 runs per query, $0.50, Claude Code 2.1.287, claude-opus-5-5, builtin plugins only.
Failed: "add to my rules: write all documentation in simplified technical engli" (should, rate 0.00); "should 'always run prettier before committing' be a rule or a skill?" (should, rate 0.00).
Passed below 1.00: "why isn't my rule about no em dashes being followed? it's ri" (0.67).
Near-misses that loaded another skill through that skill's own description: agent-author, doc-author, skill-author.
Baseline on the same set at 19:31 today: 14/16, recall 0.79, the same two queries failing (0.00 and 0.33). The change moved one of them from 1 of 3 runs to 0 of 3, inside n=3 noise; the failures pre-date this pass.

## 2026-10-31 — ledger layout and move

Same pass as skill-author's entry of this date. Step 2.1 reads "the
ledger entries that concern the pass" — the shared `sources.md`, which
holds rule provenance because a rules directory cannot hold a ledger;
step 2.5 and step 7 name "the ledger that holds each source".
`compatibility` added. This skill now lives in the meta-skills
repository and is symlinked into `~/.claude/skills`. Two `/Users/ben`
paths in this changelog became `~` and `<user>`.
