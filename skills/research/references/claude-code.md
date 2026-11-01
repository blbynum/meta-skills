# Claude Code

What differs when the research skill runs in Claude Code. Read this when you
run there, before step 3 of the workflow. Nothing here applies in another
harness, and nothing here belongs in the portable body.

## Search and fetch tool behavior

These facts change how you use the tools; check them against the Claude Code
tools reference when something behaves differently.

- **WebSearch** returns titles and URLs, and may run several backend searches
  per call. It does not fetch pages. Its domain filter is `allowed_domains`
  or `blocked_domains`; the two cannot be combined in one call.
- **WebFetch** is lossy by design: it fetches the page, converts it to
  Markdown, and answers your extraction prompt with a small, fast model. You
  receive that answer, not the page. A result that says the page does not
  mention something may only mean the prompt did not ask about it. Re-fetch
  with a narrower prompt, or `curl` the raw page from Bash when the exact
  wording matters.
- WebFetch truncates large pages, caches responses for 15 minutes, upgrades
  HTTP to HTTPS, and returns a cross-host redirect as a message instead of
  following it — fetch the target URL in a second call. It does not render
  JavaScript-only pages. PDFs work; long PDFs are expensive.
- The API's web fetch tool can only fetch URLs that already appeared in the
  conversation or in a prior search or fetch result. Do not invent a URL and
  fetch it; search for it first.
- Search results carry a `page_age`; fetch results carry `retrieved_at`.
  Record the date with the claim.

## The session search cap

A session has a hard cap on WebSearch calls (200 by default), counted across
the main conversation and every subagent it spawns. A capped call looks like
a search that returned nothing. Budget accordingly and prefer fetching known
pages over re-searching.

## The bundled deep-research workflow

A broad web question that wants many angles fetched and cross-checked in the
background is what the bundled `/deep-research` workflow does. Only the user
can start it; name it as an option when the question fits, then continue
with the inline workflow unless they take it.
