# Sources — ai-retrospective

Provenance ledger for the ai-retrospective skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

### ai-retrospective skill — runtime guidance entry points
- URLs: https://code.claude.com/docs/llms.txt ,
  https://www.anthropic.com/engineering ,
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Last verified: 2026-08-15 (all three fetched)
- Supports: `llms.txt` is a compact index of every Claude Code doc page, and
  those pages accept a `.md` suffix for clean markdown — fetching the rendered
  `/docs/en/overview` page instead costs thousands of tokens on install
  instructions. The engineering index lists posts with dates, so it works as a
  freshness check rather than a fixed post list. Page URLs confirmed present:
  `best-practices`, `sub-agents`, `skills`, `memory`, `hooks-guide`,
  `settings`, `permissions`, `mcp`, `workflows`, `costs`, `output-styles`.
  The tool-use overview supports steerable tool-calling boundaries via the
  system prompt and links a dedicated parallel-tool-use page.

### ai-retrospective skill — session analysis and compaction
- URLs: https://code.claude.com/docs/en/costs.md ,
  https://code.claude.com/docs/en/best-practices.md
- Last verified: 2026-08-15 (both fetched)
- Supports: `/insights` analyzes up to 200 recent local sessions and writes an
  HTML report on how the user works, including friction points — adjacent to
  ai-retrospective from the other direction (many sessions, user patterns,
  versus one session, agent execution), so the skill points at it rather than
  duplicating it. Auto-compaction "summarizes older history to free space"
  and `/compact` "reads the conversation it summarizes". Recorded evidence
  gap: neither page states whether the on-disk transcript keeps the
  pre-compaction turns, and none of 92 local transcripts had ever compacted,
  so the ai-retrospective skill now instructs the agent to verify this on the
  first compacted session it meets rather than assert it. Also grounds the
  context-window-as-binding-constraint framing used to rank findings by cost.
