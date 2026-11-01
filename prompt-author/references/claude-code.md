# Claude Code

Claude Code facts for the prompt-author skill. Read this when you run in
Claude Code, or when the prompt you produce will run there.

## Contents

- Session rename
- `/goal`

## Session rename

This is the tool for SKILL.md's "Session title" section. In the Claude
desktop app (Code tab), the session-rename tool is
`mcp__ccd_session_mgmt__set_session_title`, with `session_id: "self"` and
the new `title`. It is often deferred: load it with the tool search before
you call it. The terminal CLI has no such tool, and a subagent cannot
rename the session it runs in; in both cases, skip the rename without
comment.

## `/goal`

A prompt that will run in Claude Code — written, refined, or packaged —
can lead with `/goal <condition>`. The command sets a completion condition
for the session: after each turn a small model reads the conversation, and
while it judges the condition unmet it starts the next turn instead of
returning control to the user. The goal clears when the condition is met,
when the evaluator judges it impossible, or when a turn fails on an error
the user has to fix.

Decide from the shape of the work:

- Lead with `/goal` when the run is long, needs no decision from the user
  on the way, and ends in a state the agent's own output can show: a test
  result, a build exit code, a file count, an empty queue, a check that
  exits 0.
- Write an ordinary prompt when the run has a user gate — rounds of
  questions, approval of a draft, a choice between options. The evaluator
  cannot wait for the user: it starts another turn, and after several
  turns without tool use Claude Code halts the loop with a warning. If the
  user asked for a goal anyway, say why it does not fit, and offer the
  split: an ordinary prompt up to the gate, then a goal for the unattended
  remainder.
- A task one turn finishes gains nothing from a goal.

When the prompt leads with `/goal`, the condition is the whole prompt.
Setting the goal starts a turn with the condition as its directive, and no
separate message follows. So the condition carries the task; names any
skill the run should use, in prose ("use the <name> skill"); states the
end state and how the agent proves it ("`npm test` exits 0", "the page
lists every vendor with a source"); names what must not change on the way;
and bounds the run with a turn or time clause ("or stop after 20 turns"),
a bounding addition allowed like the three in SKILL.md's Scope section.
The evaluator reads only the conversation — it runs no commands and opens
no files — so an end state the agent never shows in its output is never
met. The condition can be up to 4,000 characters.

Placement: `/goal` is a built-in command, not a skill. The user types it at
the prompt or passes it to `claude -p`; the Skill tool cannot run it, and
agents do not see it in their skill list. It has to come first in the
message: in `/<skill> /goal <condition>` that skill runs and
`/goal <condition>` is its argument text, so no goal is set. Lead with
`/goal`, and name skills in prose inside the condition rather than as a
second slash command.

In delivery, the code block starts with `/goal`. Note in the rationale that
a goal does not change the permission mode: unattended turns need auto
mode, or the run stops at the first tool call the settings do not allow.
