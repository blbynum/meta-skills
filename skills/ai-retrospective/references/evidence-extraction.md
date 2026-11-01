# Evidence extraction

How to get at what actually happened in the session, rather than what you
remember happening. Your memory of the session is the thing under audit, so
it cannot also be the evidence. Where transcripts live, how to find this
session's, and how to extract from them differ by harness; the reference
for the harness you run in holds those facts, and this file holds the
method.

## Contents

- Resolve the transcript
- Build the ledger
- Dig into a specific record
- What the ledger cannot see
- Summarized or compacted sessions
- Exclude the retrospective itself

## Resolve the transcript

Find the raw transcript of this session the way the harness reference
says. Confirm it is this session: the first user turn in it must be the
opening prompt you remember, and the session id must match whatever the
harness shows you. A transcript picked by "newest file" can belong to
another session running at the same time.

With no reference for your harness, look for a transcript the harness
exposes (a sessions directory, an export command, a log). If none is
readable, work from the conversation still in context and say so in the
report's first paragraph.

## Build the ledger

The ledger is a compact table of the session, with one record index per
line: header metadata (model, start time, working directory), a
context-continuity check, user turns, every tool call in order with
parallel batches grouped, aggregates, repeated file access, repeated shell
commands, failed calls, subagent launches, and skill invocations.

Where the harness reference names an extractor, run it. Where none exists,
build the ledger by hand: number the records, list the user turns and
tool calls in order, and mark repeats and failures. Keep the numbering,
whatever produced it: findings cite record indices (`[57]`) so the user
can find the evidence.

## Dig into a specific record

The ledger truncates. Pull the full text of any record you cite, from the
transcript, before you quote it. The harness reference shows how, and
which fields a record holds.

## What the ledger cannot see

- **Subagent internals.** A subagent's own turns usually do not land in the
  main transcript. Read its own transcript, where the harness keeps one,
  when its tool use matters to a finding; otherwise judge it from what the
  main transcript shows — the prompt you sent, its returned report, and
  whether later work used that report.
- **Background agents.** A launch returns at once; the result arrives
  later. Check whether one ever arrived and whether anything acted on it.
- **Denied permissions.** A denial looks like a failed call. Separate the
  two where the harness marks them apart; a plain count of failed calls
  mixes them.
- **Hook output.** Where the harness runs hooks, their output is part of
  the harness bucket, not the agent's execution.

## Summarized or compacted sessions

Whether a transcript keeps the pre-compaction turns is unverified. No
transcript inspected when this skill was written had ever compacted, so
append-only retention is an assumption, not an observation. Treat the first
compacted session you audit as the test: if the ledger's first user turn is
a summary rather than the real opening prompt, the raw turns are not in
this file. Look for a sibling transcript whose closing records match this
file's opening ones. Then report what you found, and offer to correct this
paragraph — the skill's editing boundary applies to its own files too.

Two checks meanwhile:

1. The ledger reports any summary or compaction record it finds.
2. Compare the first user turn it prints against what you remember as the
   opening prompt. A mismatch means context was summarized regardless of
   what the ledger found.

If context was summarized, say so in the report's first paragraph. Findings
drawn from the raw transcript stay full strength; findings that rest on
your recollection of the early session do not — mark those as lower
confidence, or drop them and read the records instead.

If the raw transcript is genuinely unavailable, say that plainly and scope
the audit to the part of the session you can still evidence.

## Exclude the retrospective itself

Every tool call from the retrospective invocation onward is this skill
running, not the work under audit. The ledger flags the invoking user
turn. Findings about calls after that point are noise.
