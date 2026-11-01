# Changelog

## 2026-08-15 — created

Initial version: a nine-step desk-research workflow (frame, check notes,
plan, search, extract, weigh, stop, report, record) with two reference files,
`search-tactics.md` (where to look by source type, reformulation ladder,
chaining moves, lateral reading, Claude Code tool behavior, fetch prompts,
subagent brief, notes-file template) and `source-weighing.md` (authority by
claim type, GRADE-adapted grading, independence, disagreement, recency,
numbers and quotes, hand-offs).

Built from two evidence bodies, weighed as the user asked. Research
methodology: ACRL Framework, Kuhlthau's ISP, Bates's berrypicking, Ellis's
behaviors, Cochrane Handbook 6.5.1 chapter 4, PRISMA 2020, Kitchenham and
Wohlin (hybrid search and snowballing), GRADE, Wineburg and McGrew's lateral
reading and SIFT, Lord/Lepper/Preston's consider-the-opposite, Browne et al.
on stopping rules, Tetlock on calibration. Research as an agent: Anthropic's
multi-agent research post, web search and web fetch tool docs, Claude Code
tools reference (WebFetch is lossy, 200-search session cap), sub-agents and
workflows docs (`/deep-research` bundled workflow), the prompting page's
research section; OpenAI and Google deep-research docs; Deep Research Bench,
BrowseComp, GAIA, DeepTRACE, "Cited but Not Verified", the reference-
hallucination study, ClashEval, WASP; community deep-research skills reviewed
for shape only. Full provenance in skill-rule-creator's
`references/sources.md` under "research skill".

Judgment calls the evidence did not settle, stated in the skill: depth versus
breadth (resolved by fan-out into fresh contexts), stopping tests by question
type (a synthesis, not a validated rule), and the 18-month recency window
(user convention).

Tested against three evaluation scenarios (fast-moving fact, three-way tool
comparison for a decision, evidence question with a loaded premise) plus an
agent-specific check (lossy fetch and injected instructions). One change from
testing: the quick-fact shortcut now includes a glance at the notes index
when the question touches the user's own setup.

## 2026-10-31 — migrated: per-skill config, portable body, Claude Code facts moved to a harness reference

Migrate pass run by skill-author, following "Migrating an existing skill" in
its `references/skill-config.md`. This is the rebuilt plain-file design Ben
chose after reverting the injected design on 2026-10-27. Step 2 (research)
exempt: structural pass. No guidance was written; the facts relocated into
`references/claude-code.md` are the 2026-08-15 text unchanged, last verified
then (ledger section "research skill — tier 1: Anthropic and Claude Code"),
so `metadata.last-verified` stays 2026-08-15. An update pass should re-check
the Claude Code tools reference before those facts are relied on again.

Values moved:
- The personal vault path: `~/projects/ai/notes/INDEX.md` in SKILL.md step 2
  and `~/projects/ai/notes` in the search-tactics table. The notes skill owns
  that value (`vault-dir`), so research drops its copy and names the owner
  through a new optional key `notes-skill` (default `notes`). The Config
  table and the read instruction are the first section after the title;
  `config.local.yaml` holds `notes-skill: notes`; `.gitignore` shipped and
  confirmed with `git check-ignore` (the repository root is `~/.claude`).
  Step 2 now says what to do with no notes skill: read the project's
  `notes/INDEX.md` if there is one, skip the vault.
- Description unchanged: "study-credibility" and "the notes skill" there are
  near-miss routing names, which step 5 leaves as names.

Portability (step 6):
- `argument-hint` removed from the frontmatter (not one of the spec's six
  fields). `metadata.export: portable` kept because config-export reads it.
- The "Tool behavior in Claude Code" section of search-tactics.md, the
  `/deep-research` bullet and the session search cap in SKILL.md step 3, and
  the WebSearch and WebFetch sentences in step 4 moved to a new
  `references/claude-code.md` (43 lines), read only in Claude Code, before
  step 3. The body now names actions: a search tool, a fetch tool, "a
  harness reference, where one exists". The 403-publishers advice stayed in
  search-tactics.md under "Pages that refuse automated fetches" because it
  is not harness-specific. `allowed_domains` became "the search tool's
  domain filter"; "the scratchpad directory" became "outside the project
  (the harness's scratch directory, where it has one)".

Proposed, not applied (a hand-off changes behavior; pending Ben):
- Step 6 and the Hand-offs list in source-weighing.md name the
  study-credibility skill. Proposal: optional key `appraisal-skill`, default
  `study-credibility`, worded "the configured appraisal skill
  (`appraisal-skill`)".
- Step 9 and the same Hand-offs list name "skill-rule-creator's sources
  file". That skill was renamed on 2026-08-18 and its ledger now lives in
  `skill-rule-shared/sources.md`. Proposal: "hand the sources to the skill
  that authored the artifact; its ledger records them, not the artifact".
  No key, no name.

Holders of the moved value in other skills (hand-off candidates):
job-hunting/SKILL.md ("Do not write search data into the notes vault
(`~/projects/ai/notes`)"). cursor-export's conversion map describes
rewrites of research text that the body no longer carries; the export
skills are slated for retirement.

Checks:
- Desk-checked 4 scenarios: a quick fact about the user's own setup in
  Claude Code (Config → `notes-skill` → the vault through its owner; the
  quick-fact path skips the harness reference, as its "before step 3"
  placement allows); a three-way comparison in Claude Code (the harness
  reference supplies the lossy-fetch facts, the cap, and the
  `/deep-research` option); the same skill in Cursor with no
  `config.local.yaml` and no notes skill (the optional key defaults, step
  2's fallback applies, no harness reference to read); step 9 on that
  machine (offers to record, has no notes skill to hand to). One fix from
  the walk-through: step 3 assumed every harness has a reference file; now
  "a harness reference, where one exists, says so".
- Trigger eval skipped: the description did not change.
- One run of the migrated skill (step 7): Claude Code 2.1.287,
  claude-opus-5-5[1m], acceptEdits, in a scratch project, with reads of the
  research and notes skill directories and the vault pre-allowed plus
  `Bash(cat *)`. Prompt, in prose: "research: is chain-of-thought prompting
  still worth using on reasoning models like opus 5? check my own notes
  first, web only if the notes are thin". The skill loaded from the
  description (no slash). Its first tool call read
  `research/config.local.yaml` and then `notes/config.local.yaml`; it
  listed the vault at `vault-dir`, read INDEX.md and three notes, fetched
  the prompting page once to re-verify a `reported` note, and reported with
  graded confidence. 15 turns, 50 s, $0.44. It did not open
  `references/claude-code.md` (quick-fact path), and it resolved the vault
  by reading the notes skill's values file directly instead of loading the
  notes skill.
- A/B not run: no behavior was rewritten (the hand-offs are proposals).

Watch items (one run, one model): the companion skill's value was resolved
by reading the companion's `config.local.yaml`, not by invoking the
companion; a quick-fact run did not open the harness reference placed
"before step 3".

## 2026-10-31 — checked (kind declared; portability check run; vault hand-off confirmed)

Verify pass by skill-author's Migrate mode, after the kind decision and
the portability check were added to it. The migrate entry above came
before that check.

Kind: portable, decided by Ben. `metadata.harness: portable` added to the
flow map. `export: portable` stays beside it, because config-export
still reads that tag. The frontmatter parses as YAML with the spec fields
only (`name`, `description`, `metadata`). No body change.

Portability check, run from the skill directory with the command in
skill-author's `references/skill-config.md` (files searched: SKILL.md,
references/search-tactics.md, references/source-weighing.md;
references/claude-code.md excluded as the harness reference):

    (no output; grep exit status 1)

Zero hits. An extra scan for paths and tool names outside the pattern
found only the two pointers to the harness reference: SKILL.md:42 "When
you run in Claude Code, read references/claude-code.md" and
search-tactics.md:88. The check allows a harness's product name in that
kind of sentence.

Vault path: no change was needed. The brief for this pass said that step
2 still held `~/projects/ai/notes/INDEX.md`. It does not: the migrate pass
above removed that copy and the search-tactics copy as a value move.
Step 2 now reads notes "through the read workflow of the configured notes
skill (`notes-skill`) ... the personal vault, whose location that skill
holds". That is the one-owner hand-off Ben decided. A search of SKILL.md
and references/ for `projects/ai` finds nothing. `config.local.yaml`
holds `notes-skill: notes`. No other config key.

Research exempt: no guidance changed. `last-verified` stays 2026-08-15.

Checks:
- Desk-checked 1 scenario. In Cursor, the notes skill is installed but
  research has no `config.local.yaml`. The user asks "is it true that X?
  check my notes first". The `notes-skill` key is missing from the file,
  so it takes its default, `notes`. Step 2 reads the project's notes and
  the vault through the notes skill and holds no path. Cursor has no
  harness reference, so the Claude Code pointer does not apply. Pass; no
  text change.
- Trigger eval: none due, because the description did not change.
- Load run in this session: Claude Code 2.1.287, claude-opus-5-5, desktop
  app. The Skill tool returned the current body: the Config section, and
  step 2 with the hand-off. The body did not change, so this run shows
  that the skill still loads. It cannot show that the harness parsed the
  edited frontmatter again; the YAML parse above covers that.
- A/B: not run, because no behavior changed.

Still pending Ben, untouched: the `appraisal-skill` key and the rewrite
of the stale "skill-rule-creator's sources file" line (SKILL.md:252,
source-weighing.md:144), both proposed in the entry above. The watch item
from that entry is still open: one run read `notes/config.local.yaml`
directly instead of loading the notes skill.

## 2026-10-31 — updated (`notes-skill` defaults to none)

Behavior change at Ben's request: "Research shouldnt use notes as a
deafult. It will nto always be there. Default should be dont use a notes
skill". Step 2 exempt from research: a default the user chose, no
guidance claim. `last-verified` stays 2026-08-15.

Edits:
- Config table: the `notes-skill` Default goes from `notes` to empty. The
  Purpose now ends "when unset, use no notes skill". The key stays
  optional, so an empty value does not trigger the stop for a required
  key. The 19:40 column padding in the table is kept.
- Step 2: the vault is read through the notes skill only when
  `notes-skill` names one. When the key is unset, or the skill it names is
  not available, the skill reads the project's `notes/INDEX.md` if there
  is one and skips the vault. That was the old fallback for a missing
  skill; it now covers both cases.
- Step 9: when `notes-skill` is unset or its skill is not available,
  record nothing; the step 8 report holds the findings.
- search-tactics.md (the "Prior work" row) and source-weighing.md (the
  Hand-offs list) now say the same thing.
- `config.local.yaml` still holds `notes-skill: notes`, so this machine
  keeps the old behavior.
- Description unchanged. "durable findings to the notes skill" is
  routing text (skill-config step 5).

Portability check after the edits, from the skill directory: no output
(grep exit status 1), zero hits.

Checks:
- Desk-checked 1 scenario. On another machine, there is no
  `config.local.yaml` and no notes skill. `notes-skill` takes the empty
  default. Step 2 reads only the project's `notes/INDEX.md` if there is
  one. Step 9 records nothing. On this machine the values file sets
  `notes`, so step 2 and step 9 behave as before. Pass.
- Trigger eval: none due, because the description did not change.
- Load run in this session (Claude Code 2.1.287, claude-opus-5-5): the
  skill loaded. But the Skill tool returned the 19:40 body (Default
  `notes`, the old step 2 and step 9), not the edits from this pass. The
  file on disk has the new text, which a grep confirmed. So the load
  confirms the skill loads, but not that the session picked up this pass's
  text. A new session reads the file from disk.
- A/B: not run. On this machine the values file keeps the old behavior,
  so both arms would match. The new path runs only with no value set, and
  it is a default the user chose, not a claim to measure.

## 2026-10-31 — dependency reduction: `appraisal-skill` key; stale ledger line fixed; description names no skill

Pass from `~/projects/ai/dependency-map/reduction-plan.md`. Research
exempt. New optional key `appraisal-skill` (empty default) replaces the
study-credibility name in step 6 and in `source-weighing.md`; when unset
the skill grades the study with the source-weighing table and says the
appraisal is shallower. `config.local.yaml` adds
`appraisal-skill: study-credibility`. The stale "skill-rule-creator's
sources file" line (step 9 and the Hand-offs list) now says "the ledger
of the skill that authored the artifact". The description's last sentence
is "Hands single-study appraisal and note-keeping to other skills where
they are configured". Trigger eval: due (description changed); an eval
set was written in this pass (`evals/trigger-queries.json`, 8 + 6).

## 2026-10-31 — measured (dependency reduction trigger eval)

Trigger eval after the dependency reduction, `evals/trigger-result-2026-10-31-reduction.json`: 11/14 pass, recall 0.67, near-miss rate 0.00, 3 runs per query, $0.62, Claude Code 2.1.287, claude-opus-5-5, builtin plugins only.
Failed: "compare Tailscale and Netbird for a homelab" (should, rate 0.33); "is it true that intermittent fasting improves insulin sensitivity" (should, rate 0.00); "what does the evidence say about code review size and defect rates" (should, rate 0.33).
Passed below 1.00: "what's the current state of WebGPU support across browsers" (0.67).
Near-misses that loaded another skill through that skill's own description: doc-author, notes, study-credibility.
No earlier run of this set; the set was written in this pass, so the number is a baseline, not a comparison.
Smoke run (4 turns, $0.22): loaded from a prose prompt, read `config.local.yaml`, named study-credibility and notes from `appraisal-skill` and `notes-skill` and said the defaults are empty.

## 2026-10-31 — moved to the meta-skills repository

Directory moved with its files to `/Users/ben/src/skills/meta-skills`
and symlinked into `~/.claude/skills` by the repository's `link.sh`. No
content change in this step; see skill-author's entry of this date.
