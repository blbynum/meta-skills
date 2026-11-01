---
name: study-credibility
compatibility: Verification examples use curl against public literature APIs.
metadata:
  harness: portable
  export: portable
  last-verified: "2026-08-15"
description: Evaluates whether a study, paper, trial, meta-analysis, preprint, or research-backed claim is trustworthy and what it actually supports — appraising design, statistics, spin, replication status, and the funding, financial ties, and ideological interests behind it. Use whenever someone shares a study, DOI, PubMed/journal link, preprint, or news article about research and asks if it is legitimate, reliable, credible, well-designed, biased, industry-funded, or worth believing — including softer forms like "is this true?", "should I trust this?", "does this prove X?", "who paid for this?", or "debunk this." Use proactively when someone leans on a single study to support a health or factual claim, mentions a supplement, drug, diet, or policy study, or asks you to reconcile conflicting studies — even if they never say "credibility" or "evaluate."
---

# Evaluating study credibility

The goal is not to sort studies into "good" and "bad." It is to answer a sharper question: **given how this study was built, who built it, and what constrained them, what claim does it actually license — and how far is that from the claim being made about it?**

Most bad appraisals fail in one of two directions. They either produce a bland strengths-and-limitations list that would apply to any paper ("small sample size, more research needed"), or they discover industry funding and stop thinking. Both skip the real work, which is figuring out where *this specific study* is load-bearing and where it is soft.

## The two axes

Hold two separate questions in mind and don't let them collapse into each other.

**Evidential strength** — what the design, execution, and statistics can support, assuming everyone acted in good faith. A study can be honest and still be too small, too short, or measuring the wrong thing.

**Independence** — how much room existed for the result to be steered toward a preferred conclusion, and whether the safeguards that close that room were actually in place.

These interact through one concept that should drive most of your COI reasoning:

> **Conflicts of interest are a magnifier of discretion, not a fixed penalty.**

Discretion is the number of defensible choices standing between the raw data and the reported headline. When discretion is low — a preregistered trial with a published statistical analysis plan, blinded assessors, a hard objective outcome like all-cause mortality, data held independently of the sponsor — a conflicted sponsor has few levers to pull, and the funding matters much less than people assume. When discretion is high — subjective or composite outcomes, unblinded assessment, no protocol, many measured variables, sponsor-controlled analysis, flexible exclusion rules — sponsorship is a strong predictor of which way those choices broke.

So the sequence is: find the discretion, then ask who benefits from how it was exercised. A heavily conflicted study with almost no discretion can still be good evidence. A conflict-free study with enormous discretion can still be unreliable — just unreliable in a less predictable direction.

This also keeps you clear of the genetic fallacy. Funding is a reason to look harder at specific places, never a reason to dismiss a finding on its own. If you would not be able to say *which* methodological choice the funding plausibly bent, you have not finished the analysis.

## Workflow

Copy this checklist into the response for a full appraisal. For a quick "is
this legit?", steps 1, 2, and 6 are the minimum that keeps you honest.

```
- [ ] 1. Get to the primary source
- [ ] 2. Separate the claim from the measurement
- [ ] 3. Match the design to the question
- [ ] 4. Interrogate the numbers
- [ ] 5. Map the interests
- [ ] 6. Check the paper's standing in the world
- [ ] 7. Deliver a verdict that commits
```

### 1. Get to the primary source

News coverage, press releases, abstracts, and social media summaries routinely misstate what a study found — press releases from the institution are a frequent origin of the distortion, not just the journalism downstream. If the user gives you coverage, find and read the study itself. If you cannot reach the full text, say so explicitly and mark every conclusion that depends on unread methods as provisional. Abstract-only appraisal is real but limited work; do not present it as if you read the paper.

Record what you have access to: full text, abstract only, preprint, press release. This shapes how confident your verdict is allowed to be.

### 2. Separate the claim from the measurement

Write out, in your own words:
- What the study actually measured, in whom, for how long, compared to what.
- What the paper's abstract and conclusion say it means.
- What the user (or the article, or the headline) says it means.

The gaps between these three are usually where the whole story lives. Common gaps: a surrogate endpoint (cholesterol, tumor markers, biomarkers) reported as if it were a patient outcome; an association reported in causal language; an effect in mice reported as an effect in people; a subgroup finding reported as the main result; a short trial reported as evidence about lifelong use.

Look specifically for **spin** — a conclusion that is more favorable than the results support. Classic tells: the primary outcome missed significance but the abstract leads with a secondary outcome, a subgroup, or a per-protocol analysis; a null result described as "trending toward" or "comparable to"; a relative risk reduction quoted with no absolute numbers.

### 3. Match the design to the question

The right appraisal tool depends on the design, and the right *expectation* depends on the claim. Read `references/design-appraisal.md` for design-specific checklists (randomized trials, cohort and case-control, cross-sectional and survey, systematic reviews and meta-analyses, animal and in-vitro, modeling and simulation, and qualitative work) and pull the section that applies.

The core question in every case is which specific mechanism could produce this result other than the one being claimed — confounding, selection, measurement error, reverse causation, chance. Naming a generic risk of bias is not enough; name the confounder or the selection mechanism you actually think is operating and say why it is plausible here.

Do not apply a rigid evidence hierarchy. A well-conducted large cohort study beats a tiny, poorly-run trial, and some questions cannot ethically be randomized at all. What matters is whether the design can rule out the alternatives that matter for this specific claim.

### 4. Interrogate the numbers

Read `references/statistics-and-spin.md` for the full set, including the base rates for how often each of these problems occurs. The high-yield checks:

- **Effect size, not just significance.** Get the absolute effect, not only relative. A 50% relative reduction on a 0.2% baseline risk is a 0.1 percentage point change.
- **Precision.** How wide is the confidence interval, and what is the least impressive value it is compatible with? A "significant" result whose interval nearly touches null is weak evidence, not strong.
- **Power and sample size.** Small studies do not just miss real effects; when they do reach significance, the effect is necessarily overestimated. A surprisingly large effect from a small study is a reason for suspicion, not excitement.
- **Multiplicity.** How many outcomes, subgroups, time points, and model specifications were available? Count them. Significance at p<0.05 means little if twenty comparisons were run and one is reported.
- **Internal consistency.** Do the numbers cohere — do percentages match the stated N, do subgroup sizes sum to the total, are means possible given the sample size and scale? Inconsistencies are common and worth flagging even though they usually indicate sloppiness rather than fraud.

### 5. Map the interests

Read `references/conflicts-of-interest.md` for the taxonomy, the empirical evidence on how much each tie actually predicts, and where to verify. In brief, look for:

- **Who funded the work**, and whether the funder makes or sells the thing being studied — or has a stake in the policy question.
- **The sponsor's operational role**: design, data collection, custody of the data, statistical analysis, manuscript drafting, and veto over publication. This matters far more than the money itself, because it is the mechanism through which discretion gets exercised. A sponsor that wrote the check is different from a sponsor that held the database and wrote the draft.
- **Author ties** beyond the study: consulting, speaking fees, equity, patents, board seats, expert testimony.
- **Non-financial interests**: a career built on the hypothesis, prior public commitment to the position, advocacy-organization affiliation, ideological or political stake. These are less regulated, harder to verify, and routinely underweighted — but they are also more diffuse and less directional than a commercial stake in a specific product.
- **The absence of a disclosure statement is weak evidence of absence.** Undisclosed ties are common enough that a clean-looking paper warrants a check against an independent source, not an assumption of independence.

Verify rather than infer wherever you can, and be precise about which you did. "The paper discloses funding from X" and "I could not determine funding" and "I found payments from X in an independent database that the paper did not disclose" are three very different findings, and the third is a serious one.

### 6. Check the paper's standing in the world

A study is not just a document; it has a history. Check:

- **Retraction, correction, or expression of concern.** Always worth checking, and easy to miss because retracted papers keep circulating and keep getting cited approvingly.
- **Preregistration and protocol.** Does a registry entry exist? Does the reported primary outcome match the registered one? Outcome switching is common and inflates effect estimates. A mismatch you can actually document is one of the most damning specific findings available.
- **Replication and independent corroboration.** Has anyone reproduced it? Does it fit or contradict the larger body of evidence — and if it contradicts, is it a genuine outlier or the first crack in a consensus? Single studies overturning a well-established finding are usually wrong, but not always, so say what would distinguish the cases.
- **The venue.** Is the journal real and indexed, or predatory? Is it a preprint that never completed peer review, and how long has it sat? Peer review catches less than people think, so a good journal is weak positive evidence and a bad one is strong negative evidence — the asymmetry matters.
- **Post-publication scrutiny.** Substantive published criticism, failed replications, or documented methodological objections.
- **Whether the study happened at all.** Fabricated papers are now produced industrially, and generative text tools removed the effort barrier that used to keep the volume low. Suspect this when several signs cluster: a journal that ran a mass retraction, an author list with no topical connection to the work or to each other, boilerplate phrasing, citations that do not resolve, tortured synonyms for standard terms ("bosom peril" for breast cancer), and data too clean for the design. Treat it as a question about provenance rather than an accusation, and check the venue's retraction history before you spend effort appraising methods that may be fictional.

`references/verification-sources.md` lists where to check each of these.

### 7. Deliver a verdict that commits

Vague hedging is a failure mode, not caution. Say what you think, with the uncertainty attached to the specific parts that are uncertain.

## Output format

Adapt the depth to the request — a quick "is this legit?" deserves a tight answer, a formal appraisal deserves the full structure — but always cover these, in this order:

**Bottom line.** Two or three sentences: how much weight this study can bear, and the single most important reason. Lead with it.

**What the study actually shows.** The claim the evidence licenses, stated precisely, with the absolute effect size and the population it applies to. Where this differs from the headline claim, say so plainly.

**Confidence rating.** One of: **High** / **Moderate** / **Low** / **Very low** confidence in the study's central claim. Give the rating and the reason. Do not invent a numeric score — a "73/100" implies a precision that does not exist and invites the reader to skip the reasoning. If the user explicitly asks for a number, give the tier and explain why you are not manufacturing false precision.

**Key strengths.** Only the ones that are genuinely load-bearing. If there are none worth naming, say that instead of padding.

**Main threats to validity.** Ranked, specific, and mechanistic. Not "possible confounding" but "smokers were more likely to be in the exposed group and smoking status was self-reported at baseline only." For each, say roughly how much it could move the result and in which direction.

**Interests and independence.** Funding, sponsor role, author ties, non-financial stakes. Then the crucial sentence: *given the discretion this design allowed, here is specifically where those interests could have bent the result* — or, if the design was tight, say that the safeguards limit how much the funding matters here. Never leave this as a bare fact about who paid.

**What would change the picture.** What evidence would raise or lower your confidence — a replication, access to the protocol, the unpublished trials, a longer follow-up. This tells the reader what to look for next and marks the boundary of what you know.

**Verification status.** Briefly: what you checked and confirmed, what you could not access, and what you are inferring rather than knowing. Never present an inference as a verified fact.

A closing verification section does **not** license confident-sounding numbers earlier in the response. If a specific figure — a hazard ratio, a confidence interval, a sample size, a p-value — came from a secondary summary rather than the primary source, mark it at the point where you state it, not only in a footer. Readers quote the number from the body and never reach the caveat, and a transcribed statistic is exactly the kind of thing that drifts as it passes through summaries. When a paper is paywalled, check whether an open-access copy of the record exists (PubMed and Europe PMC carry structured abstracts with the primary results, and Europe PMC often has full text) before settling for a third-party description.

## Judgment calls

**When you can't access the full text**, appraise what you can and be loud about the limit. An abstract supports conclusions about claimed effect sizes and obvious design mismatches; it does not support conclusions about analysis quality or how outcomes were actually assessed.

**When the study is fine but the claim is not**, that is the finding — say the study is sound and the coverage is wrong. This is the most common real-world case, and it is more useful than either "good study" or "bad study."

**When you find a serious integrity problem** — a documented outcome switch, an undisclosed tie, impossible numbers, a retracted citation load-bearing to the argument — lead with it. Do not bury it under a balanced-sounding list.

**When evidence conflicts**, do not average it. Work out why the studies disagree: different populations, different doses, different outcome definitions, different lengths, different discretion. The explanation is more informative than a split verdict.

**When the honest answer is "this single study can't settle it"**, say that clearly rather than manufacturing a verdict. But pair it with what the broader evidence base does support, so the user is not left with nothing.

**Keep proportion.** Every study has limitations; listing them all flattens the important ones into noise. Two or three real threats, explained well, beat a checklist of twelve. If a limitation would not change the conclusion, either say so or leave it out.
