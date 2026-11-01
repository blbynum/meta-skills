# Design-specific appraisal

Read the section matching the study in front of you. Each section lists what the design can support, the failure modes that actually matter, and the established appraisal instrument if you want a formal frame.

**Contents**
- [Choosing the right lens](#choosing-the-right-lens)
- [Randomized controlled trials](#randomized-controlled-trials)
- [Cohort studies](#cohort-studies)
- [Case-control studies](#case-control-studies)
- [Cross-sectional studies and surveys](#cross-sectional-studies-and-surveys)
- [Systematic reviews and meta-analyses](#systematic-reviews-and-meta-analyses)
- [Animal, in-vitro, and preclinical](#animal-in-vitro-and-preclinical)
- [Modeling and simulation](#modeling-and-simulation)
- [Diagnostic and prognostic accuracy](#diagnostic-and-prognostic-accuracy)
- [Case reports and case series](#case-reports-and-case-series)
- [Qualitative research](#qualitative-research)
- [Economics and policy evaluation](#economics-and-policy-evaluation)

---

## Choosing the right lens

Formal instruments exist and are worth naming when you use one, because they make your reasoning checkable:

| Design | Instrument |
|---|---|
| Randomized trial | Cochrane RoB 2 |
| Non-randomized intervention study | ROBINS-I V2 |
| Systematic review | AMSTAR 2, or ROBIS |
| Diagnostic accuracy | QUADAS-2 |
| Prediction model | PROBAST; TRIPOD+AI for reporting |
| Body of evidence across studies | GRADE |
| General-purpose, any design | CASP checklists, JBI critical appraisal tools |

Three cautions. First, ROBINS-I is genuinely difficult and frequently misapplied even in published systematic reviews; use its structure as a thinking aid rather than claiming a formal rating you have not carefully derived. V2, released in late 2024, adds algorithms mapping signalling questions to domain judgements, but it is currently scoped to follow-up (cohort-type) studies — do not apply it to a case-control design and call the result a ROBINS-I rating. Second, an instrument is a prompt for judgment, not a substitute — a paper can pass every checklist item and still be answering the wrong question.

Third, **do not confuse a reporting guideline with a validity assessment.** CONSORT (updated to CONSORT 2025, a 30-item checklist), SPIRIT for protocols, PRISMA 2020 for systematic reviews, and STROBE for observational studies describe what a paper must *disclose*, not whether what it discloses is any good. A fully CONSORT-compliant report of a badly designed trial is a well-documented bad trial. The guidelines are still useful to you in one specific way: they tell you what should be present, so an item that is missing is a question to ask rather than a detail to skip past.

**Resist the rigid hierarchy.** The pyramid putting RCTs above cohorts above case-control is a useful default and a bad law. GRADE's own logic allows observational evidence to be rated *up* for a large effect magnitude, a dose-response gradient, or when plausible confounding would work against the observed effect. A precise relative risk above ~2 is hard for residual confounding alone to manufacture. Meanwhile a randomized trial gets rated *down* for risk of bias, imprecision, inconsistency, indirectness, or publication bias — and a small, unblinded, short trial with a surrogate endpoint may be weaker evidence than a large well-controlled cohort.

---

## Randomized controlled trials

**Can support:** causal effect of the intervention as delivered, in the population enrolled, over the follow-up period, on the outcomes measured.

**Cannot support on its own:** long-term effects beyond follow-up, effects in excluded populations, effects of a different dose or formulation, or real-world effectiveness when the trial conditions were highly idealized.

**What to check, roughly in order of how often it matters:**

- **Randomization and allocation concealment.** Was the sequence genuinely random, and was upcoming assignment hidden from those enrolling? Concealment failure is worse than blinding failure — it corrupts the groups at the outset. Check the baseline table for imbalance that suggests the randomization did not work.
- **Blinding, and of whom.** Participants, clinicians, outcome assessors, analysts. Blinding matters in proportion to how subjective the outcome is: near-irrelevant for all-cause mortality, decisive for pain scores, symptom scales, or clinician-rated improvement.
- **The primary outcome, and whether it changed.** One prespecified primary outcome. Compare it to the registry entry. Outcome switching is common and inflates effects.
- **Surrogate vs. patient-relevant endpoints.** A change in a biomarker is not a change in health. Surrogates have repeatedly failed to predict clinical benefit — and sometimes the drug improved the surrogate while harming patients. Ask whether this specific surrogate has been validated for this specific outcome.
- **Composite endpoints.** Check what drove the composite. A "major adverse cardiac events" reduction driven entirely by revascularization (a decision) rather than death or infarction (events) is a much weaker claim. Composites also inflate event counts, buying power at the cost of interpretability.
- **Attrition and analysis population.** How many dropped out, was it differential between arms, and how were they handled? Intention-to-treat preserves randomization; per-protocol analysis breaks it and generally favors the intervention. If the headline result is per-protocol, ask why.
- **The comparator.** Placebo, usual care, or an active drug — and if active, at what dose? Comparator drugs given at non-optimal doses is a documented technique for making a sponsor's product look better.
- **Early termination.** Trials stopped early for benefit systematically overestimate effects.
- **Power and enrollment.** Did it reach its target sample size, and was that target justified?

---

## Cohort studies

**Can support:** temporal association between exposure and outcome, incidence, and — with strong design and a large effect — a reasonable causal inference.

**Failure modes that matter:**

- **Confounding, named specifically.** Do not write "residual confounding is possible." Identify the confounder you think is operating, whether it was measured, how well, and which direction it would push. The classic pattern: a health-conscious behavior correlates with every other health-conscious behavior, so the exposure gets credit for the cluster.
- **Measurement quality of the exposure.** Self-report, single baseline measurement, food-frequency questionnaires, and recall over long periods are all weak. Was exposure measured once and assumed constant for twenty years?
- **Reverse causation.** Early undiagnosed disease changes behavior. People with subclinical illness eat less, exercise less, and drink less — making the "healthy" behavior look protective. Check whether early follow-up years were excluded.
- **Selection into the cohort and loss to follow-up.** Who joined, who stayed, and are the people who left different in ways related to the outcome?
- **Immortal time bias** and other time-alignment errors in database studies: participants who by construction had to survive to be classified as exposed.
- **Adjustment done badly.** Over-adjustment for a mediator on the causal pathway erases a real effect; adjustment for a collider creates a spurious one. Look at what was put in the model, not just how many covariates there were.

**Strengthening features:** dose-response gradient, consistency across independent cohorts with different confounding structures, large effect magnitude, an active-comparator design, negative controls, sensitivity analyses including an E-value quantifying how strong an unmeasured confounder would need to be.

---

## Case-control studies

**Can support:** association, efficiently, for rare outcomes.

**Failure modes:** control selection is the whole ballgame — controls must come from the population that would have become cases. Recall bias is structural, since cases search their history for explanations. Check whether exposure ascertainment was blinded to case status and whether it relied on memory or records.

---

## Cross-sectional studies and surveys

**Can support:** prevalence, and correlation at a point in time.

**Cannot support:** temporal ordering, and therefore causation. Exposure and outcome are measured simultaneously.

**For surveys and polls specifically:** sampling frame, response rate and non-response bias, question wording and order, whether weighting was applied and to what, and margin of error including design effects. A large convenience sample (an online opt-in panel) is often worse than a small probability sample. Watch for questions engineered toward an answer, especially in advocacy-commissioned polling.

---

## Systematic reviews and meta-analyses

A meta-analysis inherits every weakness of its inputs and adds its own. It is not automatically stronger than a single good trial.

**What to check:**

- **Protocol and search.** Was there a prespecified protocol (PROSPERO)? Was the search comprehensive across multiple databases, including unpublished and non-English work?
- **Inclusion criteria and whether they were applied consistently.** Loose criteria let in junk; narrow criteria can be gerrymandered around a desired result.
- **Risk of bias assessment of included studies** — and whether it was actually used. Many reviews assess risk of bias, then pool everything anyway. Check whether the conclusion changes when only low-risk studies are included.
- **Heterogeneity.** The Cochrane Handbook's rough guide for I² in meta-analyses of randomized trials uses overlapping bands: 0–40% might not be important, 30–60% may represent moderate heterogeneity, 50–90% substantial, 75–100% considerable — and warns that thresholds "can be misleading" because importance depends on the size and direction of effects and on how few studies there are. High I² tells you results differ, not why. And I² depends on the precision of included studies: very large studies produce high I² from trivial real differences. Pooling substantially heterogeneous studies into one number can produce an average that describes no real population.
- **Publication bias.** Funnel plot asymmetry and Egger's test are the standard checks, but the rule of thumb is not to run asymmetry tests with fewer than 10 studies (power is too low; with substantial heterogeneity the minimum is higher still), nor when the studies are all of similar size, and asymmetry has causes other than publication bias — genuine heterogeneity, or small studies being methodologically different. Trim-and-fill corrects under assumptions that are often wrong. Treat all of these as signals, not verdicts.
- **The unpublished literature.** The strongest evidence of publication bias comes from comparing published results against regulatory submissions. Ask whether that comparison was possible here.
- **Who wrote it.** Reviews are unusually easy to steer through inclusion criteria and risk-of-bias judgments while looking rigorous. Check the review authors' ties, not just the primary studies'.

---

## Animal, in-vitro, and preclinical

**Can support:** mechanism, plausibility, and a reason to run a human study.

**Cannot support:** claims about human health outcomes. This is one of the most common and most consequential overreaches in science coverage.

**Check:** species and strain, whether the model actually reproduces the human condition, dose translated to human-equivalent exposure (often wildly higher in animals), route of administration, randomization and blinding (frequently absent in animal work, which is one reason preclinical findings replicate poorly), and sample sizes that are typically very small. For in-vitro work, whether the concentration used is achievable in living tissue.

---

## Modeling and simulation

The output is a consequence of the assumptions. Appraise the assumptions, not the elegance of the model.

**Check:** key parameter values and their sources, sensitivity analysis over plausible ranges, whether the model was validated against out-of-sample or historical data, whether code and data are available, and how far the projection extends beyond the data supporting it. Ask which single assumption the headline result is most sensitive to — for a model, that is usually the whole story. Beware models calibrated on the same data used to claim they fit.

---

## Diagnostic and prognostic accuracy

**Check** (QUADAS-2 covers this): whether the reference standard is genuinely a good standard, whether it was applied to everyone regardless of index test result (partial verification bias), whether the test and reference were interpreted blind to each other, and whether the spectrum of patients resembles real practice — accuracy measured in clearly-sick vs. clearly-well people is inflated. Sensitivity and specificity are not what a clinician needs; positive and negative predictive value depend on prevalence in the population being tested, so a test that looks excellent can generate mostly false positives in a low-prevalence setting.

For prediction models: whether they were validated on data separate from the development data, and whether calibration (not just discrimination/AUC) was reported.

---

## Case reports and case series

**Can support:** existence — that something happened at least once. Valuable for rare harms and novel presentations, hypothesis-generating, and nothing more. No denominator, no comparison group, so no rate and no effect.

---

## Qualitative research

Do not appraise with quantitative criteria; sample size and generalizability are the wrong lens. **Check:** whether the sampling strategy fits the research question, whether data collection continued to saturation, how analysis was conducted and whether more than one analyst was involved, whether disconfirming cases were sought and reported, whether the researcher's own position and influence are addressed, and whether interpretations are grounded in quoted data.

---

## Economics and policy evaluation

**Check** the identification strategy — what provides the counterfactual. Difference-in-differences requires parallel pre-trends, and they should be shown, not asserted. Instrumental variables require an instrument that is both relevant and plausibly excluded from affecting the outcome directly; the exclusion restriction is an assumption, not a testable fact, and weak instruments produce badly biased estimates. Regression discontinuity requires no manipulation of the running variable near the cutoff. Look for specification-curve or robustness analysis: results that hold under one specification and vanish under reasonable alternatives are fragile. Check whether standard errors are clustered appropriately.

Policy research is also where non-financial and ideological interests bite hardest — see `conflicts-of-interest.md`.
