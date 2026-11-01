# Statistics, red flags, and spin

**Contents**
- [Effect size and what it means in the world](#effect-size-and-what-it-means-in-the-world)
- [Precision and confidence intervals](#precision-and-confidence-intervals)
- [Power, small samples, and the winner's curse](#power-small-samples-and-the-winners-curse)
- [Researcher degrees of freedom](#researcher-degrees-of-freedom)
- [Prior plausibility](#prior-plausibility)
- [Internal consistency and numerical forensics](#internal-consistency-and-numerical-forensics)
- [Spin: reading the gap between results and conclusions](#spin-reading-the-gap-between-results-and-conclusions)
- [Base rates worth carrying around](#base-rates-worth-carrying-around)

---

## Effect size and what it means in the world

**Always convert to absolute terms.** A relative risk reduction hides the baseline. "Cuts risk by 50%" means one thing when baseline risk is 40% and something almost meaningless when it is 0.2%. Selective reporting of relative rather than absolute effects is one of the most common forms of legitimate-looking misrepresentation, and it appears in a large fraction of published medication trials.

Useful conversions:
- **Absolute risk difference** — the percentage-point change. This is what the reader actually cares about.
- **Number needed to treat (NNT)** = 1 / absolute risk difference. How many people get the intervention for one to benefit. Report the corresponding **number needed to harm** whenever adverse events are available; a favorable NNT alongside a similar NNH is a very different picture.
- For continuous outcomes, ask whether the change exceeds the **minimal clinically important difference** for that instrument. A statistically significant 2-point shift on a 100-point quality-of-life scale is probably imperceptible to a patient.

**Statistical significance is not importance, and non-significance is not absence of effect.** A p-value confounds effect size with sample size. A huge study can produce p<0.001 for a trivial effect; a small study can miss a large real one. Never let "significant" stand in for "meaningful" — and treat "no significant difference" in an underpowered study as uninformative rather than as evidence of equivalence. Equivalence and non-inferiority require their own designs and prespecified margins.

---

## Precision and confidence intervals

Read the interval, not the point estimate. The most useful question: **what is the least impressive value the interval is compatible with?** If a treatment's 95% CI for risk reduction runs from 1% to 45%, the data are compatible with a nearly worthless effect. A result that is "significant" because the interval barely excludes null is weak evidence dressed as a finding.

Wide intervals mean imprecision, which is one of GRADE's explicit reasons to rate down certainty regardless of study design. Beware point estimates reported without any interval at all.

---

## Power, small samples, and the winner's curse

Low statistical power has a consequence people consistently miss. It does not only mean you might miss real effects. It means that **when an underpowered study does reach significance, the observed effect is necessarily inflated** — only an unusually large sample estimate could clear the threshold. This is the winner's curse, and it is why small studies produce spectacular effects that shrink or vanish on replication.

The median power in some fields is genuinely dire — estimates for neuroscience put it around 8–31%. Median power that low means most published significant findings in the field are either false positives or badly overestimated.

**Practical rule: a surprisingly large effect from a small study is a red flag, not a highlight.** Ask what the effect would look like if it were real but modest, and whether this study could have detected that.

Check whether an a priori power calculation was reported and justified. Post-hoc power calculations computed from the observed effect are uninformative and slightly misleading; their presence is itself a small red flag.

---

## Researcher degrees of freedom

The same dataset can yield many defensible analyses. Flexibility across those choices — selecting the analysis that produces the desired p-value, whether deliberately or through motivated reasoning — is what "p-hacking" describes. It does not require dishonesty; ordinary judgment applied repeatedly with a preferred answer in mind is enough.

**Where the flexibility lives:**
- Choosing among multiple outcome measures or time points, reporting the one that worked.
- Adding participants until significance appears (optional stopping), or stopping early once it does.
- Deciding exclusion rules after seeing how they affect results.
- Trying multiple covariate sets, transformations, or model specifications.
- Splitting into subgroups and reporting the one that reached significance.
- Switching from the prespecified primary outcome to a secondary one.
- **HARKing** — presenting a hypothesis formed after seeing the results as if it had been specified in advance. This is invisible in the paper by construction, which is exactly why preregistration matters: it is the only thing that makes the distinction checkable.

**What to look for:**
- Count the comparisons that were available, not just the ones reported. Was multiplicity adjusted for?
- p-values clustered just under 0.05, especially across a literature.
- A stated hypothesis that fits the results suspiciously precisely, particularly if it is oddly specific ("the effect appeared in women over 50 with prior exposure").
- Methods sections vague about analysis choices, or missing prespecification entirely.
- Unexplained variable transformations, unusual exclusion criteria, or an odd final sample size relative to what was enrolled.
- **Registry comparison.** If a registration exists, compare the registered primary outcome, timeframe, and analysis to what was published. This is the closest thing to a direct test, and discrepancies are common enough to be worth checking every time.

Subgroup findings deserve particular skepticism. A subgroup result is credible mainly when it was prespecified, when the interaction test (not just the within-subgroup p-value) is significant, when there are few subgroups, and when there is a prior mechanistic reason. Otherwise treat it as hypothesis-generating.

---

## Prior plausibility

Ioannidis's central point is that the probability a published finding is true depends heavily on the **pre-study odds** that the hypothesis was true in the first place, not only on the p-value or the power. In a field testing many long-shot hypotheses with modest power, most "significant" findings will be false positives even with everyone behaving correctly.

Practically: a result that contradicts a large well-replicated body of evidence, or that proposes a mechanism with no plausible basis, requires much stronger evidence than a result that fits established understanding. This is not conservatism for its own sake — it is what the arithmetic requires. State it explicitly when it is doing work in your assessment, and be honest that it cuts both ways: genuine discoveries also start out as implausible outliers, so prior implausibility raises the evidentiary bar rather than settling the question.

---

## Internal consistency and numerical forensics

Checkable arithmetic in a paper is worth checking, because errors are far more common than most readers assume.

- **Do percentages match the stated denominators?** Recompute a few. Do subgroup Ns sum to the total? Does the flow diagram account for everyone?
- **Are reported means possible given the sample size?** The **GRIM** test exploits the fact that a mean of integer-valued data over N observations must be expressible as a fraction with denominator N. In one analysis, 71 of 260 recent psychology papers could be GRIM-tested; 36 of those 71 (about half) appeared to contain at least one mean inconsistent with the reported sample size and scale, and 16 contained several.
- **Do test statistics, degrees of freedom, and p-values agree?** The **statcheck** analysis of over 250,000 p-values across major psychology journals found roughly half of papers using null-hypothesis significance testing contained at least one inconsistent p-value, and about one in eight contained an inconsistency large enough to potentially change the conclusion.
- **Are standard deviations plausible** given the scale's bounds? An SD too large for a bounded scale is impossible; **SPRITE** formalizes this by attempting to reconstruct datasets matching the reported mean and SD.
- **Do numbers agree between the abstract, the text, the tables, and the figures?**

Interpret findings carefully. These tools identify values that are impossible or implausible; they **cannot distinguish a typo, a rounding convention, a mis-stated N, or fabrication.** Report an inconsistency as an inconsistency and say what it would take to resolve it. Most are sloppiness. But a paper with several is a paper whose numbers were never carefully checked, which is relevant regardless of cause.

---

## Spin: reading the gap between results and conclusions

Spin is a conclusion more favorable than the results support. It is extremely common, it survives peer review routinely, and it is the main vector by which sound data become unsound public claims. Read the results section first and form your own conclusion *before* reading the discussion — then compare.

How common: among published RCTs whose *primary outcome was statistically nonsignificant*, Boutron and colleagues (JAMA 2010) found spin in 58.3% of abstract conclusions, 37.5% of abstract results sections, and 18.0% of titles. In other words, when a trial fails on its primary endpoint, the abstract still spins it more often than not. Treat a nonsignificant primary outcome plus an upbeat abstract as the expected pattern rather than an anomaly.

**Tells:**
- The primary outcome was null, but the abstract's conclusion leads with a secondary outcome, a subgroup, or a per-protocol analysis.
- A null result described as "trending toward significance," "showed a tendency," "numerically favored," or "comparable to" (which quietly converts a failure to find a difference into a claim of equivalence).
- Relative effects in the abstract, absolute effects buried or absent.
- Causal verbs — "reduces," "improves," "protects against," "leads to" — attached to observational data that can only support association.
- Conclusions about a population that was not studied, or a duration that was not observed.
- Mechanistic or animal findings described in terms of human health outcomes.
- Harms reported with less prominence, precision, or statistical rigor than benefits — or a safety claim from a trial powered only for efficacy and far too small to detect rare harms.
- The title or abstract makes a claim the results section does not support. Many readers never get past the abstract, which makes this the highest-leverage place to check.

Also compare the paper to the **press release** and the **news coverage** when those are what prompted the question. Distortion frequently originates in the institution's own press office, so identifying where the overstatement entered the chain is a genuinely useful finding.

---

## Base rates worth carrying around

Useful for calibration. Cite them as approximations, and note that most come from specific fields and may not transfer cleanly. Quote a figure only in the form given here — these are the numbers the primary sources actually report, and inflated or rounded-up versions of several of them circulate widely.

| Finding | Figure as reported |
|---|---|
| Psychology studies replicating with significance in the same direction (OSC 2015, n=100) | 36%, down from 97% significant in the originals; replication effect sizes about half |
| Median statistical power in neuroscience (Button et al. 2013) | 8–31% across 49 meta-analyses; median ~21% |
| Psychology NHST papers with ≥1 inconsistent p-value (statcheck, >250,000 p-values) | ~50%; ~1 in 8 with a gross inconsistency that may change the conclusion |
| Psychology papers with ≥1 impossible mean (GRIM, n=71) | ~50% |
| RCTs with primary-outcome discrepancies vs. registry | ~18–45% depending on field and venue; no single defensible rate |
| Selectivity of outcome switching (Jia 2021, 294 mainland-China drug RCTs) | Registered primary outcomes with negative findings switched at OR 2.64 (1.16–6.02) vs positive, among trials registered before start; OR 8.84 (3.62–25.93) when registered while ongoing |
| FDA-registered antidepressant trials never published (Turner 2008) | 31% unpublished; literature appeared 94% positive vs. FDA's 51%; pooled effect inflated 32% |
| Industry-sponsored studies favoring the sponsor (Lundh 2017) | RR 1.27 (1.17–1.37) favorable efficacy results; RR 1.34 (1.19–1.51) favorable conclusions |
| Agreement between results and conclusions, industry vs. non-industry (Lundh 2017) | RR 0.83 (0.70–0.98) — industry studies agree with their own data less often |
| Guideline authors with undisclosed financial ties | ~32% (figure not re-verified against the primary source) |
| Spin in abstract conclusions of RCTs with nonsignificant primary outcomes (Boutron 2010, n=72) | 58.3%; 18.0% of titles |
| Major errors detected by peer reviewers when 9 were deliberately inserted (Schroter et al.) | mean 2.6 of 9 at baseline; training improved it by ~0.5 |
| Preprint vs. peer-reviewed version of the same study (Janda 2022, 547 medRxiv clinical-study pairs) | Sample size concordant in 86.4%; primary end-point results in 81.1%; interpretation in 96.2% (an interim conference abstract of the same cohort gave 89.2% on sample size) |

Two implications worth stating explicitly. First, **peer review is weak quality control** — reviewers find roughly a quarter of deliberately planted major errors, so passing review is mild positive evidence and failing to appear in a peer-reviewed venue is not by itself disqualifying. Second, **preprints are not categorically unreliable**; where the same study has been compared in both forms, effect estimates and conclusions usually survive review intact. Judge the preprint's methods rather than its status, while noting that it has not been through even that weak filter and that individual papers do change.

One caution about this table specifically. Meta-research figures degrade as they are relayed: a confidence interval gets dropped, a null result becomes a positive one, an odds ratio from a subgroup becomes a headline rate. If a figure is load-bearing for your assessment, pull it from the primary source rather than from memory or from a secondary summary — the same standard this skill applies to everyone else.
