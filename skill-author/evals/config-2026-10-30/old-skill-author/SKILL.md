---
name: skill-author-old
description: >-
  Creates, evaluates, and updates Claude Code skills — SKILL.md directories
  that load on demand — keeping a sources ledger, an evidence bar, a
  per-skill changelog, and trigger and A/B eval scripts. Use when the user
  asks to make, write, add, fix, or update a skill; reports that an existing
  skill misbehaves or picks a bad default; wants a repeatable workflow or
  procedure captured so a future session runs it; asks why a skill does not
  trigger or triggers too often; wants a skill tuned, tested, or measured
  against a baseline; or asks to refresh or audit existing skills against
  current best practices. Also answers whether guidance should be a skill or
  a rule. Triggers include "make a skill for", "turn this into a skill",
  "update the X skill", "the X skill keeps doing Y", "why doesn't my skill
  fire", "test whether this skill helps", and "update all the skills". For an
  always-loaded rule (CLAUDE.md, .claude/rules/), use rule-author; for a
  subagent, agent-author; for a durable fact or write-up, notes.
argument-hint: "[create <topic> | update <skill> | update all]"
metadata:
  export: portable
  last-verified: "2026-10-28"
---

# Skill Creator

This skill produces and maintains one artifact kind: the **skill** — a
directory `<name>/SKILL.md` plus optional `references/` and `scripts/`.
Personal skills live in `~/.claude/skills/`, project skills in
`.claude/skills/`. Only the name and description (plus `when_to_use`, if set)
load at startup; the body loads when a task matches or the user types
`/<name>` (the command comes from the directory name), and it then stays in
context for the rest of the session. A skill therefore fails in two places:
the description that decides whether it loads, and the body that decides what
it changes once loaded.

Its ledger, evaluation method, eval scripts, prose standards, and the
skill-vs-rule decision framework are shared with the `rule-author` skill and
live in `~/.claude/skills/skill-rule-shared/`, called the shared directory
below.

Out of scope — redirect rather than force a skill:

- A convention, prohibition, or standing constraint that must hold in every
  session, including sessions where nothing would trigger a skill → that is a
  rule; invoke `rule-author`. When the request could be either, apply the
  [decision framework](~/.claude/skills/skill-rule-shared/skill-vs-rule.md)
  first and say which property decided it.
- A specialized worker with its own context → a subagent; `agent-author`.
- "Remember X" for a personal or one-project fact → auto memory already covers
  it.
- Behavior that must fire at a fixed lifecycle point → a hook in
  settings.json; a skill can state the policy but cannot enforce timing.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 0. Observe first: run three real prompts without the skill; record the failures
- [ ] 1. Classify the request
- [ ] 2. Research current guidance, scoped to what the pass needs
- [ ] 3. Confirm a skill is the right mechanism, and say why
- [ ] 4. Draft or revise the skill
- [ ] 5a. Desk-check against 2–3 evaluation scenarios
- [ ] 5b. Measure: trigger eval for every description change, A/B against a baseline for user-wide skills — or state the skip reason
- [ ] 6. Record dates and changelog
- [ ] 7. Self-maintenance pass on this skill and the shared files
```

For a pure choice question ("should this be a skill or a rule?"), run steps
1–3 only and answer with reasons; create nothing unless asked.

### 0. Observe first

Before you research or draft, see the failure the skill is meant to fix. For
a new skill, run three realistic prompts in a fresh session without it, or
read three real past transcripts of the task, and write down what went
wrong (in the desktop app, `list_events` renders user turns, assistant
text, and tool-call names only; tool arguments and results are in the raw
transcript under `~/.claude/projects/<cwd-slug>/<session>.jsonl`): the missing step, the wrong default, the question the user had to
answer twice. Those failures are the eval set for step 5 (three is its
working minimum) and the reason the skill exists. If nothing fails, say so
and ask whether the skill is still wanted — the vendor's own guidance is that
Claude writes well-formed skills unaided, so a skill has to earn its place by
fixing something observed. For an update prompted by an observed failure,
the failure is the observation; record it in the changelog with the session
or transcript it came from.

### 1. Classify

- **Create**: "make a skill for X" → full workflow.
- **Update**: "update <skill>" or "update all the skills" → find the skills
  in the locations listed above, then follow the Updating section. For
  "update all", enumerate every `SKILL.md` in both the personal and project
  locations before starting, and report the list so nothing is silently
  skipped. If the request also names rules ("update all the skills and
  rules"), invoke `rule-author` for that half and report both lists.
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

1. Read the entries in the shared
   [sources.md](~/.claude/skills/skill-rule-shared/sources.md) that concern
   the pass: the core-source entries named in step 7 for any skill work, plus
   the skill's own subject section (the Contents list names the sections).
   Reading the whole file is not required. Re-read an entry immediately
   before you edit it: another session may have written to the file in
   between, and an edit built on a stale read discards their work.
2. Re-fetch the tier-1 sources relevant to the request — the skill-authoring
   best-practices page and the Claude Code skills doc for skill work — and
   search the web for changes since the oldest relevant last-verified date.
3. Rank evidence: (1) Anthropic docs and engineering posts, (2) research
   papers and empirical studies, (3) community findings. Use tier 3 only when
   corroborated by tier 1–2, or explicitly labeled as unverified community
   practice.
4. Every entry records the models or vintage a finding was measured on. Carry
   that qualifier into the skill; a claim that drops it is the most common
   error the ledger has recorded.
5. Provenance lives in the shared `sources.md`, not in the user's notes vault
   (`~/projects/ai/notes`, a 2026-08-15 snapshot these skills do not update). Write to
   the vault only when the user asks for a note, via the notes skill.

### 3. Confirm the mechanism

Apply the shared
[decision framework](~/.claude/skills/skill-rule-shared/skill-vs-rule.md).
Three cases:

- User didn't specify → decide, then state the choice and the deciding
  property in one or two sentences. If it is a rule, hand the request to
  `rule-author`.
- User asked for a skill and the framework agrees → proceed without
  commentary.
- User asked for a skill and the framework disagrees → recommend a rule with
  one or two concrete reasons ("this is one prohibition; nothing matches it
  until it is already being violated, so it has to be loaded every session"),
  then follow whichever the user picks.

### 4. Draft

Read [references/skill-standards.md](references/skill-standards.md) — the
frontmatter, body, and script rules — and the shared
[guidance-style.md](~/.claude/skills/skill-rule-shared/guidance-style.md) —
prose style and deprecated patterns — before writing. Three rules bear
repeating because they are easy to miss:

- Produced skills carry no citations or source URLs. Provenance lives in the
  shared ledger, so the skills stay clean and cheap.
- Every skill gets a verification marker: `metadata: {last-verified:
  "YYYY-MM-DD"}` in frontmatter.
- The description is the only text that decides whether the body ever loads:
  third person, what the skill does and when, the phrases users actually
  type, key use case first. Name where near-miss requests go instead.

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
rewrote a description. Skip it only for a wording fix, and write the skip
and its reason in the changelog entry — an unstated skip reads as a run. Read the shared
[evaluating.md](~/.claude/skills/skill-rule-shared/evaluating.md) for the
method, the eval set format, the confounds to record, and the two scripts in
`~/.claude/skills/skill-rule-shared/scripts/`:

- `trigger_eval.py` measures how often the skill actually loads, across
  should-trigger prompts and near-misses. Run it for every description
  change.
- `ab_eval.py --mode skill` runs task prompts with and without the skill,
  three runs per arm, and saves outputs, transcripts, cost, the Claude Code
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
  numbers, the model, and the Claude Code version.

### 7. Self-maintain

Every pass ends by turning the findings on this skill itself:

- If research contradicted or extended anything this skill, its standards
  file, or a shared file says, update them in the same pass, subject to the
  same evidence bar. A change to a shared file is logged in this skill's
  changelog and named as shared, so rule-author's next pass sees it.
- A claim about model behavior — a rate, a tendency, an effect — observed
  in this pass on one query, one session, or fewer than ten runs goes into
  the CHANGELOG as a watch item, never into a standards file or
  evaluating.md. Promote it only when a later pass finds it clears the
  evidence bar (tier 1–2 support, or a measured effect across a real eval
  set). A method trap whose mechanism is understood — an eval that measured
  nothing because of how it was built — may go into evaluating.md at once,
  dated.
- Refresh last-verified dates in the shared `sources.md` for each source
  actually re-checked, and this skill's own `metadata.last-verified` when
  the pass verified its core sources: the skill-authoring best-practices
  page, the Claude Code skills doc, and the prompting best-practices page.
  A pass that touches the shared decision framework re-reads the memory doc
  as well.
- Log the pass in `${CLAUDE_SKILL_DIR}/CHANGELOG.md`.

## Updating

An update is a check against evidence, not a rewrite:

1. Name what prompted it: an observed failure (step 0 — record the session),
   a guidance refresh (run step 2, scoped to the skill's subject), or a
   feature request or wording fix that does not touch guidance (step 2
   exempt; say so).
2. Diff current guidance, or the observed failure, against the skill.
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
