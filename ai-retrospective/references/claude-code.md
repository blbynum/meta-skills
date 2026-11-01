# Claude Code

What differs when ai-retrospective runs in Claude Code: where transcripts
live, how to find this session's, how to build the ledger, and what the
records hold. Read this at step 1. Nothing here applies in another
harness.

## Contents

- Resolve the transcript
- Build the ledger with the bundled script
- Dig into a specific record
- What the main transcript does not hold
- The cross-session report
- Guidance pages

## Resolve the transcript

Transcripts live at `~/.claude/projects/<cwd-slug>/<session-id>.jsonl`,
where the slug is the working directory with every non-alphanumeric
character replaced by a hyphen (`/Users/<user>/ai` becomes `-Users-<user>-ai`).

Get the session id in this order:

1. The scratchpad path in your system prompt ends with
   `.../<session-id>/scratchpad`. That id is exact.
2. Otherwise pass `--contains` with a distinctive phrase from the opening
   user turn. The script picks the transcript holding it.
3. Only as a last resort, let the script fall back to newest-by-mtime. A
   second session writing at the same moment wins that race, so confirm the
   session id and the first user turn in the header before trusting the
   output.

The desktop app's `mcp__ccd_session_mgmt__get_session` and `list_events`
tools refuse the current session, so they cannot supply this. Read the
file.

## Build the ledger with the bundled script

```bash
python3 <skill-dir>/scripts/session_facts.py --session-id UUID
```

`<skill-dir>` is this skill's directory. Execute the script; do not read
it as reference. It prints the ledger the method describes: header
metadata, a context-continuity check, user turns with record indices,
every tool call in order with parallel batches grouped, aggregates,
repeated file access, repeated shell commands, failed calls, subagent
launches, and skill invocations.

The JSONL layout is internal to Claude Code and can change between
releases. If the ledger looks wrong — no tool calls, missing user turns, a
record count far below the file size — suspect a format change before you
suspect the session. Fall back to reading records directly, and fix the
script.

## Dig into a specific record

The ledger truncates. Pull the full text of any record by index:

```bash
python3 -c "import json,sys; p=sys.argv[1]; i=int(sys.argv[2]); print(json.dumps(json.loads(open(p).read().splitlines()[i]), indent=2)[:6000])" TRANSCRIPT.jsonl 57
```

Useful fields per record: `type` (`user`, `assistant`, `attachment`,
`queue-operation`), `message.content` (blocks of `text`, `tool_use`,
`tool_result`), `toolUseResult`, `timestamp`, `uuid`, `parentUuid`,
`isSidechain`, `isMeta`, `attributionSkill`, `permissionMode`, `effort`.

Failed calls carry `is_error: true` on the `tool_result` block.

Large tool results are spilled to a sidecar directory next to the
transcript, `<session-id>/tool-results/<tool_use_id>`. Read those files
when a truncated result matters to a finding.

## What the main transcript does not hold

- **Subagent internals.** Each subagent writes its own transcript at
  `<project>/<session-id>/subagents/agent-<id>.jsonl`, next to the main
  `<session-id>.jsonl` (workflow agents under
  `<session-id>/subagents/workflows/<run-id>/`). The main file's
  `sidechain` count is often zero.
- **Background agents.** These return `Async agent launched successfully`
  at once; the real result arrives later as a task notification record.
- **Denied permissions.** A denial is a `tool_result` block with
  `is_error: true`, and the record carries a top-level `toolDenialKind`
  field naming the cause — seen values `permission-rule`,
  `user-rejected`, `automode-unavailable`, `automode-blocked`. Grep for
  `toolDenialKind` to count denials by cause; a plain `is_error` count
  mixes them with ordinary failed calls.
- **Hook output.** Hooks appear as `attachment` records with
  `hookName`/`hookEvent`.

## The cross-session report

The built-in `/insights` command analyzes many recent sessions on the
machine for patterns in how the user works. When the user's question is a
pattern across sessions rather than one session's execution, point at it.

## Guidance pages

Harness guidance lives on `code.claude.com/docs/en/`: `best-practices`,
`sub-agents`, `skills`, `memory`, `hooks-guide`, `settings`,
`permissions`, `mcp`, `workflows`, `costs`, `output-styles`.

Fetch cheaply: `https://code.claude.com/docs/llms.txt` is a compact index
of every page; append `.md` to a `code.claude.com/docs/en/...` URL for
clean markdown. Cite as `code.claude.com/docs/en/sub-agents — checked
<date>`.
