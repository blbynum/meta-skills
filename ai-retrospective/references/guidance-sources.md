# Checking current guidance

## Contents

- Why fetch instead of recall
- Entry points
- Fetching cheaply
- Which page for which finding
- Recording what you checked

## Why fetch instead of recall

Agent and prompting guidance changes with each model release, and each release
ships its own prompt changes. Recalled advice is routinely a release or two
stale: verification instructions that helped on one model waste tokens on the
next, subagent-delegation defaults differ between models of the same
generation, and harness features arrive faster than any training cutoff. A
retrospective that grades a session against stale guidance produces confident
wrong findings, which is worse than no finding.

So: fetch before you conclude. Fetch the pages for the model that actually ran
the session — read the model id from the transcript header, do not assume it
matches the model running the retrospective.

## Entry points

Model and prompting guidance, on `platform.claude.com/docs/en/`:

- `build-with-claude/prompt-engineering/claude-prompting-best-practices` —
  shared techniques, plus links to a per-model page.
- `build-with-claude/prompt-engineering/prompting-claude-<model>` — the
  per-release page (for example `prompting-claude-opus-5`). This is where
  per-model behavior lives: verbosity, subagent eagerness, self-verification,
  scope expansion, literal instruction following.
- `agents-and-tools/tool-use/overview` and its children — when Claude calls
  tools, parallel tool use, tool definitions.

Harness guidance: the harness's own documentation on subagents, skills,
rules or memory files, hooks, settings, permissions, and cost. The
reference for the harness you run in lists the pages and how to fetch
them cheaply; for a harness with no reference, start from its docs index.
For a session that ran another vendor's model, fetch that vendor's
prompting guide instead of Anthropic's.

Anthropic engineering blog, `https://www.anthropic.com/engineering` — the index
lists posts with dates, so read the index first and pick what is current rather
than fetching a post you remember. Recurring relevant titles include effective
context engineering, writing effective tools for agents, harness design for
long-running agents, and Claude Code best practices.

## Fetching cheaply

- Prefer a docs index and a plain-text or markdown rendering of a page
  where the site offers one; a rendered landing page can burn thousands of
  tokens on install instructions. The harness reference names both for
  Claude Code.
- Budget three to five fetches, chosen by what the session's facts show. Fetch
  the per-model prompting page in every run; choose the rest from the table
  below. Fetching everything is its own waste.

## Which page for which finding

| The session showed | Check |
|---|---|
| Odd tool choices, tool avoidance, over-calling | tool-use overview; per-model prompting page |
| Serial calls that were independent | tool-use parallel tool use page |
| Subagent spawned, scoped, or skipped badly | the harness's subagents page; per-model page (delegation eagerness differs by model) |
| A skill did not fire, or fired wrongly | the harness's skills page; skill authoring best practices |
| A rule was loaded but not followed | the harness's rules or memory page; per-model page on instruction literalness |
| Permission prompts, denials, hook behavior | the harness's permissions, hooks, and settings pages |
| Context filled, work redone after summarization | effective context engineering post; the harness's cost page |
| Long multi-phase task drifted | the harness's workflows page; harness-design engineering post |

## Recording what you checked

Every claim about current practice carries its source and the date you fetched
it: `<docs host>/sub-agents — checked 2026-08-15`. Put the list at
the end of the report.

Any recommendation you cannot tie to a page you fetched in this run is your own
judgment. Label it as such in the finding itself, not only in a footnote. A
reader must be able to tell which recommendations rest on published guidance
and which rest on your reading of the session.
