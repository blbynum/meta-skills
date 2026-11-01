---
name: rule-author-old
description: >-
  Creates, evaluates, and updates Claude Code rules — the always-loaded
  instructions in CLAUDE.md, ~/.claude/rules/, and .claude/rules/, including
  paths-scoped rules — keeping a sources ledger, an evidence bar for every
  change, a budget check on the always-loaded total, a contradiction check,
  and a rule A/B eval. Use when the user asks to add, write, change, or
  remove a rule; wants a convention, prohibition, preference, or standing
  constraint to hold in every session; asks to add something to CLAUDE.md or
  a rules file; asks why Claude ignores a rule; or asks to refresh,
  re-verify, or audit existing rules against current best practices. Also
  answers whether guidance should be a rule or a skill. Triggers include "add
  a rule", "make it a rule that", "put this in CLAUDE.md", "add to my rules",
  "why isn't my rule followed", and "update all the rules". For an on-demand
  skill (a SKILL.md directory), use skill-creator; for behavior at a fixed
  lifecycle point, a hook; for "remember X", auto memory.
argument-hint: "[create <topic> | update <rule> | update all]"
metadata:
  export: portable
  last-verified: "2026-08-18"
---

# Rule Creator

This skill produces and maintains one artifact kind: the **rule** — an
always-loaded instruction. It is an entry in CLAUDE.md (`~/.claude/CLAUDE.md`
user-wide; `./CLAUDE.md` or `./.claude/CLAUDE.md` project; `./CLAUDE.local.md`
personal and gitignored for one project) or a topic file in `.claude/rules/`
(project) or `~/.claude/rules/` (user). Everything unscoped loads at the
start of every session and is delivered as context, not enforced; a rules
file with `paths:` frontmatter loads only when Claude works with matching
files. A rule therefore fails in three places: the always-loaded total that
its lines add to, conflicts with other loaded rules, and the gap between
stating a policy and enforcing it.

Its ledger, evaluation method, eval scripts, prose standards, and the
skill-vs-rule decision framework are shared with the `skill-creator` skill and
live in `~/.claude/skills/skill-rule-shared/`, called the shared directory
below.

Out of scope — redirect rather than force a rule:

- A multi-step workflow, procedure, domain reference, or anything with
  scripts or supporting files → that is a skill; invoke `skill-creator`. When
  the request could be either, apply the
  [decision framework](~/.claude/skills/skill-rule-shared/skill-vs-rule.md)
  first and say which property decided it.
- "Remember X" for a personal or one-project fact → auto memory already covers
  it; offer a rule only if the user wants a durable instruction.
- Behavior that must fire at a fixed lifecycle point (before every commit,
  after each edit) → that requires a hook in settings.json. A rule can state
  the policy but cannot enforce timing; say so and point to hook
  configuration.
- A pure tool prohibition that a `permissions.deny` entry covers exactly →
  offer the deny rule first; it is enforced and costs no context. A rule
  earns its place only when it also says what to do instead.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 0. Observe first: run three real prompts without the rule; record the failures
- [ ] 1. Classify the request
- [ ] 2. Research current guidance, scoped to what the pass needs
- [ ] 3. Confirm a rule is the right mechanism, and say why
- [ ] 4. Draft or revise the rule; check the always-loaded budget and contradictions
- [ ] 5a. Desk-check against 2–3 evaluation scenarios
- [ ] 5b. Measure against a no-rule baseline (required for user-wide rules), or state the skip reason
- [ ] 6. Record dates and changelog
- [ ] 7. Self-maintenance pass on this skill and the shared files
```

For a pure choice question ("should this be a skill or a rule?"), run steps
1–3 only and answer with reasons; create nothing unless asked.

### 0. Observe first

Before you research or draft, see the failure the rule is meant to fix. For
a new rule, run three realistic prompts in a fresh session without it, or
read three real past transcripts of the behavior, and write down what went
wrong: the wrong default, the step skipped, the correction the user had to
type twice. Those failures are the eval set for step 5 (three is its working
minimum) and the reason the rule exists. If nothing fails, say so and ask
whether the rule is still wanted — every rule line taxes every session, so
a rule has to earn its place by fixing something observed. For an update
prompted by an observed failure, the failure is the observation; record it
in the changelog with the session or transcript it came from.

### 1. Classify

- **Create**: "add a rule for X" → full workflow.
- **Update**: "update <rule>" or "update all the rules" → find the rules in
  the locations listed above, then follow the Updating section. For "update
  all", enumerate every rules file and every CLAUDE.md in both the personal
  and project locations before starting, and report the list so nothing is
  silently skipped. If the request also names skills ("update all the
  skills and rules"), invoke `skill-creator` for that half and report both
  lists.
- **Choice question** → decision framework only, as above.

### 2. Research

Research is a fact-currency control, not the first step of every pass. Run
it when the pass writes or refreshes guidance that depends on model or
platform behavior, and whenever the rule will state a load-bearing fact — a
rate, a version, a flag, a limit, a quoted rule — which must be checked
against its primary source before it is written. Skip it, and say which
exemption applies in the changelog, for a feature request that adds
capability without touching guidance, a wording fix, or same-day reuse of
sources already read in this pass. Trained knowledge and this skill's own
text both go stale; the ledger exists to catch that.

1. Read the entries in the shared
   [sources.md](~/.claude/skills/skill-rule-shared/sources.md) that concern
   the pass: the core-source entries named in step 7 for any rule work, plus
   the rule's own subject section (the Contents list names the sections).
   Reading the whole file is not required. Re-read an entry immediately
   before you edit it: another session may have written to the file in
   between, and an edit built on a stale read discards their work.
2. Re-fetch the tier-1 sources relevant to the request — the Claude Code
   memory doc for rule work, and the permissions doc when the rule needs an
   enforcement layer — and search the web for changes since the oldest
   relevant last-verified date.
3. Rank evidence: (1) Anthropic docs and engineering posts, (2) research
   papers and empirical studies, (3) community findings. Use tier 3 only when
   corroborated by tier 1–2, or explicitly labeled as unverified community
   practice.
4. Every entry records the models or vintage a finding was measured on. Carry
   that qualifier into the rule; a claim that drops it is the most common
   error the ledger has recorded.
5. Provenance lives in the shared `sources.md`, not in the user's notes vault
   (`~/ai/notes`, a 2026-08-15 snapshot these skills do not update). Write to
   the vault only when the user asks for a note, via the notes skill.

### 3. Confirm the mechanism

Apply the shared
[decision framework](~/.claude/skills/skill-rule-shared/skill-vs-rule.md).
Three cases:

- User didn't specify → decide, then state the choice and the deciding
  property in one or two sentences. If it is a skill, hand the request to
  `skill-creator`.
- User asked for a rule and the framework agrees → proceed without
  commentary.
- User asked for a rule and the framework disagrees → recommend a skill with
  one or two concrete reasons ("this is forty lines of procedure used in
  maybe one session in ten; as a rule it taxes every session"), then follow
  whichever the user picks.

### 4. Draft

Read [references/rule-standards.md](references/rule-standards.md) — the
format and budget rules — and the shared
[guidance-style.md](~/.claude/skills/skill-rule-shared/guidance-style.md) —
prose style and deprecated patterns — before writing. Three rules bear
repeating because they are easy to miss:

- Produced rules carry no citations or source URLs. Provenance lives in the
  shared ledger, so the rules stay clean and cheap.
- Every rule gets a verification marker: a `<!-- last-verified: YYYY-MM-DD -->`
  comment, which is stripped before context injection and therefore costs
  nothing.
- Rules are imperative and concrete: "Use X", never "we generally prefer X
  when possible".

Two checks belong to this step, not to testing, because their result changes
what you write:

- **Budget.** Sum everything that loads unscoped — user CLAUDE.md, project
  CLAUDE.md, both rules directories — and report the total with the new
  lines added. When the total creeps up, scope with `paths:` or demote
  procedures to skills; splitting files does not reduce the cost.
- **Contradictions.** Read the whole always-loaded set and list every pair
  the new rule could conflict with, then say for each why it does not, or
  change one side. Conflicting rules get arbitrary compliance.

### 5. Test

**5a. Desk-check (always).** Write 2–3 evaluation scenarios: realistic prompts
in which the rule should change behavior, each with the expected behavior,
including one scenario for the opposite failure — the behavior the rule
would produce if over-applied. Re-read the rule with fresh eyes and walk each
scenario through it; wherever the text permits a wrong path, fix the text,
not the scenario. Report the scenarios and outcomes to the user; keep them
out of the rule itself.

**5b. Measure.** A desk-check shows the text is clear to a reader who already
knows what it means. It cannot show that the rule changes what the model
does — for that, a fresh session has to run it against a no-rule baseline,
on the failures step 0 recorded.

5b is required for every user-wide rule. Skip it only for a wording fix or a
single-project rule, and write the skip and its reason in the changelog
entry — an unstated skip reads as a run. Read the shared
[evaluating.md](~/.claude/skills/skill-rule-shared/evaluating.md) for the
method, the eval set format, the confounds to record, and the script in
`~/.claude/skills/skill-rule-shared/scripts/`:

- `ab_eval.py --mode rule --rule-file <path>` runs task prompts with and
  without the rule, three runs per arm, and saves outputs, transcripts, cost,
  the Claude Code version, and the resolved model. Rule mode approximates
  delivery: it injects the rule as system-prompt text, while a real rule
  arrives as a user-turn reminder alongside every other loaded rule, so a
  rule that competes with other loaded rules looks better here than in
  practice. Phrase rule-mode queries as the bare task.
- There is no trigger eval for a rule: an unscoped rule loads every session.
  A `paths:` rule does have a loading condition; check it by hand once per
  `paths:` edit, as evaluating.md describes.

Grade the outputs yourself; the script deliberately stops at collecting them.
Report the comparison including cost, and say plainly when the arms are too
close to call rather than reading a win into noise.

### 6. Record

- Set or refresh the rule's last-verified comment.
- Rules stay lean: they carry no changelog of their own. Record the pass —
  what was checked, changed, or left as is, and the 5b result or skip — in
  `${CLAUDE_SKILL_DIR}/CHANGELOG.md`.
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
  changelog and named as shared, so skill-creator's next pass sees it.
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
  the pass verified its core sources: the Claude Code memory doc, the
  permissions doc, and the prompting best-practices page. A pass that
  touches the shared decision framework re-reads the Claude Code skills doc
  as well.
- Log the pass in `${CLAUDE_SKILL_DIR}/CHANGELOG.md`.

## Updating

An update is a check against evidence, not a rewrite:

1. Name what prompted it: an observed failure (step 0 — record the session),
   a guidance refresh (run step 2, scoped to the rule's subject), or a
   feature request or wording fix that does not touch guidance (step 2
   exempt; say so).
2. Diff current guidance, or the observed failure, against the rule.
3. Apply the **evidence bar**: change the rule only when the latest evidence
   indicates the change would improve output, or when a not-yet-incorporated
   strategy or tool is clearly established — tier 1–2 support, or wide and
   verified community adoption. Novelty alone never clears the bar.
4. Below the bar → report "no change needed" with reasons: what was checked,
   what was found, why it didn't clear. Still refresh the last-verified
   marker and changelog so the check is on record.
5. At or above the bar → apply the smallest change that incorporates the
   evidence, re-test (workflow step 5), and record.
