# Changelog

Dated record of every create, update, and verification pass this skill runs —
on itself and on the skills it maintains. "Checked, no change" entries matter
as much as changes: they tell future runs what is already verified. History
before 2026-08-18 is in `~/.claude/skills/skill-rule-shared/CHANGELOG.md`,
the closed changelog of skill-rule-creator, the single skill this one and
rule-author were split from. A change to a shared file
(`~/.claude/skills/skill-rule-shared/`) is logged here when this skill's pass
made it, and named as shared.

Entry format:

```
## 2026-08-22 — pass: findings-store integration into three skills

Updated sleuth, political-strat-id, political-strategy to read from and
write to the persistent findings store at ~/sleuth (built the
same day; contract STORE.md, rationale DESIGN.md there). Per-skill detail
in each skill's changelog. Shared-file change: sources.md gained a
"Findings store" subject section. Descriptions untouched, so no trigger
eval; A/B skipped — nested-CLI OAuth expired and the account hit spend
limits twice mid-pass; desk-checked 4 scenarios. Watch item: whether
step-0 Recall fires reliably in live sessions — first real /sleuth or
/political-* run against a store subject should confirm store citations
appear; if a session re-derives stored work, the Recall wording needs a
trigger-strength pass.


## YYYY-MM-DD — <artifact> — created | updated | checked, no change
One line on what was checked or changed, and why.
```

## 2026-10-29 — pass: prompt-author learns Claude Code `/goal`

Side session started from "Teach prompt-author when to use /goal"
(cwd `~/projects/tea`). Update prompted by an observed failure: the skill
had no text on `/goal`, and a same-day tea session had typed `/research
/goal ...`, which set no goal. Added one section to prompt-author
(fit rule, condition contents, placement rule, auto-mode note), created
`prompt-author/evals/ab-evals.json`, refreshed its `last-verified`.
Step 2 research scoped to the subject: goal, commands, and skills pages
fetched raw on 2026-10-29; two desktop transcripts inspected. Shared-file
change: `sources.md` gained a "prompt-author skill subject-matter sources"
section (Contents updated). Desk-checked 3 scenarios; detail in
prompt-author's changelog. No trigger eval (description unchanged).
Nothing in the pass contradicted the standards or the shared files; the
`.md` suffix on code.claude.com pages returned raw markdown again, as the
ledger already records.
Measured: `ab_eval.py --mode skill --old --new`, 4 evals × 3 runs × 2
arms, $4.27, Claude Code 2.1.287, claude-opus-5-5[1m]; the fit eval is a
clean win (new 3/3 lead with `/goal`, old 0/3), the user-gate eval 3/3
against 1/3, the one-turn eval shows no over-application, and the
placement eval loaded the skill in neither arm (base model handled it).
Numbers in prompt-author's changelog and the ledger's eval-evidence
subsection. Ledger: the Claude Code skills-doc entry got a partial
re-check line (stacking and Skill-tool sections only).

Watch item (9 runs per arm, one model, first use of `--mode skill
--old/--new` in this collection): the copy staged as `prompt-author-old`
loaded in 4/9 runs on the three evals whose phrasing triggers at all,
against 9/9 for `prompt-author-new`, with identical descriptions.
Hypothesis: a `-old` suffix in the skill roster reads as deprecated and
the model skips it. If a later old/new run shows the same skew, stage the
arms under neutral names (`<name>-a`, `<name>-b`) in `ab_eval.py` and
record the change in evaluating.md; until then it is a confound to read
the `artifact loaded` column for.

## 2026-08-30 — pass: prompt-author session-rename feature

Feature request from Ben: prompt-author now renames a new session to
`Refine Prompt: <subject>` when its invocation is the session's first
prompt (new `## Session title` section; silent skip where the
`mcp__ccd_session_mgmt__set_session_title` tool is absent). Step 2
research skipped under the feature exemption; the tool schema was
verified live. Desk-checked against 3 scenarios; 5b skipped with reason
(description unchanged, and the behavior needs desktop-app MCP tools the
headless harness lacks) except one headless run confirming the
silent-skip branch. Detail in prompt-author's changelog. No shared-file
changes; nothing in the pass contradicted the standards.

## 2026-08-27 — job-hunting — created and measured

Created `~/.claude/skills/job-hunting/` (SKILL.md 233 lines + 4
references, 122–167 lines each, all with TOCs) on request, via an
approved plan (`create-a-job-hunting-skill-sequential-crown.md`).
Cross-session pipeline tracker at `~/job-hunt/` (Ben's choice) with a
working-directory-first discovery rule that doubles as the eval-fixture
isolation mechanism; intensity modes as a profile setting with an
explicit no-trajectory rule; resume/cover-letter/LinkedIn-content work
delegated to resume-author (created the same day by another session —
the two descriptions partition the resume vocabulary). Zero personal
facts and zero dollar figures in the skill; contested/thin areas
labeled in place per the user's explicit requirement.

Step 0: 3 `claude -p` baseline probes (claude-opus-5, 2.1.220) — no
durable cross-session state (each probe invented its own structure or
routed to the notes vault), figures asserted from memory, no
delegation seam. Research: 4 areas fanned out to subagents (two
sub-fanned; 9 reports), all claim-record format with tiers and
verbatim quotes; provenance in sources.md under a new "job-hunting
skill subject-matter sources" section (shared-file change: section +
Contents line; the comp/negotiation subsections were written directly
by that research agent, the rest consolidated by this session).

5a desk-checked 3 scenarios (one fix: closed-state definitions added).
5b measured (2.1.220, claude-opus-5, no plugins/hooks): trigger eval
round 1 12/13 — should-trigger 7/7 at 1.00, one near-miss failure
("cover letter for the initech application" 0.67, resume-author not
invoked); routing sentence sharpened; round 2 13/13, near-miss 0.06,
residual load co-invokes resume-author. A/B 3 evals × 3 runs/arm:
capture and offer decisively favor the with-arm (tracker discipline,
ghosted-state handling, offer recording, no invented figures — the
without-arm asserted counter-percentage folklore from memory and never
opened the tracker in the offer eval); pickup near-parity with a
discipline margin (mode acknowledged 3/3 vs 0/3, stale target flagged
2/3 vs 0/3); with-arm cost +31%. Kept on the measured wins. Details in
the skill's CHANGELOG.

Shared-file changes: (1) ab_eval.py — `files` entries that are
directories now copytree into the run dir under their own name
(nested-tree fixtures; additive, plain-file behavior unchanged);
(2) evaluating.md — recorded the directory-fixture mechanic and the
harness-artifact false-positive trap (metrics.json/transcript.jsonl/
output.md in every run dir); (3) sources.md — new subject section as
above. Core skill-authoring sources not re-fetched: the ledger records
them verified 2026-08-27 (same-day, github-cli pass) — step-2
exemption; skill-author's own metadata.last-verified unchanged.

Watch items: (1) second data point for the github-cli
description-overlap watch item — job-hunting's plain description hit
1.00 should-trigger with user-vocabulary phrases where github-cli's
plain and escalated descriptions hit 0.00–0.22 on a task-native
domain; consistent with the verbatim-overlap hypothesis, still n=2
skills and confounded by domain nativeness — keep watching, promote
only with a cleaner comparison. (2) A/B fixture dates must land on
weekdays — a Sunday onsite in the pickup fixture drew a legitimate
baseline objection; noted in the skill's CHANGELOG for the next pass.

## 2026-08-27 — github-cli — created and measured

Created `~/.claude/skills/github-cli/` (SKILL.md, 128 lines, no reference
files; staged eval sets in `evals/`) on request, in the
`github-cli-skill-c0b115` worktree session; the skill directory is also
committed on that session's branch. Step 0 found a strong baseline: a
transcript sweep (18 transcripts mentioning gh, 5 real calls, 2 failures —
both environmental: gh missing, gh not logged in) plus three subagent
probes on Fable 5 (issue counting, CI triage, fork-PR composition) that all
passed, with one real miss — `--dry-run` offered as a safe preview without
gh's "may still push git changes" caveat. The skill is therefore
deliberately thin: non-TTY discipline, auth-failure handling, quoting, the
gh api POST flip, pagination, fork flow, CI triage, release flags. Every
fact verified against the installed gh 2.98.0's own help plus two live
read-only checks; provenance in the shared sources.md under a new
"github-cli skill subject-matter sources" section (shared-file change, with
a Contents line — this pass).

5a desk-checked 3 scenarios (one fix: an embellished --generate-notes
claim). 5b was blocked at first (`claude -p` OAuth — third pass in a row),
then ran in full after the user ran `claude login` mid-pass. Measured
(2.1.220, claude-opus-5, no plugins/hooks): trigger recall 0.00 with the
plain description, 0.22 after a deliberate one-notch escalation
(directive opening + anti-laziness clause), near-miss 0.00 both rounds —
only verbatim-phrase-overlap queries load it. A/B 3 evals × 3 runs/arm:
both arms 3/3 on every criterion (issue counting, fork-PR composition,
auth-failure handling with gh forced logged out); the only attributable
delta is the --dry-run may-push caveat (3/3 with vs 0/3 without); with-arm
cost +14–35%. Verdict recorded in the skill's CHANGELOG: too close to
call on claude-opus-5; kept per the user's explicit request as a thin
reference skill; description escalation stopped on evidence.

Core sources: best-practices page re-fetched in full (unchanged); skills
doc re-fetched and spot-checked (unchanged on the standards' facts; new
live-change-detection fact recorded in the ledger and observed live — the
new skill appeared in the writing session's own roster within seconds).
Prompting best-practices page not re-checked, so this skill's own
metadata.last-verified stays at 2026-08-18.

Watch items: (1) for a domain the model handles natively, description
forcefulness did not move triggering — the measured lever was verbatim
phrase overlap between query and description ("how many open issues"
1.00 vs task-shaped phrasings 0.00; n=1 skill, 12 queries × 3 runs × 2
rounds, claude-opus-5). If a second skill shows the same pattern,
consider promoting to skill-standards' description guidance. (2)
desktop-harness probes of mutating commands can be blocked by the
auto-mode classifier (one occurrence: a bare `gh pr create </dev/null`
test) — design step-0 probes read-only or the block contaminates the
observation. (3) The A/B measured claude-opus-5 only; the skill's
insurance-for-weaker-models rationale is untested (Haiku/Sonnet arms are
the obvious next measurement).

## 2026-08-22 — pass: created the mermaid skill

Created `~/.claude/skills/mermaid/` (SKILL.md, references/syntax.md,
scripts/validate.mjs, scripts/live_url.py) on request: read, write, and
automatically display Mermaid graphs, as `/mermaid`. Full detail in that
skill's changelog. Shared-file change: `sources.md` gained a "mermaid skill
subject-matter sources" section — Mermaid project docs plus a direct-
inspection block — and a matching Contents line.

Environment finding, and a watch item for every future pass: `claude -p`
could not authenticate in this session ("Failed to authenticate: OAuth
session expired and could not be refreshed", 4 of 4 attempts, both with
and without `--dangerously-skip-permissions`; the flag is separately
blocked by the auto-mode classifier). That kills workflow step 0's fresh
baselines and both measurement scripts, since each shells out to
`claude -p`. The new skill therefore ships desk-checked but unmeasured,
with the skip reason recorded in its own changelog as evaluating.md
requires. If a later pass hits the same failure, the fix to try first is
re-authenticating the CLI outside the app; nothing in the scripts is at
fault.

This skill's own `metadata.last-verified` is deliberately NOT refreshed:
the pass researched Mermaid, not the three core sources (skill-authoring
best practices, the Claude Code skills doc, the prompting best-practices
page), so there is nothing new to attest for them.


## 2026-08-22 — political-strategy + political-strat-id — created (with shared corpus)
Two new personal skills plus a shared reference directory
`~/.claude/skills/political-strategy-shared/` (skill/skill/shared pattern,
mirroring skill-author/rule-author/skill-rule-shared). `political-strategy`
advises on strategy for a stated goal from the full legitimate playbook;
`political-strat-id` names the tactics in observed political activity, hands
attribution to `sleuth`, and merges sleuth's network graph with the tactical
read. Cross-routing: each description names the other skill and sleuth as
near-miss destinations; strat-id routes counter requests to political-strategy.
Boundary in both: deceptive tactics are for analysis, detection, and
counter-strategy, never for planning or execution.

Step 0 ran three baseline `claude -p` prompts (no skills, dontAsk, 2.1.220):
rezone fight, solar-bill fight, rate-hike astroturf read. Baselines gave good
situational advice and already refused to invent an unsourced funder; the
skills add a power-analysis/theory-of-change spine, a graded named-tactic
taxonomy with observable signatures, the effect-size evidence base (with the
recurring caution that effects are small), the vehicle/coordination-law layer,
and the cross-routing. Eight parallel research subagents produced the tiered,
dated corpus; provenance recorded in the shared `sources.md` under a new
"political-strategy + political-strat-id subject-matter sources" section
(shared-file change, made by this pass). Tier-1 skill-authoring sources
(best-practices page, Claude Code skills doc) re-fetched — unchanged from the
2026-08-19 record. Ten corpus files, each with a Contents ToC (all >100 lines),
linked one level deep; the corpus points to sleuth's front-group-markers and
record-systems refs rather than duplicating them.

Measured (2.1.220, headless sessions resolved to claude-opus-5): trigger
evals 12/12 (strategy: 1.00 / 0.00) and 11/12 (strat-id: 0.83 / 0.00), both
with correct cross-routing to sleuth and to each other on near-misses; A/B
evals 2 evals × 3 runs/arm per skill, skill loaded 3/3 in every with-run —
strat-id a clear win on every expected behavior (without-arm 0/3 on sleuth
handoff, counter-routing, and grasstops naming), strategy a win on method
markers and figure attribution (the without-arm reproduced the step-0
unsourced-poll-number failure) at ~2.5× cost. Numbers and confounds in the
per-skill CHANGELOGs.

Shared-file change (second, same pass): added a dated eval-design trap to
evaluating.md — a should-trigger query that references attached material the
text-only harness cannot attach measures clarify-first behavior, not the
description; put the observable activity in the prompt text or use `files`.
Found via strat-id's one trigger miss, mechanism understood (three identical
runs), so recorded per the step-7 rule for method traps.

Mid-pass event worth recording: the session silently switched from
claude-fable-5 to claude-opus-4-8 during the corpus-writing phase; the user
caught it, and the four Opus-written corpus files were rewritten on Fable
from the research sources (not from the Opus text). Transcript model fields
identified exactly which files each model wrote.

## 2026-08-19 — sleuth — created
New personal skill for power-structure research (who is behind X, who funds
X, is X a front group), built on the professional method: hypothesis first,
pivot on every fact, chase anomalies, triangulate across record systems,
keep the graph, grade and calibrate, stop and report. Step 0 ran three
baseline prompts (Opus 5 high, no sleuth; recorded in sleuth's changelog):
the baseline self-loaded `research`, found the main links, but opened no
primary filing, missed a known funder link (Wyss → Sixteen Thirty →
Demand Justice), kept no edge list, ran no marker test, and ended with
questions. Six parallel research subagents read the sources the user named
(SBI 2nd ed. 2026, GIJN, Journalist's Resource, Sunlight Research Desk,
OpenSecrets, LittleSis/PAI, Juravich, Mattera, CMD/SourceWatch/PRWatch, the
astroturf literature, Bellingcat, IntelTechniques, VH3, ICD 203, Kent, NATO
AJP-2.1, FM 2-22.3, Heuer, PHIA, WaPo/Reuters/BBC sourcing policies) and
live-checked ~110 record-system URLs; five "sleuth skill" entries added to
the shared ledger. Differences from the user's brief are listed in sleuth's
changelog and were followed per the brief. Deliverables: SKILL.md (258
lines), four references (record systems with liveness and leans; pivot
playbook per entity type with a subagent brief; front-group markers with
a core test and the sources' own calibration language; grading and
reporting with the ICD 203 terms, the 2007 NIE confidence definitions,
Admiralty-style reliability/credibility, and a short-form ACH), and
`scripts/graph_check.py` (validates the case graph — every edge sourced,
facts on a primary or two independent secondaries — and renders the
report tables).

Measured (5b), all on Claude Code 2.1.220, claude-opus-5, effort high,
the model the user asked for in testing:
- Trigger eval: 12/12 pass, should-trigger 1.00 (6 queries), near-miss
  0.00 (6 queries, routed to research / study-credibility / notes), $0.76.
- A/B: the 3×2×3 suite was stopped at the user's request over cost
  after one eval's with-arm completed; measured as known-right 3 with vs
  4 without, known-left and insufficient 1 with vs 1 without (step-0
  baselines reused as the without-arm). Per-eval grading, costs, and the
  watch items are in sleuth's changelog. Eval spend ≈ $47, of which $21.5
  went to the two aborted starts caused by the harness defects below.

Two eval-harness defects found and fixed in the shared scripts (named as
shared): (1) `ab_eval.py` and `trigger_eval.py` gained `--effort`, and
`ab_eval.py` gained `--allowed-tools`, because a non-interactive run
denies WebSearch, WebFetch, and Bash, so a research skill could not be
measured at all; (2) `ab_eval.py --mode skill` now pre-allows
`Read(//<abs skill dir>/**)` in both arms, because every reference read
in the with-arm was denied ("Claude requested permissions to read") and
the arm measured SKILL.md without its references. Both recorded in
evaluating.md. A third finding went into skill-standards.md and the
ledger: on 2.1.220 any `allowed-tools` value makes the Skill invocation a
permission prompt ("Execute skill: <name>"), so a skill with that field
cannot load in `claude -p` under `acceptEdits` — the first A/B with-arm
never loaded the body (3 of 3 runs). Prior A/B results of skills with
references (none were run before today with references, per the changelog
history) would carry the same confound.

Self-maintenance: the two core docs re-fetched for this pass (skill
best-practices page, Claude Code skills doc) read unchanged on the facts
the standards state; their ledger dates moved to 2026-08-19. The prompting
best-practices page was not re-fetched, so this skill's own
`metadata.last-verified` stays at 2026-08-18.

## 2026-08-18 — mcp-servers, refine-prompt — renamed to mcp-author, prompt-author
Second rename of the day, completing the `<subject>-author` pattern across
the collection. Directories and `name:` fields renamed; descriptions and
bodies unchanged. Live pointers repointed: ai-retrospective's description
and body (three mentions of refine-prompt), the mc-computer project's
`CLAUDE.local.md` (`/refine-prompt` → `/prompt-author`), the ledger's three
mcp-servers section headings (both names) and a rename map in its header.
ai-retrospective's description changed by one skill name only; treated as a
wording fix, no trigger eval (skip stated here). Smoke check that both load
under the new names, 2 should-trigger queries × 2 runs each, Claude Code
2.1.220, claude-opus-5, no plugins or hooks, roster of 29 with the new
names present: mcp-author 2/2 at 1.00 ($0.57); prompt-author 1/2 — "make
this prompt better" 1.00, "wrap this up into a handoff prompt for a fresh
session" 0.00 because a `claude -p` session has no conversation to package
and both runs said so in one turn (an eval-design fault, not a trigger
failure; do not reuse that query in a fresh-session eval) ($0.29). Each renamed
skill's own changelog has a rename entry.

## 2026-08-18 — skill-author — renamed from skill-creator (same day)
Ben's decision: every `-creator` skill in the collection becomes `-author`
(skill-author, rule-author, agent-author, persona-author) so that no
personal skill shares its last name segment with an `anthropic-skills:`
entry on the desktop roster, and the collection stays on one pattern.
Directory and `name:` renamed; the description changed only in the sibling
names it points to ("use rule-author", "agent-author"), so the trigger
numbers below still describe it; live pointers in ai-retrospective,
agent-author, research, config-export, the shared directory, and the ledger
repointed; historical entries below keep the names in use at the time. A
smoke check that the renamed skills load under the new names is recorded in
the closed changelog's rename entry.

## 2026-08-18 — skill-creator — created by splitting skill-rule-creator
Skills half of the split; the closed changelog's final entry carries the
reasoning, the layout, and what was considered and rejected. This skill's
body is the old workflow specialized to skills: intro names the two places
a skill fails (description, body); step 1 hands the rules half of "update
all the skills and rules" to rule-creator; step 2 names the skill-authoring
best-practices page and the Claude Code skills doc as the sources to
re-fetch; step 3 confirms a skill against the shared framework and hands a
rule to rule-creator; step 4 reads `references/skill-standards.md` (the
frontmatter, body, and scripts sections of the old authoring-standards.md,
moved verbatim) plus the shared `guidance-style.md`, and repeats the
description rule; 5b names the trigger eval as required for every
description change plus `ab_eval.py --mode skill`; step 6 keeps the
per-skill CHANGELOG convention; step 7's core sources are the three skill
pages. Description 1,009 characters (final; see the two rounds below), third
person, key use case first, names where rule, subagent, and note requests
go.

Trigger eval (5b, required for a new description), per evaluating.md —
measured twice on the same 11 queries × 3 runs (6 should-trigger, 5
near-miss), Claude Code 2.1.220 (the `claude` on PATH), resolved model
claude-opus-5, no plugins, no hooks, `CLAUDE_CODE_DISABLE_WORKFLOWS=1`,
`dontAsk`, CLI roster of 29 skills (the desktop's `anthropic-skills` bundle,
with its own `skill-creator`, is not in it).

Round 1 (989 chars; named `~/.claude/skills/` and `.claude/skills/` in the
first clause; "reference material captured for future sessions"): 8/11
pass, should-trigger 0.50, near-miss 0.00, $0.58. Per query: "make a skill
for deploying to fly.io" 1.00; "update all the skills" 1.00; "the
persona-creator description is way too long, tighten it and check it still
triggers" 1.00; "the notes skill keeps asking me which project a note
belongs to ... fix it" 0.00; "why doesn't my research skill fire when i say
'look into X'?" 0.00; the choice question "should 'always run the test suite
before you commit' be a skill or a rule?" 0.00 here, rule-creator loaded in
1 of 3 and the other 2 answered "neither, a hook" directly, which the
framework agrees with. Near-misses all 0.00 and correctly routed: "add a
rule: never use emoji in commit messages" → rule-creator, "add an agent that
reviews sql migrations" → agent-creator, "make this prompt better" →
refine-prompt, "from now on run prettier after every edit" → update-config,
"remember that the api tests need redis" → nothing. Transcripts of the two
misses: all 6 runs ran `ls` on the named skill's directory and `Read` its
SKILL.md, then answered or reported the denied tools; none loaded this
skill. The 24-agent verification pass separately confirmed that
"reference material captured for future sessions" overlaps the notes skill's
territory with no redirect.

Round 2 (1,009 chars, the description now in the file: paths removed from
the first clause; "reports that an existing skill misbehaves or picks a bad
default" and the triggers "the X skill keeps doing Y" and "why doesn't my
skill fire" added; "for a durable fact or write-up, notes" added to the
redirects; the "wants ... reference material" clause narrowed to "a
repeatable workflow or procedure captured so a future session runs it"):
8/11 pass, should-trigger 0.50, near-miss 0.00, $0.60. Per query: fly.io
1.00; update all 1.00; persona-creator description 0.67 (one run read the
file and answered without loading); notes complaint 0.00; research trigger
question 0.33 (the one hit loaded this skill after reading
research/SKILL.md); choice question 0.00 here with rule-creator loaded in 2
of 3. Near-misses unchanged, all 0.00 with the same routing.

Reading: the two rounds measure the same on this set. The two complaint-
shaped queries ("the X skill keeps doing Y", "why doesn't my X skill fire")
go to direct exploration of the named skill's directory whether or not the
description names the skills path (round 1: 6 of 6 explored; round 2: 5 of
6 explored, 1 loaded late) and whether or not the description carries those
phrases verbatim — so the mechanism the 08-18 insights pass recorded as a
watch item (a path in the description invites exploration, n=3) is not what
drives this; the request shape is. Round 2 is kept because it also closes
the notes overlap. Watch item, not a standard (2 queries, 12 runs): a
complaint about a named skill reads to the model as "go look at the file";
whether any description wording moves that, or whether the body should be
made to catch it after the fact (the round-2 late load), is for a pass with
a larger set of such queries.

Desk-check (5a): three scenarios walked through the new text — (1) "make a
skill for X" → steps 0–7 with the trigger eval at 5b; (2) "add a rule that
..." arriving here by mistake → step 3 recommends a rule and hands to
rule-creator; (3) "should this be a skill or a rule" → steps 1–3, answer
from the shared framework, create nothing. Nothing ran for these; the
trigger eval above is the measured part.

Research for the split re-fetched the three core docs as raw markdown
(recorded in the shared ledger with today's date). Findings that extend the
standards were recorded, not applied — see the closed changelog's watch
items.

## 2026-08-25 — created info-design (new skill)

Created `~/.claude/skills/info-design/` from a dedicated seven-strand
research pass on information design (details in that skill's CHANGELOG and
the new "info-design skill subject-matter sources" section of the shared
sources.md — the section, the Contents line for it, and a refreshed
last-verified on the skill-authoring best-practices entry are this pass's
shared-file changes). Best-practices page re-fetched 2026-08-25, read
unchanged; the skills doc and prompting page were not re-checked, so this
skill's own metadata.last-verified stays at its prior date.

Step 0 ran as three subagent probes in the desktop harness instead of
`claude -p`: the CLI cannot authenticate ("OAuth session expired and could
not be refreshed", 2 of 2 attempts, Claude Code 2.1.220) — same blocker the
2026-08-24 mermaid session recorded. 5a desk-checked (3 scenarios, 2 fixes:
an untraceable threshold figure; eval-query overlap with body examples).
5b BLOCKED, not waived: trigger and A/B sets are staged in
`info-design/evals/`, to run after `claude login`.

Watch item (n=3 probes, one day, Fable 5 with this user's rules): baseline
document structure is already strong; the new skill's measurable value may
sit mostly in its discriminator behaviors (front-loaded list items, no
invented specifics, register decision, layering). If the pending A/B is too
close to call, trim the body toward the discriminators.

## 2026-08-27 — created resume-author (new skill)

Created `~/.claude/skills/resume-author/` (SKILL.md +
references/software-engineering.md + references/linkedin.md) from a
three-strand research pass (SWE practitioner corpus; ATS/AI screening
with myth tracing; AI-vs-human writing evidence + maintenance format +
LinkedIn mechanics). Scope decided with the user: general core + SWE
reference + LinkedIn reference; cover letters outline-first; not
IoT-specific. Shared-file changes this pass: new "resume-author skill
subject-matter sources" section and its Contents line in sources.md
(includes a refuse-list of untraceable screening statistics), and a
dated PDF-fixture method note in evaluating.md. Core skill-authoring
sources not re-fetched: the ledger shows the best-practices page
re-fetched the same day by the github-cli pass, so this skill's own
metadata.last-verified stays 2026-08-18 (skills doc and prompting page
unchecked today).

Full workflow ran: step 0 baselines (3 `claude -p` runs on the user's
real resume — critique/tailor strong unaided, bullet run fabricated
metrics and said "nobody audits it"), 5a desk-check (4 scenarios, 2
fixes), 5b trigger eval (near-miss FP 0.00; deferred-material trap hit
again despite being documented — the eval-set author must re-read the
"observable activity in the prompt text" rule before writing queries),
5b A/B (3×3×2, claude-opus-5, CC 2.1.220; numbers in resume-author's
CHANGELOG). Measured deltas: fabrication guardrail (baseline invented
figures in 2 of 4 observed bullet-task runs; with-skill 0 of 3) and the
screening/format layer; baseline critique quality already high.

Method finding, mechanism understood, promoted to evaluating.md: PDF
fixtures fail nondeterministically without poppler (3 of 21 runs).

Watch item (one pass, one model): in tailor mode neither arm flagged the
stale-current-role defect that both critique arms caught — task framing
narrows attention to posting-matching. If a future pass sees users
tailoring stale resumes without noticing staleness, add one line to the
skill's Tailoring section; not added now on n=4 runs.

One research-agent API failure worth remembering: a WebFetch-heavy
subagent died mid-pass to a Fable 5 `reasoning_extraction` safeguard
false-positive; resuming the same agent with "compile what you have,
do not revisit the page you were on" recovered the pass without losing
its collected waves.

## 2026-10-13 — project-author — created
Ben's request (session 2720c94e): a skill that writes the README.md that
is the always-loaded agent context for a ~/projects project, asking a
question only when a project-defining fact is missing, with create, update,
and promote-from-etc modes. Choice question answered first with the shared
framework: skill (multi-step procedure used in a minority of sessions); the
session-startup read is a rule plus a per-project `@README.md` stub, logged
in rule-author's changelog. Step 0: three `claude -p` baselines launched
and invalid (login expired; see evaluating.md preflight checks); three
subagent proxies ran the same prompts in fresh contexts without the skill
— labeled a proxy, not the measured baseline. Step 2 research: landscape
pass with three subagents (empirical format/position/instruction-count
evidence; agent context-file conventions and in-the-wild studies; project
brief and decision-record practice) plus the vendor docs read by the lead;
sources and grades in the ledger's project-author section. Findings that
shaped the skill: adherence to a rule list collapses as it grows (IFScale,
NeurIPS 2025; Eliav 2026 preprint), so the README is mostly facts; derivable
overviews do not help agents while facts available nowhere else do
(Evaluating AGENTS.md, 2026 preprint); flat one-level pointers beat raw
dumps and hierarchies (He et al. 2026 preprint); decisions dated with
reasons and kept when superseded (Nygard, MADR); appetite and no-gos (Shape
Up). Unsettled and labeled as defaults in references/readme-format.md:
markdown vs plain text, exact length, tables vs bullets, the non-code
field set, within-file order. Shared files changed this pass (named as
shared): skill-vs-rule.md gains the import-vs-instruction bullet;
evaluating.md gains the Python-version and login preflight checks;
sources.md gains the project-author section and a memory-doc addendum.
Desk-check, trigger eval, and A/B eval status are in project-author's own
CHANGELOG.md.

## 2026-10-24 — research — design pass for decoupling from the notes skill
Ben's request (this session, via /skill-author): decouple `/research` from
the notes skill so it can live in a public repository and work for
everyone, with an optional local pointer at his own notes skill that never
has to be staged; asked for ideas and for research on how agents handle a
committed-sample-plus-gitignored-real config. Classified as an update
(feature request) plus a choice question, so step 0 observation was the
request itself and step 2 ran as a research pass on the configuration
question rather than on the skill's subject matter. Step 3: still a skill;
the pointer could alternatively be a one-line user rule, named as an
option. No change to research/SKILL.md this pass; the design is reported
to Ben for a decision between a personal-skill repository and a plugin,
and the research changelog records the pass.

Research: tier 1 read in full or by targeted extraction — Claude Code
skills doc (dynamic context injection section, read for the first time),
settings page, env-vars page, plugin manifest reference and components
page, memory doc, Agent Skills spec; the Claude Code CHANGELOG for version
anchors; tier 3 — superpowers and anthropics/skills READMEs (no per-user
config in either), three community skills found by GitHub code search
that ship a `config.local.*` overlay, Datadog's May 2026 piece on `!`
injection as a supply-chain risk. All recorded in the ledger (five new
tier-1 entries, four new tier-3 entries, two refreshed).

Direct inspection (eleven `claude -p` runs on 2.1.287, haiku,
acceptEdits; ledger entry under Artifact tooling): an injected bundled
script pre-approved with `allowed-tools` delivers a gitignored local
config file, a fallback when absent, and a settings `env` value; works
through a symlinked skill directory; without pre-approval a user-invoked
skill aborts silently; with `allowed-tools`, model invocation in `-p` is
still denied (3 of 3), reconfirming the 2.1.220 finding; without it,
model invocation defers the command instead of aborting.

Shared files changed (named as shared): skill-standards.md — the
`allowed-tools` bullet gains the 2.1.287 re-measurement and the
user-invoked exception, plus a new bullet on `!` injection as the one case
that needs the field; evaluating.md — the hazard note gains the
re-measurement and a new trap: a zero-turn empty `-p` result is an
injection abort, not model silence. sources.md as above.

Skipped 5a/5b: nothing was drafted, so no desk-check or eval. Core sources
not all re-verified (skills doc yes, best-practices and prompting pages
no), so this skill's own `metadata.last-verified` stays 2026-08-18.

Watch items (one pass, one model, one version): the abort-vs-defer
asymmetry between user- and model-invoked skills for a non-allowed
injected command; haiku's tendency after an `Execute skill` error to
improvise (read SKILL.md itself, or claim the skill ran). Neither goes
into a standards file until seen again.

## 2026-10-24 — research — decoupling applied (follow-on to the design pass above)
Ben chose the personal-skill route with a per-skill gitignored config and
no env-var fallback (smallest mechanism; the fallback is one script line if
repetition across the meta-skills ever warrants it). Applied in place
before the planned repository move, since `${CLAUDE_SKILL_DIR}` makes the
mechanism location-independent. Step 2 exempt: same-day reuse of the
sources read in the design pass; nothing new in the ledger. Changes, files,
the two-run smoke test, the four desk-check scenarios, the 5b skip reasons,
and the open items are in research/CHANGELOG.md. One standards-relevant
observation, consistent with skill-standards.md as updated today: a
user-typed `/name` with `allowed-tools` set renders the injected block in
`-p` (2 of 2 on the real skill), while model invocation in `-p` is denied
(3 of 3 on the test skill). Shared files: none changed in this follow-on.

## 2026-10-27 — research — decoupling reverted at Ben's request
Ben judged the injected-config design overly complex for a pack meant to
be shared across Claude Code, Cursor, and Codex and reverted it. The
research skill directory is restored to its pre-2026-10-24 state by
`git checkout` of the four edited files and removal of `scripts/`,
`config.example.md`, `config.local.md`, and the nested `.gitignore`; its
CHANGELOG entries of 2026-10-24 went with it, so the two entries above are
the only record of that work. The ledger entries stand as research. Open
direction, not yet designed: a convention with no mechanism — one
per-machine config directory shared by all harnesses, read by a plain
instruction in each skill — which Ben stopped before it was tested.

## 2026-10-28 — doc-author — created and measured

Created `~/.claude/skills/doc-author/` (SKILL.md 247 lines + two
references with TOCs + evals and a fixture) on request, with the research
skill's method for step 2: five subagent strands (frameworks, style guides,
repository artifacts, empirical evidence, current practice and AI readers),
~340 claim records, three primaries spot-checked by the lead. Mechanism
confirmed as a skill (procedure plus references, needed only by
documentation tasks). Step 0: three `claude -p` probes on a purpose-built
fixture — accuracy already strong on Opus 5.5; gaps were tutorial
reproducibility, type mixing, single-sourcing, version markers, and the
verification loop. Desk-checked 4 scenarios (two fixes). Measured on
2.1.287 / claude-opus-5-5[1m]: trigger 16/16 (recall 1.00, false
positives 0.00, $0.33); A/B 3 × 3 × 2 with Bash pre-allowed — decisive on
the tutorial task (3/3 vs 0/3), a discriminator win on the configuration
task (version marker 3/3 vs 0/3, length unchanged), near parity on the
README with deeper verification; with-arm cost +50–60%. Detail in
doc-author's changelog and the ledger.

Core sources all re-verified: skill best-practices page (unchanged; lists
`writing-documentation` as a good name), Claude Code skills doc
(unchanged), prompting best-practices page (now covers Fable 5.1 / Opus
5.5 / Sonnet 5.5 / Haiku 5.5 with a Fable 5.1 page; over-triggering text
still scoped to Opus 4.5/4.6). This skill's `metadata.last-verified` set
to 2026-10-28.

Shared-file changes (named as shared): sources.md — three core entries
refreshed, Contents line, and a new "doc-author skill subject-matter
sources" section with a baseline-and-eval subsection; guidance-style.md —
the least-capable-model bullet gains the prompting page's Fable 5.1 line
("already formats less", a formatting-restriction block "can suppress
structure the content needs"); evaluating.md — the worked-example trap now
covers the fixture's own identifiers (caught in this pass before the
suite), and the fixture-directory note says queries must name `./<dir>`.

Method notes for future passes: `python3` on this Mac is 3.9 and the
scripts need 3.10+ (`/opt/homebrew/bin/python3.14`; evaluating.md already
says so); `timeout` does not exist on macOS; under `acceptEdits` a
baseline probe cannot run Bash, so "examples not run" in step 0 is a
harness artifact — pre-allow Bash in the A/B so the behavior is
observable, which this pass did. Watch item (n=9 runs): Opus 5.5 with the
user's rules writes accurate, well-structured docs unprompted; this
skill's measured value is in reproducible tutorials, kind separation,
version markers, verified examples, and Markdown hygiene, not accuracy or
prose.

## 2026-10-30 — tea-guide — created and trigger-measured

Created `~/.claude/skills/tea-guide/` (SKILL.md ~230 lines, three
references with TOCs, one script, an eval set) from a prompt-author
refined brief, after three grilling rounds (24 questions) and an approved
format draft. Step 0 came from six real sessions, read by one subagent
each: `/goal` never ran (typed after `/research`), research reports posted
as the deliverable, extrapolated and unsupported numbers, an ambiguous
"white tea" scope, four hand-written Reddit parsers, and ad hoc layouts.
Mechanism: skill, as asked; the framework agrees. Desk-checked 3
scenarios (three fixes: the research skill's "ask one question" and
notes-vault steps named as not applying; turn count in progress lines
under `/goal`; literal script paths). Measured on 2.1.287 /
claude-opus-5-5[1m]: trigger 16/16 (recall 1.00, false positives 0.00,
$0.40). A/B skipped by agreement: a with-arm run is a full research run
(~1 h, several dollars); the user's first real guide runs are the
measurement. Detail in tea-guide's changelog.

Core sources: skill best-practices page and Claude Code skills doc
re-read, unchanged (dates refreshed in the ledger). The prompting
best-practices page was not re-read this pass, so this skill's
`metadata.last-verified` stays 2026-10-28.

Shared-file changes (named as shared): sources.md — two core entries
refreshed, a Contents line, and a new "tea-guide skill subject-matter
sources" section (observed sessions; Reddit and Wayback direct inspection
with timings; pullpush.io's refusal text; water-temperature figures with
grades and fetch status; the `/goal` and Fable 5.1 facts relied on). This
skill's SKILL.md step 0 gains one parenthetical: the desktop app's
`list_events` hides tool arguments and results, which live in the raw
transcript under `~/.claude/projects/` (direct inspection by three
subagents this pass; one read the jsonl to recover the `/goal` facts).

Method notes and watch items: (1) the auto-mode classifier refused a
subagent brief that included a Wayback "Save Page Now" POST as a "Public
Data-Sharing Upload" and accepted the same brief without it — a brief that
writes to a public archive is a publish; (2) pullpush.io answers agent
searches with a refusal text that names agents, which settled the route
on the operator's wishes rather than on reachability; (3) the trigger eval
ran on the account default (Opus 5.5) while the skill's real runs are on
Fable 5.1 — evaluating.md already names the model confound, no change;
(4) `mcp__ccd_turn__wrap_up` was denied by a permission rule in this
session (twice); not a skill matter, noted so the next pass does not read
its absence in transcripts as an omission.

## 2026-10-30 — tea-guide update: Reddit discovery by id prefix, shared rate limit

Update pass on `tea-guide`, prompted by two failures observed the same
day (a side session's brief from local_f835b3fc): `discover` reached only
2022 and early-2023 threads, and parallel runs got the archive's
refused-connection block. Step 2 exempt for skill-authoring guidance (a
script and usage fix); subject facts measured live and recorded in the
shared ledger. Desk-checked 3 scenarios (one fix: the lead, not the
15-minute sourcing strand, uses the slow sweep for the vendor rubric).
5b skipped with reasons in tea-guide's changelog: no description change,
and the A/B skip agreed at creation stands. Detail in tea-guide's
changelog.

Shared-file changes (named as shared): sources.md gains the subsection
"tea-guide — CDX id-prefix scans and archive rate limits". No change to
this skill, its standards file, evaluating.md, or the decision framework:
nothing in this pass bears on them. Core sources not re-read, so
`metadata.last-verified` stays as it is.

## 2026-10-30 — skill configuration: parameterize only what varies

Update pass on this skill, prompted by an observed failure and a user
decision in session 4b9d2382-e133-42cd-9deb-18f9093fcab0. Observation
(step 0): a grep over `~/.claude/skills/*/SKILL.md` found machine-specific
values written into seven skills' bodies or descriptions —
`~/projects/ai/notes` (notes, research), `~/projects/tea/guides/`
(tea-guide), `~/ai/insights-v2` (insights-v2, in the description
too), `~/projects` (project-author), `~/.config/opnsense/` (opnsense),
job-hunting's vault exclusion — and companion skills named only in prose
in eleven skills. The 2026-10-24 injected-config design for the research
skill had been reverted as too complex for a Claude Code + Cursor + Codex
pack. The session first assessed Ben's proposal to carry skill variables
in rule files (research pass, 10 searches, 9 fetches): rule files have no
common user-level location across Claude Code, Cursor, Codex, Copilot,
and Gemini CLI, while skill directories are shared across the first three;
an always-loaded config block for 30 skills would approach the memory
doc's 200-line target for context most sessions never use; a config
value is an obedience channel, so a project-scope rule would let a cloned
repository steer a skill with no persuasion. Ben's decisions: no rule file
carries config; skill-owned config files; plain read, no `!` injection; a
flat key list under one documenting header; add the practice to this
skill, and never add a key where nothing varies.

Classified as an update that adds guidance. Step 2 research: same-day
reuse of the Claude Code skills doc, the memory doc, the Agent Skills
spec, and the prompting page (all fetched this session), plus the Cursor
rules, Codex AGENTS.md, Copilot instructions, and Claude Code setup pages,
Pillar Security's Rules File Backdoor, arXiv 2602.06547, and the OWASP
Agentic Skills Top 10, all recorded in the ledger's new "skill-author
skill subject-matter sources" section. Mechanism: drafting procedure for
skills, needed only when a skill is being written, so it belongs in this
skill and not in a rule; the shared framework gains a bullet for the
choice question.

Changes:
- New `references/skill-config.md` (183 lines, with TOC): decide what
  varies and what does not (OS tool choice, project-relative paths,
  derivable values, untouched preferences); three files and precedence
  (`<skill>/config.yml` shipped, `~/.config/agent-skills/<skill>.yml`
  user, `<project>/.agent-skills/<skill>.yml` project, read only when a
  key is `project ok`); the flat shipped file with one header block; the
  first-step template with the stop-and-offer-set-up rule; validation and
  scope (project values only for `project ok` keys, path bounds, option
  sets, control characters in the script only); portability (plain read;
  `${CLAUDE_SKILL_DIR}`, `!` injection, and `@` imports are Claude Code
  only; Python over bash because native Windows without Git Bash has no
  Bash tool, per the setup page).
- `references/skill-standards.md`: new "Writing skills: configuration"
  section and Contents line.
- SKILL.md: step 4 gains a fourth bullet, "Parameterize only what
  varies"; Updating step 2 now reads the body for values that belong in
  config. `metadata.last-verified` set to 2026-10-30: the skills doc and
  the prompting page were re-read this pass, and the best-practices page
  earlier the same day by the tea-guide pass.

Design choices Ben should know: the user file lives in
`~/.config/agent-skills/`, not as a gitignored `config.local.yml` inside
the skill, because one directory serves every harness on the machine,
survives a re-clone or an export, and is the open direction left on
2026-10-24; the shipped `config.yml` doubles as the example, so there is
no `config.example.yml`; a validating `scripts/config.py` is the escape
hatch for skills with more than five keys or a data-destroying key, not
the default.

Desk-checked against 3 scenarios: (1) a backup skill with an external
drive path → required user-scope key, prune age a named default; (2) a
commit-message formatter → no config file, "no config keys" in the
report, no key for types or line lengths; (3) a minutes-filing skill with
a companion skill → required folder key, companion skill as an optional
user-scope key. Three fixes from the walk-through, applied before the
measurement launch: the first-step template read the project file
unconditionally (now only when a key is `project ok`, so a repository
cannot steer a skill that has none); nothing said a description must not
carry a value (added, found while walking "update the notes skill", whose
description names its vault path; the notes skill itself is out of scope
and unchanged); the invisible-Unicode check was asked of a plain read that
cannot see it (moved to the script).

5b BLOCKED, not waived. The old-vs-new A/B (3 evals × 3 runs × 2 arms,
`--budget 3`, `--allowed-tools` for the shared directory) was launched;
every session died at "Failed to authenticate: OAuth session expired and
could not be refreshed" (Claude Code 2.1.287; summary header resolved
claude-opus-5-5[1m]). `claude auth status` read `loggedIn: true` before
the suite and `false` after it, and a sandbox-disabled one-word `-p` run
failed the same way, so the cause is the terminal CLI's login, not the
sandbox. Fixture-name check done before launch: none of Lightroom,
Photos-Backup, Obsidian, summarize, conventional commits appears in the
skill. No description change, so no trigger eval. The eval set and the
old version are staged in `evals/config-2026-10-30/` (`evals.json`;
`old-skill-author/` with its frontmatter name changed to
`skill-author-old` so Claude Code cannot register it). Run after
`claude auth login`:

    /opt/homebrew/bin/python3.14 ~/.claude/skills/skill-rule-shared/scripts/ab_eval.py --evals ~/.claude/skills/skill-author/evals/config-2026-10-30/evals.json --out /tmp/skill-author-ab --mode skill --old ~/.claude/skills/skill-author/evals/config-2026-10-30/old-skill-author/SKILL.md --new ~/.claude/skills/skill-author/SKILL.md --runs 3 --workers 3 --budget 3 --allowed-tools "Read(//Users/ben/.claude/skills/skill-rule-shared/**)"

Grade against `expected_behavior`; eval 2 is the over-application guard
and should show no config file in either arm.

Shared-file changes (named as shared): skill-vs-rule.md — new bullet
under "Neither kind is the answer for": a per-machine or per-project value
one skill needs → that skill's config, not a rule. sources.md — the memory
doc entry gains a 2026-10-30 re-fetch bullet (AGENTS.md rules, trust
dialog rationale); the Agent Skills spec and prompting page entries are
refreshed to 2026-10-30; the skills doc entry gains the same-day second
extraction (substitution table, portability and security lines); a
Contents line and the new "skill-author skill subject-matter sources"
section (observed hardcoding; Cursor, Codex, Copilot, Gemini CLI, Claude
Code setup; Pillar, arXiv 2602.06547, OWASP, Snyk). evaluating.md — the
login-state preflight now records that `claude auth status` can read
`loggedIn: true` on a refresh token the first `-p` run then fails to
refresh; run a one-word `-p` before a suite.

Watch items: none about model behavior; this pass measured nothing.

## 2026-10-31 — skill configuration rebuilt to the grilled design; migrate mode; portable by default

Supersedes the design in the 2026-10-30 entry. Prompted by a grilling
session with Ben in session 4b9d2382-e133-42cd-9deb-18f9093fcab0 (six
rounds, 27 questions), confirmed in full before any edit. Decisions, all
Ben's: keys are declared in a `## Config` table at the top of SKILL.md
(key, required, default, purpose); values live in `config.local.yaml`
beside it, ignored by a `.gitignore` shipped in the skill; no shipped or
example values file; no project scope, since a project skill's local file
is project-scoped by location; no script of any language (Python rejected
as a setup dependency, and with no untrusted file left there was nothing
for a script to check, which is the plain-instruction direction left open
on 2026-10-24); one owner per value, with hand-offs between skills and
the companion skill's name as a key; a required key missing stops the
skill with an offer to write the file, print fallback when the harness
refuses; a configured directory that does not exist stops the skill,
never creates it (mount-point hazard), defined once in the template; a
value never appears in a description; no secrets, only where one lives;
portable by default with `metadata: {harness: <name>}` as the opt-out,
spec-only frontmatter, actions named instead of tools; a Migrate mode
("migrate <skill>", "make <skill> shareable", or a path) that moves values
automatically and proposes hand-off rewrites; migration checks are
desk-check, trigger eval where a runner exists, one smoke run, A/B only
when behavior was rewritten; skill-author itself portable, with a
`skills-dir` key and the Claude Code material moved to a harness
reference; A/B and trigger evals stay required where a runner exists and
are recorded as "not measured: no runner in <harness>" elsewhere;
rule-author and the two export skills deferred, the export skills to be
retired once migration is done. Verified targets Claude Code, Cursor,
Codex; best effort Gemini CLI, Copilot, Antigravity; macOS and Windows.

Classified as an update that adds guidance. Step 2: same-day reuse of the
sources read 2026-10-30, plus an Antigravity research subagent and a
direct inspection of config parsers on this machine's two Pythons, both
recorded in the ledger's skill-author section. Mechanism: unchanged, this
is drafting procedure.

Changes:
- `references/skill-config.md` rewritten (158 lines, TOC): decide what
  varies, the Config table, the values file, the read instruction, set-up
  and failure wording, migrating an existing skill.
- New `references/claude-code.md` (120 lines, TOC): skill and transcript
  locations, the frontmatter extensions and their measured quirks
  (`allowed-tools`, `disable-model-invocation`, `when_to_use`,
  substitutions), dynamic context injection, writes under `~/.claude`,
  the runner and the two eval scripts, sources to re-check. All moved out
  of SKILL.md and skill-standards.md.
- `references/skill-standards.md` rewritten (115 lines): neutral
  frontmatter rules (the spec's six fields; `metadata` carries
  `last-verified` and `harness`), the configuration section updated to the
  table and values file, a new portability section, a portable-script
  rule.
- SKILL.md rewritten in place (299 lines): a `## Config` section with the
  `skills-dir` key and the read instruction; the shared directory derived
  from it and links made relative; "read references/claude-code.md before
  step 0 when you run in Claude Code"; Classify gains **Migrate**; step 4
  gains the portability rule and the config bullet now names the table;
  5b says where a runner exists and what to record without one; step 7
  core sources now include the Agent Skills specification and "the
  harness's skills doc"; a new Migrating section. Frontmatter: description
  rewritten to add migrate and shareable triggers (trimmed twice to 993
  characters, under the 1,024 limit); `argument-hint` and
  `metadata.export` removed, since a portable skill uses spec fields only
  and the export tag belonged to the retiring export skills;
  `last-verified` 2026-10-31.
- New `config.local.yaml` (`skills-dir: ~/.claude/skills`) and
  `.gitignore` in this skill; `git check-ignore` confirms the nested
  ignore applies.
- Evals re-staged in `evals/config-2026-10-30/`: `evals.json` rewritten
  for the table design and adds frontmatter and tool-wording checks;
  `trigger-queries.json` new, 8 should-trigger including the migrate and
  shareable phrasings and 8 near-misses (database migration, repo sharing,
  rules, subagents, dotfiles, notes). The old version in
  `old-skill-author/` is unchanged.

Desk-checked against 4 scenarios: (1) a backup skill with an external
drive path → table with a required key, local file, ignore, read
instruction, spec-only frontmatter; (2) a commit-message formatter → no
Config section, "no config keys" in the report; (3) "migrate the notes
skill" → Classify to Migrating, the vault path becomes the key and leaves
the description, hand-offs proposed not applied; (4) a session in Cursor
→ no harness reference to read, 5b recorded as not measured. Fixes from
the walk-through and the preflight checks: the mount-point example in
skill-config.md used the A/B fixture's path and now uses `/Volumes/Archive`;
step 0's transcript sentence now reads "a harness reference, where one
exists"; the description was over the limit twice and lost its method
clause.

5b measured, after Ben renewed the CLI login the same day. Trigger eval
on Claude Code 2.1.287, claude-opus-5-5[1m], 16 queries × 3 runs: 16/16
pass, trigger rate 1.00 on should-trigger and 0.00 on near-misses, the
near-misses routed to doc-author, rule-author, agent-author, and notes as
intended; $0.62. A/B old-vs-new, 3 evals × 3 runs × 2 arms, 18 sessions,
$8.20 ($4.13 old, $4.07 new), no timeouts or API errors, artifact loaded
17 of 18 (old commit-style run 1 did not load and is excluded). By eval:
- photo-backup-path: new 3/3 on all six criteria (Config table first, no
  fixture path in body or description, the read instruction verbatim,
  `.gitignore` with `config.local.yaml`, retention as a named default or
  an optional key with default 90, spec-only frontmatter); old 0/3, the
  path in the description and body on every run, `argument-hint` and
  `${CLAUDE_SKILL_DIR}` in two.
- commit-style-no-config: new 3/3 (no Config section, no keys, the report
  says "no config keys"); old 2/2 usable runs also no config, so the
  over-application guard holds and the only old-arm difference is
  `argument-hint` in both.
- minutes-companion-skill: new 3/3 (required folder key, companion skill
  as an optional key with default `summarize`, no other keys, no tool
  names); old 0/3 by the criteria, and the three old runs each improvised
  a different shape for the same need: a `<SET ME: absolute path>`
  placeholder, a "## Configuration" section, a "## Settings" section.
Transcript spot-check (photo run 1): the new arm read its own
`config.local.yaml`, `skill-config.md`, `skill-standards.md`, and the
shared style file, then wrote the produced skill's `config.local.yaml`
with the value from the prompt; the old arm read the standards and style
files only. Cost per run near parity: $0.52 vs $0.61 on the backup task,
$0.42 vs $0.40 and $0.42 vs $0.37 on the other two. Results copied to
`evals/config-2026-10-30/results-2026-10-31/`. Fixture-name check passed
before launch. Rerun, output outside `~/.claude`:

    /opt/homebrew/bin/python3.14 ~/.claude/skills/skill-rule-shared/scripts/trigger_eval.py --skill skill-author --eval-set ~/.claude/skills/skill-author/evals/config-2026-10-30/trigger-queries.json --json /tmp/skill-author-trigger.json

    /opt/homebrew/bin/python3.14 ~/.claude/skills/skill-rule-shared/scripts/ab_eval.py --evals ~/.claude/skills/skill-author/evals/config-2026-10-30/evals.json --out /tmp/skill-author-ab --mode skill --old ~/.claude/skills/skill-author/evals/config-2026-10-30/old-skill-author/SKILL.md --new ~/.claude/skills/skill-author/SKILL.md --runs 3 --workers 3 --budget 3 --allowed-tools "Read(//Users/ben/.claude/skills/skill-rule-shared/**)"

Shared-file changes (named as shared): guidance-style.md gains the
"name actions, not tools" rule for portable skills; skill-vs-rule.md's
config bullet now names the table and `config.local.yaml`; sources.md
gains, in the skill-author section, a superseding decision record, a
"Config file format facts" direct-inspection entry, and an Antigravity
documentation entry (subagent-fetched, quotes relayed, lead did not open
the pages). evaluating.md unchanged this pass.

Follow-ups Ben named, not done here: migrate the existing skills, notes
first (started as its own session the same day); retire cursor-export and
config-export after the migration; rule-author's own portability is a
later task. Watch items (n=3 runs each): the old skill-author, given a
path it was not told, invented a config convention on every run and a
different one each time, while the new one produced one shape 6 of 6; one
old commit-style run did not load the skill (1 of 9 old runs). Method
note: `ab_eval.py --new` copies the whole skill directory, so this
skill's `evals/` tree, including the renamed old snapshot, travelled into
the scratch project; harmless here, but keep eval fixtures that contain a
`SKILL.md` renamed, as this one is.

## 2026-10-31 — notes — updated (migrated to per-skill config)

First Migrate pass, run in a side session on the notes skill, following
"Migrating an existing skill" in references/skill-config.md. The vault
path `~/projects/ai/notes` became the required key `vault-dir`; the
Config table and read instruction went in as the first section after the
title; today's value went into `config.local.yaml` with the shipped
`.gitignore`; the description and body now say "the configured vault
directory (`vault-dir`)". Portability rules applied with no `harness`
key. Detail, checks, and the items left for a later pass are in
`~/.claude/skills/notes/CHANGELOG.md`.

5b ran: the login block recorded earlier today is lifted. `claude auth
status` reported logged in and a one-word `claude -p` returned OK at
16:22, so the suites staged by the build pass above can run now. Notes
trigger eval: 16/16 after one eval-set fix (recall 1.00, near-miss rate
0.00, 3 runs per query, $0.31, Claude Code 2.1.287, claude-opus-5-5[1m]).
The first run scored 15/16 because one should-trigger query referenced
conversation context a fresh `-p` session lacks: the 2026-08-22 trap in
evaluating.md, hit again. No shared-file change: the trap is already
recorded.

Procedure gap, not fixed here: migration step 1 lists values inside the
migrated skill, but the holders of copies in other skills had to be
supplied by hand (research, job-hunting, rule-author hold the vault path).
A grep of `skills-dir` for each moved value, with the holders listed as
hand-off candidates in the report, would make step 5 complete. Check
trap for step 7: the `grep` in Claude Code's shell snapshot is a shell
function that honors `.gitignore`, so a grep for the moved value reads
clean without ever seeing `config.local.yaml`; confirm the values file
with `/usr/bin/grep` or by reading it. Watch items: none about model
behavior; the eval measured the description only.

## 2026-10-31 — migrate pass on study-credibility: no config keys; procedure gaps closed

Second Migrate pass, on study-credibility, following "Migrating an
existing skill". Step 1 found no machine-specific value: no path outside
the skill, no host, account, vendor choice, or companion skill in prose;
the registries and databases it names are subject matter. No Config
section, no values file, no text change; `metadata.export: portable` kept
because config-export still reads it. Detail and the desk-check are in
`~/.claude/skills/study-credibility/CHANGELOG.md`. Research step exempt:
structural pass. 5b not run: the description did not change and no value
moved, so neither the trigger eval nor the smoke run had anything to
measure; stated here rather than left as an unstated skip.

Self-maintenance, procedure only, no model-behavior claim:
- SKILL.md Migrating: the trigger eval is conditioned on the description
  changing and the smoke run on a value moving; a skill with nothing to
  move is reported as "no config keys" with the skipped checks recorded.
  The text previously assumed both always happen.
- references/skill-config.md step 1: for each moving value, search the
  skills directory for copies in other skills and list the holders as
  hand-off candidates, the gap the notes pass recorded. Step 7: confirm
  the values file by reading it (the `grep` wrapper trap from the same
  entry), condition the trigger eval on a description change, and add the
  nothing-to-move outcome.

No shared-file change. Core sources not re-verified; `last-verified`
unchanged. Watch items: none.

## 2026-10-31 — migrate pass on prompt-author: no config keys; two portability edits

Third Migrate pass, on prompt-author, in its own desktop session while
three other migrate sessions (agent-author, doc-author, rule-author) and
the study-credibility pass ran in parallel. The study-credibility pass
closed the nothing-to-move gap in SKILL.md and skill-config.md before
this pass needed it; the first read here showed the old text and a
re-read after the file changed showed the new, so every shared edit below
was made by exact match after a fresh read. Step 1 found no value to
move. Step 6 changed two things: dropped `argument-hint`, the first
non-spec frontmatter field a migration has removed, and replaced the
desktop rename tool's name in the Session title section with the action.
Detail, the desk-check, and the smoke run ($0.22, Claude Code 2.1.287,
claude-opus-5-5[1m], skill loaded, write-mode output, no rename attempt)
are in `~/.claude/skills/prompt-author/CHANGELOG.md`. Trigger eval not
run: description unchanged. No A/B: behavior not rewritten. Research
exempt: structural pass. `metadata.export: portable` kept, as the two
earlier migrations did.

Self-maintenance, procedure only:

- references/skill-config.md step 7: the nothing-to-move outcome said the
  run was skipped "because nothing changed", which a pass that edits the
  frontmatter under step 6 would misread as licence to skip. Added one
  sentence: when step 6 changed the frontmatter or the body, run the
  skill once to confirm it still loads.

Observation for the parallel passes, no file changed: `argument-hint` is
on 11 skills in `skills-dir`, five of them tagged `export: portable`
(ai-retrospective, political-strat-id, political-strategy, research,
sleuth). A migration of any of them should drop the field the same way or
declare `metadata: {harness: claude-code}` and keep it. No shared-file
change. Core sources not re-verified; `last-verified` unchanged. Watch
items: none about model behavior (one smoke run); the rename-branch
watch item is in prompt-author's changelog.

## 2026-10-31 — migrate pass on rule-author: no config keys; relative links to the shared directory

Third Migrate pass, on rule-author, following "Migrating an existing
skill". Two values left the body and none became a key: the shared
directory's absolute path, now the sibling directory reached by relative
links (`../skill-rule-shared/...`, the form its rule-standards.md already
used), and the copy of the notes vault path, now "the user's notes vault,
which the notes skill owns", this skill's own wording. rule-author gets no
`skills-dir` key: this skill needs one to enumerate personal skills for
"update all", rule-author enumerates rules files at the harness's fixed
paths and needs the shared directory only, and a key for that alone would
be a key added for show. Portability: `argument-hint` and the two
`${CLAUDE_SKILL_DIR}` substitutions removed; 5b gains the same
"wherever a runner exists" clause this skill carries. No `harness` key:
the subject is Claude Code rules, the mechanics are not. Detail, the
desk-check, the three smoke runs ($0.56, Claude Code 2.1.287,
claude-opus-5-5), and the remaining holders of the vault path are in
`~/.claude/skills/rule-author/CHANGELOG.md`. Research exempt: structural
pass. Trigger eval not run: the description did not change. A/B not run:
no behavior rewritten.

Self-maintenance:
- references/claude-code.md, "Writes under the configuration directory":
  under `--permission-mode dontAsk` a read under `~/.claude` is denied too
  unless an allow rule names the path, so a `claude -p` smoke run of a
  skill whose body links to the shared directory needs the
  `Read(//Users/<user>/.claude/skills/skill-rule-shared/**)` rule the A/B
  command already passes. Permission-mode mechanism, not a model-behavior
  claim: 1 of 1 run denied without the rule, 1 of 1 read with it, same
  prompt.
- The two edits to skill-config.md this pass had planned (search for
  other holders of a moving value; read the values file rather than grep
  for it) were already in the file from the study-credibility pass that
  ran in parallel, caught when the Edit tool refused a stale read. Nothing
  to add.

Watch item (n=1): a prose choice question that ends "Create nothing" did
not load rule-author in `claude -p` (0 tool calls); the model answered
from its always-loaded rules. Both authoring skills claim the choice
question in their descriptions; whether either loads on such a prompt is
unmeasured. No shared-file change. Core sources not re-verified;
`last-verified` unchanged.

## 2026-10-31 — migrate pass on agent-author: no config keys; script path relativized, `compatibility` added

Migrate pass on agent-author, in its own desktop session, in parallel with
the study-credibility, prompt-author, and rule-author passes. Step 1 found
no value to move. `~/.claude/agents/` is the documented location for
personal agents on every Claude Code install (sub-agents page re-fetched
raw, read for that fact only), so it is subject matter, not a value that
varies — the opposite call from this skill's own `skills-dir`, which varies
by harness. The one known second environment, a `CLAUDE_CONFIG_DIR`
override, is not documented to move agents (env-vars page, same fetch), so
the skill keeps the literal path rather than deriving one; both facts are
dated lines in agent-author's own sources.md. The two paths inside the
skill became `<skill-dir>/scripts/delegation_eval.py` and "this skill's
`CHANGELOG.md`"; a path into the shared directory in evaluating-agents.md
was dropped. Companion skills in prose (`skill-author`, `rule-author`) were
proposed as a hand-off key in the report, not applied. Step 6:
`argument-hint` dropped; the spec field `compatibility` added, naming the
`claude` CLI and Python 3 — no other SKILL.md in `skills-dir` carried one
at the time. Detail and the desk-check are in
`~/.claude/skills/agent-author/CHANGELOG.md`. Load check after the
frontmatter change: a `claude -p` roster run (haiku, $0.019, Claude Code
2.1.287) lists the skill. Trigger eval not run: description unchanged. A/B
not run: no behavior rewritten. Research exempt: structural pass.

Self-maintenance: the nothing-to-move wording this pass planned for
SKILL.md and skill-config.md was already on disk from the
study-credibility pass — the first read showed the old text, the anchored
edit script found zero matches and wrote nothing, and a fresh read showed
the new text. Nothing added. Observation, no file changed:
skill-config.md lists "a companion skill the skill hands work to" as a
usual key, while this skill names `rule-author` and `agent-author` in
prose with no key, and the rule-author pass made the same call; "Decide
what varies" could say when a bare pointer to another skill is not a
hand-off. Left for the user. No shared-file change. Core sources not
re-verified; `last-verified` unchanged. Watch items: none (one load run).

## 2026-10-31 — migrate pass on doc-author: no config keys; routing names stay; `when_to_use` folded

Third Migrate pass. Step 1 found nothing to move: doc-author's
machine-specific content is eight mentions of other skills (five as
near-miss routing in the description, two routing lines in its doc-types
reference, one scope-boundary clause naming info-design) plus the
`~/projects` vocabulary of the project-author route. Step 6 changed the
frontmatter: `when_to_use` (Claude Code only) folded into the description,
trimmed to 1,020 characters by dropping triggers the kinds list already
implies, and two "Grep" instructions now name the action. Detail in
`~/.claude/skills/doc-author/CHANGELOG.md`. Research exempt: structural
pass. 5b: the trigger eval ran because the description changed. 16/16,
recall 1.00, near-miss rate 0.00, 3 runs per query, $0.48, Claude Code
2.1.287, claude-opus-5-5[1m], builtin plugins only, no hooks. The
near-misses invoked info-design, notes, project-author, and mermaid, so
the routing names earn their characters. Smoke run not applicable (no
value moved); the 24 should-trigger loads cover "still loads". No A/B.

Self-maintenance, procedure only, no model-behavior claim:
references/skill-config.md step 5 gains the routing-name case. A skill
named in the description only to route a near-miss stays as a name: the
description decides loading before any file is read, so a key cannot
route there, and a missing skill elsewhere only means the request is
handled without it. Reached by applying step 5 to five such names and
finding that a key would configure nothing. Method note: the first
attempt to edit steps 1 and 7 found the study-credibility session had
written both changes minutes earlier; the exact-match replace refused and
nothing was lost. Re-read before every edit of a file another session may
hold.

No shared-file change. Core sources not re-verified; `last-verified`
unchanged. Pending Ben: the info-design clause rewording in doc-author,
proposed in the report. Watch items (n=1 pass): folding `when_to_use` into
a trimmed description lost no recall on 8 should-trigger queries at 3 runs
each.

## 2026-10-31 — migrate pass on research: one key (`notes-skill`); Claude Code facts to a harness reference; two hand-offs proposed

Migrate pass on research, the skill the 2026-10-24 decoupling was first
asked for and whose injected design Ben reverted on 2026-10-27; this pass
applies the rebuilt plain-file design instead. Step 1 found one value to
move, the vault path held in step 2 and in the search-tactics table, owned
by the notes skill: research drops the copy and gains the optional key
`notes-skill` (default `notes`), `config.local.yaml`, and `.gitignore`
(`git check-ignore` confirmed). Step 6: `argument-hint` removed; the
WebSearch and WebFetch facts, the 200-search cap, and `/deep-research`
moved from the body and search-tactics.md into a new
`references/claude-code.md`, read before step 3 in Claude Code; the body
names actions. Description unchanged (routing names stay, step 5).
Proposed, pending Ben: an `appraisal-skill` key for the study-credibility
hand-off, and a rewrite of the stale "skill-rule-creator's sources file"
line. Hand-off candidates listed: job-hunting still holds the vault path;
cursor-export's conversion map describes text the body no longer has.
Detail in `~/.claude/skills/research/CHANGELOG.md`. Research exempt:
structural pass; the relocated facts carry their 2026-08-15 verification
and research's `last-verified` stays. 5b: trigger eval skipped (description
unchanged); smoke run on 2.1.287 / claude-opus-5-5[1m], prose prompt,
loaded from the description, read `research/config.local.yaml` then
`notes/config.local.yaml`, read the vault, 15 turns, $0.44. No A/B.

Self-maintenance, procedure only, no model-behavior claim:
- references/skill-config.md step 1: a copy of a value another skill owns,
  held beside an existing hand-off to that skill, is a value move, not a
  hand-off. This pass hit the case: the step-5 wording alone would have
  left the path in the body pending a yes.
- references/skill-standards.md portability: a portable skill keeps one
  harness's measured tool behavior in `references/<harness>.md`, read only
  there, and says so once near the top of SKILL.md; this skill's own
  claude-code.md is the pattern. Written down because the research body
  carried tool names a portable skill cannot, and nothing said where the
  facts behind them go.

No shared-file change. Core sources not re-verified; this skill's
`last-verified` unchanged. Watch items (n=1 run, Opus 5.5): the model
resolved the companion's value by reading `notes/config.local.yaml`
directly instead of loading the notes skill; a quick-fact run did not open
the harness reference placed "before step 3". Neither goes into a standards
file until seen again.

## 2026-10-31 — kind decision, portability check, one reference per harness

Prompted by Ben's review of the day's migrations in session
4b9d2382-e133-42cd-9deb-18f9093fcab0: sessions running the Migrate mode
labeled rule-author and agent-author "portable" while their bodies stayed
harness-bound, and left harness terms in notes, job-hunting, and
prompt-author. The cause was in this skill: step 6 of the migration said
"apply the portability rules unless the skill declares a harness" and
never asked the author to decide what kind of skill it had, and nothing
checked the claim. Ben's principles, applied here: the kind is a decision
made first and always declared; each kind is written best for what it is;
quality of outcome stays priority one and the kind only moves where facts
live. Step 2 exempt: no guidance fact changed; same-day sources.

Changes:
- SKILL.md: step 3 decides and states the kind (portable or
  harness-specific; the subject decides, the user overrides; a harness
  feature that would improve a portable skill is raised, never dropped
  silently, and a harness-specific skill is never neutralized); checklist
  line 3 says so; step 4's bullet is now "Write for its kind"; the Config
  paragraph points at `references/<harness-id>.md` for the harness in
  use, Claude Code's existing; the two out-of-scope redirects name the
  mechanism generically; the Migrating section decides the kind first;
  frontmatter gains `harness: portable` and the Config table's example
  path is gone.
- references/skill-standards.md: `metadata.harness` is required on every
  skill (`portable` or a harness id); the portability section is now
  "Writing skills: kind" with the priority statement and the one-file-per-
  harness rule.
- references/skill-config.md: migration step 1 decides the kind and
  writes it before anything else; step 6 is by kind and keeps every
  needed step; step 7 runs the check; a new "The portability check"
  section lists the terms and the shell command, with the three allowed
  exceptions (subject matter, description trigger vocabulary, the check's
  own text). The step 5 and step 7 additions another session made the
  same day (near-miss names stay in descriptions; the grep-wrapper and
  reload notes) are kept.
- Shared (named as shared): guidance-style.md's tool-naming bullet now
  says harness-specific skills may name tools and portable skills keep
  tool behavior in harness references.

Portability check on this skill, run after the edits with the fixed
command, check-section lines excluded:
    SKILL.md:16:  skills". For an always-loaded rule (CLAUDE.md, .claude/rules/), use
Remaining hits are the description's trigger vocabulary (line 16) and
the check's own text (16 lines in skill-config.md); no dependence.

5b measured later the same day on Ben's instruction, with Opus agents:
old-vs-new A/B, old = the 2026-10-30 snapshot, new = this version, 3
evals × 3 runs × 2 arms, `--model opus`, Claude Code 2.1.287,
claude-opus-5-5, $9.05 ($4.16 old, $4.89 new), artifact loaded 18 of 18,
no timeouts. New arm: Config table, read instruction, `.gitignore`, and
`metadata: {harness: portable}` in 6 of 6 configured drafts, no fixture
path, no tool names, spec-only frontmatter (one draft adds
`compatibility`, a spec field, for its macOS script); no Config section
and no invented key in 3 of 3 drafts where nothing varied. Old arm:
fixture path hardcoded 3 of 3 on the backup task, `argument-hint` in 6 of
9 runs, one ad hoc "## Config" section without a table on the minutes
task. Cost per run rose in the new arm (+6%, +17%, +35% by eval) with
more turns: the kind decision and the check are extra steps, and the
drafts carry one more reference read. Results in
`evals/config-2026-10-30/results-2026-10-31-kind/`. No trigger eval was
due: the description did not change in this pass. Desk-checked against 3
scenarios by reading: a new skill about one harness's hooks
(harness-specific, named at step 3); "make X shareable" on a skill with a
runner command in its body (portable; the command moves to the harness
reference and the step stays worded "where the harness has a runner"); a
portable skill whose quality needs one harness's feature (raised to the
user at step 3, not dropped). Watch item (n=9 runs): the new arm's extra
turns are the price of the kind decision and the check; worth re-measuring
once the procedure is familiar to the model through use.

## 2026-10-31 — verify pass on doc-author and research: `harness: portable` declared; portability check run

Side session. It ran Migrate mode again on two skills that earlier passes
today called portable before the portability check existed. Ben decided
both kinds: portable. Each skill got `metadata.harness: portable` and no
other edit. Detail in each skill's CHANGELOG.md.

doc-author. Check output from the skill directory:

    SKILL.md:17:  CLAUDE.md or AGENTS.md, rule-author; for a diagram, mermaid.
    references/doc-types.md:21:- Files that are not this skill's: CLAUDE.md, AGENTS.md, llms.txt
    references/doc-types.md:308:## Files that are not this skill's: CLAUDE.md, AGENTS.md, llms.txt
    references/doc-types.md:310:- `CLAUDE.md` and `AGENTS.md` are instruction files for coding agents, not

All four hits are subject matter: they name document kinds that the skill
does not write, and they route those requests to rule-author. No other
hits.

research. Check output from the skill directory: no output (grep exit
status 1), zero hits. `export: portable` stays beside `harness`, because
config-export reads it. The vault hand-off that the brief asked for was
already in place. The 18:07 migrate pass removed the
`~/projects/ai/notes/INDEX.md` copy, and step 2 reads the vault through
the notes skill's read workflow (`notes-skill`). This pass confirmed that
and changed nothing in the body. A search for `projects/ai` in SKILL.md
and references/ finds nothing.

Both: the frontmatter parses as YAML with spec fields only. Research
exempt (no guidance changed), and `last-verified` is unchanged on both.
Desk-checked 1 scenario each, both pass: an AGENTS.md-plus-README request
in Codex for doc-author, and a check-my-notes question in Cursor with no
values file for research. Trigger eval: none due, because neither
description changed. Load run: each skill loaded through the Skill tool
in this session (Claude Code 2.1.287, claude-opus-5-5). A/B: not run,
because no behavior changed.

No change to this skill or the shared files. Method note, not promoted
(one pass): if a pass changes only the frontmatter, an in-session load
returns the unchanged body, so it cannot show that the harness parsed the
new frontmatter. A YAML parse of the frontmatter covers that gap.
Pending Ben, unchanged: doc-author's info-design clause; research's
`appraisal-skill` key and its stale skill-rule-creator line.

## 2026-10-31 — migrate pass on prompt-author (kind decision): portable; `/goal` and rename facts to a harness reference

This pass redoes the prompt-author migration under the kind-decision
procedure above. It supersedes the entry "migrate pass on prompt-author:
no config keys; two portability edits": that pass ran no portability
check and left the `## Claude Code /goal` section in the body. Kind:
portable, decided in the brief. Step 1: no value to move, no config keys.
Step 6: the `/goal` section moved in full to a new
`references/claude-code.md` (one word change, so the "three in Scope"
cross-reference resolves from the new file), with a "Session rename"
section that names the desktop rename tool again, verified against the
live tool schema; the body keeps a 4-line "Harness references" pointer;
`export: portable` removed; description unchanged. Detail in
`~/.claude/skills/prompt-author/CHANGELOG.md`.

Portability check, from the skill directory, before the edit:

    SKILL.md:304:the prompt or passes it to `claude -p`; the Skill tool cannot run it, and

After the edit: no output, grep exit 1. Zero hits; the pointer sentence
is the one product name left, exempt by the check's own text.

Checks: desk-checked against 2 scenarios (a refine request; a package
request in Claude Code that reaches the `/goal` reference). Trigger eval
not due: description unchanged. One run in this session (Claude Code
2.1.287, desktop, claude-opus-5-5): the skill loaded with the new body
and produced a refine-mode result. No A/B. Research exempt: structural
pass.

Two procedure observations, no file changed:

- skill-standards.md says the body points at harness references once,
  "read the reference for the harness you run in". That wording misses a
  skill whose output targets a harness: prompt-author's `/goal` guidance
  depends on where the produced prompt runs, not where the skill runs.
  The prompt-author pointer adds "or the prompt will run there". If
  doc-author, agent-author, or rule-author write for a target harness,
  they need the same clause; a later pass can generalize the standard.
- `last-verified` meaning: the brief set prompt-author to 2026-10-31,
  but no guidance source was re-fetched. The standards do not say
  whether a portability check counts as verification. Prompt-author's
  changelog records the real guidance dates (2026-10-29 and 2026-10-28)
  so the next refresh searches from there. Ben to decide whether
  migrations refresh the date.

Core sources not re-verified; this skill's `last-verified` unchanged.
Watch item (n=0 runs measured): the `/goal` guidance now needs the model
to open the reference; prompt-author's 2026-10-29 eval set measures it.

## 2026-10-31 — migrate pass on notes and job-hunting: `harness: portable` declared; portability check run

Side session. It ran Migrate mode on two skills, one at a time, under the
kind-decision procedure. The brief decided both kinds: portable. Detail
in each skill's CHANGELOG.md.

notes. `metadata.harness: portable` added beside `export: portable`,
which config-export reads. The Config table (`vault-dir`) and
`config.local.yaml` from the earlier pass today are kept. Two lines
reworded: "What not to write" now names "the harness's always-loaded
rule files for that project" instead of `CLAUDE.md`, `CLAUDE.local.md`,
and `.claude/rules/`; style-ste.md now names "the user-wide STE rule,
where one exists" instead of its path. No `references/claude-code.md`:
a model in Claude Code already knows its rule files. Check output from
the skill directory, after the edits:

    (no output; grep exit status 1)

job-hunting. `metadata.harness: portable` added. No config keys. The
copy of the notes vault path is gone as a value move: the notes skill
owns the value, and job-hunting does no work in the vault. The tracker
fallback `~/job-hunt/` is relative to the home directory, and the
tracker on this machine is inside a project. Proposed, not applied, and
recommended against: an optional `resume-skill` key. The "Skill tool"
sentence now reads "Invoke the resume-author skill". Check output from
the skill directory, before the edits:

    SKILL.md:164:`resume-author` skill. Invoke it with the Skill tool; hand it the resume

After the edits:

    (no output; grep exit status 1)

Both: the frontmatter parses as YAML with spec fields only. Research
exempt (no guidance changed), and `last-verified` is unchanged on both.
Desk-checked 1 scenario each, both pass. Trigger eval: none due, because
neither description changed. Load runs in this session (Claude Code
desktop app, claude-opus-5-5): notes loaded the new body and read
`vault-dir` from `config.local.yaml`. job-hunting returned the pre-edit
body on the first invocation, seconds after the edit, and the edited
body on the second. A/B: not run, because no behavior changed.

Observations for this skill, no file changed:
- The check's `auto memory` pattern misses the hyphenated "auto-memory".
  notes uses that form twice (the description and SKILL.md:182), both as
  scope statements, not as a dependence. A later pass can change the
  pattern to `auto[- ]memory`.
- The check cannot see a slash-command invocation (`/job-hunting` in
  job-hunting SKILL.md:130) or a user rule named by filename
  (`ste100.md` in notes references/style-ste.md:102). Neither is a
  dependence. Both are named in the skills' changelogs.
- Watch item (n=1, harness behavior): an in-session load seconds after a
  body edit served the cached body. It adds to the method note of the
  verify pass above, which covers a frontmatter-only change. Before you
  count a load run, confirm that the loaded text shows the edit.

Remaining holder of the vault path: cursor-export's
references/conversion-map.md, already listed by the research pass.
Pending Ben: the job-hunting tracker location rule does not match the
tracker on this machine (detail in job-hunting's changelog).

No change to this skill or the shared files. Core sources not
re-verified; this skill's `last-verified` unchanged.

## 2026-10-31 — migrate pass on agent-author (kind decision): portable; Claude Code facts to `references/claude-code*.md`

Migrate pass on agent-author ("make the agent-author skill shareable"),
run in a side session after the kind-decision rebuild above. Kind:
portable, `metadata: {harness: portable}`, decided before the pass. This
supersedes the portability claim in this file's earlier "migrate pass on
agent-author" entry, which left 33 check-hit lines and more unflagged
harness terms. Its "no config keys" finding stands. Research exempt:
structural pass, and agent-author's `last-verified` stays 2026-08-16.

What moved where:

- New `references/claude-code.md` (217 lines, TOC): the two-surface
  table, locations and precedence, the `ls` and `claude -p` load check,
  `claude --version`, tool names and grants, the background filter, `mcp__`
  naming, and what reaches a subagent. It maps the step-3 mechanisms to
  `isolation: worktree`, `memory`, `/subtask`, `/btw`, the Workflow tool,
  and agent teams. It also holds the Opus 5 preset brake, the marker
  convention, the `delegation_eval.py` command and arm construction, and
  the `Task` alias.
- `references/definition-fields.md` is now `references/claude-code-fields.md`.
- New `references/claude-code-sources.md`, with the Claude Code and Agent
  SDK provenance and the machine measurements, moved verbatim out of the
  skill's own `references/sources.md`.
- SKILL.md, `delegation-economics.md`, and `evaluating-agents.md` are
  rewritten in neutral terms. Every step, the economics, the desk-check, the
  measurement step, the failure table, and Old patterns are kept.

Frontmatter: `name`, `description`, `compatibility` ("Measurement needs
Python 3 and a non-interactive runner for the harness."), and `metadata`
(`harness: portable`, `last-verified`). `export` and `claude-code-version`
are dropped. Two stale lines from the 2026-08-18 fixes were corrected in
passing: the script no longer stops on `hooks` and `mcpServers`, and the
economics file now names five benefits. Detail is in agent-author's
CHANGELOG.

Portability check output, full:

    SKILL.md:3:description: Creates, reviews, and updates subagent definitions — the routing description plus fresh-context system prompt an agent harness delegates work to, written as an agent file (such as ~/.claude/agents/ or .claude/agents/) or as an agent object in an SDK app. Covers whether to delegate at all, the description that decides when the orchestrator delegates, the system prompt body, tool grants, model and effort selection, permission modes, and tests that delegation happens and beats inline work. Use when the user asks to make, write, add, fix, audit, or update a subagent or an agent; wants a specialized worker for reviews, research, tests, or migrations; asks whether something should be a subagent, a skill, or just done in the main conversation; or reports that their agent is never delegated to, is delegated to too eagerly, or returns useless results. Triggers include "make a subagent for", "write an agent", "my agent never runs", "should this be a subagent", "update my agents", and "add an agent to my SDK app".

One hit: description trigger vocabulary. No dependence.

Checks:

- Desk-checked 2 scenarios: a Cursor create with no reference file, and a
  Claude Code repair. Two text fixes came from the walk: read the
  reference before step 1, not step 2; a harness with no reference file
  has no supported runner.
- Trigger eval: 16/16 pass, 3 runs per query. The trigger rate is 0.96 on
  should-trigger queries and 0.00 on near-misses, which routed to
  skill-author and rule-author. $0.47, Claude Code 2.1.287,
  claude-opus-5-5, builtin plugins only, no hooks. The set is in
  `agent-author/evals/trigger-queries.json`.
- Live run in the session: "should a PR reviewer be a subagent?" loaded the
  skill, which read `references/claude-code.md` before step 1 and answered
  steps 1–3 only.
- No A/B.

Total measured cost $0.49: the eval plus a $0.018 login preflight.

No shared-file change. No new source read, so no `sources.md` line. Core
sources not re-verified; this skill's `last-verified` unchanged.

Observations for the procedure, not applied (no file of this skill
changed):

1. The check covers a skill's own provenance file under `references/`.
   agent-author's `sources.md` held seven Claude Code entries (four docs, three machine measurements). They fit
   the `<harness-id>-*.md` companion pattern
   (`claude-code-sources.md`), but `skill-config.md` says nothing about
   ledgers. ai-retrospective (`guidance-sources.md`) and study-credibility
   (`verification-sources.md`) carry local ledgers too, so their
   migrations will meet the same case.
2. The check's term list missed about a dozen harness lines that the brief
   named. They were a tool-grant list (`Read, Grep, Glob`), slash commands
   (`/subtask`, `/btw`), "the Workflow tool", field values
   (`isolation: worktree`, `model: opus`), and backticked tool names such as
   `` `Agent` `` and `` `Task` ``, which `(Agent|Task) tool` does not match
   across a backtick. A second grep found them. Adding those shapes to the
   check would catch them for every skill.

Watch item (n=3): the one should-trigger query under 1.00 (0.67) is the
SDK "agents map" phrasing. It is the vocabulary the new description traded
away; detail is in agent-author's CHANGELOG.

## 2026-10-31 — research — updated (`notes-skill` defaults to none)

At Ben's request, the optional key `notes-skill` in research now has an
empty Default, which means no notes skill. Step 2 reads the vault only
through a configured notes skill, and otherwise falls back to the
project's `notes/INDEX.md`. Step 9 records nothing when no notes skill is
set. This machine's `config.local.yaml` keeps `notes-skill: notes`.
Detail in research's changelog. The description did not change, so no
trigger eval is due. The portability check gave zero hits. A/B not run:
the behavior on this machine did not change.

Method note, not promoted (one observation): after this pass edited
research's body, an in-session Skill load returned the older body from
19:40, not the text on disk. In this session, a load proves that the skill
loads, not which version loaded. To check new text, grep the file or use a
fresh session.

## 2026-10-31 — portability check: the memory pattern matches the hyphenated form

Follow-up to the notes and job-hunting pass above, at Ben's request.
references/skill-config.md, "The portability check": the pattern
`auto memory` is now `[Aa]uto[- ]memory`, and the term list says "also
spelled `auto-memory`". The old pattern missed the notes skill's two
mentions, "auto-memory" and "Auto-memory". Procedure fix with a known
mechanism, no model-behavior claim.

Re-run with the new pattern on the five skills that declare `harness:
portable` (agent-author, doc-author, rule-author, notes, skill-author).
The only new hits are the notes skill's description and SKILL.md:182.
Both are explained in notes' CHANGELOG.md: trigger vocabulary and a scope
statement. Every other hit also matched the old pattern. notes:
references/style-ste.md:102 now names "the user-wide STE rule" instead
of the file `ste100.md`.

Ben deleted the job-hunting skill the same day, after the pass above.
The directory is in the Trash, not removed with `rm`.

No shared-file change. Core sources not re-verified; this skill's
`last-verified` unchanged.

## 2026-10-31 — doc-author — updated (companion names become config keys)

Ben asked for "references to other skills should be a property" in
doc-author. Four companion names in the body and in doc-types.md became
optional keys with an empty Default, meaning none: `style-rule`,
`structure-skill`, `agent-files-skill`, and `project-readme-skill`. This
machine's values (ste100, info-design, rule-author, project-author) are in
`config.local.yaml`, and `.gitignore` was added. The `~/projects` path
left doc-types.md with the project-author name. The description's routing
names stay (step 5). Portability check: the same four explained hits. A
smoke run in a fresh session read the values file first and routed
AGENTS.md through `agent-files-skill`: 2 turns, $0.21, 2.1.287,
claude-opus-5-5. No trigger eval (description unchanged). A/B not run
(same routing on this machine). Detail in doc-author's changelog.

Open question for this skill, not applied: references/skill-config.md
still shows a companion key with a filled Default (`notes-skill`, Default
`notes`). Ben's same-day direction on research and doc-author is the
opposite: a companion may be absent, so its key defaults to none. Changing
the example and the table rules waits for his yes.

## 2026-10-31 — dependency reduction, authoring cluster: one direction, config keys, shared files name no consumer

Pass from the dependency map at `~/projects/ai/dependency-map/`
(reduction-plan.md, decisions 1, 3, 4, 8). Ben's goal: skills and rules
stand alone, point to a dependency only when needed and through config,
one direction, no cycles. Research exempt: structural pass.

skill-author: new optional key `rule-skill` (empty default) replaces
every `rule-author` name in the body; when unset, the skill says a rule
is needed and stops. `config.local.yaml` holds `rule-skill: rule-author`.
The description drops rule-author, agent-author, and notes ("Not for an
always-loaded rule ..., a subagent, or a durable fact or write-up"). The
subagent redirect names the mechanism, not agent-author. Step 2.5 names
"whatever notes skill the user has". `skill-config.md`'s example key now
has an empty default, closing the open question from the 19:30 entry.
Smoke run, fresh `claude -p` (2.1.287, claude-opus-5-5, dontAsk, reads
allowed on this skill and the shared directory): a rule-shaped request;
first tool call read `config.local.yaml`, answer named rule-author and
cited the `rule-skill` key as its source; 2 turns, $0.22.

Shared files (named as shared): README.md, skill-vs-rule.md,
guidance-style.md, evaluating.md, and the two scripts' usage text name no
consumer skill: "the two authoring skills", "an agent-authoring skill,
where one exists", "a persona-writing skill, where one exists",
placeholder names in examples. README's link paragraph now gives the
relative path and drops the config-export note (that skill is retired to
`~/.claude/retired-skills/`, with cursor-export and grill-me).

Portability check after the edits: SKILL.md:16 only (the description's
"CLAUDE.md, .claude/rules/" trigger vocabulary); skill-config.md hits are
the check's own text. Trigger eval: due (description changed); run and
recorded in the reduction pass's combined entry below when done.

## 2026-10-31 — pass: dependency reduction across all skills and rules

Ben's goal: skills and rules stand alone, point to a dependency only when
necessary and through config, one direction, no cycles. Map and plan at
`~/projects/ai/dependency-map/` (dependencies.md, reduction-plan.md,
edges.tsv, tools/check.py as the gate). Before: 78 skill/rule/shared
edges, 3 cycles, 12 two-way pairs. After: 20 edges, gate PASS. Research
exempt: structural pass. Per-skill detail is in each skill's changelog
(22 skills touched; config-export, cursor-export, grill-me retired to
`~/.claude/retired-skills/`).

Rules applied, now the working standard for this collection and
candidates for skill-standards.md and skill-config.md in a later pass
(not written into them yet, pending Ben's read of the result):
- A description names no other skill; it says what the skill is not for,
  in its own words. The harness routes by each skill's own description.
- A skill reaches another skill only through a config key with an empty
  default, and states what it does when the key is unset.
- Layers point down: rule → skill → shared directory. A shared directory
  names no consumer; a scope note names no skill or rule.
- Harness facts live in `references/<harness-id>.md` or in a skill
  declared `harness: <id>`; a skill's own files are reached by
  `<skill-dir>/`, another directory by `../<dir>/`; shared state by a
  configured path whose contract lives with the state.
- CLIs a skill runs are declared in `compatibility`.

Shared-file changes (named as shared): README.md, skill-vs-rule.md,
guidance-style.md, evaluating.md, trigger_eval.py and ab_eval.py usage
text name no consumer skill. skill-config.md's example key has an empty
default.

Checks: portability check on each portable skill touched (hits are
description trigger vocabulary and the check's own text); fresh-session
smoke run of this skill's `rule-skill` hand-off (2.1.287, claude-opus-5-5,
2 turns, $0.22); `tools/verify.py` clean over 91 rows; five Mermaid charts
parse. Six more smoke runs and thirteen trigger evals (every changed
description, `--model opus`, output outside `~/.claude`) were launched in
one background job; their numbers go in the next entry.

Watch items (n=1 pass): whether a near-miss prompt that a removed route
used to catch now loads nothing — the trigger evals measure the changed
skill's recall, not that; one combined near-miss run is owed. Whether a
skill with a required key (tea-guide, sleuth, the political pair,
opnsense, insights-v2) stops correctly when `config.local.yaml` is
absent — desk-checked, not run.

## 2026-10-31 — measured (dependency reduction trigger eval)

Trigger eval after the dependency reduction, `evals/trigger-result-2026-10-31-reduction.json`: 16/16 pass, recall 1.00, near-miss rate 0.00, 3 runs per query, $0.53, Claude Code 2.1.287, claude-opus-5-5, builtin plugins only.
Near-misses that loaded another skill through that skill's own description: agent-author, doc-author, notes, rule-author.
Baseline on the same set at 16:29 today: 16/16, recall 1.00. Unchanged.

## 2026-10-31 — measured: dependency reduction trigger evals and smoke runs

Thirteen trigger evals ran in one background job (`--model opus`, 3 runs
per query, Claude Code 2.1.287, claude-opus-5-5, builtin plugins only,
results outside `~/.claude` and copied to each skill's `evals/`);
info-design's set needed a format conversion and ran after. Total
$5.63 for the twelve below.

| Skill | Pass | Recall | Near-miss rate | Cost |
|---|---|---|---|---|
| ai-retrospective | 14/14 | 0.96 | 0.00 | $0.39 |
| doc-author | 16/16 | 1.00 | 0.00 | $0.47 |
| mermaid | 14/14 | 0.96 | 0.00 | $0.45 |
| political-strat-id | 13/14 | 0.88 | 0.00 | $0.34 |
| political-strategy | 14/14 | 1.00 | 0.00 | $0.42 |
| project-author | 12/12 | 1.00 | 0.00 | $0.70 |
| research | 11/14 | 0.67 | 0.00 | $0.62 |
| resume-author | 10/10 | 0.89 | 0.00 | $0.45 |
| rule-author | 14/16 | 0.71 | 0.00 | $0.50 |
| skill-author | 16/16 | 1.00 | 0.00 | $0.53 |
| sleuth | 14/14 | 1.00 | 0.00 | $0.36 |
| tea-guide | 16/16 | 1.00 | 0.00 | $0.40 |

Comparisons where a baseline exists: skill-author, tea-guide, and
doc-author unchanged at 16/16; rule-author's two failing queries failed
before the change (14/16 at 19:31, same queries); project-author improved
from 11/12 (one near-miss loaded it) to 12/12. The other seven sets were
written in this pass and are baselines. research's 11/14 (recall 0.67)
has three should-trigger prompts that the model answered without loading
any skill ("compare Tailscale and Netbird", "is it true that intermittent
fasting ...", "what does the evidence say about code review size"); the
description change was one sentence about hand-offs, so this is a watch
item on the description's trigger phrases, not evidence about the
removed routes.

Watch item closed: of 78 near-miss prompts, every one that a removed
route used to name loaded the intended skill through that skill's own
description (notes 9 times, doc-author 5, rule-author 4,
study-credibility 3, research 3, skill-author 3, sleuth 2,
political-strategy 2, political-strat-id 2, prompt-author 2, agent-author
2, info-design 1, project-author 1, mermaid 1); the 38 that loaded nothing
were prompts with no skill to go to. Near-miss rate was 0.00 on every
set. n=3 runs per query, one model.

Six smoke runs (fresh `claude -p`, dontAsk, reads allowed on the skill
directory): political-strat-id, tea-guide, opnsense, insights-v2,
ai-retrospective, and research each read `config.local.yaml` first and
named the configured values with their keys; $0.18–$0.22 each.

info-design (run after the format conversion): 8/10, recall 0.53, near-miss rate 0.00, $0.37; detail in its changelog.
info-design reading: its set predates doc-author; the getting-started failure loaded doc-author, where the request now belongs. Watch item: the runbook prompt loaded nothing.

## 2026-10-31 — ai-retrospective — updated (made portable at Ben's decision)

Reverses this morning's `harness: claude-code` call. Facts moved into a
new `references/claude-code.md`; the method files are harness-neutral;
`argument-hint` dropped. Check: zero hits. Smoke run 2 turns, $0.21.
Detail in ai-retrospective's changelog. Observation for a later
standards pass (n=1): a skill whose evidence comes from harness-owned
files (transcripts) stays portable when the body describes the evidence
and the reference describes where it lives and how to extract it.

## 2026-10-31 — pass: ledger split by owner; six skills and the shared directory moved to the meta-skills repository

Ben's decisions, in order: split `sources.md` by owner first; move
prompt-author, skill-author, rule-author, ai-retrospective, research, and
study-credibility with `skill-rule-shared` into
`/Users/ben/src/skills/meta-skills` (agent-author not for now); declare
study-credibility `harness: portable`; link the repository into
`~/.claude/skills` with symlinks and say so in a README; scrub personal
paths from the moving files. Research exempt: structural pass.

Ledger split (shared-file change, named as shared): `sources.md` kept its
core sections (the five tiers, artifact tooling, prompt-author,
skill-author, and the ai-retrospective, research, study-credibility, and
notes/ste100 sections of the subject-matter group) — 2,244 lines. Every
other skill's sections went to a `sources.md` in that skill's directory,
never linked from its SKILL.md: doc-author (670 lines), sleuth (420,
with the findings-store section), political-strategy-shared (297, and
its corpus files now say "Provenance: sources.md in this directory"),
info-design (217), resume-author (198), tea-guide (197),
project-author (196), persona-author (131), mcp-author (90), mermaid
(67), notes (9). Sections for config-export, github-cli, and job-hunting
went to `~/.claude/retired-skills/sources-orphaned.md`. 5,169 body lines
in, 5,169 out. The core file's intro and Contents were rewritten; the
ASD-STE100 section stays in the core file because rule-author owns the
ste100 rule and a rules directory cannot hold a ledger. Wording changed
to match in this skill's steps 2.1, 2.5, and 7, in rule-author's, in
`skill-standards.md` ("provenance lives in a ledger: the skill's own
`sources.md` ... or the shared one"), and in the shared README's table
row.

Move: the seven directories moved with `mv` (values files and
`.gitignore` files travel with them). `link.sh` at the repository root
symlinks every top-level directory except `tools/` and dot-directories
into a target skills directory (default `~/.claude/skills`), relinks a
link that points elsewhere, skips a real directory of the same name, and
prunes links into the repository whose source is gone; tested: seven
links created, a second run prints nothing, a removed directory's link
is pruned. Root `.gitignore`: `config.local.yaml`, `.DS_Store`,
`__pycache__/`. `README.md` written with doc-author (install, layout,
per-machine config, portability with its evidence and limits, the
ledger, requirements); its `link.sh` output was pasted from a real run.
`compatibility` added to this skill and rule-author (Python 3.10+ and a
non-interactive runner for measurement). Scrubbed: `/Users/ben` in this
changelog, rule-author's, the shared changelog, the core ledger, and
ai-retrospective's Claude Code reference, replaced by `~` or `<user>`
with the lines kept effective.

Checks: study-credibility loaded through its symlink in a fresh
`claude -p` and reported `harness: portable` (3 turns, $0.23); this
skill, through its symlink, listed all 25 entries of `~/.claude/skills`
including the seven links (4 turns, $0.25); the dependency map's
extractor now follows symlinks, and `tools/check.py` still passes (90
rows, 20 skill/rule/shared edges; the corpus-to-ledger soft edge is gone).
Nothing committed in either repository: `~/.claude` shows the seven
directories deleted and seven symlinks untracked; the meta-skills
repository shows everything untracked beyond its first commit.

Watch items: a `find` without `-L` under `skills-dir` would skip the
symlinked skills (the smoke run used `ls` and a glob, which follow
them); `skills-dir` varies by harness on one machine, so it belongs in
the harness reference rather than in config — a later pass.
