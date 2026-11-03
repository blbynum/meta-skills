# Sources — research

Provenance ledger for the research skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

### research skill — tier 1: Anthropic and Claude Code
- URLs: https://www.anthropic.com/engineering/multi-agent-research-system ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool ,
  https://code.claude.com/docs/en/tools-reference (WebFetch and WebSearch
  behavior sections) , https://code.claude.com/docs/en/sub-agents ,
  https://code.claude.com/docs/en/workflows , and the "Research and
  information gathering" and "Subagent orchestration" sections of the
  prompting best-practices page listed under Tier 1 above
- Last verified: 2026-08-15 (all fetched)
- Supports: orchestrator-worker research with parallel subagents; effort
  scaling by query complexity ("Simple fact-finding requires just 1 agent
  with 3-10 tool calls, direct comparisons might need 2-4 subagents with
  10-15 calls each, and complex research might use more than 10 subagents");
  "start wide, then narrow" because agents "default to overly long, specific
  queries that return few results"; each subagent brief needs "an objective,
  an output format, guidance on the tools and sources to use, and clear task
  boundaries"; early agents "consistently chose SEO-optimized content farms
  over authoritative but less highly-ranked sources" until source-quality
  heuristics were added; observed failure modes (excess subagents for simple
  queries, endless search for nonexistent sources, duplicated subagent work,
  research continuing past sufficiency); "instilling good heuristics rather
  than rigid rules"; a citation pass after research; token usage explains
  80% of BrowseComp variance (the depth side of the depth-vs-breadth
  tension). Web search docs: citations always on with `cited_text` up to
  150 characters and `page_age`; "Simple factual queries typically use 1–3
  searches; comparative or multientity research can use 10 or more". Web
  fetch docs: fetches only URLs already seen in the conversation or in
  prior search/fetch results; explicit exfiltration warning; citations
  optional; PDF sizes (~125k tokens for a 500 kB paper). Claude Code tools
  reference: WebSearch returns titles and URLs only and "may issue up to
  eight backend searches per call"; WebFetch "is lossy by design" — a small
  model answers the extraction prompt, so "a result that says a page doesn't
  mention something may only mean the prompt didn't ask about it", with
  re-fetch or `curl` as the remedy; 15-minute cache; cross-host redirects
  returned rather than followed; a 200-call session search cap "counted
  across the main conversation and every subagent". Sub-agents doc: use
  subagents for self-contained work returning a summary and for parallel
  independent investigations; a subagent "doesn't see your conversation
  history"; concurrency 20, nesting depth 3. Workflows doc: `/deep-research`
  is a bundled workflow that "runs only when you invoke it" (the version
  anchor is in the Claude Code CHANGELOG, not this doc: 2.1.218 "Changed
  `/deep-research` to start only when invoked manually; Claude no longer
  launches it on its own"), fans out searches, cross-checks
  and votes on claims, and lists unverifiable claims as unverified; the
  "stop once two rounds in a row find nothing new" example. Prompting page:
  "Provide clear success criteria", "verify information across multiple
  sources", "develop several competing hypotheses. Track your confidence
  levels ... research notes file", and the subagent-overuse damping prompt.

### research skill — tier 1: other vendors' deep-research documentation
- URLs: https://developers.openai.com/api/docs/guides/deep-research ,
  https://ai.google.dev/gemini-api/docs/deep-research
- Last verified: 2026-08-15 (fetched)
- Supports (for their own products only): OpenAI recommends a clarification
  step before research, steering toward primary sources ("the original paper
  or official journal publication" over aggregators), `max_tool_calls` as
  the cost lever, and warns of prompt injection through web content with a
  worked exfiltration example. Google's loop is "Plan -> Search -> Read ->
  Iterate -> Output"; it recommends stating output structure, telling the
  agent how to handle missing data ("explicitly state they are projections
  or unavailable rather than estimating"), and "reviewing the citations
  provided in the response to verify the sources". Neither addresses
  contradictory sources or stopping.

### research skill — tier 2: agent benchmarks and audits
- URLs: https://arxiv.org/html/2506.06287 (Deep Research Bench, FutureSearch,
  May 2025) , https://arxiv.org/html/2504.12516 (BrowseComp, OpenAI, April
  2025) , https://arxiv.org/abs/2311.12983 (GAIA, 2023) ,
  https://arxiv.org/html/2509.04499 (DeepTRACE, Sept 2025) ,
  https://arxiv.org/html/2605.06635 (Cited but Not Verified, May 2026) ,
  https://arxiv.org/html/2604.03173v1 (reference hallucination in
  commercial LLMs and deep research agents, April 2026) ,
  https://arxiv.org/html/2404.10198v2 (ClashEval, NeurIPS 2024; via fetched
  search summary) , https://arxiv.org/html/2605.14473v4 (Does RAG Know When
  Retrieval Is Wrong?, July 2026) , https://arxiv.org/pdf/2504.18575
  (WASP, 2025; via fetched search summary) ,
  https://arxiv.org/abs/2506.18096 (Deep Research Agents roadmap survey)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports: Deep Research Bench — "forgetting information" is the strongest
  predictor of task failure (coefficient −0.843); repeated searches common;
  hallucination "not the central issue"; "a tendency towards satisficement
  rather than optimization" with minimum-effort answers; search terms
  "overly influenced" by task phrasing; best agent 0.51 against a ~0.8 noise
  ceiling. BrowseComp — humans solved 29.2% and gave up on 70.8% within two
  hours; accuracy scales with browsing effort and parallel sampling; models
  with browsing showed higher calibration error, "access to web tools may
  increase the model's confidence in incorrect answers"; success needs
  "strategic perseverance, flexible search reformulation, and ability to
  assemble fragmented clues". GAIA — questions "conceptually simple for
  humans yet challenging for most advanced AIs" (92% vs 15%). DeepTRACE —
  deep research agents 54.7–94.8% one-sided on debate queries, 53.6–97.5%
  unsupported statements, citation accuracy 50.3–79.1%; "more sources and
  longer answers do not translate into reliability". Cited but Not Verified
  — 14 models: link works >94%, content relevant >80%, but factual accuracy
  of the cited claim only 39–77%; raising tool calls from 2 to 150 dropped
  GPT-5.4's fact-check accuracy from 78.6% to 16.7% and Claude Opus 4.6's
  from 80% to 57.9% ("information overload effect"); recommends "depth of
  source understanding over breadth of source coverage" (the breadth side
  of the depth-vs-breadth tension). Reference hallucination — 3–13% of
  cited URLs fabricated even with web search, 5–18% non-resolving, deep
  research agents highest; a URL-check tool cut non-resolving citations to
  under 1% when the model acted on it. ClashEval — models adopt incorrect
  retrieved content over a correct prior over 60% of the time, more so when
  the wrong content is realistic and the model's prior confidence is low.
  Does RAG Know — standard RAG at 15% accuracy under adversarial
  misconception injection; conflict-aware decomposition helps. WASP —
  partial injection success up to 86%, "security by incompetence" rather
  than robust defense. Roadmap survey — definition and taxonomy of deep
  research agents; open challenges include sequential inefficiency and
  metric misalignment.
- Contradiction recorded 2026-08-15: Anthropic's post ties research quality
  to token spend (more effort → better on BrowseComp) while the 2026 audits
  find more retrieval into one context lowers citation factual accuracy.
  They measure different things (finding hard facts vs faithful synthesis);
  the research skill resolves it as fan-out into fresh contexts with a lean
  synthesizing context, and labels this a judgment call.

### research skill — tier 2: research methodology (academic and standards)
- URLs: https://www.ala.org/acrl/standards/ilframework (ACRL Framework,
  2016; revision draft out for comment through May 2026) ,
  https://wp.comminfo.rutgers.edu/ckuhlthau/information-search-process/
  (Kuhlthau ISP; via fetched search summary) ,
  https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html (Bates 1989)
  , Ellis 1989/1993 (via fetched search summary) ,
  https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
  (Cochrane Handbook 6.5.1, chapter 4, March 2025) ,
  https://www.prisma-statement.org/prisma-2020 (PRISMA 2020) ,
  https://arxiv.org/abs/2307.02612 (Wohlin et al., hybrid database search
  plus snowballing) and Wohlin 2014 snowballing guidelines (via search) ,
  https://gdt.gradepro.org/app/handbook/handbook.html (GRADE handbook) ,
  https://journals.sagepub.com/doi/10.1177/016146811912101102 (Wineburg &
  McGrew 2019, via fetched search summary) and
  https://www.scienceofboosting.org/project/lateral-reading/ (evidence
  base for lateral reading) , SIFT (Caulfield; library guides and Brodsky
  et al. 2021 via search) , Lord, Lepper & Preston 1984 and Mussweiler et
  al. 2000 (consider-the-opposite; via fetched search summary) , Nickerson
  1998 (confirmation bias; via search) ,
  https://aisel.aisnet.org/misq/vol31/iss1/7/ (Browne, Pitts & Wetherbe
  2007, MIS Quarterly) plus the AMCIS 2016 and TRR replications , Ilani et
  al. 2024 systematic review of stopping behavior (abstract) , capture–
  mark–recapture as a stopping rule (Kastner et al. 2009) and Booth 2010
  "How much searching is enough?" (via search) , Tetlock's Good Judgment
  Project findings (via fetched search summaries)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports: ACRL — "Authority Is Constructed and Contextual", "Research as
  Inquiry" (formulate questions from gaps and conflicting information;
  monitor for gaps), "Searching as Strategic Exploration" ("first attempts
  at searching do not always produce adequate results"; refine strategy
  from results), skeptical stance with self-awareness of bias. Kuhlthau —
  six stages with exploration before focus formulation; the uncertainty
  principle ("information commonly increases uncertainty in the early
  stages"). Bates — the evolving query, "bit-at-a-time" retrieval, and six
  techniques (footnote chasing, citation searching, journal run, area
  scanning, subject searches, author searching), which ground the chaining
  moves table. Ellis — starting, chaining, browsing, differentiating,
  monitoring, extracting, verifying, ending. Cochrane — "aim for high
  sensitivity, which may result in relatively low precision"; search
  multiple sources including grey literature, reference lists, and
  contacting experts; text words plus controlled vocabulary; avoid too many
  concepts; peer-review the search; document and report the search
  (PRISMA-S); "balance the thoroughness of the search with efficiency in
  the use of time and funds" (section 4.4.11 on stopping was not
  retrievable through the fetch). PRISMA 2020 — transparent, replicable
  reporting of sources, strategies, selection, and certainty. Wohlin — the
  hybrid strategy "identified 30 percent more primary studies" than either
  alone. GRADE — four certainty levels with their verbatim meanings; RCTs
  start high, observational low; rate down for risk of bias, inconsistency,
  indirectness, imprecision, publication bias; rate up for large effect,
  dose-response, residual confounding; certainty applies to the body of
  evidence per outcome, not per study — adapted in source-weighing.md.
  Wineburg & McGrew — fact-checkers "read laterally, leaving a site after a
  quick scan and opening up new browser tabs" while historians and students
  "read vertically" and fell for surface features; interventions of hours
  produce measurable gains. SIFT — Stop, Investigate the source, Find
  better coverage, Trace claims to the original. Lord et al. — a
  consider-the-opposite instruction "had greater corrective effect than more
  demand-laden alternative instructions to be as fair and unbiased as
  possible"; Mussweiler — considering the opposite reduces anchoring.
  Browne et al. — "people utilize a number of stopping rules to terminate
  search, and that the stopping rule used depends on the type of task";
  replications confirm for structured tasks and find drift for poorly
  structured ones. The five named rules (mental list, representational
  stability, difference threshold, magnitude threshold, single criterion)
  are trained knowledge verified only at abstract level on this pass. Ilani
  2024 — "the lack of a comprehensive model of factors affecting search
  stopping behavior" (the evidence-is-thin statement). Capture–recapture and
  Booth — empirical stopping estimates exist for systematic reviews but
  not for desk research. Tetlock — granular probabilities, frequent small
  updates, base rates and the outside view.

### research skill — tier 3: community
- URLs: https://paddo.dev/blog/three-ways-deep-research-claude/ ,
  https://github.com/Weizhena/Deep-Research-skills ,
  https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
  (Tow Center, March 2025; via fetched search summary)
- Last verified: 2026-08-15 (fetched unless noted)
- Supports (corroboration or labeled unverified): the practitioner account
  that led to the `/deep-research` workflow (confirmed against the Claude
  Code docs); community research skills converge on outline → parallel
  per-item search → report with a human checkpoint after the outline
  (adopted only as "ask one question when it changes the work"); the Tow
  Center test of eight AI search engines found over 60% of source-
  identification answers wrong and most wrong answers given confidently
  (corroborates the tier-2 audits, tier 3 because it is journalism rather
  than peer review).
