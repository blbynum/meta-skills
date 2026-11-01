---
name: skill-rule-creator
description: >-
  Creates, evaluates, and updates the two kinds of persistent Claude guidance
  artifacts: skills (SKILL.md directories that load on demand) and rules
  (entries in CLAUDE.md or .claude/rules/ that load every session). Use when
  the user asks to make, write, add, or update a skill or a rule; wants a
  convention, prohibition, standing constraint, or repeatable workflow captured
  for future sessions; asks whether guidance should be a skill or a rule; or
  asks to refresh, re-verify, or audit existing skills and rules against
  current best practices. Triggers include "make a skill for", "add a rule",
  "turn this into a skill", "should this be a skill or a rule", "update the X
  skill", and "update all the skills and rules".
argument-hint: "[create <topic> | update <artifact> | update all]"
metadata:
  export: portable
  last-verified: "2026-08-18"
---

# Skill & Rule Creator

This skill produces and maintains two artifact kinds, distinguished by how
they load:

- **Skill** — a directory `<name>/SKILL.md` plus optional `references/` and
  `scripts/`. Personal skills live in `~/.claude/skills/`, project skills in
  `.claude/skills/`. Only the name and description (plus `when_to_use`, if
  set) load at startup; the body
  loads when a task matches or the user types `/<name>` (the command comes
  from the directory name).
- **Rule** — an always-loaded instruction: an entry in CLAUDE.md
  (`~/.claude/CLAUDE.md` user-wide; `./CLAUDE.md` or `./.claude/CLAUDE.md`
  project) or a topic file in `.claude/rules/` (project) or `~/.claude/rules/`
  (user). A rules file with `paths:` frontmatter loads only when Claude works
  with matching files.

Out of scope — redirect rather than force an artifact:

- "Remember X" for a personal or one-project fact → auto memory already covers
  it; offer a rule only if the user wants a durable instruction.
- Behavior that must fire at a fixed lifecycle point (before every commit,
  after each edit) → that requires a hook in settings.json. A rule can state
  the policy but cannot enforce timing; say so and point to hook configuration.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 0. Observe first: run three real prompts without the artifact; record the failures
- [ ] 1. Classify the request
- [ ] 2. Research current guidance, scoped to what the pass needs
- [ ] 3. Choose skill vs rule, and say why
- [ ] 4. Draft or revise the artifact
- [ ] 5a. Desk-check against 2–3 evaluation scenarios
- [ ] 5b. Measure against a baseline (required for user-wide skills and user-wide rules), or state the skip reason
- [ ] 6. Record dates and changelog
- [ ] 7. Self-maintenance pass on this skill
```

For a pure choice question ("should this be a skill or a rule?"), run steps
1–3 only and answer with reasons; create nothing unless asked.

### 0. Observe first

Before you research or draft, see the failure the artifact is meant to fix.
For a new artifact, run three realistic prompts in a fresh session without
it, or read three real past transcripts of the task, and write down what
went wrong: the missing step, the wrong default, the question the user had
to answer twice. Those failures are the eval set for step 5 (three is its
working minimum) and the reason the artifact exists. If nothing fails, say so and ask
whether the artifact is still wanted — the vendor's own guidance is that
Claude writes well-formed skills unaided, so a skill has to earn its place
by fixing something observed. For an update prompted by an observed
failure, the failure is the observation; record it in the changelog with the
session or transcript it came from.

### 1. Classify

- **Create**: "make a skill/rule for X" → full workflow.
- **Update**: "update <artifact>" or "update all the skills and rules" → find
  the artifacts in the locations listed above, then follow the Updating
  section. For "update all", enumerate every `SKILL.md` and every rules file
  in both the personal and project locations before starting, and report the
  list so nothing is silently skipped.
- **Choice question** → decision framework only, as above.

### 2. Research

Research is a fact-currency control, not the first step of every pass. Run
it when the pass writes or refreshes guidance that depends on model or
platform behavior, and whenever the artifact will state a load-bearing fact
— a rate, a version, a flag, a limit, a quoted rule — which must be checked
against its primary source before it is written. Skip it, and say which
exemption applies in the changelog, for a feature request that adds
capability without touching guidance, a wording fix, or same-day reuse of
sources already read in this pass. Trained knowledge and this skill's own
text both go stale; the sources file exists to catch that.

1. Read the entries in [references/sources.md](references/sources.md) that
   concern the pass: the core-source entries named in step 7 for any skill
   or rule work, plus the artifact's own subject section (the Contents list
   names the sections). Reading the whole file is not required. Re-read
   an entry immediately before you edit it: another session may have written
   to the file in between, and an edit built on a stale read discards their
   work.
2. Re-fetch the tier-1 sources relevant to the request (skill-authoring docs
   for skills; memory/rules docs for rules), and search the web for changes
   since the oldest relevant last-verified date.
3. Rank evidence: (1) Anthropic docs and engineering posts, (2) research
   papers and empirical studies, (3) community findings. Use tier 3 only when
   corroborated by tier 1–2, or explicitly labeled as unverified community
   practice.
4. Every entry records the models or vintage a finding was measured on. Carry
   that qualifier into the artifact; a claim that drops it is the most common
   error this file has recorded.
5. Provenance for this skill's subject lives in `sources.md`, not in the
   user's notes vault (`~/ai/notes`, a 2026-08-15 snapshot this skill does
   not update). Write to the vault only when the user asks for a note, via
   the notes skill.

### 3. Choose the mechanism

Apply the decision framework below. Three cases:

- User didn't specify → decide, then state the choice and the deciding
  property in one or two sentences.
- User specified and the framework agrees → proceed without commentary.
- User specified and the framework disagrees → recommend the other mechanism
  with one or two concrete reasons ("this is forty lines of procedure used in
  maybe one session in ten; as a rule it taxes every session"), then follow
  whichever the user picks.

### 4. Draft

Read [references/authoring-standards.md](references/authoring-standards.md)
before writing — it holds the format rules, quality bars, and deprecated
patterns for both artifact kinds. Three rules from it bear repeating because
they are easy to miss:

- Produced artifacts carry no citations or source URLs. Provenance lives in
  this skill's sources file, so the artifacts stay clean and cheap.
- Every artifact gets a verification marker: skills take
  `metadata: {last-verified: "YYYY-MM-DD"}` in frontmatter; rules take a
  `<!-- last-verified: YYYY-MM-DD -->` comment, which is stripped before
  context injection and therefore costs nothing.
- Rules are imperative and concrete: "Use X", never "we generally prefer X
  when possible".

### 5. Test

**5a. Desk-check (always).** Write 2–3 evaluation scenarios: realistic prompts
the artifact should handle, each with the expected behavior. Re-read the
artifact with fresh eyes and walk each scenario through it; wherever the text
permits a wrong path, fix the text, not the scenario. Report the scenarios and
outcomes to the user; keep them out of the artifact itself.

**5b. Measure.** A desk-check shows the text is clear to a reader who already
knows what it means. It cannot show that the skill loads when it should, or
that the artifact changes what the model does — for that, a fresh session has
to run it against a no-artifact baseline, on the failures step 0 recorded.

5b is required for every user-wide skill and every user-wide rule, and
whenever this pass rewrote a skill description. Skip it only for a wording
fix or a single-project rule, and write the skip and its reason in the
changelog entry — an unstated skip reads as a run. Read
[references/evaluating.md](references/evaluating.md) for the method, the eval
set format, the confounds to record, and the two scripts:

- `scripts/trigger_eval.py` measures how often a skill actually loads, across
  should-trigger prompts and near-misses. Skills only.
- `scripts/ab_eval.py` runs task prompts with and without the artifact, three
  runs per arm, and saves outputs, transcripts, cost, the Claude Code
  version, and the resolved model.

Grade the outputs yourself; the scripts deliberately stop at collecting them.
Report the comparison including cost, and say plainly when the arms are too
close to call rather than reading a win into noise.

### 6. Record

- Set or refresh the artifact's last-verified marker (formats in step 4).
- Skills keep a `CHANGELOG.md` in their directory: create it on first touch
  and append a dated entry each pass. Rules stay lean — their checks are
  recorded in this skill's own changelog during step 7 instead.
- "Checked, no change" entries count as entries — future runs use them to
  decide what needs re-verification.
- Name the check honestly. A step-5a walk-through is "desk-checked against N
  scenarios". Write "tested" or "measured" only when 5b ran, and give the
  numbers, the model, and the Claude Code version.

### 7. Self-maintain

Every pass ends by turning the findings on this skill itself:

- If research contradicted or extended anything this skill or its references
  say, update them in the same pass, subject to the same evidence bar.
- A claim about model behavior — a rate, a tendency, an effect — observed
  in this pass on one query, one session, or fewer than ten runs goes into
  the CHANGELOG as a watch item, never into authoring-standards.md or
  evaluating.md. Promote it only when a later pass finds it clears the
  evidence bar (tier 1–2 support, or a measured effect across a real eval
  set). A method trap whose mechanism is understood — an eval that measured
  nothing because of how it was built — may go into evaluating.md at once,
  dated.
- Refresh last-verified dates in [references/sources.md](references/sources.md)
  for each source actually re-checked, and this skill's own
  `metadata.last-verified` when the pass verified its core sources: the
  skill-authoring best-practices page, the Claude Code skills doc, the memory
  doc, and the prompting best-practices page.
- Log the pass in `${CLAUDE_SKILL_DIR}/CHANGELOG.md`.

## Decision framework: skill vs rule

Decide on loading behavior, never on topic:

| Property | Rule | Skill |
|---|---|---|
| Loads | Every session, unconditionally | Metadata always; body on demand |
| Cost | Every line taxes every session, summed across all loaded files | Near zero until triggered |
| Fits | Short universal constraints: conventions, prohibitions, exact commands | Procedures: multi-step workflows, domain references, scripts, supporting files |
| Form | Imperative lines; under 200 per file | SKILL.md under 500 lines plus references |

Borderline calls:

- Prefer a **skill** when the content exceeds a few lines, applies to only
  some sessions, or has grown from a fact into a procedure.
- Prefer a **rule** when the guidance must hold even in sessions where nothing
  would trigger a skill. Prohibitions are the classic case: nothing "matches"
  a prohibition until it is already being violated.
- A rules file with `paths:` frontmatter is the middle ground for guidance
  tied to a file area rather than to a task.
- A skill with `disable-model-invocation: true` fits actions only the user
  should time (deploys, releases): it becomes a pure slash command.

## Updating

An update is a check against evidence, not a rewrite:

1. Name what prompted it: an observed failure (step 0 — record the session),
   a guidance refresh (run step 2, scoped to the artifact's subject), or a
   feature request or wording fix that does not touch guidance (step 2
   exempt; say so).
2. Diff current guidance, or the observed failure, against the artifact.
3. Apply the **evidence bar**: change the artifact only when the latest
   evidence indicates the change would improve output, or when a
   not-yet-incorporated strategy or tool is clearly established — tier 1–2
   support, or wide and verified community adoption. Novelty alone never
   clears the bar.
4. Below the bar → report "no change needed" with reasons: what was checked,
   what was found, why it didn't clear. Still refresh the last-verified
   marker and changelog so the check is on record.
5. At or above the bar → apply the smallest change that incorporates the
   evidence, re-test (workflow step 5), and record.
