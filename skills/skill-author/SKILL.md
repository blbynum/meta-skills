---
name: skill-author
description: >-
  Creates, evaluates, migrates, and updates skills — SKILL.md directories
  under the Agent Skills standard. Use when the user asks to make, write,
  add, fix, or update a skill; to migrate a skill or make it shareable so
  it runs on another machine or harness; reports that a skill misbehaves
  or picks a bad default; wants a repeatable workflow captured for future
  sessions; asks why a skill does not trigger or triggers too often; wants
  a skill tested or measured against a baseline; or asks to refresh or
  audit skills against current best practices. Also answers whether
  guidance should be a skill or a rule. Triggers include "make a skill
  for", "turn this into a skill", "update the X skill", "migrate the X
  skill", "make X shareable", "the X skill keeps doing Y", "why doesn't my
  skill fire", "test whether this skill helps", and "update all the
  skills". Not for an always-loaded rule (CLAUDE.md, .claude/rules/), a
  subagent, or a durable fact or write-up.
compatibility: Measurement needs Python 3.10 or later and a non-interactive runner for the harness; without one, the skill records that it did not measure.
metadata:
  harness: portable
  last-verified: "2026-10-31"
---

# Skill Creator

This skill produces and maintains one artifact kind: the **skill** — a
directory `<name>/SKILL.md` plus optional `references/` and `scripts/`,
under the Agent Skills standard that Claude Code, Cursor, Codex, and other
harnesses read. Only the name and description load at startup; the body
loads when a task matches or the user invokes the skill by name, and it
then stays in context for the rest of the session. A skill therefore fails
in two places: the description that decides whether it loads, and the body
that decides what it changes once loaded.

## Config

| Key | Required | Default | Purpose |
|---|---|---|---|
| skills-dir | yes | | directory that holds the personal skills on this machine |
| rule-skill | no | | skill that writes always-loaded rules; when unset, say the request needs a rule and stop |

Read `config.local.yaml` in this skill's directory before anything else.
A key missing there takes its Default from the table. If a required key is
missing or empty, stop: name the key and its purpose, and offer to write
`config.local.yaml` with the values the user gives. If a configured
directory does not exist, stop and say so; do not create it.

The shared directory is `<skills-dir>/skill-rule-shared/`. Its ledger,
evaluation method, eval scripts, prose standards, and the skill-vs-rule
decision framework are shared with the configured rule skill
(`rule-skill`). Before step
0, read the reference for the harness you run in, `references/<harness-id>.md`;
[references/claude-code.md](references/claude-code.md) exists and says
where skills and transcripts live there, which frontmatter extensions
exist, and how to run the measurement scripts. For a harness with no
reference file, read its skills documentation first and add the file in
step 7.

Out of scope — redirect rather than force a skill:

- A convention, prohibition, or standing constraint that must hold in every
  session, including sessions where nothing would trigger a skill → that is a
  rule; hand it to the configured rule skill (`rule-skill`), or, when none
  is set, say the request needs a rule and stop. When the request could be
  either, apply the
  [decision framework](../skill-rule-shared/skill-vs-rule.md)
  first and say which property decided it.
- A specialized worker with its own context → a subagent, not a skill.
- "Remember X" for a personal or one-project fact → the harness's own
  memory feature already covers it, where one exists.
- Behavior that must fire at a fixed lifecycle point → a lifecycle hook,
  where the harness has them; a skill can state the policy but cannot
  enforce timing.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 0. Observe first: run three real prompts without the skill; record the failures
- [ ] 1. Classify the request
- [ ] 2. Research current guidance, scoped to what the pass needs
- [ ] 3. Confirm a skill is the right mechanism, decide its kind, and say why
- [ ] 4. Draft or revise the skill
- [ ] 5a. Desk-check against 2–3 evaluation scenarios
- [ ] 5b. Measure where a runner exists: trigger eval for every description change, A/B against a baseline for user-wide skills — or state the skip reason
- [ ] 6. Record dates and changelog
- [ ] 7. Self-maintenance pass on this skill and the shared files
```

For a pure choice question ("should this be a skill or a rule?"), run steps
1–3 only and answer with reasons; create nothing unless asked.

### 0. Observe first

Before you research or draft, see the failure the skill is meant to fix. For
a new skill, run three realistic prompts in a fresh session without it, or
read three real past transcripts of the task, and write down what went
wrong (a harness reference, where one exists, says where raw transcripts
live and what the harness's own event view leaves out): the missing step, the wrong default,
the question the user had to answer twice. Those failures are the eval set
for step 5 (three is its working minimum) and the reason the skill exists.
If nothing fails, say so and ask whether the skill is still wanted — the
vendor's own guidance is that Claude writes well-formed skills unaided, so a
skill has to earn its place by fixing something observed. For an update
prompted by an observed failure, the failure is the observation; record it
in the changelog with the session or transcript it came from.

### 1. Classify

- **Create**: "make a skill for X" → full workflow.
- **Update**: "update <skill>" or "update all the skills" → find the skills
  under `skills-dir` and in the project's skills directory, then follow the
  Updating section. For "update all", enumerate every `SKILL.md` in both
  locations before starting, and report the list so nothing is silently
  skipped. If the request also names rules ("update all the skills and
  rules"), hand that half to the configured rule skill (`rule-skill`) and
  report both lists; when none is set, say the rules half is not covered.
- **Migrate**: "migrate <skill>", "make <skill> shareable", or a path to a
  skill in any repository → the Migrating section.
- **Choice question** → decision framework only, as above.

### 2. Research

Research is a fact-currency control, not the first step of every pass. Run
it when the pass writes or refreshes guidance that depends on model or
platform behavior, and whenever the skill will state a load-bearing fact —
a rate, a version, a flag, a limit, a quoted rule — which must be checked
against its primary source before it is written. Skip it, and say which
exemption applies in the changelog, for a feature request that adds
capability without touching guidance, a wording fix, or same-day reuse of
sources already read in this pass. Trained knowledge and this skill's own
text both go stale; the ledger exists to catch that.

1. Read the ledger entries that concern the pass: the core-source entries
   named in step 7, in the shared
   [sources.md](../skill-rule-shared/sources.md), plus the skill's own
   subject entries — in its own `sources.md` beside its SKILL.md, or in
   the shared file for a skill that lives beside this one. Reading a whole
   ledger is not required. Re-read an entry immediately before you edit
   it: another session may have written to the file in between, and an edit
   built on a stale read discards their work.
2. Re-fetch the tier-1 sources relevant to the request — the skill-authoring
   best-practices page, the Agent Skills specification, and the harness's
   skills doc for skill work — and search the web for changes since the
   oldest relevant last-verified date.
3. Rank evidence: (1) Anthropic docs and engineering posts, (2) research
   papers and empirical studies, (3) community findings. Use tier 3 only when
   corroborated by tier 1–2, or explicitly labeled as unverified community
   practice.
4. Every entry records the models or vintage a finding was measured on. Carry
   that qualifier into the skill; a claim that drops it is the most common
   error the ledger has recorded.
5. Provenance lives in a ledger, not in the user's notes: the shared
   `sources.md` for the authoring sources, the skill's own `sources.md`
   (never linked from its SKILL.md) for its subject matter.
   Write a note only when the user asks for one, through whatever notes
   skill the user has.

### 3. Confirm the mechanism

Apply the shared
[decision framework](../skill-rule-shared/skill-vs-rule.md).
Three cases:

- User didn't specify → decide, then state the choice and the deciding
  property in one or two sentences. If it is a rule, hand the request to
  the configured rule skill (`rule-skill`), or say a rule is needed when
  none is set.
- User asked for a skill and the framework agrees → proceed without
  commentary.
- User asked for a skill and the framework disagrees → recommend a rule with
  one or two concrete reasons ("this is one prohibition; nothing matches it
  until it is already being violated, so it has to be loaded every session"),
  then follow whichever the user picks.

Then decide the skill's **kind**, and state it with the reason. A skill is
either portable, `metadata: {harness: portable}`, or harness-specific,
`metadata: {harness: <harness-id>}`; every skill declares one. The subject
decides: a skill about one harness's own artifacts, or one that needs that
harness's command-line tool to do its job, is harness-specific; everything
else is portable. When the user named a kind, use it. When a feature of
one harness would make a portable skill do its job better, say so and let
the user choose the kind; never leave the feature out silently and never
neutralize a harness-specific skill.

### 4. Draft

Read [references/skill-standards.md](references/skill-standards.md) — the
frontmatter, body, script, configuration, and portability rules — and the
shared [guidance-style.md](../skill-rule-shared/guidance-style.md) — prose
style and deprecated patterns — before writing. Five rules bear repeating
because they are easy to miss:

- Produced skills carry no citations or source URLs. Provenance lives in the
  shared ledger, so the skills stay clean and cheap.
- Every skill gets a verification marker: `metadata: {last-verified:
  "YYYY-MM-DD"}` in frontmatter.
- The description is the only text that decides whether the body ever loads:
  third person, what the skill does and when, the phrases users actually
  type, key use case first. Name where near-miss requests go instead.
- Parameterize only what varies. A path outside the skill and the project,
  a companion skill, or a vendor or account choice becomes a key in a
  `## Config` table with the user's value in `config.local.yaml`, per
  [references/skill-config.md](references/skill-config.md); an
  operating-system tool choice, a project-relative path, or a preference
  nobody asked to change does not. When nothing varies, the skill has no
  Config section and the report says so in one line.
- Write for its kind. A portable skill uses spec-only frontmatter, names
  actions instead of tools, carries no harness-only syntax, and puts
  harness facts in `references/<harness-id>.md`. A harness-specific skill
  uses that harness's features in full. Both are written to do their job
  as well as the standards allow; the kind changes where facts live, not
  how good the skill is. The check that a portable skill is portable is in
  [references/skill-config.md](references/skill-config.md).

### 5. Test

**5a. Desk-check (always).** Write 2–3 evaluation scenarios: realistic prompts
the skill should handle, each with the expected behavior. Re-read the skill
with fresh eyes and walk each scenario through it; wherever the text permits
a wrong path, fix the text, not the scenario. Report the scenarios and
outcomes to the user; keep them out of the skill itself.

**5b. Measure.** A desk-check shows the text is clear to a reader who already
knows what it means. It cannot show that the skill loads when it should, or
that the body changes what the model does — for that, a fresh session has to
run it against a no-skill baseline, on the failures step 0 recorded.

5b is required for every user-wide skill and whenever this pass wrote or
rewrote a description, wherever a non-interactive runner exists; the
harness reference says whether one does and how to use it. In a harness
with no runner, desk-check and record "not measured: no runner in
<harness>" in the changelog. Skip it otherwise only for a wording fix, and
write the skip and its reason in the changelog entry — an unstated skip
reads as a run. Read the shared
[evaluating.md](../skill-rule-shared/evaluating.md) for the method, the
eval set formats, the confounds to record, and the two scripts in the
shared directory's `scripts/`:

- `trigger_eval.py` measures how often the skill actually loads, across
  should-trigger prompts and near-misses. Run it for every description
  change.
- `ab_eval.py --mode skill` runs task prompts with and without the skill,
  three runs per arm, and saves outputs, transcripts, cost, the harness
  version, and the resolved model.

Grade the outputs yourself; the scripts deliberately stop at collecting them.
Report the comparison including cost, and say plainly when the arms are too
close to call rather than reading a win into noise.

### 6. Record

- Set or refresh the skill's `metadata.last-verified`.
- Every skill keeps a `CHANGELOG.md` in its directory: create it on first
  touch and append a dated entry each pass.
- "Checked, no change" entries count as entries — future runs use them to
  decide what needs re-verification.
- Name the check honestly. A step-5a walk-through is "desk-checked against N
  scenarios". Write "tested" or "measured" only when 5b ran, and give the
  numbers, the model, and the harness version.

### 7. Self-maintain

Every pass ends by turning the findings on this skill itself:

- If research contradicted or extended anything this skill, its standards
  file, or a shared file says, update them in the same pass, subject to the
  same evidence bar. A change to a shared file is logged in this skill's
  changelog and named as shared, so the rule skill's next pass sees it.
- A claim about model behavior — a rate, a tendency, an effect — observed
  in this pass on one query, one session, or fewer than ten runs goes into
  the CHANGELOG as a watch item, never into a standards file or
  evaluating.md. Promote it only when a later pass finds it clears the
  evidence bar (tier 1–2 support, or a measured effect across a real eval
  set). A method trap whose mechanism is understood — an eval that measured
  nothing because of how it was built — may go into evaluating.md at once,
  dated.
- Refresh last-verified dates in the ledger that holds each source
  actually re-checked, and this skill's own `metadata.last-verified` when
  the pass verified its core sources: the skill-authoring best-practices
  page, the Agent Skills specification, the harness's skills doc, and the
  prompting best-practices page. A pass that touches the shared decision
  framework re-reads the memory doc as well.
- Log the pass in this skill's `CHANGELOG.md`.

## Updating

An update is a check against evidence, not a rewrite:

1. Name what prompted it: an observed failure (step 0 — record the session),
   a guidance refresh (run step 2, scoped to the skill's subject), or a
   feature request or wording fix that does not touch guidance (step 2
   exempt; say so).
2. Diff current guidance, or the observed failure, against the skill, and
   read its body for values that belong in config: an absolute path
   outside the project, a companion skill named in prose, an account or
   vendor. Each one is a candidate key per
   [references/skill-config.md](references/skill-config.md); a value that
   no second environment would change stays in the body.
3. Apply the **evidence bar**: change the skill only when the latest
   evidence indicates the change would improve output, or when a
   not-yet-incorporated strategy or tool is clearly established — tier 1–2
   support, or wide and verified community adoption. Novelty alone never
   clears the bar.
4. Below the bar → report "no change needed" with reasons: what was checked,
   what was found, why it didn't clear. Still refresh the last-verified
   marker and changelog so the check is on record.
5. At or above the bar → apply the smallest change that incorporates the
   evidence, re-test (workflow step 5), and record.

## Migrating

A Migrate request first decides the skill's kind, as step 3 does, then
moves its machine-specific values into config and, for a portable skill,
moves its harness facts into harness references and passes the
portability check, so the skill runs as written on another machine or
harness and in someone else's hands. Follow "Migrating an existing skill"
in [references/skill-config.md](references/skill-config.md).
Values move automatically and the author's machine keeps working, because
today's values go into `config.local.yaml`. A hand-off to another skill
changes behavior, so it is proposed in the report and applied on the
user's yes. Checks: desk-check; the trigger eval where a runner exists,
when the description changed; one run of the migrated skill to confirm it
used a value from `config.local.yaml`, when a value moved; the A/B only
when behavior was rewritten. A skill with nothing to move is already
portable: report "no config keys" and record the skipped checks with that
reason. Record the pass in the migrated skill's changelog.
