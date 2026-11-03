# Sources — study-credibility

Provenance ledger for the study-credibility skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

### study-credibility skill — tier 2: meta-research primary sources
- URLs (all resolved through the Europe PMC REST API rather than the
  publisher, which is the technique the skill itself documents):
  https://doi.org/10.1002/14651858.MR000033.pub3 (Lundh 2017, Cochrane) ,
  https://doi.org/10.1056/NEJMsa065779 (Turner 2008) ,
  Barnes & Bero, JAMA 1998, "Why review articles on the health effects of
  passive smoking reach different conclusions" ,
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1885451/ (Bero 2007,
  PLoS Medicine, statin drug-drug comparisons) ,
  Nuijten et al., "The prevalence of statistical reporting errors in
  psychology (1985-2013)" (statcheck) ,
  https://www.science.org/doi/10.1126/science.aac4716 (OSC 2015) ,
  https://www.nature.com/articles/nrn3475 (Button et al. 2013) ,
  Boutron et al., JAMA 2010 (spin) ,
  Schroter et al., J R Soc Med 2008 (inserted-error detection)
- Last verified: 2026-08-15 (Lundh, Turner, Barnes & Bero, and Bero 2007
  abstracts and full text retrieved directly from Europe PMC; statcheck
  abstract retrieved directly; OSC 2015, Button 2013, Boutron 2010, and
  Schroter via fetched search summaries)
- Supports: Lundh — favorable efficacy RR 1.27 (1.17–1.37, 25 papers,
  moderate quality); favorable conclusions RR 1.34 (1.19–1.51, 29 papers,
  low quality); harms RR 1.37 (0.64–2.93, four papers, very low quality —
  interval spans null); no difference between industry and non-industry on
  sequence generation, allocation concealment, follow-up, or selective
  outcome reporting; industry studies more often low risk of bias from
  blinding RR 1.25 (1.05–1.50); results-to-conclusions agreement RR 0.83
  (0.70–0.98); verbatim authors' conclusion that the effect "cannot be
  explained by standard 'Risk of bias' assessments". Turner — 74
  FDA-registered antidepressant studies, 31% unpublished; 37 of 38 positive
  published; 22 negative unpublished and 11 published conveying a positive
  outcome; literature appeared 94% positive vs. FDA's 51%; pooled effect
  inflation 32%. Barnes & Bero — 106 reviews, 37% (39/106) concluded passive
  smoking not harmful, 74% of those industry-affiliated, adjusted OR 88.4
  (16.4–476.5). Bero 2007 — 192 statin comparison RCTs, 98% surrogate
  outcomes only; test-drug-company funding associated with favorable results
  OR 20.2 and favorable conclusions OR 34.6 in multivariate analysis of
  industry-funded trials; adequately blinded trials less likely to favor the
  test drug. statcheck — >250,000 p-values, ~half of NHST papers contain a
  p-value inconsistent with its test statistic, ~1 in 8 a gross
  inconsistency. OSC 2015 — 36 of 100 replications significant in the same
  direction, down from 97% in the originals, effect sizes about half. Button
  2013 — median power 8–31% across 49 meta-analyses. Boutron 2010 — 72 RCTs
  with nonsignificant primary outcomes, spin in 58.3% of abstract
  conclusions, 18.0% of titles. Schroter — nine major errors inserted, mean
  2.6 detected at baseline.
- Corrections recorded 2026-08-15: the skill previously stated a Lundh harms
  RR of 1.87 (no such figure; the real one spans null), a Lundh claim that
  restricting to low-risk-of-bias studies strengthened the association (not
  in the review), Barnes & Bero rates of 6% vs. 87% (not in the paper), Bero
  2007 rates of 66%/79%/10% (not in the paper), and a Schroter figure of
  8 errors with "none caught more than 5" (9 major errors; the second clause
  unverified). Five of seven checked numeric claims were wrong — treat
  unsourced meta-research figures in any artifact as suspect until pulled
  from the primary source.

### study-credibility skill — tier 2: figures added to the ledger 2026-08-18
- Sources and how read (all 2026-08-18): Bekelman, Li & Gross, JAMA 2003
  (PMID 12533125; abstract via Europe PMC) ; Jia et al., "Association
  between switching of primary outcomes and reported trial findings among
  randomized drug trials from China", J Clin Epidemiol 2021;132:10-17 (PMID
  33309887; abstract via Europe PMC — full text paywalled, methods not read)
  ; Brown & Heathers, "The GRIM Test", SPPS 2017 (DOI
  10.1177/1948550616673876; abstract via Crossref, preprint abstract via
  Europe PMC) ; Janda et al., "Comparison of Clinical Study Results Reported
  in medRxiv Preprints vs Peer-reviewed Journal Articles", JAMA Netw Open
  2022;5(12):e2245847 (PMID 36484989; abstract via Europe PMC) and the same
  group's Peer Review Congress 2022 abstract (interim data) ; Higgins et al.,
  "Measuring inconsistency in meta-analyses", BMJ 2003;327:557 (PMC192859;
  full text) ; Cochrane Handbook v6.5 ch. 10 §10.10.2 and ch. 13 §13.3.4.4
  (fetched) ; Sterne et al., BMJ 2011;343:d4002 (LSHTM repository PDF).
- Supports, verbatim: Bekelman — "Eight articles, which together evaluated
  1140 original studies ... pooled Mantel-Haenszel odds ratio, 3.60; 95%
  confidence interval, 2.63-4.91" and "Approximately one fourth of
  investigators have industry affiliations" (the artifact had said "about a
  third"; corrected). Jia — a retrospective cohort of "294 RCTs" from
  mainland China: "Among RCTs registered before they started, the odds of
  switching primary outcomes with negative findings were 2.64 (95% CI:
  1.16-6.02) times the odds of switching those with positive findings. Among
  RCTs registered when they were ongoing, the odds ... were 8.84 (95% CI:
  3.62-25.93)"; the artifact had stated the 2.6 without population or
  interval; corrected. GRIM — "Of the articles that we could test with the
  GRIM technique (N = 71), around half (N = 36) appeared to contain at least
  one inconsistent mean, and more than 20% (N = 16) contained multiple";
  matches. Janda 2022 (version of record, 547 pairs) — sample size concordant
  86.4%, primary end-point results 81.1%, interpretation 96.2%; the "~89%"
  the artifact carried is the interim conference figure (290/325 = 89.2%);
  corrected to the version of record with the interim noted. Higgins 2003 —
  "we would tentatively assign adjectives of low, moderate, and high to I2
  values of 25%, 50%, and 75%"; Cochrane ch. 10 — "0% to 40%: might not be
  important; 30% to 60%: may represent moderate heterogeneity; 50% to 90%:
  may represent substantial heterogeneity; 75% to 100%: considerable
  heterogeneity" with "Thresholds for the interpretation of the I2 statistic
  can be misleading"; the artifact's non-overlapping 0–25/25–50/50–75/75–100
  bands matched neither and now quote Cochrane. Cochrane ch. 13 / Sterne
  2011 — "As a rule of thumb, tests for funnel plot asymmetry should be used
  only when there are at least 10 studies included in the meta-analysis"
  and "should not be used if the standard errors ... are all similar";
  matches the artifact, which now carries both conditions.

### study-credibility skill — tier 1: appraisal instruments and reporting guidelines
- URLs: https://www.equator-network.org/reporting-guidelines/consort/ ,
  https://www.nature.com/articles/s41591-025-03635-5 (CONSORT 2025) ,
  https://www.riskofbias.info/welcome/robins-i-v2 ,
  https://methods.cochrane.org/bias/resources/rob-2-revised-cochrane-risk-bias-tool-randomized-trials
- Last verified: 2026-08-15 (fetched search summaries)
- Supports: CONSORT 2025 published April 2025 across multiple journals,
  30-item checklist plus flow diagram, superseding CONSORT 2010; SPIRIT 2025
  as the protocol counterpart; ROBINS-I V2 first released November 2024 with
  a revision posted November 2025, adding signalling-question algorithms,
  six bias domains, judgements from Low to Critical, currently scoped to
  follow-up (cohort) studies with other designs in development, and
  preferred over V1 for non-randomized studies in Cochrane reviews.
- Note: reporting guidelines describe required disclosure, not validity.
  The skill states this explicitly because conflating the two is a common
  reader error.

### study-credibility skill — tier 3: research-integrity landscape
- URLs: https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/ ,
  https://retractionwatch.com/ ,
  https://dbrech.irit.fr/pls/apex/f?p=9999:1 (Problematic Paper Screener) ,
  https://www.chemistryworld.com/features/ai-tools-tackle-paper-mill-fraud-overwhelming-peer-review/4022253.article
- Last verified: 2026-08-15 (Problematic Paper Screener URL confirmed live
  with a 200 and page-title match; the rest via fetched search summaries)
- Supports (labeled approximate in the artifact): Crossref acquired the
  Retraction Watch database in September 2023 and publishes it openly, daily
  updated; database past 60,000 entries; five-figure annual retraction counts
  since 2023 driven mainly by mass retractions; roughly 1.5–2% of 2022
  publications closely resembling paper-mill output; the Wiley/Hindawi event
  retracting ~8,000 papers and closing 19 journals; paper-mill detection
  signals (mismatched affiliations, coauthor patterns, fabricated citations,
  tortured phrases, image duplication). Figures are journalism and vendor
  estimates rather than peer-reviewed measurement, so the skill states them
  as approximate trends and never as precise rates.
