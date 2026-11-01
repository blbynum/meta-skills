# Changelog (skill-rule-creator, 2026-08-15 to 2026-08-18 — closed)

Dated record of every create, update, and verification pass the
skill-rule-creator skill ran — on itself and on the artifacts it maintained.
"Checked, no change" entries matter as much as changes: they tell future runs
what is already verified.

This file is closed. On 2026-08-18 skill-rule-creator was split into
`skill-creator` and `rule-creator`, renamed the same day to `skill-author`
and `rule-author`; the two entries below record the split and the rename.
New entries go to `~/.claude/skills/skill-author/CHANGELOG.md` (passes on
skills) and `~/.claude/skills/rule-author/CHANGELOG.md` (passes on rules); a
change to a file in this shared directory is logged in the changelog of the
skill that ran the pass.

Entry format:

```
## YYYY-MM-DD — <artifact> — created | updated | checked, no change
One line on what was checked or changed, and why.
```

## 2026-08-18 — all four `-creator` skills — renamed to `-author` (rename entry)
Ben's decision, hours after the split: `skill-creator` → `skill-author`,
`rule-creator` → `rule-author`, `agent-creator` → `agent-author`,
`persona-creator` → `persona-author`, so that no personal skill shares its
last name segment with an `anthropic-skills:` entry on the desktop roster
(the trigger was `anthropic-skills:skill-creator` against `skill-creator`;
the skills doc says the bare name resolves to the personal skill, but the
model still saw two `skill-creator`s in the listing) and the collection
stays on one pattern. Directories moved with `git mv`; `name:` fields
updated; descriptions unchanged except the sibling names the two split
skills point to. Live pointers repointed: the two split
SKILL.md bodies and their standards files, this directory's README,
skill-vs-rule.md, guidance-style.md, the ledger header, the split-decision
line and the collision line in the ledger's Anthropic entries, the ledger's
persona section headings, ai-retrospective, agent-author (SKILL.md and
evaluating-agents.md script paths), research (SKILL.md, source-weighing.md),
config-export (scrub-categories.md; the replacement
`agent-creator-local-agent-name.md` renamed to `agent-author-…` with its
`replaces:` path updated). Left as they were: historical entries in every
changelog (the names in use at the time), the retired SKILL.md, and every
mention of Anthropic's own `skill-creator` plugin in the ledger,
skill-standards.md, and the notes vault — those are the vendor's, not ours.
Smoke check that the renamed skills load (not a full trigger eval — the
descriptions did not change): 2 should-trigger queries × 2 runs per skill,
Claude Code 2.1.220, claude-opus-5, no plugins, no hooks, roster of 29 with
only `-author` names present: skill-author 2/2 at 1.00 ($0.74), rule-author
2/2 at 1.00 ($0.64), agent-author 2/2 at 1.00 ($0.77), persona-author 2/2
at 1.00 ($0.54). The entry below and the two skills' own changelogs
describe the split under the names it was made with.

## 2026-08-18 — skill-rule-creator — split into skill-creator and rule-creator (split entry)
Ben's ask: skills should be pointed, and this skill covered two artifact
kinds that load, test, and fail differently. Research first (three core docs
re-fetched as raw markdown the same day; a 10-agent pass diffed SKILL.md and
both references against them — one internal inconsistency found, no
contradiction; the corpus and a live probe checked, see the ledger's Artifact
tooling entry). Weighed and done, not forced: the split's benefit is
expected, not measured — the old description already hit 9/9 should-trigger
runs — and rests on the skills doc's "Once a skill loads, its content stays
in context across turns, so every line is a recurring token cost" (a rule
request no longer loads skill-body guidance and vice versa; each workflow's
steps 3–6 differ by kind), on the family convention of one artifact kind per
`<kind>-creator` skill (agent-creator, persona-creator), and on the
best-practices naming rule against inconsistent patterns in a collection.
The cost is one more listing entry (skill-creator 1,009 chars, rule-creator
1,002; the 1%-of-context budget did not bite at 28 skills) and one shared
skeleton (steps 0, 1, 2, 7 and Updating) that now lives in two files. The
page's own alternative — Pattern 2, one skill navigating per-domain
references — was what existed and was chosen against.

Layout. `skill-creator/` (SKILL.md, references/skill-standards.md = the
frontmatter/body/scripts sections of authoring-standards.md, CHANGELOG.md)
and `rule-creator/` (SKILL.md, references/rule-standards.md = the Writing
rules section, CHANGELOG.md). Shared pieces in `skill-rule-shared/`, a
directory with no SKILL.md, which Claude Code 2.1.220 ignores (probed):
`sources.md` (one ledger; header names both skills), `evaluating.md` (whole;
its trigger-eval section was already marked skills-only; script paths
updated), `scripts/` (both scripts; ab_eval serves both modes), the
decision framework as `skill-vs-rule.md` (moved from SKILL.md, plus the old
out-of-scope bullets, because a request may need it before either skill is
chosen and two bodies inlining the same text are not deduplicated),
`guidance-style.md` (the two both-kinds sections of authoring-standards:
style, old patterns), this CHANGELOG, a README, and
`retired/skill-rule-creator.SKILL.md` (the last SKILL.md, kept so the tree
records what the bodies were cut from). Both SKILL.md files link every
shared file directly, one level deep, by absolute `~/.claude/skills/` path.
Considered and rejected: a plugin (`.claude-plugin/plugin.json`) for
`${CLAUDE_PLUGIN_ROOT}` sharing — plugin skills are namespaced and
`skillOverrides` does not reach them, so `ab_eval.py --mode skill` would
lose its baseline; keeping the shared files under one of the two skills —
asymmetric, and the ledger already serves eight artifacts; symlinked
`references/` — copies diverge in zip and sync. Names: `skill-creator` and
`rule-creator` keep the collection's pattern; the desktop's
`anthropic-skills:skill-creator` cannot conflict by name (plugin namespace;
the bare name resolves to the personal skill) but competes by description
on the desktop roster, where the CLI eval cannot see it. The corpus shows
that collision happened once with the old name (cd0e864b, a testing
question), so the new skill-creator description names testing and
measuring; whether that is enough on the desktop is untested.

Content moved, not rewritten. Specializations beyond a verbatim move, all
drawn from text already in the standards or this changelog: skill-creator
step 4 repeats the description rule in place of the rules-are-imperative
rule; rule-creator step 4 pulls the budget and contradiction checks up from
rule-standards.md as named checks; rule-creator 5a asks for one
opposite-failure scenario (the guidance-style bound, and what caught the
scope-discipline miss on 08-15); rule-creator's out-of-scope list carries
the 08-15 questions-rule lesson (a pure tool prohibition → offer the deny
rule first). Core sources per skill: skill-creator = skill-authoring
best-practices, Claude Code skills doc, prompting best-practices;
rule-creator = memory doc, permissions doc, prompting best-practices; a
pass that touches skill-vs-rule.md re-reads the other's doc too.
Cross-references updated in ai-retrospective, agent-creator (SKILL.md and
evaluating-agents.md), research (SKILL.md and source-weighing.md), and
config-export (scrub-categories.md; the stored replacement renamed to
`skill-rule-shared-eval-query.md`, its `replaces:` path updated, block hash
unchanged). config-export must treat `skills/skill-rule-shared` as an item
both skills depend on; its inventory will list it with no description.

Trigger eval, both descriptions, per evaluating.md (11 queries each — 6
should-trigger, 5 near-miss — × 3 runs, Claude Code 2.1.220 on PATH,
resolved model claude-opus-5, no plugins, no hooks,
`CLAUDE_CODE_DISABLE_WORKFLOWS=1`, `dontAsk`, CLI roster of 29 skills
without the anthropic-skills bundle). rule-creator: 10/11 pass,
should-trigger 0.78, near-miss 0.00, $0.63; the one FAIL is "claude keeps
ignoring my ste100 rule ... why, and fix it" at 0.33. skill-creator, two
rounds on the same set because the first description was revised
(989 → 1,009 chars; paths dropped from the first clause, complaint-shaped
triggers added, notes named as a redirect): 8/11 pass both
rounds, should-trigger 0.50, near-miss 0.00, $0.58 and $0.60; the misses
are the two complaint-shaped queries ("the notes skill keeps asking ...
fix it" 0.00 both rounds; "why doesn't my research skill fire" 0.00 then
0.33) plus the choice question, which rule-creator took instead (1 of 3,
then 2 of 3; the remaining runs answered "neither, a hook" directly, which
the framework agrees with). Every near-miss in both evals was 0.00 and
went to the right place (rule-creator, skill-creator, agent-creator,
refine-prompt, update-config, or nothing). Each skill's own CHANGELOG has
the per-query numbers and transcripts reading. Compared with the old
description's 9/9 should-trigger runs on 2026-08-18: not the same set —
the old set had no complaint-shaped query — so the two are not comparable
on that shape; on the shapes both sets share (create, update-all, tune a
named description) both hit 1.00 or 0.67. Union across the pair for the
choice question: a skill loaded in 4 of 6 runs.

Watch items for the next pass, not applied (stay inside the split): 5a
says "2–3 evaluation scenarios" while step 0 and evaluating.md set three as
the minimum (the desk-check floor may be intentionally lower; decide and
say so); skills now take a `paths:` frontmatter field, so the framework's
"`paths:` rules are the middle ground" is incomplete; a malformed
frontmatter YAML loads the body with no description (zero trigger rate with
a working `/name` is that signature — for evaluating.md); `skillOverrides`
does not affect plugin skills, so ab_eval's baseline cannot remove one; the
`InstructionsLoaded` hook logs which instruction files load (a mechanical
check for `paths:` rules); rule locations omit `./CLAUDE.local.md` in the
framework (rule-creator's intro now lists it); the memory doc's `/doctor`
content test (cut what Claude can derive from the codebase; keep pitfalls,
rationale, conventions that differ from defaults) is a rule content test the
standards lack; the description validation rule "cannot contain XML tags"
is not in skill-standards.md. All in the ledger with line numbers.

## 2026-08-18 — cross-cutting: superpowers removed, listing budget measured, collision test, rules baseline (step 8 of 8)
Superpowers (6.3.0, the only installed plugin) uninstalled by Ben's decision
after the review: 2 invocations in 72 sessions against a listing cost of
~688 tokens plus a SessionStart hook injecting ~1.1k tokens of "you
ABSOLUTELY MUST invoke the skill" into every session — the pressure pattern
this skill's own standards say to test, not default to — and a confound in
every trigger eval to date. Fresh `claude -p` roster after removal: 28
skills (was 42), no plugins, no hook.

Listing budget: the CLI's default model resolved to claude-opus-5 with a
1,000,000-token context window (`modelUsage.contextWindow` in the result
event), so the 1% budget is ~10k tokens and the 42-skill roster (~20k chars)
was not cut; in the desktop session (Fable 5) every description in the
listing was complete at the same roster size (agent-creator 991 chars,
persona-creator 914, xlsx 950 all end where their files end). No
description was shortened; the report's "[gap]" on this point is closed:
the budget does not bite on either surface today.

Collision trigger test on this skill's description, run before the
uninstall so superpowers:writing-skills was in the roster (Claude Code
2.1.220, claude-opus-5, superpowers hook active; the anthropic-skills bundle
incl. skill-creator is not in the CLI roster and stays untested there): six
queries × 2 runs; 9 of 9 completed should-trigger runs loaded
skill-rule-creator (incl. "make its description trigger better" and "write a
new skill ... be careful how you write it"), writing-skills fired in none;
the near-miss ("add an agent that reviews sql migrations") went to
agent-creator both runs; 3 runs timed out before a result and are excluded;
$0.93. `trigger_eval.py` gained `--save-transcripts` and an "also invoked"
column for this. Latent collision, not observed — same as the corpus (72
sessions: superpowers skills fired twice, never in a skill-rule-creator
session).

Rules baseline recorded in `~/ai/insights-v2/README.md` ("Notes for the next
run"): the three user-wide rules were on disk before the 08-16 incidents, so
they failed once rather than being untested; the next insights run compares
post-2026-08-18 incidents against that.

## 2026-08-18 — seven skills — review findings applied (step 7 of 8)
Each skill's own CHANGELOG carries the detail; this is the index. config-
export: identity terms and project names are derived and stated, not asked
(the user rejected both questions on 08-16). notes: the private host address
and port in the example note (SKILL.md and maintenance.md) replaced by a
generic alias; grep of skills and rules = 0 hits. persona-creator: the drift
reference states what the 2026 benchmark measured (the trained register) and
labels the custom-persona mapping and anchor transfer as inference; the tier
claim now agrees with the paper; two claims labelled reasoned/rule-of-thumb.
agent-creator: "exactly three things" → five (worktree isolation, per-agent
memory added, per the doc and step 6); "measured failure" → reasoning, with
the Cognition entry in its sources.md corrected. ai-retrospective: denials
do carry `is_error` and a top-level `toolDenialKind`; subagent transcripts
at `<session>/subagents/agent-<id>.jsonl` — both confirmed by inspecting
transcripts on this machine and recorded in sources.md. study-credibility:
six figures traced to primaries (three agents, Europe PMC / PMC / Cochrane /
Crossref), four corrected (Bekelman "a third" → "one fourth"; the OR 2.64
given its population — 294 mainland-China drug RCTs, Jia 2021 — and interval;
"~89%" preprint concordance was an interim conference figure, version of
record 86.4%; I² bands matched neither Higgins nor Cochrane and now quote
Cochrane), two matched (GRIM; the 10-study funnel-test rule), all with a
new ledger entry. mcp-servers: Old-patterns intro qualified for hosts on the
handshake era, with the SDK v2 default `legacy: 'stateless'` read from the
SDK's protocol-versions doc and recorded. Every changed figure has a
sources.md entry read from the primary; `last-verified` untouched on skills
whose subject pages were not re-fetched.

## 2026-08-18 — scripts (trigger_eval.py, ab_eval.py; agent-creator's delegation_eval.py) — updated (step 6 of 8)
trigger_eval.py: a trigger is now a Skill call whose `skill` field equals the
name exactly (or `plugin:name`), or a tool input naming `<name>/SKILL.md` as
a whole path segment — the old code substring-matched the whole Skill input
JSON and used an unanchored regex, so `notes` counted a refine-prompt call
whose args said "meeting notes" and `footnotes/SKILL.md`. Every result now
carries `claude_code_version`, `model` (resolved, from the `init` event),
`plugins_loaded`, whether the skill was in the roster, and cost per query
and in total; an `is_error` run counts as failed. ab_eval.py: `--mode skill`
baseline removes only the skill under test (`--settings skillOverrides off`
plus `--disallowed-tools Skill(<name>)`) instead of all skills; the with arm
is checked for the artifact loading and flagged when it did not; `--mode
rule` strips frontmatter and HTML comments before injection and the
docstring says rule mode approximates delivery (a real rule is a
`<system-reminder>` in the user turn); new `--old/--new` mode (rule: two
texts; skill: renamed scratch-project copies with the personal copy off,
because personal shadows project); version, model, plugins recorded; API
errors counted, not averaged. delegation_eval.py: PyYAML when installed,
otherwise a subset parser (scalars, folded/literal blocks, block and flow
lists, one nesting level) that refuses deeper structure by name; hooks and
mcpServers pass through as the sub-agents doc says `--agents` accepts;
`isolation` added; `--allowed-tools` passthrough with the acceptEdits +
Agent-only constraint disclosed in the docstring and the summary; version
and model recorded.

Checks run (Claude Code 2.1.220, model claude-opus-5, plugin superpowers
6.3.0 loaded — its hook was active in every session): unit tests on the
detector (7 cases incl. `footnotes/SKILL.md` and a Skill(refine-prompt) call
with "notes" in args, all correct), rule_text stripping, and the YAML subset
parser on the sub-agents doc's `skills:` block-list example (parsed as a
two-item list; `>-` description folded; `isolation` carried; hooks refused
with the PyYAML message). Live: trigger eval on notes, 2 queries × 2 runs —
should-trigger 1.00, the "meeting notes" near-miss 0.00, $0.45; smoke A/B
on refine-prompt, 1 run per arm — with arm loaded 1/1, without arm roster 41
skills (all but refine-prompt), $0.40. Two earlier attempts hit API 529,
which is what prompted the is_error handling. Not live-run: delegation_eval
(no agent under test this pass) and the skill `--old/--new` staging beyond
a dry check of the staged directory and the arm commands.

## 2026-08-18 — skill-rule-creator — workflow text updated (step 5 of 8)
The review found the workflow honoured selectively: text said research
precedes every pass and 5b is skipped "and say so", practice exempted
feature requests and skipped 5b silently; the prescribed vendor order (run
without the artifact → record failures → write minimal → measure) was quoted
in sources.md and not followed. Changes:

- New step 0, Observe first: three real prompts (or three real transcripts)
  without the artifact; the recorded failures are the eval set and the reason
  the artifact exists; if nothing fails, say so and ask.
- Step 2 is a fact-currency control: run it for guidance refreshes and for
  every load-bearing fact; skip it — and name the exemption — for a feature
  request that adds capability without touching guidance, a wording fix, or
  same-day reuse. Read the core-source entries plus the artifact's subject
  section of sources.md, not the whole file. Carry the model/vintage
  qualifier. The vault clause is gone: sources.md is the reference and
  `~/ai/notes` a snapshot this skill does not update (step 4 decision).
- 5b required for every user-wide skill and user-wide rule and for every
  description rewrite; skips must state a reason in the changelog.
- Step 6: name the check honestly — "desk-checked" for 5a; "tested" or
  "measured" only with numbers, model, and Claude Code version. Ten older
  entries across six changelogs that said "Tested against N scenarios" or
  "Evaluation scenarios run" for a desk-check are annotated in place
  "(nothing ran)".
- Step 7: single-query / single-session / <10-run claims about model
  behavior are watch items in this changelog, never standards; a method trap
  with an understood mechanism may go into evaluating.md dated. "Core
  sources" defined: skill-authoring best-practices page, Claude Code skills
  doc, memory doc, prompting best-practices page. `metadata.last-verified`
  → 2026-08-18 (all four re-read in step 1).
- Updating: names what prompted the update (observed failure / guidance
  refresh / feature or wording change) and which steps that exempts.
- evaluating.md: 5b requirement mirrored; the three 08-17 lessons moved in
  (real transcripts first; no eval query as a worked example; rule mode has
  no slash-command framing); `paths:` rules have a loading condition to
  check by hand; new "Confounds to record" section (Claude Code version on
  PATH vs desktop, resolved model, injected hooks such as a plugin's
  SessionStart skill-pressure hook, CLI skill roster); the arms description
  now matches what step 6 implements (targeted baseline, loaded check,
  stripped rule text, old/new mode) and states that rule mode approximates
  delivery, since a real rule arrives as a `<system-reminder>`.
- authoring-standards.md: the n=3 residue removed from the description
  guidance; "no citations" stated for skills as well as rules; the
  time-sensitive-phrasing rule distinguishes dated instructions from the
  model/date qualifier a claim must carry; Old-patterns header admits the
  measured ALL-CAPS exception.

Contradiction check: a fresh subagent read SKILL.md, both references, and
this changelog and listed 16 items; 9 were real conflicts and are fixed
above (n=3 residue, step-0 count vs the three-eval minimum, `when_to_use`
at startup, no-citations scope, feature-request exemption wording, "every
rule" vs single-project skip, Old-patterns header vs the ALL-CAPS exception,
time-sensitive phrasing vs vintage qualifiers, watch-item rule vs the
evaluating.md lessons). The rest were script flags evaluating.md now
describes ahead of step 6, and historical entries. Baseline for the record:
before this entry, agent-creator (08-16) and insights-v2 (08-18) ran a
trigger eval only, config-export (08-16) ran none, and no entry stated a 5b
skip; those entries predate the requirement and are left as written.

## 2026-08-18 — research vault (~/ai/notes) — three notes corrected, vault retired as this skill's reference (step 4 of 8)
`automatic-prompt-optimization.md`: "about 13 percent" and "about 20 percent"
were not in the paper; now quotes the arXiv abstract (GRPO: 6% on average,
up to 20%, up to 35x fewer rollouts; MIPROv2: over 10%) and names the models,
with the hand-tuning comparison attributed to VMware 2024. INDEX hook fixed.
`chain-of-thought-declining-value.md`: the uncited "meta-analysis" is Sprague
et al. arXiv 2409.12183, now cited with the verbatim "much smaller gains"
wording in place of "minimal or negative"; the Wharton line names the three
reasoning models and Gemini Flash 2.5's −3.3%. INDEX hook fixed.
`skills-vs-rules-vs-commands.md`: AGENTS.md removed from the always-loaded
list (memory doc: "Claude Code reads CLAUDE.md, not AGENTS.md"); the 200-line
figure marked as tier-1 corroborated; the under-trigger bullet carries the
split Anthropic guidance. `updated:` set to 2026-08-18 on all three;
`confidence` stays `reported` because each note still carries claims from
sources not re-read this pass. Every changed number was checked against the
abstract or doc page named in the ledger.

Decision (Ben, 2026-08-18): the vault is no longer this skill's research
foundation. Four research passes since 08-15 wrote only to sources.md, so the
notes drifted; keeping two records in sync had failed every time. INDEX.md
now carries a scope note saying the prompting/skills notes are a 2026-08-15
snapshot and that sources.md is the working reference. Step 5 rewrites
workflow step 2.4 accordingly. TAGS.md unchanged; INDEX stays sorted.

## 2026-08-18 — rules (ste100, anti-sycophancy, scope-discipline) — updated (step 3 of 8)
ste100.md, each change checked against the Issue 9 PDF text: the vocabulary
pair inverted the dictionary (ABOUT is "concerned with"; APPROXIMATELY is the
approved word — STE example "DRAIN APPROXIMATELY 2 LITERS") and now reads
"approximately" not "about" for a quantity; "3 nouns" is now "three words,
adjectives included" (Rule 2.1); the active-voice line carries Rule 3.6's
exception (passive in descriptive text only when the agent is unknown); the
"three or more" list threshold, which Rule 4.3 does not have, is gone; the
rule scopes notes out to the notes skill's own STE reference, and that
reference now names this rule and lists its deviations (hazard-first
warnings, "about"), so the two regimes are reconciled by pointer in each
direction. One new line from the insights-v2 report: put a pending question
on its own last line.

anti-sycophancy.md gains a "Check before you assert" section (four lines:
check state with a tool call before stating it, or say you cannot; do not
ask the user to re-run a command they say they ran — check its effect;
read a current primary source for facts that change often, or say you
answered from memory; run a gating check and its action as separate tool
calls and read the result first). scope-discipline.md gains the
user-content line (keep content the request did not name; do not remove
text the user wrote or restore text they removed unless asked), revived
because the general line it was said to duplicate was loaded when both
incidents happened. Rejected from the same report, as decided before this
pass: the `&&`/`;` ban, "put long detail in a file", and the gloss-labels
line that duplicates a system-prompt fragment.

Budget: to keep the comment-stripped total under 7 KiB after the additions,
seven existing sentences were tightened without dropping a rule (merged the
two "answer the question" bullets, folded "do not invent an objection" into
the manufactured-disagreement line, shortened three STE examples, cut two
rationale clauses). Result 7,162 bytes stripped (was 6,493), 7 KiB is 7,168.

Contradiction pairs compared, none found: new check-before-assert vs
scope-discipline "do not run exploratory commands against hosts the request
does not name" (the check applies to what you are about to assert about a
named target; otherwise "if you cannot check, say so" applies); new
"do not ask them to re-run" vs "if the premise is wrong, correct it first"
(checking the effect is how the premise is tested); new question-last-line
vs "start your reply with the finding" (start vs end); new user-content line
vs the system prompt's look-before-overwriting text (same direction); ste100
warning order vs notes hazard-first (notes scoped out, deviation declared);
"approximately" vs style-ste (declared); "if you cannot check, say so" vs
"do not hedge on a settled question" (an unchecked state fact is not
settled).

5b skipped, with reason: `ab_eval.py --mode rule` misdescribes rule delivery
and injects the comment header verbatim until step 6 fixes it, and the next
insights run over real sessions is the designated test of these rules
against their "failed once" baseline (recorded in step 8).

## 2026-08-18 — authoring-standards.md, refine-prompt, agent-creator, persona-creator — copies of ledger claims scoped (step 2 of 8)
Every copy of the four claims corrected in step 1 now carries the scope its
source gives it. authoring-standards.md: description guidance states that
Anthropic is split on pushiness (skill-creator says pushy; prompting page
says Opus 4.5/4.6 over-trigger) and tells the author to measure the
direction; the n=3 "one run in three straight to `ls`" observation is
demoted from a standard to a watch item (below); `metadata` is "for your own
tooling", not "ignored"; the system card "ties" is now "potentially linked";
"least capable model" is bounded by the Fable 5 over-prescription warning;
Old patterns scope ALL-CAPS to Opus 4.5/4.6, anti-laziness to Claude 4.6
models, self-checks to "a model whose vendor page says it self-verifies
(Opus 5 today)" with Fable 5 named as the exception, prefill to 4.6+.
refine-prompt: same four bullets scoped, CoT bullet points at Target model,
Capability tier reworded as a default the target's page settles, worked
example moves "check current sources" to the offers, "up to five, zero is
valid", optimizer line softened, CHANGELOG "three of four" → two of four.
agent-creator (two lines) and persona-creator (one line) scoped; their own
CHANGELOGs record it.

Desk-check (5a), three scenarios walked through the new refine-prompt text:
(1) refine a Fable 5 long-run build prompt containing "every N files, verify
against the spec with a subagent" — the self-check bullet says keep it for
Fable 5 and Target model says the page settles it: kept, and the rationale
notes the target dependence. (2) Same prompt targeting Opus 5 — stripped,
with the deprecated technique listed. (3) A Haiku-target prompt with "think
step by step" — the CoT bullet points at Target model, which keeps it for a
small target. Both the CoT and self-check bullets now cross-reference
Target model. Grep check: every remaining "over-trigger" in skills and rules
names Opus 4.5/4.6 or Claude 4.6; "Opus 5, Fable 5" occurs nowhere.

5b skipped for this step, with reason: wording scoped to its evidence, no
requirement moved and no description changed; the refine-prompt CHANGELOG
records the same skip.

Watch item (from step 7 of the 2026-08-18 insights-v2 pass, n=3): a
description that named the tool directory sent one trigger-eval run in
three to `ls` the directory without loading the body. Re-check with a
larger set before it becomes a standard.

## 2026-08-18 — sources.md — corrected after the meta-tooling review (step 1 of 8)
A 27-agent review of the rules, skills, vault, and this ledger found one
mechanism behind most errors: the model or vintage a finding was measured on
was dropped when the claim entered this file, then copied into several
artifacts. This pass re-read the primary sources (ten parallel readers, each
returning verbatim quotes with grep-verified absences) and rewrote the
affected entries; the copies in refine-prompt, authoring-standards,
agent-creator, and persona-creator follow in step 2. Corrections, each with
the primary text now quoted in the entry:

- Self-check exception names Opus 5 only; the Fable 5 page says the
  opposite for long runs ("Make self-verification explicit"). The "(and
  Fable 5)" was this file's addition.
- ALL-CAPS/MUST over-triggering is scoped in its only source to Opus
  4.5/4.6 tool triggering; the Fable 5, Opus 5, and Sonnet 5 pages carry no
  such guidance (grepped); the same page recommends a "you MUST read the
  file" sample; Anthropic's skill-creator says the opposite direction.
  Recorded as split guidance, direction to be measured, not asserted.
- The "no built-in eval runner" rationale for the in-house scripts was
  wrong: the Claude Code skills doc documents the skill-creator plugin
  harness (announced 2026-03-03), the vendor harness was used on 2026-08-06
  to build study-credibility, and the 2026-08-15 session chose in-house
  scripts for three stated reasons (install-scoped path, unused bulk, no
  rule mode). New Artifact-tooling entry records this and what each side
  adds.
- JudgeSense read against its own conclusion ("model scale is not a
  reliable proxy for consistency"); entry retitled and rewritten.
- 46%/17% belong to FlipFlop (ten 2023 models); "unfaithful capitulation" to
  arXiv 2605.29087 (Qwen3/GPT-OSS/Gemma-4, 2026); TRUTH DECAY tested Claude
  Haiku 2024, GPT-4o-mini, Llama 3.1 8B. Entry split three ways.
- Tag-question paper: Fable 5 hedges (44%→79%), rejects fall (5%→2%); the
  33%→48% rise is the mean of the other resisters. Single-author preprint,
  20 ground-truth-free items, now stated.
- SkillsBench average is +16.6 pp (v4); 15.8 was one row. Added "Focused
  Skills with at most three modules outperform larger or exhaustive
  bundles" and the compact-beats-comprehensive ablation.
- Vintage added: 2505.13360 (Llama-3.3-70B, gpt-4o-2024-08-06, o3-mini),
  Sharma 2023 (claude-1.3/2.0, gpt-3.5/4, llama-2-70b), Wharton (−3.3% to
  +3.1% on o3-mini, o4-mini, Gemini Flash 2.5).
- Sonnet 5 system card read from the PDF (p.86): "potentially linked", not
  "links"/"ties". ELEPHANT v2 names four dimensions on 11 models, not
  three. "public good" belongs to the skill-authoring best-practices page;
  the v2.1.218 `/deep-research` anchor to the Claude Code CHANGELOG;
  `CLAUDE_CODE_SYNC_SKILLS` → `~/.claude/skills/synced/` exists.
- Six tier-2 entries formerly "fetched search summary" (JudgeSense, VMware,
  Chroma, Sharma, TRUTH DECAY, ELEPHANT) are now read from the primary; both
  substantive misreadings were in that set. Contents lists all six sections.
  New entries: Sprague et al. 2409.12183 (for the vault's CoT note), GEPA
  arXiv numbers (6% avg / up to 20% vs GRPO; over 10% vs MIPROv2), memory
  doc AGENTS.md line.

Cost note: the file grew from 76 KB to 100 KB because corrections quote the
primary text; step 5 scopes what a pass must read.

## 2026-08-18 — insights-v2 skill — created
New personal skill wrapping the insights-v2 usage-report pipeline at
`~/ai/insights-v2`: prep, Workflow launch, result extraction, and a
render step in a separate session. Built from the tool's README,
render-prompt, workflow meta, and the pipeline write-up, checked against the
code and one completed run; five doc/code gaps recorded in the skill and a
result-extraction script added where the docs left a step undocumented.
Trigger eval ran three times across description versions (see that skill's
changelog): the final description hits 11/12 should-trigger and 0/12
near-miss. After the trade-off was reported, the user chose
`disable-model-invocation: true` instead — harness enforcement, slash
command only — so the description was trimmed to menu text and the eval
numbers describe the superseded version.

Learned for this skill's own method, all applied in the same pass:

- `disable-model-invocation: true` removes the description from context, so
  it also blocks prose requests; description gating is the tool for "only
  when asked, but asked in prose". Recorded in sources.md and
  authoring-standards.md, with the measured pattern that a description
  naming a path invites the model to explore instead of loading the body.
- A trigger eval of a skill that launches a workflow can start the real run
  from `claude -p`, where workflows launch with no prompt. evaluating.md now
  requires `CLAUDE_CODE_DISABLE_WORKFLOWS=1` for such evals.
- New skills-doc facts recorded: `when_to_use`, the 1,536-character listing
  cap, the 1% listing budget, `skillOverrides`.
- The workflows doc names where a run's script is saved but not its result;
  the result-file path is now recorded from inspection with the caveat that
  it is internal.

Sources re-fetched: skills doc (2026-08-18), workflows doc (new entry). The
skill-authoring best-practices page and memory doc were not re-fetched, so
this skill's own `last-verified` stays at its previous date.

## 2026-08-17 — refine-prompt skill — updated
Added a Scope section that binds produced prompts to the user's own
requirements, after the user reported repeated additions they never asked for.
Sixteen past sessions were read to ground the diagnosis; the addition size
scales inversely with the length of the ask, and the licensing lines were
identifiable in the skill's own text. That skill's changelog carries the
counted evidence and the A/B result.

Three things learned here that apply to this skill's own method:

- `sources.md` now records the Opus 5 "Task scope and over-verification"
  section verbatim, the best-practices "Overeagerness" clamp, and arXiv
  2505.13360 on underspecification. The last is the general lesson: when an
  artifact pushes against a behavior, look for the source that measures the
  opposite failure before writing the push. Here it changed the design from a
  ban into an offers list.
- Real past transcripts are the best eval set available for an artifact that
  has been in use. The queries carry the texture `evaluating.md` asks for, and
  the old outputs give measured baselines to compare against, which no
  synthetic eval provides. Worth doing first whenever the artifact has history.
- Two eval-design traps, both hit on this pass and worth avoiding next time.
  Do not reuse an eval query as a worked example inside the artifact — that
  arm is testing on training data. And `ab_eval.py --mode rule` gives the model
  no slash-command framing, so an eval query that only makes sense as a skill
  invocation gets answered as an ordinary question in both arms and measures
  nothing. Half the evals on this pass were lost to these two faults.

## 2026-08-16 — agent-creator skill — created
Created `~/.claude/skills/agent-creator/` for authoring and maintaining agent
definitions. Skill rather than rule: a nine-step workflow with three reference
files and a script. The scoping question the user raised — one skill or two —
resolved to one, on the property this skill decides everything else by: the
Claude Code agent file and the SDK `AgentDefinition` are one definition with
two serializations, so one workflow produces both and a split would duplicate
the body to vary a syntax table. That skill's own changelog and sources file
carry the subject-matter evidence.

Two findings that bear on this skill's own scripts, recorded in the new
skill's sources file rather than here because they are agent-specific: a
scratch `CLAUDE_CONFIG_DIR` does not authenticate on macOS, so the clean-room
arm construction used by `ab_eval.py --mode rule` has no equivalent for
agents; and `--disallowed-tools "Agent(<name>)"` removes an on-disk agent from
the types the model can see, which is the sound way to build an agent
baseline. Neither script here needed a change: `trigger_eval.py` detects the
`Skill` tool and `ab_eval.py` cannot see a delegation, so the new skill ships
its own `delegation_eval.py` instead of extending these.

`trigger_eval.py` run against the new skill: 5/5 queries pass, recall 1.00 on
three should-trigger prompts, 0.00 on two near-misses aimed at
`skill-rule-creator` and `refine-prompt`. Desk-checked against three
scenarios; three gaps found and fixed.

## 2026-08-16 — config-export skill — updated
Ben asked for the export to land in iCloud automatically. Added step 8 and a
`pack.py deliver` subcommand. No research pass: this is a feature request
against a fresh artifact, not a guidance refresh, so the evidence bar does not
apply. Worth recording because the first implementation was wrong in an
instructive way — delivery hung off `verify` as a flag and fired on structural
PASS, which precedes the scrub rescan, so it would have synced an
unconfirmed-clean archive to every device on the account. The fix separates
the two and leaves the machine-checkable half enforced in code and the
human-judgment half stated in the workflow. General lesson for artifacts with
an irreversible final step: check where the last *judgment* gate sits, not
just the last automated one.

## 2026-08-16 — config-export skill — created
Created `~/.claude/skills/config-export/` — a slash-command-only skill
that packages a scrubbed subset of `~/.claude/` as a verified zip for import
on another machine. Skill rather than rule was never in question: a
seven-step workflow with two scripts and two reference files. Four design
decisions the user asked to have resolved rather than guessed are recorded in
that skill's own changelog; the one that changed this skill's sources file is
tagging, which rests on the `metadata` field being documented as read by your
own tooling rather than merely ignored — a distinction the earlier sources
entry had flattened. Scripts were tested against a staged copy of the live
configuration rather than a fixture, which is what proved the false-positive
load real (a three-letter identity term matching `benefit` throughout a
research skill) and the second-hop dependency problem real (two reference
files invoke scripts their `SKILL.md` never names). Three failure modes were
tested and caught: checksum mismatch, a smuggled excluded file, and a stray
file absent from the manifest. Desk-checked against five scenarios; three
gaps found and fixed.

## 2026-08-15 — scope-discipline rule — created
Created `~/.claude/rules/scope-discipline.md` from a triage of a `/insights`
report over 72 sessions, which counted 13 wrong-approach flags and 10 rejected
actions. Five bullets across three ideas: prefer the smallest mechanism, act
only on what the request names (including pasted context, which is material to
read rather than a task list), and check why a behaviour exists before
proposing its removal. Named `scope-discipline` rather than the requested
`scope-and-consent` because "consent" covered only two of the five bullets and
is not plain vocabulary under the user's ste100 rule. Two rules were rejected
during triage as already covered by `anti-sycophancy.md`. Paired with two
`permissions.deny` entries in `~/.claude/settings.json` for the two ssh
directories, since rules are context and only permission rules are enforced; a
PreToolUse hook was rejected because the candidate matched any `ssh ` command
and would have broken a working `ssh mc-public` workflow. Desk-checked against
four scenarios including one for the opposite failure, which caught a missing
bound — without it the act-only-on-what-is-named bullet reads as a licence to
ask permission before every step. Step 5b skipped by agreement: six paid
sessions at roughly $0.23 each, and starting an unrequested paid run is the
behaviour the rule itself prohibits. Sources file extended with the Read/Edit
path anchors and the verbatim scope limit on Read deny rules.
Amended same day: Ben deleted `~/ai/.ssh/`, so its deny rule was dropped and
only `Read(~/.ssh/id_*)` remains. He also asked for the `Bash(ssh *)` ask rule
I had advised against, on the reasoning that it cannot distinguish a probe
against an unnamed host from a legitimate ssh. It does buy something the
default does not: `ssh` is not a built-in read-only command, so it already
prompts in manual mode, but an explicit ask rule outranks any saved "don't ask
again" approval and survives `auto` and `bypassPermissions` modes, which skip
prompts except those forced by explicit ask rules.

## 2026-08-15 — skill-rule-creator — updated
Added measurement to the Test step, which until now was a desk-check only.
Step 5 splits into 5a (desk-check, unchanged) and 5b (measure against a
no-artifact baseline, gated on stakes). The gap was against tier 1: the skill
authoring page prescribes establishing a baseline without the skill and
testing with a fresh instance, and states there is no built-in runner, so the
skill now ships two: `scripts/trigger_eval.py` measures how often a skill
loads across should-trigger prompts and near-misses, and `scripts/ab_eval.py`
runs task prompts in both arms and captures outputs, transcripts, and cost.
Neither script grades — grading needs judgment and stays with the agent. New
`references/evaluating.md` holds the method. CLI flags and result-event fields
verified by direct inspection of Claude Code 2.1.229 and recorded in
sources.md; SkillsBench added as labeled tier-3 corroboration; the authoring
page's "MUST filter" suggestion recorded as a contradiction against the newer
model-specific prompting pages, which authoring-standards.md follows. Both
scripts smoke-tested end to end: trigger_eval separated a should-trigger
prompt (1.00) from a near-miss (0.00) on the notes skill, and ab_eval ran both
arms with per-run outputs and a cost table. Testing surfaced one hazard now
documented in evaluating.md — run directories contain work that stays in the
working directory, but an artifact that writes to an absolute path writes
there on every run, in both arms.

## 2026-08-15 — skill-rule-creator, ai-retrospective — updated
Self-audit of the ai-retrospective build session (`/ai-retrospective`) drove
two changes. This skill's Research step now says to re-read `sources.md`
immediately before editing it: two sessions edited that file within minutes
during this pass, and the second edit reported a stale-read warning. The
hazard is live, not theoretical — concurrent sessions in the same project
share these reference files. Separately, ai-retrospective's unverified
compaction claim was demoted to an instruction to verify; the audit caught
that the skill asserted on-disk behavior nobody had observed. Two source
blocks added for it (session analysis and compaction; a format-instability
caveat on the transcript block).

## 2026-08-15 — research — created
New personal skill for desk research: nine-step workflow plus two reference
files (search tactics; source weighing). Two evidence bodies researched and
weighed as the user specified — research methodology (ACRL, Kuhlthau, Bates,
Ellis, Cochrane 6.5.1 ch. 4, PRISMA 2020, Wohlin, GRADE, Wineburg & McGrew,
SIFT, consider-the-opposite, Browne et al. stopping rules, Tetlock) and
research as an agent (Anthropic multi-agent research post, web search/fetch
docs, Claude Code tools reference, sub-agents and workflows docs, prompting
page research section; OpenAI and Google deep-research docs; Deep Research
Bench, BrowseComp, GAIA, DeepTRACE, Cited but Not Verified, reference
hallucination, ClashEval, WASP; community sources labeled). Five source
blocks added to sources.md under "research skill". Skill chosen over rule as
the user specified and the framework agrees. Desk-checked (nothing ran) against three scenarios
plus an agent-specific check; one change from testing (notes glance in the
quick-fact path). Thin-evidence areas (stopping, depth versus breadth,
recency window) stated in the skill as judgment calls.

## 2026-08-15 — skill-rule-creator — updated
Self-maintenance from the research pass: added a verification-method note to
sources.md that WebFetch in Claude Code returns an extraction model's answer
rather than the page, so a "fetched" negative holds only for what the prompt
asked (from the Claude Code tools reference); extended the prompting
best-practices entry with the page's research and subagent-orchestration
sections. No change to SKILL.md or authoring-standards.md: nothing found
contradicts them, and the tier-1 skill-authoring sources were verified
earlier the same day and were not re-fetched.

## 2026-08-15 — ai-retrospective — created
New personal skill auditing the agent side of the session it runs in: tool
use, subagents, skills and rules, context and rework, task decomposition.
Scope boundary drawn against refine-prompt, which already covers prompt
wording. Two source blocks added to sources.md: runtime guidance entry points,
and the session transcript format from direct inspection. The transcript
inspection changed the design twice — parallel tool calls occupy separate
JSONL records sharing a `message.id`, so a per-record count reports missed
parallelism on every session, and `leafUuid` turned out to be routine rather
than a compaction marker. Same deliberate deviation from the no-URLs rule as
mcp-servers: this skill's function is to fetch guidance at run time, so the
URLs are operational addresses, not citations. Tier-1 sources were verified
earlier the same day and were not re-fetched.

## 2026-08-15 — mcp-servers — created
New personal skill for writing and auditing MCP servers, targeting protocol
revision 2026-07-28 (`SKILL.md` plus five reference files; changelog in the
skill directory). Source list built fresh rather than from memory, as the
request required: trained knowledge describes the pre-2026-07-28 era, before
the protocol became stateless. Three source blocks added to sources.md
(specification, tooling/SDKs/registry, Anthropic tool-design and client
limits), including a recorded contradiction — Anthropic's own
`mcp-server-dev` plugin skills and connector docs lag the specification.
Deliberate deviation from the no-URLs rule in authoring-standards: the skill
carries the versioning URL and package-check commands, because the first
workflow step is a live staleness check that needs an address, not a
citation. Two tier-1 skill-authoring sources re-fetched during the pass and
found unchanged.

## 2026-08-15 — mc-computer CLAUDE.local.md — updated
Added one bullet under "Working with Ben": use `/refine-prompt` to write or
rewrite the model-facing prompt text, naming `minecraft-computer.md`,
`local-lore.md`, and `server/personas/`, plus the defining property (every file
the in-game assistant reads as instructions) so an unlisted prompt file is
covered. Rule over skill because the failure is an editing instinct — nothing
triggers a skill until the bad patch is already written. Gitignored file over
committed `CLAUDE.md` at Ben's direction: it is a preference about method, not
a project fact. Contradiction check against the always-loaded set found none,
and the "prompts, not documentation" clause does useful extra work against
`~/.claude/rules/ste100.md`, whose scope list would otherwise leave a persona
file ambiguous. Desk-checked (nothing ran) against four scenarios; the generalization case and the
read-only case both passed on the first draft. Known consequence accepted, not
patched: a one-word typo fix in a prompt file also triggers the skill, because
an exemption for small edits reopens exactly the hole the rule closes. Added a
file-level last-verified marker; the file had none. Same-day research reused,
no re-fetch.

## 2026-08-15 — mc-computer project rules — audited by audience
Split the repo's project-level guidance by who needs it. Re-fetched the Claude
Code memory docs to confirm `CLAUDE.local.md` still loads after `CLAUDE.md` at
the same level and that `paths:` rules load on file reads. Moved world-specific
test coordinates out of the committed `world-edit-tools.md` rule and Ben's
private persona out of committed `CLAUDE.md`. Promoted two irreversible-harm
lines (`--dry-run` before destructive edits, never delete a backup) from the
gitignored file and the path-scoped rule into always-loaded committed text,
because both apply in sessions that never open `server/bin/`. Removed the
`save-all flush` duplication between `CLAUDE.md` and the scoped rule: the
operator warning stays committed and always loaded, the author guidance stays
scoped. Corrected an inaccurate claim that a TTY-less deploy fails silently.
Dropped two `CLAUDE.local.md` bullets that duplicate always-loaded global
rules. Proposed no new skills: the upgrade and deploy procedures already live
in `README.md`, so a skill would be a second copy to keep in sync.

Second pass at Ben's direction: rewrite rather than refine, because these
artifacts predate any skill-authoring standard. Reshaped `CLAUDE.md` into
five sections, splitting destructive-operation safety out of the read/write
architecture list and moving the pointer to the scoped rule in beside it;
converted stated facts into the instruction each implies ("nothing runs
locally" became "test a change by deploying it"). Renamed the scoped rule to
cover running the tools, not only writing them, matching how `CLAUDE.md` now
cites it. Fixed a voice inconsistency inside it: one rule addressed "the
model" in the third person while every other rule addresses the reader.
Checked whether the fail-closed rule needs a wider `paths:` scope, since it
came from a `server/mcbot/` incident — no, because `server/bin/mcpersona` is
where the permission check runs, and `config.py` documents the incident in
its own docstring.

## 2026-08-15 — refine-prompt skill — updated
Research pass on whether prompting advice diverges by target model, and how to
cover that without bloat. Added one Target model section to refine-prompt: the
running model is the default target, a user-named target overrides it,
reasoning scaffolding scales inversely with capability, and volatile
per-release behavior is looked up in the vendor's page rather than recalled.
The section names axes and lookup points, never per-model facts, so it carries
no staleness debt. Rejected per-target sub-skills with a triage layer: about
five axes diverge, per-model files would duplicate shared craft and expire
each release, and no public benchmark shows a vendor's per-model page beats
generic good prompting. Sources file gained the reorganized Anthropic
best-practices page structure, the Opus 5 and Sonnet 5 prompting pages, a new
"Tier 1: other vendor documentation" section for the OpenAI GPT-5.1/5.2 guides
and the Gemini 3 developer guide, and tier-2 entries for PromptBridge
2512.01420, JudgeSense 2604.23478, and VMware 2402.10949. Recorded an explicit
evidence gap on the GEPA entry: nobody has measured whether the refining model
should be the model that runs the prompt.

## 2026-08-15 — anti-sycophancy rule (~/.claude/rules/anti-sycophancy.md) — created
New user-level rule in five sections: answer the question, judge on the
merits, hold a position, cut empty praise, do not overcorrect. Rule over
skill because sycophancy appears in ordinary work where nothing triggers a
skill. Research pass added eight sources: Claude's Constitution and the
Sonnet 5 system card (tier 1), and Sharma et al. 2310.13548, Ask Don't Tell
2602.23971, BrokenMath 2510.04721, TRUTH DECAY/FlipFlop 2503.11656, the tag-
question reversal 2607.23976, the sycophancy taxonomy 2605.21778, and
ELEPHANT 2505.13995 (tier 2). Mitigations chosen by measured effect: the
restate-as-a-question line comes from Ask Don't Tell, where 1-step question
reframing (β=0.16) beat a plain "do not be sycophantic" instruction (β=0.51)
against a β=1.13 control, and third-person rewriting failed outright, so it
was left out. The judge-a-claim-the-same-way line targets the measured
residual gap: all 45 models tested still fold for a tentative "…maybe?" and
for bare assertions, even where they now resist "…, right?". Assess-vs-act
wording follows the Fable 5 prompting page nearly verbatim. Overcorrection
section carries equal weight, grounded in the system card's "wet blanket"
tradeoff and the −5.9-points-per-year drift into contrarianism. Tested
against six scenarios; two fixes: revision now requires the user's argument
to hold up under a check (the first draft licensed capitulation to any
merely-new argument), and a bullet was added for arguments that fail.
Aggregate always-loaded budget: user CLAUDE.md 1 line, ste100.md 62, this
rule 60. No conflict with ste100.md, which governs style only; the rule is
written in STE.

## 2026-08-15 — skill-rule-creator — updated
Self-maintenance from the anti-sycophancy pass: added a bound-the-opposite-
failure principle to the guidance-prose section of authoring-standards.md.
Evidence bar cleared by tier 1 (Sonnet 5 system card ties higher "wet
blanket" rates to the sycophancy fix) plus tier 2 (45-model measurement of
frontier models crossing into active contradiction). Nothing else in the
skill or its references was contradicted by this pass.

## 2026-08-15 — questions rule (~/.claude/rules/questions.md) — removed
Replaced by config the same day. The user preferred the enforcement layer
over always-loaded context, so the rule file was deleted and
`permissions.deny: ["AskUserQuestion"]` was added to ~/.claude/settings.json.
A bare tool name in `deny` removes the tool from context, so the behavior is
enforced and costs no tokens. Lesson for future passes: when a request is a
pure tool prohibition and a deny rule covers it exactly, offer the config
first — a rule only earns its context when it also says what to do instead,
and that half can live in auto memory.

## 2026-08-15 — questions rule (~/.claude/rules/questions.md) — created
New user-level rule: ask questions in the chat reply and wait, instead of
using the AskUserQuestion card; carries the user's reason (too little
context to choose, several questions at once, no way to ask a follow-up
first) plus two positive bullets on one-question-at-a-time and context with
a recommendation. Rule over skill because nothing triggers a skill until
the card is already used. Re-fetched the memory/rules doc (no change to
existing guidance) and the permissions and permission-modes docs, which
are new to sources.md: a bare tool name in `permissions.deny` removes the
tool from context, which is the enforcement layer offered to the user
alongside the rule. Desk-checked (nothing ran) against three scenarios; the plan-mode case
failed the first draft (the plan-mode tool text tells Claude to use the
card), so the rule now names plan mode and tool- or skill-suggested cards
explicitly. Aggregate always-loaded budget checked: user CLAUDE.md 1 line,
ste100.md 63 lines, this rule 16 lines. No contradiction with ste100.md.

## 2026-08-15 — ste100 rule (~/.claude/rules/ste100.md) — updated
Scope widened at the user's request: STE now also applies to chat replies
that explain technical content (explanations, bug rundowns, findings,
requirements, step-by-step guidance), not only documentation deliverables.
Casual conversation, code, and code comments stay exempt. Grounded by the
FAQ's note that STE principles can be adopted in other writing contexts;
re-tested the chat-answer scenario, which now expects STE. Same-day
research reused, no re-fetch.

## 2026-08-15 — ste100 rule (~/.claude/rules/ste100.md) — created
New user-level rule: write documentation deliverables in ASD-STE100
Simplified Technical English, scoped out of chat and code per the official
FAQ's "not intended for general-purpose writing". Verified Issue 9 (January
2025) is current through 2026 (Issue 10 due January 2028) and confirmed the
20/25-word sentence limits via the official FAQ and search; sources.md STE
entry extended with those claims. Rule chosen over skill because doc
writing occurs incidentally mid-session where a skill would not trigger;
aggregate always-loaded budget checked (user CLAUDE.md 1 line, no prior
rules files). Desk-checked (nothing ran) against four scenarios (README, chat answer,
troubleshooting procedure, non-dictionary technical terms) before
finalizing. Tier-1 memory/rules docs not re-fetched — verified earlier the
same day.

## 2026-08-15 — notes skill — updated
Verified subject matter (STE Issue 9 counts and FAQ quote confirmed; 2026
community agent-memory practice corroborates the design — recorded under
"Artifact subject-matter sources" in sources.md, a section added this pass).
Brought the skill up to authoring standards: last-verified marker and
CHANGELOG.md were missing. One content change from scenario testing: an
absolute-dates style rule, because nothing stopped "last week" landing in a
durable note. Skill-authoring tier-1 sources not re-fetched — all verified
earlier the same day.

## 2026-08-15 — refine-prompt — created
New personal skill with four modes (write, refine, package, retrospective).
Research pass re-fetched the consolidated prompting best-practices page, the
Prompting Claude Fable 5 page, the Wharton CoT report, and the GEPA repo, and
reviewed community prompt-refinement skills. Desk-checked (nothing ran) against three evaluation
scenarios (refine a legacy-style prompt, package a debugging session,
retrospective) before finalizing.

## 2026-08-15 — skill-rule-creator — updated
Self-maintenance from the refine-prompt research pass: corrected the
old-patterns entry on "verify your answer" (model-dependent — still
recommended on most current models, harmful on Opus 5/Fable 5 per the
fetched best-practices page), added the reasoning-echo refusal pattern from
the Fable 5 page, upgraded three sources from via-vault to fetched, and
added the Fable 5 prompting page, console prompting tools, and community
prompt-refinement skills to sources.md.

## 2026-08-15 — skill-rule-creator — updated
Added the aggregate always-loaded budget rule for rules (audit the sum
across user/project CLAUDE.md and both rules directories; path-scope or
demote to skills when it grows; splitting files doesn't reduce cost).
Verified against the Anthropic context-engineering post (attention budget,
context rot; upgraded to directly fetched), the Claude Code memory docs
(imports/splitting don't reduce loaded context), and the Chroma Context Rot
study (added as tier 2). Framework table cost cell updated to match.

## 2026-08-15 — skill-rule-creator — created
Initial version. Sources seeded from the ~/ai/notes research vault (tags
`skills`, `prompting`). Fetched and verified directly: Anthropic skill
authoring best practices, Claude Code memory/rules docs, Claude Code skills
docs. Notable facts adopted beyond the vault: official under-200-line
guidance for CLAUDE.md files, `paths:`-scoped and user-level rules, free-form
`metadata:` frontmatter for verification dates, HTML comments stripped from
rules before context injection (used as the zero-cost last-verified marker).
Desk-checked (nothing ran) against three evaluation scenarios (create-skill, wrong-mechanism
recommendation, no-change update) before finalizing.

## 2026-08-15 — study-credibility — updated (first pass under this skill)
Re-researched and rewrote study-credibility, which predated this skill.
Subject-matter provenance recorded in sources.md for the first time (three
new sections: meta-research primary sources, appraisal instruments and
reporting guidelines, research-integrity landscape).

Finding that fed back into this skill: seven of study-credibility's specific
numeric claims were checked against primary sources and five were wrong or
unverifiable — including a Cochrane harms figure stated as RR 1.87 when the
review reports RR 1.37 with an interval spanning null, i.e. the artifact
converted a null result into a positive one. Added a bullet to
authoring-standards.md requiring every stated figure to trace to sources.md,
verified against the primary source, with intervals preferred over bare point
estimates and unverifiable figures cut or marked.

Also added to study-credibility: paper mills and fabricated papers (its
methods all assumed a real study underneath), the reporting-guideline vs.
validity-assessment distinction (CONSORT 2025, SPIRIT 2025, PRISMA 2020,
STROBE), ROBINS-I V2, and PROBAST/TRIPOD+AI. Authoring fixes: third-person
description, metadata.last-verified, copyable workflow checklist with a light
path for quick questions, table of contents on the reference file that had
passed 100 lines. Full detail in that skill's own CHANGELOG.md.

## 2026-08-15 — created persona-creator

Created `~/.claude/skills/persona-creator/` (SKILL.md, four references,
CHANGELOG.md) from a fresh research pass on LLM persona authoring. Subject
provenance added to sources.md in two new sections.

Verification: trigger eval, 12 queries x 3 runs, 12/12 pass — 1.00 on
should-trigger queries, 0.00 on near-misses. Near-misses were chosen to
compete with existing skills (a code-review system prompt, de-AI-ing a
README, a novel-dialogue request), so the separation is real rather than an
artifact of easy negatives. The A/B eval was not run: the desk-check plus a
clean trigger result was judged sufficient for a first version, and grading
persona output quality against a no-skill baseline needs a human reader on
voice, which the script cannot supply.

Desk-check caught three places the draft permitted a wrong path, all fixed:
the collect-lines step did not say who drafts the lines (an agent would have
asked the user for fifteen lines); the permission step had no skip path for
voices that need no grant; and the spec template offered "never break
character" as an option, which conflicts with the standing scene-break cases.

Fed back into this skill: the "elaborate personas" old-pattern line in
authoring-standards.md now distinguishes personas as a task-performance trick
(still deprecated) from personas where the voice is the deliverable (a real
technique, now covered by persona-creator). Without the split the two
artifacts contradicted each other.

Notable evidence findings recorded in sources.md: the widely repeated
"persona collapses within eight rounds" result is from 2024-era models and
current measurement finds short dialogues near-stable; Anthropic's
in-character docs page still sits inside "Increase output consistency" and
the prefill technique community guides recommend for holding a role is
unsupported on Claude 4.6+; and no study was found comparing trait
descriptions against dialogue exemplars for persona fidelity, so that
recommendation is labeled as practice rather than a measured effect.
