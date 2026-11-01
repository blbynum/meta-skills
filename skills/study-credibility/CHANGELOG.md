# Changelog — study-credibility

## 2026-10-31 — migrated: no config keys; already portable

Migrate pass under skill-author's "Migrating an existing skill"
(skill-author/references/skill-config.md). Read SKILL.md and the four
reference files for machine-specific values. Found none: no absolute path
outside the skill, no hostname, user name, or account, no vendor or account
choice, and no companion skill named in prose. The databases and registries
in `verification-sources.md` (PubMed, Europe PMC, CMS Open Payments,
ClinicalTrials.gov, and the rest) are the subject matter and are the same
on every machine, so they are not keys. Result: no Config section, no
`config.local.yaml`, no `.gitignore`.

Portability rules checked, no text changed: the frontmatter uses spec
fields only (`name`, `description`, `metadata`); `metadata.export:
portable` stays because config-export reads it to skip per-item questions
and is not yet retired (the notes migration of the same day kept it too);
the reference files are linked by relative path; the body names actions,
not harness tools; the two `curl` examples in `verification-sources.md`
show one way to reach the Europe PMC API and are not on the core path. No
`harness` key.

Checks: desk-checked against three scenarios — the skill copied into a
Cursor project on Windows, a user with no `~/projects` and no notes vault,
and a reader expecting a Config table — and each read the skill as written
with nothing to resolve. Trigger eval not run: the description did not
change, so it had nothing to measure. Smoke run not applicable: no value
moved. No A/B: behavior not rewritten. Step 2 research exempt: a
structural pass that touched no guidance. `last-verified` unchanged at
2026-08-15; the subject sources were not re-fetched.

## 2026-08-18 — updated: six figures traced to their primaries; four corrected

A review found figures with no ledger entry. Each was read from its primary
on 2026-08-18 and now has an entry in skill-rule-creator's sources.md:

- Bekelman 2003 pooled OR 3.60 (95% CI 2.63–4.91) — matched; the interval
  and the "8 studies, 1,140 trials" basis are now stated. "About a third of
  researchers held conflicts" was wrong: the abstract says "approximately one
  fourth of investigators"; corrected.
- Outcome-switching selectivity "2.6x" — matched to Jia et al. 2021 (J Clin
  Epidemiol): 294 randomized drug trials from mainland China, OR 2.64 (95% CI
  1.16–6.02) among trials registered before start; OR 8.84 (3.62–25.93) when
  registered while ongoing. Population and interval now stated in the prose
  and the table, with a "does not transfer" caveat.
- GRIM 71 papers / ~half — matched (36/71; 16 with several); wording now
  says "appeared to contain", as the paper does.
- Preprint concordance "~89% on sample size" — that is an interim conference
  figure; the version of record (Janda et al. JAMA Netw Open 2022, 547 pairs)
  gives 86.4% (sample size), 81.1% (primary end-point results), 96.2%
  (interpretation). Table row corrected.
- I² bands — the artifact's 0–25/25–50/50–75/75–100 matched neither Higgins
  2003 (points 25/50/75, low/moderate/high, "tentatively") nor the Cochrane
  Handbook (overlapping 0–40/30–60/50–90/75–100). Now quotes Cochrane with its
  "can be misleading" caveat.
- Egger / funnel tests "fewer than ~10 studies" — matched (Cochrane 13.3.4.4;
  Sterne 2011); the similar-size condition added.

The "~32% of guideline authors with undisclosed ties" row keeps its
"not re-verified" label. Wording-level pass on reference files; `last-verified`
unchanged (the tier-1 instrument pages were not re-fetched).

## 2026-08-15 — updated (first pass under skill-rule-creator)

The skill predates skill-rule-creator, so this pass covered both the
subject matter and the authoring standards. No provenance had ever been
recorded; the sources are now in
`~/.claude/skills/skill-rule-creator/references/sources.md`.

**Factual corrections.** Seven of the skill's specific numeric claims were
checked against primary sources. Five were wrong or unverifiable:

- Lundh 2017 harms result was stated as "more favorable harms results
  (RR ≈ 1.87)". The review reports *similar* harms results, RR 1.37
  (95% CI 0.64–2.93), from four papers rated very-low-quality — an interval
  spanning null. Corrected, with an explicit warning not to cite it as a
  demonstrated effect.
- Lundh efficacy and conclusions ratios were given as ranges (1.27–1.32,
  1.31–1.34). Replaced with the reported values and intervals: RR 1.27
  (1.17–1.37) and RR 1.34 (1.19–1.51).
- The claim that "restricting the analysis to studies at low risk of bias
  made the association stronger, not weaker" is not in the review. Replaced
  with what it does report: no difference on the standard risk-of-bias
  domains, industry studies *more* often at low risk of bias from blinding
  (RR 1.25), and the authors' conclusion that the effect "cannot be explained
  by standard 'Risk of bias' assessments". Added the results-vs-conclusions
  agreement finding (RR 0.83), which was missing and is the most directly
  actionable result in the review.
- Barnes & Bero 1998 was cited as "6% of independent reviews vs. 87% of
  affiliated ones". Those figures are not in the paper. Replaced with the
  reported 37% (39/106) concluding no harm, 74% of those industry-affiliated,
  adjusted OR 88.4 — and the CI (16.4–476.5), which the skill's own
  read-the-interval rule demands.
- Bero 2007 was cited as "66% / 79% / 10%". Not in the paper. Replaced with
  the multivariate ORs (20.2 for results, 34.6 for conclusions) plus two
  details worth more than the headline: 98% of the 192 trials used only
  surrogate outcomes, and blinded trials were less likely to favor the test
  drug.
- Peer-review error detection was "8 inserted, ~2 caught, none caught more
  than 5". Schroter et al. inserted 9 major errors; reviewers found a mean of
  2.6 at baseline. The "none more than 5" claim was dropped as unverified.
- Outcome switching was given as a single ~18% rate with ~16% effect
  inflation. Published rates range ~18–45%; replaced with the range plus the
  more stable and more useful finding that negative-finding trials switch at
  ~2.6x the odds of positive-finding ones.
- Preprint-vs-published was given as "~6% change, correlation ~0.99".
  Replaced with the verified concordance findings.

Verified correct and left alone: Turner 2008 (strengthened with the 94%-vs-51%
framing), statcheck, OSC 2015, Button 2013, Boutron 2010.

The base-rate table now marks the one figure not re-verified against a primary
source, and carries a caution that meta-research figures degrade as they are
relayed — the failure this pass found in the skill itself.

**Additions clearing the evidence bar.**

- Paper mills and fabricated papers: a new section in `verification-sources.md`
  and a check in workflow step 6. Every other method in the skill assumes a
  real study underneath, so this gap produced confident appraisals of possibly
  fictional methods. Includes the Problematic Paper Screener (URL verified
  live).
- Reporting guidelines are not validity assessments — CONSORT 2025 (April
  2025, 30 items), SPIRIT 2025, PRISMA 2020, STROBE. The skill previously said
  nothing about them.
- ROBINS-I V2 (released November 2024, revised November 2025): named in the
  instrument table, with the caveat that V2 is scoped to follow-up/cohort
  designs.
- PROBAST and TRIPOD+AI added for prediction models.
- Retraction-volume context, read in both directions (more active integrity
  apparatus, plus an unaddressed backlog).

**Authoring standards.** Description rewritten to third person (it is injected
into the system prompt). Added `metadata.last-verified`. Added a copyable
workflow checklist with an explicit light path for quick questions, so the
checklist does not turn a one-line question into a full appraisal. Added a
table of contents to `verification-sources.md`, which had passed 100 lines.
No deprecated patterns (ALL-CAPS pressure, manual chain-of-thought, persona
scaffolding) were present.

Desk-checked (nothing ran) against four evaluation scenarios: a user repeating the bad harms
figure, a suspected paper-mill preprint, a CONSORT-implies-quality inference,
and a quick-take request used as a regression check against over-triggering
the full workflow.

## 2026-10-31 — dependency reduction: compatibility declared

Pass from `~/projects/ai/dependency-map/reduction-plan.md`. Only change:
`compatibility: Verification examples use curl against public literature
APIs.` No other dependency; description unchanged; no trigger eval due.

## 2026-10-31 — kind declared: portable; moved to the meta-skills repository

Ben decided the kind; the portability check returns zero hits and the
skill has no harness-specific step, so it has no harness reference.
`metadata.harness: portable` added. Now symlinked into `~/.claude/skills`
from the repository; loaded through the link in a fresh session (3 turns,
$0.23). Description unchanged; no trigger eval due.
