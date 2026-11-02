---
name: rule-author
description: >-
  Creates, evaluates, and updates rules — the always-loaded instruction
  files an agent harness reads every session, such as CLAUDE.md, AGENTS.md,
  GEMINI.md, .cursor/rules, or .claude/rules, including file-scoped rules —
  keeping a sources ledger, an evidence bar for every change, a budget
  check on the always-loaded total, a contradiction check, and a rule A/B
  eval. Use when the user asks to add, write, change, or remove a rule;
  wants a convention, prohibition, preference, or standing constraint to
  hold in every session; asks to add something to CLAUDE.md, AGENTS.md, or
  a rules file; asks why the agent ignores a rule; or asks to refresh,
  re-verify, or audit existing rules against current best practices. Also
  answers whether guidance should be a rule or a skill. Triggers include
  "add a rule", "make it a rule that", "put this in CLAUDE.md", "add to my
  rules", "why isn't my rule followed", and "update all the rules". Not
  for an on-demand skill (a SKILL.md directory), for behavior at a fixed
  lifecycle point (a hook), or for "remember X" (the harness's own
  memory).
compatibility: Measurement needs Python 3.10 or later and a non-interactive runner for the harness; without one, the skill records that it did not measure.
metadata:
  harness: portable
  last-verified: "2026-10-31"
---

# Rule Author

This skill produces and maintains one artifact kind: the **rule** — an
always-loaded instruction. Every agent harness reads a set of instruction
files at the start of every session and delivers them as context, not as
enforcement; most also offer a way to scope a file to matching paths so it
loads only when the agent works there. Which files, where they live, how
they scope, and in what order they load differ by harness: before step
1, read the reference for the harness you run in, `references/<harness-id>.md`
([claude-code](references/claude-code.md), [cursor](references/cursor.md),
[codex](references/codex.md), [copilot](references/copilot.md),
[antigravity](references/antigravity.md), [gemini-cli](references/gemini-cli.md)). A rule therefore fails in three places: the
always-loaded total that its lines add to, conflicts with other loaded
rules, and the gap between stating a policy and enforcing it.

Its ledger, evaluation method, eval scripts, prose standards, and the
skill-vs-rule decision framework live in `skill-rule-shared/`, the
directory beside this skill's directory, called the shared directory
below; links to it are relative.

Out of scope — redirect rather than force a rule:

- A multi-step workflow, procedure, domain reference, or anything with
  scripts or supporting files → that is a skill, not a rule; say so and
  stop. When
  the request could be either, apply the
  [decision framework](../skill-rule-shared/skill-vs-rule.md)
  first and say which property decided it.
- "Remember X" for a personal or one-project fact → the harness's own
  memory feature already covers it where one exists; offer a rule only if
  the user wants a durable instruction.
- Behavior that must fire at a fixed lifecycle point (before every commit,
  after each edit) → that requires a lifecycle hook, where the harness has
  them. A rule can state the policy but cannot enforce timing; say so and
  point to the hook mechanism the harness reference names.
- A pure tool prohibition that a tool permission rule covers exactly, where
  the harness has them → offer the permission rule first; it is enforced
  and costs no context. A rule earns its place only when it also says what
  to do instead.

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
- [ ] 6. Refresh dates, write the pass record, and delete the eval directory
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
prompted by an observed failure, the failure is the observation; put it
in the pass record (step 6) with the session or transcript it came from.

### 1. Classify

- **Create**: "add a rule for X" → full workflow.
- **Update**: "update <rule>" or "update all the rules" → find the rules in
  every file the harness loads, as the harness reference lists them, then
  follow the Updating section. For "update all", enumerate every rule file
  in both the personal and project locations before starting, and report
  the list so nothing is silently skipped. If the request also names
  skills ("update all the skills and rules"), do the rules half here,
  report its list, and say that the skills half is not this skill's work.
- **Choice question** → decision framework only, as above.

### 2. Research

Research is a fact-currency control, not the first step of every pass. Run
it when the pass writes or refreshes guidance that depends on model or
platform behavior, and whenever the rule will state a load-bearing fact — a
rate, a version, a flag, a limit, a quoted rule — which must be checked
against its primary source before it is written. Skip it, and say which
exemption applies in the pass record, for a feature request that adds
capability without touching guidance, a wording fix, or same-day reuse of
sources already read in this pass. Trained knowledge and this skill's own
text both go stale; the ledger exists to catch that.

1. Read the ledger entries that concern the pass: the core-source entries
   named in step 7, in the shared
   [sources.md](../skill-rule-shared/sources.md), plus the rule's own
   subject entries, which live in the shared file too (a rules directory
   cannot hold a ledger, because every file there loads as a rule).
   Reading the whole file is not required. Re-read an entry immediately
   before you edit it: another session may have written to the file in
   between, and an edit built on a stale read discards their work.
2. Re-fetch the tier-1 sources relevant to the request — the harness's
   documentation for its rule files, and its permissions documentation when
   the rule needs an enforcement layer, both named in the harness
   reference — and search the web for changes since the oldest relevant
   last-verified date.
3. Rank evidence: (1) the harness vendor's docs and engineering posts, (2)
   research papers and empirical studies, (3) community findings. Use tier
   3 only when corroborated by tier 1–2, or explicitly labeled as
   unverified community practice.
4. Every entry records the models or vintage a finding was measured on. Carry
   that qualifier into the rule; a claim that drops it is the most common
   error the ledger has recorded.
5. Provenance lives in the shared `sources.md`, not in the user's notes;
   a skill's subject matter lives in that skill's own `sources.md`.
   Write a note only when the user asks for one, through whatever notes
   skill the user has.

### 3. Confirm the mechanism

Apply the shared
[decision framework](../skill-rule-shared/skill-vs-rule.md).
Three cases:

- User didn't specify → decide, then state the choice and the deciding
  property in one or two sentences. If it is a skill, say so and stop.
- User asked for a rule and the framework agrees → proceed without
  commentary.
- User asked for a rule and the framework disagrees → recommend a skill with
  one or two concrete reasons ("this is forty lines of procedure used in
  maybe one session in ten; as a rule it taxes every session"), then follow
  whichever the user picks.

### 4. Draft

Read [references/rule-standards.md](references/rule-standards.md) — the
format and budget rules — and the shared
[guidance-style.md](../skill-rule-shared/guidance-style.md) —
prose style and deprecated patterns — before writing. Three rules bear
repeating because they are easy to miss:

- Produced rules carry no citations or source URLs. Provenance lives in the
  shared ledger, so the rules stay clean and cheap.
- Every rule gets a verification marker: a one-line
  `<!-- last-verified: YYYY-MM-DD -->` comment. Whether the harness strips
  it before injection is in the harness reference; one line costs little
  either way.
- Rules are imperative and concrete: "Use X", never "we generally prefer X
  when possible".

Two checks belong to this step, not to testing, because their result changes
what you write:

- **Budget.** Sum everything the harness loads unconditionally — every
  user-level and project-level rule file the harness reference lists — and
  report the total with the new lines added. When the total creeps up,
  scope the rule with the harness's file-scoping mechanism where it has
  one, or demote procedures to skills; splitting files does not reduce the
  cost.
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

5b is required for every user-wide rule, wherever a non-interactive runner
exists; the harness reference says whether one does and how the shared
script uses it. Without one, desk-check and record "not measured: no
runner in <harness>" in the pass record. Skip it otherwise only for a
wording fix or a single-project rule, and write the skip and its reason in
the pass record — an unstated skip reads as a run. Read the shared
[evaluating.md](../skill-rule-shared/evaluating.md) for the method, the
eval set format, and the confounds to record. Two facts hold in every
harness:

- The script's rule mode is an approximation of delivery: it injects the
  rule as system-prompt text, while a real rule arrives beside every other
  loaded rule, so a rule that competes with others looks better in the
  eval than in practice. Phrase rule-mode queries as the bare task.
- There is no trigger eval for a rule: an unscoped rule loads every
  session. A file-scoped rule has a loading condition the script cannot
  see; check it by hand once per scoping edit, as evaluating.md describes.

Keep every eval file in a temporary directory outside the repository, and
delete that directory before the pass ends. Eval files never go in a commit;
the pass record keeps the result.

Grade the outputs yourself; the script deliberately stops at collecting them.
Report the comparison including cost, and say plainly when the arms are too
close to call rather than reading a win into noise.

### 6. Record

- Set or refresh the rule's last-verified comment.
- Do not create a changelog file, even when the rule is not in a version
  control repository. Write the pass record — what was checked, changed,
  or left as is, the step 0 observation, each skipped step and its reason,
  and the 5b result — into the report to the user, and
  into the commit message when the change is committed. If the user wants
  a history of the rule, recommend a version control repository for it.
- A "checked, no change" pass still refreshes the last-verified markers —
  future runs use those dates to decide what needs re-verification.
- Name the check honestly. A step-5a walk-through is "desk-checked against N
  scenarios". Write "tested" or "measured" only when 5b ran, and give the
  numbers, the model, and the harness version.

### 7. Self-maintain

Every pass ends by turning the findings on this skill itself:

- If research contradicted or extended anything this skill, its standards
  file, or a shared file says, update them in the same pass, subject to the
  same evidence bar. Name a change to a shared file as shared in the pass
  record, so the next pass over the shared files sees it.
- A claim about model behavior — a rate, a tendency, an effect — observed
  in this pass on one query, one session, or fewer than ten runs goes to
  the user in the report, labeled unconfirmed. Do not write it into a file
  for a later pass to read: not the rule, this skill, a standards file,
  evaluating.md, the ledger, or the commit message. It enters guidance
  only when it clears the evidence bar (tier 1–2 support, or a measured
  effect across a real eval set).
- Refresh last-verified dates in the ledger that holds each source
  actually re-checked, and this skill's own `metadata.last-verified` when
  the pass verified its core sources: the harness's rule-file and
  permissions documentation named in the harness reference, and the
  prompting best-practices page. A pass that touches the shared decision
  framework re-reads the harness's skills documentation as well.
- Include the changes to this skill and the shared files in the pass
  record.

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
   marker and write the pass record, so the check is on record.
5. At or above the bar → apply the smallest change that incorporates the
   evidence, re-test (workflow step 5), and record.
