# Conflicts of interest, funding, and other ties

**Contents**
- [What the evidence actually shows](#what-the-evidence-actually-shows)
- [The discretion model](#the-discretion-model)
- [Financial ties: a taxonomy by strength](#financial-ties-a-taxonomy-by-strength)
- [Sponsor role: the mechanism that matters most](#sponsor-role-the-mechanism-that-matters-most)
- [Non-financial interests](#non-financial-interests)
- [Institutional and structural interests](#institutional-and-structural-interests)
- [Reading a disclosure statement](#reading-a-disclosure-statement)
- [Verifying independently](#verifying-independently)
- [Weighing without committing the genetic fallacy](#weighing-without-committing-the-genetic-fallacy)
- [Common errors in both directions](#common-errors-in-both-directions)

---

## What the evidence actually shows

Funding effects are not a suspicion; they are one of the better-replicated findings in meta-research. Knowing the size helps you calibrate instead of hand-waving.

**Industry sponsorship and outcomes.** The Cochrane methodology review by Lundh and colleagues (2017, 75 included papers) found industry-sponsored drug and device studies more often reported favorable efficacy results, RR 1.27 (95% CI 1.17–1.37, 25 papers, moderate-quality evidence), and more often reported favorable conclusions, RR 1.34 (95% CI 1.19–1.51, 29 papers, low-quality evidence). Harms results were *similar* between sponsorship types, RR 1.37 (95% CI 0.64–2.93) — an interval that spans null, drawn from four papers rated very-low-quality. Do not cite the harms figure as a demonstrated effect; it is uninformative, which is itself worth saying when someone claims industry trials systematically hide harms on the strength of this review.

Two findings from that review matter more for appraisal than the headline ratios. First, industry-sponsored studies were **not** methodologically worse on the standard domains — no difference in sequence generation, allocation concealment, follow-up, or selective outcome reporting, and they were *more* often at low risk of bias from blinding (RR 1.25, 95% CI 1.05–1.50). The authors' conclusion is that the effect reflects "an industry bias that cannot be explained by standard 'Risk of bias' assessments." A clean RoB 2 rating therefore does not neutralize sponsorship; the effect operates through question framing, comparator choice, dose selection, which outcomes get emphasized, and which studies get published at all. Second, industry-sponsored studies showed **less agreement between their own results and their conclusions**, RR 0.83 (95% CI 0.70–0.98). That is the most directly actionable finding in the review: it tells you to weight the reported numbers over the authors' interpretation of them.

An earlier systematic review (Bekelman, Li & Gross, JAMA 2003, covering 37 studies) put the association higher: across the 8 studies that assessed sponsorship against outcome (1,140 original studies), industry sponsorship carried 3.6 times the odds of pro-industry conclusions (pooled OR 3.60, 95% CI 2.63–4.91), and approximately one fourth of investigators had industry affiliations. The gap between that figure and Lundh's ~1.3 risk ratio is a reminder that these estimates depend on the measure, the era, and the field — cite them as evidence that the effect is real and non-trivial, not as a precise multiplier to apply to a specific paper.

**How large it can get in a contested area.** Barnes & Bero (JAMA 1998) reviewed 106 review articles on the health effects of passive smoking. 37% (39/106) concluded it was not harmful, and 74% of those (29/39) were written by tobacco-industry-affiliated authors. Controlling for article quality, peer review status, topic, and year, the only factor associated with that conclusion was industry affiliation: adjusted odds ratio 88.4. Note the confidence interval — 16.4 to 476.5. The effect is unmistakably real and its magnitude is barely estimated at all, which is a useful reminder that a huge point estimate from a small sample is still a huge point estimate from a small sample. This is the ceiling case: a well-funded industry facing an existential finding. Most domains look nothing like this, but it establishes that the effect size is not bounded by anything reassuring.

**Selective publication.** Turner and colleagues (2008) compared FDA antidepressant trial registrations against the published literature. Of 74 FDA-registered studies, 31% were never published. 37 of 38 studies the FDA viewed as positive were published; of those the FDA viewed as negative or questionable, 22 were not published and 11 were published in a way that conveyed a positive outcome. **The published literature made 94% of trials appear positive; the FDA's own analysis put it at 51%.** Pooled effect sizes were inflated 32% relative to the full FDA dataset. The individual published papers were not necessarily fraudulent — the distortion was in which ones existed publicly, and in how the negative ones were framed. This is why "each study looks fine" is not a defense of a literature.

**Comparator manipulation.** Bero and colleagues (PLoS Medicine 2007) examined 192 published RCTs comparing one statin against another drug. In multivariate analysis restricted to the industry-funded trials, funding from the maker of the *test* drug was associated with results favoring that drug at OR 20.2, and with conclusions favoring it at OR 34.6, controlling for other factors. Two details from the same paper are worth carrying: 98% of the 192 trials used only surrogate outcome measures, and adequately blinded trials were significantly *less* likely to report results favoring the test drug. Same drug class, different sponsors, different answers — and the discretion ran through the endpoint choice and the blinding.

**Undisclosed ties are common.** In a comparison of physician-author disclosures in NEJM and JAMA against the CMS Open Payments database, a large majority of authors who had received industry payments had payments that went undisclosed. Across clinical practice guideline authors, roughly a third had undisclosed financial relationships with industry. **The practical implication: a paper with no disclosed conflicts has weak evidence of independence, not proof of it.** Absence of disclosure is much less informative than presence of disclosure.

**Outcome switching.** Comparisons of trial registry entries against publications find primary-outcome discrepancies in a large minority of trials. Published rates range from roughly 18% to 45% depending on field, venue, and how strictly a discrepancy is defined — do not quote a single number as the rate. Two findings are more stable than the prevalence figure and more useful: trials whose primary outcome changed report larger intervention effects than those with stable outcomes, and switching is selective rather than random. The selectivity figure comes from one cohort — 294 randomized drug trials from mainland China (Jia et al., J Clin Epidemiol 2021): among trials registered before they started, a registered primary outcome with negative findings had 2.6 times the odds of being switched compared with one with positive findings (OR 2.64, 95% CI 1.16–6.02), and among trials registered while ongoing the odds ratio was 8.84 (95% CI 3.62–25.93). Treat it as evidence that switching is selective, not as a rate that transfers to other registries or fields. Discrepancies are verifiable from public records, which makes this one of the most concrete things you can actually check.

---

## The discretion model

The single most useful framing: **conflicts of interest convert available discretion into directional bias.** They do not create bias out of nothing, and they do not automatically invalidate anything.

So the analysis has two steps, in this order:

**Step 1 — Inventory the discretion.** Where in this study were there defensible choices that could have gone more than one way?

| High discretion | Low discretion |
|---|---|
| Subjective outcomes (pain, symptom scales, clinician impression) | Hard objective outcomes (all-cause mortality, verified events) |
| Unblinded assessment | Blinded assessors and analysts |
| No public protocol or SAP | Preregistered with a published analysis plan |
| Composite or surrogate endpoints | Single prespecified patient-relevant endpoint |
| Many outcomes, subgroups, time points | Few, prespecified |
| Sponsor holds and analyzes the data | Independent data custody and analysis |
| Sponsor drafts the manuscript, controls publication | Authors have unrestricted publication rights |
| Flexible exclusions, per-protocol headline | Intention-to-treat, prespecified exclusions |
| Choice of comparator and dose is free | Head-to-head at established equivalent doses |

**Step 2 — Ask who benefits from how each choice broke.** For each high-discretion point, was it exercised in the direction that favors the interested party? A pattern of choices all breaking the sponsor's way is far more informative than any single choice.

The output of this should be a sentence you can actually write, like: *"The outcome was clinician-rated symptom improvement, assessment was unblinded, and the sponsor's staff performed the analysis — so the funding relationship has a specific and plausible route to the reported effect."* Or: *"The trial was preregistered, the primary outcome was all-cause mortality, an independent committee adjudicated events, and the reported outcome matches the registry — so despite industry funding there is little room for the sponsorship to have produced this result."*

If you cannot write either sentence, you have identified funding but have not analyzed it.

---

## Financial ties: a taxonomy by strength

Roughly ordered by how strongly each predicts directional bias:

1. **Equity, stock options, or patent/royalty interest in the specific product studied.** The strongest tie — the author's personal wealth moves with the result. Also applies to founders and to those with an ownership stake in a company or clinic offering the intervention.
2. **Direct sponsorship of the study by the manufacturer of the thing studied**, especially with operational control (see below).
3. **Employment by the sponsor**, including authors listed with company affiliations. Sometimes disclosed only in the affiliation line rather than the COI statement.
4. **Ongoing consulting or advisory-board relationships** with the sponsor or its competitors.
5. **Speaking fees, honoraria, travel support** — smaller sums, but meta-research finds even modest payments associate with more favorable views, and their effect is systematically underestimated by recipients.
6. **Grant funding from an interested party for other work**, or departmental/institutional funding.
7. **Expert testimony** in litigation touching the question, which creates a commitment to a position on the record.

Also worth noting: ties held by a spouse or dependent children (ICMJE requires these to be disclosed), and ties to the *competitor* of the studied product, which bias in the opposite direction — a genuine phenomenon that is easy to miss when you are only looking for the obvious one.

**Timeframe.** ICMJE asks for relationships in the 36 months before submission, plus funding for the current work with no time limit. A relationship that ended four years ago falls outside the window and will not appear, which is worth remembering when a disclosure looks clean.

---

## Sponsor role: the mechanism that matters most

The money is a proxy. The mechanism is control. Papers usually state this in a "role of the funding source" section — read it carefully, and note when it is absent.

Ask specifically:

- Who designed the study, chose the comparator, and set the dose?
- Who collected the data, and **who held it**? Sponsor-held databases mean the independent authors may never have seen the raw data.
- Who performed the statistical analysis? Sponsor statisticians analyzing sponsor trials is common and is a major discretion point.
- Who drafted the manuscript? **Ghostwriting** — where a sponsor-hired medical communications firm produces the draft and academic authors are added afterward — is documented, and named authors' revisions do not necessarily change the message. Tells include an acknowledgment of "editorial assistance" or "medical writing support" funded by the sponsor, and a mismatch between the paper's polish and the listed authors' output.
- Did the authors have the right to publish regardless of results, and access to all the data? A stated guarantee of unrestricted publication rights and full data access is a genuine positive signal.

The paradigm case for how bad this can get is Study 329 on paroxetine in adolescents: the trial was negative for efficacy and positive for harm, and the ghostwritten publication reported efficacy and safety. Nothing in the paper's surface appearance flagged this; it took independent access to the underlying data.

---

## Non-financial interests

Real, less regulated, and harder to verify — but also more diffuse, and they do not point in a single commercial direction the way a product stake does. Weight them as a reason for scrutiny rather than as equivalent to a financial stake, and be careful, because "everyone has non-financial interests" can be used to launder genuine commercial conflicts by false equivalence.

- **Intellectual allegiance.** A researcher whose career, reputation, and grant pipeline rest on a hypothesis has a real stake in its survival. In psychotherapy research, allegiance effects — the developer of a therapy evaluating that therapy — are large and well-documented, comparable in size to some funding effects.
- **Prior public commitment.** Having argued a position in print, in testimony, or in the press creates pressure toward consistency.
- **Advocacy affiliation.** Employment by or leadership in an organization with a mission position on the question.
- **Political and ideological stakes**, especially in policy, economics, climate, education, criminal justice, and public health research.
- **Career incentives that apply to everyone**: novel, positive, striking results publish; null results and replications do not. This is a background pressure on the entire literature rather than a property of one paper, but it explains why surprising findings are disproportionately likely to be wrong.
- **Personal and professional rivalries**, cronyism, and disciplinary turf — reported by researchers themselves as often *more* prevalent than financial conflicts, particularly in peer review and grant evaluation.

---

## Institutional and structural interests

- **The institution's press office.** University press releases routinely overstate findings; a large share of exaggeration in health news originates there rather than with journalists.
- **The journal's incentives.** Journals sell reprints, and reprint revenue from a pharmaceutical company for a favorable trial can be substantial. Journals also compete for citations, which favors striking results.
- **Think tanks and advocacy research.** Assess funding transparency first: an organization that will not disclose its funders has already told you something. Look for whether the organization publishes findings contrary to its apparent position — an organization that has never reached an inconvenient conclusion is producing advocacy, not research. Also check whether the work went through any external review at all, since much of it does not.
- **Trade associations and industry-funded institutes**, which often carry neutral-sounding names. If an organization's name gives no hint of its backing, look it up rather than assuming.
- **Government and regulatory bodies** have interests too — reputational stakes in past decisions, political pressure, budget justification. Less commercially directional, but not neutral.
- **Litigation-driven research**, produced or funded to support a legal position on either side.

---

## Reading a disclosure statement

- **"The funder had no role in study design, data collection, analysis, or publication"** is a meaningful claim when specific, and boilerplate when generic. Check whether it is contradicted elsewhere — for instance by a company-affiliated author who is also listed as performing the analysis.
- **Check author affiliations against the COI statement.** Company employment sometimes appears only in the affiliation line.
- **"The authors declare no competing interests" on a paper whose subject matter obviously touches commercial interests** is worth an independent check rather than acceptance at face value.
- **Look at the acknowledgments**, not just the disclosures: editorial assistance, statistical support, and data management are frequently where sponsor involvement is recorded.
- **Distinguish the funder of the study from the funder of the authors.** Independent grant funding for the study does not mean the authors have no ties.

---

## Verifying independently

Do not rely solely on what the paper says about itself. See `verification-sources.md` for the full list; the essentials:

- **CMS Open Payments** (openpaymentsdata.cms.gov) for payments from drug and device manufacturers to US physicians and teaching hospitals. This is the single most powerful check available for US medical research, because it lets you directly compare disclosed against actual.
- **ClinicalTrials.gov / registry entries** for the sponsor, the registered primary outcome, and the registered analysis.
- **The authors' other recent papers** — disclosure statements vary between publications, and a fuller statement elsewhere can reveal what is missing here.
- **The funder's own materials** — an organization's website, annual report, or 990 filing often names its backers.
- **Prior corporate history** on the question: has this sponsor previously been found to have suppressed or distorted research?

State clearly which checks you performed and which you could not. "I could not verify" is an honest and useful finding; presenting an unverified assumption as fact is not.

---

## Weighing without committing the genetic fallacy

The genetic fallacy is rejecting a claim because of its origin rather than its content. The rule that keeps you clear of it:

> **A conflict of interest is a reason to look harder at specific things, never by itself a reason to reject a finding.**

Concretely:

- **Do** let a conflict raise your threshold for accepting claims that depend on the researchers' unverifiable discretion.
- **Do** name the specific methodological choice you think the interest could have bent.
- **Do** weight independently-verifiable elements — the registered protocol, the raw numbers, an objective outcome, an independent replication — much more heavily than the authors' interpretation, which is where sponsorship most reliably shows up. The Lundh review found the sponsorship effect on *conclusions* even when the underlying methods were sound.
- **Don't** dismiss a study solely because of who funded it. Much of the best clinical evidence is industry-funded, because that is who runs large trials. Blanket dismissal would discard most of what is known about most drugs.
- **Don't** treat conflict as symmetric with methodology. A rigorous industry-funded trial is better evidence than a sloppy independent one.
- **Don't** assume independence is the same as competence, or that an academic funder is disinterested.
- **Do** consider what independent evidence exists. If a conflicted study agrees with independent replications, the conflict matters much less. If it is the lone outlier supporting a commercially valuable conclusion, the conflict is doing explanatory work.

---

## Common errors in both directions

**Under-weighting:**
- Treating an undisclosed conflict as equivalent to no conflict.
- Accepting "the funder had no role" without checking who analyzed the data.
- Ignoring what is *not* published — the missing negative trials are usually invisible from any single paper.
- Assuming peer review screens for this. It does not, reliably.

**Over-weighting:**
- Dismissing on funding alone without engaging the methods — the genetic fallacy proper.
- Treating any industry contact, however small or old, as disqualifying.
- Applying scrutiny asymmetrically: rigorously auditing the funding of studies you dislike while accepting congenial ones without checking. This is the most common failure among people who believe they are being appropriately skeptical, and it is worth self-checking for.
- Treating "independently funded" as "unbiased," when career, ideological, and publication incentives all still apply.
- Inferring conspiracy from a pattern that ordinary publication bias explains.
