# Source weighing

Detail for step 6 of the research workflow: how to rank sources per claim,
grade the body of evidence, count independence, and resolve conflicts.

## Contents

- Authority is contextual: rank by claim type
- Grading the body of evidence
- Independence: count sources, not pages
- Resolving disagreement
- Recency
- Numbers, quotes, and figures
- Hand-offs

## Authority is contextual: rank by claim type

Ask "authoritative for what?" A source can be tier 1 for one claim and tier 3
for the next. Rank per claim.

| Claim type | Highest | Then | Corroborating or labeled |
|---|---|---|---|
| How a tool, model, or API behaves | The vendor's current docs and the code | The vendor's engineering posts, changelogs, issue tracker | Community posts, tutorials, forum answers |
| Whether a technique or intervention improves outcomes | Peer-reviewed studies, systematic reviews, standards-body guidance | Preprints (labeled), benchmark papers, vendor evaluations | Blog posts, case studies, testimonials |
| What a standard or law says | The standard's own text, the statute or ruling | The body's official summaries and FAQs | Explainers, vendor interpretations |
| What software actually does | The code, its tests, tagged releases | Maintainer statements, docs | Third-party descriptions |
| What happened, and when | Primary announcements and records, dated | Independent reporting that cites them | Aggregators, reposts, social posts |
| Prices, limits, and versions | The vendor's live page, dated today | Recent independent reporting, dated | Anything undated |
| Practical patterns and gotchas | Maintainers and issue threads | Experienced practitioners with a track record | Anonymous posts; label as unverified |

Vendor material is highest for how the vendor's own thing behaves and lower
for whether it is better than alternatives. Vendor docs also lag: when the
docs and the code disagree, the code wins and the disagreement is a finding.

## Grading the body of evidence

Grade the evidence behind each load-bearing claim, not each source. This is
GRADE's structure adapted from clinical evidence to desk research; the four
labels keep GRADE's meanings.

| Grade | Meaning |
|---|---|
| **High** | Further evidence is very unlikely to change the conclusion. |
| **Moderate** | Further evidence may change the estimate; the direction is unlikely to flip. |
| **Low** | The conclusion may well be substantially different. |
| **Very low** | Any estimate is very uncertain. |

Start from the source type: a primary source of the highest-ranked type for
this claim starts high; a well-conducted secondary or an independent
measurement starts moderate; a single practitioner report or an undated
page starts low; an inference of your own starts very low.

Rate down one level for each that applies seriously:

- **Risk of bias or conflict of interest** — the source benefits from the
  claim being believed and the design leaves room to steer the result.
- **Inconsistency** — independent sources disagree and you cannot explain
  why.
- **Indirectness** — the source is about a different version, population,
  scale, or setting than the question.
- **Imprecision** — one anecdote, a tiny sample, a wide interval, a
  benchmark with a few items.
- **Selective publication** — only the party with an interest has published;
  failures would not have been reported.

Rate up one level for each:

- **Independent replication** — separate parties, separate methods, same
  result.
- **Direct measurement** — you ran the command, read the code, or the
  source reports a measurement rather than an opinion.
- **Large, consistent effect** that no plausible bias would produce.

Report the grade with the claim, and say what drove it in a few words:
"moderate — vendor docs, confirmed by the code, but a single version".

## Independence: count sources, not pages

Corroboration means separate parties reached the same conclusion by separate
routes. It does not mean the claim appears in many places.

- Trace each page to its origin. Ten pages that quote one press release,
  one benchmark table, or one tweet are one source.
- Ask what each source would know first-hand. A reporter, an aggregator, and
  a model-generated summary usually know nothing first-hand.
- Model-generated pages now saturate search results. A fluent page with no
  author, no date, and no first-hand basis is not a source; treat it as a
  pointer at best.
- Two independent sources with first-hand basis outweigh twenty derivatives.

## Resolving disagreement

Do not split the difference. Find the reason the sources differ:

- **Version or date** — one describes an older release or a rule that
  changed. Prefer the current one and say when it changed.
- **Definition** — the two measure or name different things. Report both
  definitions.
- **Population or setting** — both are right in their own context. Say which
  context matches the question.
- **Measurement** — different methods, one weaker. Prefer the stronger and
  say why.
- **Incentive** — one party benefits from its version. Rate it down; do not
  dismiss it.

When the reason does not resolve, report both positions with their grades
and the reason they differ; that is more useful than a false consensus.
Before finalizing, spend one search on the strongest case against your
leading answer — a search, not a resolution to be balanced.

## Recency

Newer is not truer, but for fast-moving subjects the age of a source is part
of its grade:

| Subject | Sources older than | Are |
|---|---|---|
| Model behavior, prices, API parameters, tool features | about 6 months | Suspect until confirmed against the live page |
| Software behavior, best-practice guidance in fast fields | about 18 months | Suspect; check the changelog since |
| Established method, standards, foundational research | Their own supersession | Fine; note the current revision |

Record the date of every source next to its claim, and mark a claim as
contested when a recent source disagrees with an older consensus.

## Numbers, quotes, and figures

- Copy numbers exactly, with units and denominators. A relative change
  without a base is not a finding.
- Quote short and verbatim, and keep the quote next to the claim in your
  records so the report can show it.
- A figure that reached you through a summary — a search snippet, a fetch
  extraction, a secondary article — is marked as such at the point of use,
  not only in a footer. Readers quote the number and never reach the
  caveat.
- If the primary source could not be read (paywall, 403, dead link), say so,
  and grade any claim resting on it no higher than low.

## Hand-offs

- A single study carrying weight → the configured appraisal skill
  (`appraisal-skill`): design, statistics, spin, funding, replication.
  When none is set, grade it with the table above.
- Durable findings → the configured notes skill (`notes-skill`), with the
  provenance records as the note's sources. When none is set, record
  nothing; the report holds the findings.
- Sources that shaped a skill or rule → the authoring skill's ledger, not the artifact.
