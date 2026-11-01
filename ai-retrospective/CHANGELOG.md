# Changelog

## 2026-08-18 — evidence-extraction.md corrected on two transcript facts

Both checked by direct inspection of `~/.claude/projects/-Users-ben-ai/`
this pass. (1) A denied tool call does carry `is_error: true` on its
`tool_result` block, and the record has a top-level `toolDenialKind` field
(seen: `permission-rule` ×5, `user-rejected` ×2, `automode-unavailable` ×1;
`automode-blocked` reported by the reviewer) — the reference had said
denials are not `is_error` and told the reader to grep for "denied". (2)
Subagent transcripts live at `<session-id>/subagents/agent-<id>.jsonl` next
to the main file (workflow agents under `subagents/workflows/<run-id>/`);
the reference had said to search for a distinctive phrase and hope. Two
bullets rewritten; nothing else touched; `last-verified` unchanged (subject
sources not re-fetched). The ledger entry for the transcript format in
skill-rule-creator's sources.md records the same facts.

## 2026-08-15 — updated after a self-audit

Ran `/ai-retrospective` on the session that created the skill. Three changes,
all from findings the audit raised against the artifact itself:

- **The compaction claim is now a test, not an assertion.** The first draft
  said the JSONL "normally retains the raw turns even after your context was
  summarized." That was never observed — a grep across 92 local transcripts
  found zero compaction events, and neither `costs.md` nor `best-practices.md`
  states the on-disk behavior. The section now tells the agent to verify on
  the first compacted session it audits and to write down what it finds. This
  mattered most because compaction is the case the skill exists for.
- **Added a format-instability caution.** The transcript layout is internal to
  Claude Code and can change between releases, so a wrong-looking ledger
  should point at the parser before it points at the session.
- **Pointed at `/insights`.** The built-in command analyzes up to 200 recent
  sessions for how the user works. It is the cross-session counterpart to this
  skill's single-session, agent-side depth; naming it stops the two from
  being confused.

## 2026-08-15 — created

Created `ai-retrospective`: an agent-side session audit covering tool use,
subagents, skills and rules, context and rework, and task decomposition.

Design decisions and what they rest on:

- **Reads the raw JSONL transcript, not recollection.** The agent's memory of
  the session is the thing under audit. Verified that
  `mcp__ccd_session_mgmt__get_session` and `list_events` both refuse the
  current session, so the transcript file is the only route.
- **Fetches guidance at run time.** Per-release prompting deltas are real and
  documented across three vendors; a retrospective graded against stale
  guidance produces confident wrong findings.
- **Ships `scripts/session_facts.py`.** A 400 KB transcript becomes a compact
  indexed ledger. Two bugs were found and fixed by testing it on live
  transcripts: newest-by-mtime resolution picked a concurrently running
  session (added `--session-id` and `--contains`), and parallel tool calls are
  written as separate JSONL records, so grouping had to key on `message.id`
  rather than the record — without that the script reported missed
  parallelism on every session.
- **Evidence rule and an anti-manufacturing bound.** Every finding quotes a
  record index; a clean session is a valid result. The bound is deliberate —
  an audit skill is pulled toward inventing findings to look thorough.
- **Scope split with refine-prompt.** Prompt-wording findings are named in one
  line and handed off, not reanalyzed.
- **Proposes, does not edit.** Durable changes go to skill-rule-creator;
  harness changes to update-config.

Runtime source entry points verified this date: the Claude Code docs index at
`code.claude.com/docs/llms.txt` (page URLs take a `.md` suffix for cheap
markdown fetches), the dated post index at `anthropic.com/engineering`, and
`platform.claude.com/docs/en/agents-and-tools/tool-use/overview`.

Evaluation scenarios walked (desk-check; nothing ran): a long compacted session with a wasted subagent
and an ignored rule; a short clean session (checks the null result and the
research budget); "how could I have set this up better" (checks the harness
bucket and the update-config handoff). The first two produced fixes — a
reduced fetch budget for clean short sessions, and a recollection fallback for
the evidence rule when no transcript exists.

## 2026-10-31 — dependency reduction: four config keys; declared harness: claude-code

Pass from `~/projects/ai/dependency-map/reduction-plan.md`. Research
exempt. Kind: `metadata.harness: claude-code`, because the skill reads
Claude Code's JSONL transcripts and names `/insights`; its Claude Code
facts stay in the body. New `## Config` with four optional keys, all
empty by default: `prompt-skill`, `rule-skill`, `skills-skill`,
`settings-skill`. When a key is unset the skill states the change for
the user instead of handing it off. `config.local.yaml` holds
prompt-author, rule-author, skill-author, update-config; `.gitignore`
added. The description ends "Covers the agent side only, not how the
user worded the prompt" (was "defer to the prompt-author skill"); the
body's prompt-wording and hand-off paragraphs use the keys. Trigger
eval: due (description changed); no eval set existed, one is written in
the reduction pass. Smoke run not done: the hand-off path needs a
transcript and an accepted finding; desk-checked by reading.

## 2026-10-31 — measured (dependency reduction trigger eval)

Trigger eval after the dependency reduction, `evals/trigger-result-2026-10-31-reduction.json`: 14/14 pass, recall 0.96, near-miss rate 0.00, 3 runs per query, $0.39, Claude Code 2.1.287, claude-opus-5-5, builtin plugins only.
Passed below 1.00: "audit this session's tool use, you ran the same grep five ti" (0.67).
Near-misses that loaded another skill through that skill's own description: notes, prompt-author, rule-author.
No earlier run of this set; the set was written in this pass, so the number is a baseline, not a comparison.
Smoke run (2 turns, $0.19): read `config.local.yaml` and named the four hand-off skills with their keys.

## 2026-10-31 — updated: made portable (harness facts moved to a harness reference)

At Ben's decision ("ai-retrospective needs to be made portable"), the
same day it was declared `harness: claude-code`. Kind is now
`metadata.harness: portable`; `argument-hint` dropped (not a spec field;
the body names the focus in prose). Research exempt: facts moved, none
added.

New `references/claude-code.md` holds every Claude Code fact: the
transcript path and slug rule, the three ways to get the session id, the
desktop-app tools that refuse the current session, the bundled
`scripts/session_facts.py` command (now `<skill-dir>/scripts/...`), the
JSONL record fields and sidecar directories, subagent and workflow
transcript paths, `toolDenialKind` values, hook attachment records, the
`/insights` report, and the docs pages with the `llms.txt` and `.md`
fetching tips. `references/evidence-extraction.md` keeps the method only:
resolve the transcript the way the harness reference says, build the
ledger with an extractor where one exists or by hand, cite record
indices, what a ledger cannot see, compacted sessions, exclude the
retrospective itself. `references/guidance-sources.md` names "the
harness's subagents page" and so on instead of Claude Code page names,
and says to fetch another vendor's prompting guide when that vendor's
model ran the session. SKILL.md: the `/insights` paragraph became "some
harnesses bundle a cross-session usage report"; a pointer to the harness
reference sits before the workflow; step 1 and step 2 say what to do with
no reference or no readable transcript (work from the conversation in
context and say so); "CLAUDE.md, `.claude/rules/`" became "a rule file";
`settings.json` became "the settings edit".

Portability check from the skill directory: zero hits. Frontmatter
parses with `name`, `description`, `metadata` only.

Checks: desk-checked 2 scenarios by reading — a Claude Code session (the
reference supplies the path and the script, unchanged behavior) and a
Cursor session with no reference file (reads Cursor's docs on
transcripts first; with none readable, audits from context and labels
findings as recollection). Smoke run, fresh `claude -p` (2.1.287,
claude-opus-5-5, dontAsk, reads allowed on the skill directory, 2 turns,
$0.21): first tool call read `references/claude-code.md`; the answer gave
the transcript path, the ledger command, and the no-reference fallback.
Trigger eval: none due; the description did not change (its "/ai-
retrospective" trigger phrase stays as vocabulary). A/B not run: the
method is unchanged. Watch item: a real audit in Cursor or Codex has not
happened; the by-hand ledger path is untested.

## 2026-10-31 — moved to the meta-skills repository

Directory moved with its files to `/Users/ben/src/skills/meta-skills`
and symlinked into `~/.claude/skills` by the repository's `link.sh`. No
content change in this step; see skill-author's entry of this date.
