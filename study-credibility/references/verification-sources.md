# Where to verify

**Contents**
- [Finding the paper itself](#finding-the-paper-itself)
- [Retractions and post-publication concerns](#retractions-and-post-publication-concerns)
- [Fabricated papers and paper mills](#fabricated-papers-and-paper-mills)
- [Trial registration and protocols](#trial-registration-and-protocols)
- [Financial ties and funding](#financial-ties-and-funding)
- [Journal and venue legitimacy](#journal-and-venue-legitimacy)
- [Corroboration and context](#corroboration-and-context)
- [Author background](#author-background)

Verify rather than infer, and always distinguish the three states: **confirmed**, **could not access**, and **inferred**. Presenting an inference as a verified fact is the worst outcome of an appraisal, worse than admitting a gap.

---

## Finding the paper itself

- **DOI resolution** — `https://doi.org/<DOI>` gets you to the publisher's page and confirms the paper exists as described.
- **PubMed** (pubmed.ncbi.nlm.nih.gov) — biomedical indexing, and the record carries retraction, correction, and expression-of-concern tags directly under the abstract. Search by PMID or DOI.
- **PubMed Central**, **Europe PMC** — free full text where available.
- **Semantic Scholar**, **OpenAlex**, **Google Scholar** — citation counts, related work, and often an accessible PDF. Citation *context* matters more than count: a heavily cited paper may be heavily cited as an example of what went wrong.
- **Unpaywall**, institutional repositories, and author preprint copies for paywalled work.

**When the publisher's site is paywalled or returns 403** — common for NEJM, Lancet, JAMA, BMJ — do not fall back to third-party summaries before trying Europe PMC's API, which is free and needs no key:

```bash
curl -s 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1136/bmj.l1949"&resultType=core&format=json'
```

The response gives the PMCID, open-access status, and a structured abstract that usually contains the primary results verbatim. If `inEPMC` is `Y`, fetch the full text — including the results tables, which is where per-arm event counts and the numbers behind the headline actually live:

```bash
curl -s 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6538973/fullTextXML'
```

This routinely gets you the real numbers when the journal will not, and the difference between a figure read from the source and one relayed by a summary is the difference between an appraisal and a rumor.
- **medRxiv / bioRxiv / arXiv / SSRN / PsyArXiv** for preprints. Check whether a preprint has since been published, and whether the conclusions changed.

If you cannot reach full text, say so and scope your conclusions to what the abstract supports.

---

## Retractions and post-publication concerns

- **Retraction Watch Database** — now distributed through Crossref, and the most complete source. Note the *reason* for retraction: an administrative or duplicate-publication retraction is very different from data fabrication.
- **PubMed** retraction and correction tags.
- **PubPeer** (pubpeer.com) — post-publication commentary, often where image duplication and statistical inconsistencies surface first. Read critically: comments range from decisive forensic analysis to unfounded complaint, and their presence is a prompt to look, not a verdict.
- **Crossref metadata** for the current status of a DOI.
- **Expressions of concern** — an unresolved editorial flag. Treat as a serious open question, not as clearance.

Always check retraction status when a study is load-bearing for a claim. Retracted papers continue to circulate and continue to be cited approvingly for years.

Retraction volume has risen steeply — the Retraction Watch database passed 60,000 entries, and single years since 2023 have produced five-figure retraction counts, driven mostly by mass retractions of fraudulent work rather than by ordinary error. Read this two ways at once: a retraction is now somewhat more likely to reflect an active integrity apparatus than it once was, and the unretracted literature still contains a backlog that nobody has got to yet.

---

## Fabricated papers and paper mills

Papers produced for sale, with fabricated or recycled data, are a live and growing share of the literature. Estimates put roughly 1.5–2% of papers published in 2022 as closely resembling paper-mill output, and the largest single event to date saw a publisher retract around 8,000 papers and close 19 journals. Generative text tools removed the effort barrier, so volume is the trend to expect.

This matters for appraisal because every method in this skill assumes a real study underneath. Appraising the statistics of a fabricated paper produces a confident and completely wrong answer.

**When to suspect it:** the venue has a mass-retraction or delisting history; author affiliations have no topical connection to the work or to each other; the paper cites sources that do not resolve or that do not say what they are cited for; phrasing is generic or uses tortured synonyms for standard terms; images look duplicated, spliced, or reused across unrelated papers; the data are implausibly clean for the design.

**Where to check:** PubPeer often carries the first public analysis, especially for image problems. The Retraction Watch database shows whether the journal or author has a retraction history. The [Problematic Paper Screener](https://dbrech.irit.fr/pls/apex/f?p=9999:1) flags tortured phrases and fabricated citations across the indexed literature.

Report a suspicion as a suspicion, with the specific signs you observed. Publication in a mill-affected journal is a reason to demand independent corroboration before relying on a finding — it is not by itself proof that a particular paper is fake, and real work does get published in compromised venues.

---

## Trial registration and protocols

- **ClinicalTrials.gov** — US-centric but broad. Compare the **registered primary outcome, timeframe, and analysis plan** against what was published. Check the registration date against enrollment start: registration *after* enrollment began weakens the guarantee. The record also names the sponsor and collaborators.
- **WHO ICTRP** — aggregates international registries.
- **EU Clinical Trials Register / EudraCT** and **ISRCTN** for European trials.
- **PROSPERO** for systematic review protocols.
- **OSF Registries / AsPredicted** for preregistration outside clinical medicine.
- **Registered Reports** — where peer review happened *before* results were known. The strongest available structural guard against outcome switching, HARKing, and publication bias. Worth noting prominently as a positive when present.

Also check whether results were posted to the registry at all. Non-reporting of completed trials is common and is itself a finding.

---

## Financial ties and funding

- **CMS Open Payments** (openpaymentsdata.cms.gov) — mandatory reporting of payments from drug and device manufacturers to US physicians and teaching hospitals. Searchable by name. The highest-value check available, because it permits direct comparison of disclosed against actual.
- **NIH RePORTER** — US federal grant funding by investigator and institution.
- **The journal's own COI and funding statements**, plus the "role of the funding source" section and the acknowledgments.
- **The authors' other recent publications** — disclosures vary between papers, and a fuller statement elsewhere reveals omissions.
- **Company press releases, SEC filings, and pipeline pages** to confirm a commercial interest in the specific product.
- **IRS Form 990** (via ProPublica Nonprofit Explorer or Candid/GuideStar) for US nonprofits, think tanks, and foundations — reveals revenue, major grants, and officers.
- **OpenSecrets** and **LittleSis** for lobbying and organizational relationship mapping.
- **Industry document archives** — the UCSF Industry Documents Library holds internal tobacco, pharmaceutical, chemical, food, and fossil fuel documents released through litigation.

---

## Journal and venue legitimacy

Use several signals together; no single check is sufficient.

- **DOAJ** (doaj.org) — vetted open-access journals. Inclusion is a positive signal.
- **Scopus, Web of Science, PubMed/MEDLINE indexing** — legitimate journals are generally indexed somewhere substantial. Beware fake or self-invented "impact factors"; verify against Journal Citation Reports if a figure is claimed.
- **ISSN Portal** (portal.issn.org) to confirm the ISSN is real and matches the title.
- **COPE, OASPA, or STM membership** — publisher-level commitments to publication ethics.
- **Think. Check. Submit.** (thinkchecksubmit.org) — a structured checklist.
- **Cabells Predatory Reports** — subscription, uses dozens of weighted indicators.
- **Beall's List** — archived and unmaintained since 2017. Historically useful, but out of date; a journal's absence proves nothing and its presence may be stale. Never rely on it alone.

**Website red flags:** guaranteed rapid publication, hidden or surprise fees, a scope so broad it spans unrelated fields, editorial board members who cannot be verified or who did not consent, spam solicitation, grammatical errors throughout, stock photography, broken links, and a name closely mimicking an established journal.

Remember the asymmetry: publication in a reputable indexed journal is **weak** positive evidence, since peer review catches relatively little. Publication in a clearly predatory venue is **strong** negative evidence, because it usually means no meaningful review occurred at all.

---

## Corroboration and context

- **Cochrane Library** — systematic reviews with generally strong methodology and explicit COI policies.
- **Epistemonikos, Trip Database, Google Scholar "cited by"** to find syntheses and later work.
- **Clinical practice guidelines** for what expert bodies concluded — while remembering that guideline panels have their own documented conflict problems.
- **Regulatory reviews** — FDA and EMA assessment documents contain data from unpublished trials and independent statistical review, and are among the few ways to see the evidence base rather than the published subset.
- **Failed replications**, replication projects, and adversarial collaborations in the relevant field.

---

## Author background

- **ORCID** for a verified publication record.
- **Institutional pages** to confirm affiliation and position, which are occasionally misrepresented.
- **Google Scholar profiles** for output patterns — including whether an author publishes only in one direction on a contested question.
- **Prior retractions or misconduct findings** associated with the author.

Keep this proportionate. The point is to assess the work, and author background is context for how much independent verification the work needs — not a substitute for reading it. Avoid assembling personal profiles beyond what bears on the research question at hand.
