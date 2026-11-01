---
name: ai-retrospective
description: Audits how the agent worked in the current session — tool choices, subagent use, which skills and rules fired, rework after corrections, and how the task was decomposed — against guidance fetched at run time, then proposes changes to rules, skills, and settings. Use when the user asks "how did that go", "retrospective on this session", "what went wrong with how you worked", "audit this session", "how could I have set this up better", "what should I change in my rules", or types /ai-retrospective. Reads the raw session transcript and quotes it in every finding. Covers the agent side only, not how the user worded the prompt.
metadata: {harness: portable, export: portable, last-verified: "2026-08-15"}
---

# AI Retrospective

Audit how this session was worked, find what cost time or quality, and propose
changes that would prevent a repeat.

The subject is the agent's own execution: tools, subagents, skills, rules,
context, and task decomposition. Prompt wording is out of scope — when a
finding is really "the opening prompt should have said X", name it in one line
and point the user at the configured prompt skill (`prompt-skill`), which
does that analysis; when none is set, say the prompt is out of scope here.

Some harnesses bundle a cross-session usage report that analyzes many recent
sessions for patterns in how the user works; the harness reference names it
where one exists. This skill audits one session's agent-side execution in
depth. When the user's question is really about a pattern across sessions,
say so and point at that report where the harness has one.

Assess and propose by default. Ask before editing a rule file or a skill.

Before step 1, read the reference for the harness you run in,
`references/<harness-id>.md`;
[references/claude-code.md](references/claude-code.md) exists and says
where transcripts live there and how to build the ledger from them. With no
reference for your harness, read its documentation on session transcripts
first.


## Config

| Key | Required | Default | Purpose |
|---|---|---|---|
| prompt-skill | no | | skill that rewrites prompts; when unset, state the rewording and stop |
| rule-skill | no | | skill that writes always-loaded rules; when unset, state the rule text for the user |
| skills-skill | no | | skill that writes skills; when unset, state the change for the user |
| settings-skill | no | | skill that edits harness settings; when unset, state the exact settings edit |

Read `config.local.yaml` in this skill's directory before anything else.
A key missing there takes its Default from the table. If a required key is
missing or empty, stop: name the key and its purpose, and offer to write
`config.local.yaml` with the values the user gives. If a configured
directory does not exist, stop and say so; do not create it.

## Workflow

Copy this checklist into the response and check items off as you go:

```
- [ ] 1. Establish the evidence base
- [ ] 2. Extract the session facts
- [ ] 3. Check current guidance
- [ ] 4. Analyze the five areas
- [ ] 5. Write the assessment
- [ ] 6. Propose changes
```

If the user named a focus ("tool use", "why the subagent stalled"), run the whole
workflow but weight the analysis there. Report anything major found elsewhere
in one line rather than dropping it.

### 1. Establish the evidence base

Read [references/evidence-extraction.md](references/evidence-extraction.md)
for the method, and locate the raw transcript the way the harness reference
says, before analyzing anything. With no readable transcript, work from the
conversation still in context and say so.

Your memory of the session is the thing under audit, so it cannot also be the
evidence. Where the transcript and your recollection differ, the transcript
wins.

State the evidence quality in the report's opening paragraph: whether the raw
transcript was readable, and whether context was summarized or compacted during
the session. If it was, say so up front — findings that rest on recollection of
the pre-summary session are weak, and the reader needs to know which ones do.

### 2. Extract the session facts

Build the ledger: user turns, tool calls with parallel batches grouped,
repeats, failures, subagent launches, and skill invocations, each tagged
with a record index. Where the harness reference names an extractor, run it;
otherwise build the ledger by hand as the method describes.

Read the ledger before forming any hypothesis. Findings should come from the
ledger, not from a hypothesis you then search for support for.

### 3. Check current guidance

Read [references/guidance-sources.md](references/guidance-sources.md) and fetch
three to five pages, chosen by what the ledger shows. Always fetch the
prompting page for the model that ran the session — take the model id from the
ledger header, which may differ from the model running this retrospective.

Trained knowledge about agent behavior goes stale by a release or two, which is
how a retrospective produces confident wrong findings. Fetch first, conclude
after.

For a short session whose ledger shows nothing anomalous, fetch only the
per-model prompting page and say the audit was scoped to match. A five-fetch
research pass over a clean twenty-minute session costs more than it returns.

### 4. Analyze the five areas

**Tool use.** Which tool was chosen and whether a better one existed. Bash used
where a dedicated tool fit. Independent calls issued one at a time. The same
file read repeatedly. Failed calls, and whether the retry changed anything or
repeated the same call. Tool output that was fetched and never used.

**Subagents.** Whether any were spawned, and whether the task warranted one —
both directions are findings: a subagent for work the main thread should have
done, and a fan-out search done serially in the main thread. How well each was
scoped: did its prompt carry the context it needed to start cold. Whether its
result was actually used, or launched and forgotten.

**Skills and rules.** Which fired. Which should have fired and did not — check
the loaded skill list against the work. Which fired and did not fit. Where a
loaded rule was stated and then not followed, quoting both the rule and the
behavior. A rule ignored twice is a rule-design finding, not a discipline
finding.

**Context and rework.** Work redone after a correction. Effort spent on paths
the user later rejected, and how early the signal was available. Points where a
question would have been cheaper than a guess — but only where the guess
actually went wrong or a wrong guess would have been expensive; asking has a
cost too.

**Task decomposition.** How the work was broken up, whether phases ran in a
sensible order, and where an assumption was made silently instead of stated.
Silent assumptions that turned out right are still findings when a wrong one
would have wasted the session.

### The evidence rule

Every finding quotes the specific message or tool call it comes from, with its
record index. A finding you cannot quote is a finding you do not report — even
when you are confident it happened. Unevidenced findings are the failure mode
this skill exists to avoid: they read as insight and cannot be checked.

When the transcript is unavailable, quote from the conversation still in
context and mark the finding as recollection rather than record. The bar is a
quotable source, not the file specifically.

### Do not manufacture findings

A session with nothing significant to report is a real result. Say "three minor
findings, none costing more than a minute" when that is what the ledger shows.
Padding the list with small findings buries the one that mattered and trains
the user to skim.

Judge your own execution the way you would judge another agent's: neither
softer because it was yours, nor harsher to appear rigorous. Both distort the
ranking, which is the part the user acts on.

### 5. Write the assessment

Prose, not a bare list. Structure:

1. **Evidence and scope** — one paragraph: which transcript, whether context
   was summarized, what the audit covers.
2. **Findings, ranked by cost** — most expensive first, measured in time lost
   or quality lost. Each finding: what happened, the quoted evidence with its
   record index, the cost, and what current guidance says (with the source and
   date, or labeled as your own judgment).
3. **Buckets** — sort every finding into one, because the fix differs:
   - **Prompt, rule, or skill** — the user can change something they wrote.
   - **Harness or configuration** — permissions, hooks, settings, MCP servers,
     model or effort choice.
   - **Agent execution** — no rule would have prevented it. Say so plainly
     rather than inventing a rule to make it look actionable.
4. **Proposed changes** — see below.
5. **Sources checked** — each URL with the date fetched.

Rank by cost, not by bucket. A large execution-only finding outranks a small
rule finding.

### 6. Propose changes

Make each proposal concrete: the rule text to add, the skill to create or the
specific section to amend, or the exact settings change. "Be more careful about
X" is not a proposal.

Then stop and ask. Do not edit a rule file or any skill without the user
agreeing to that specific change.

When the user accepts a durable change:

- Rules and skills — hand off to the configured rule skill (`rule-skill`)
  or skills skill (`skills-skill`) rather than writing the file here. Each
  runs the research, the skill-versus-rule decision, and the evaluation
  scenarios that keep the artifact sound. When the key is unset, state the
  exact text to add and leave the edit to the user.
- Settings, hooks, permissions — hand off to the configured settings skill
  (`settings-skill`); when unset, state the exact settings edit.
- Prompt wording — hand off to the configured prompt skill (`prompt-skill`);
  when unset, state the rewording.

Before proposing a new rule, weigh what it costs. Every always-loaded line
taxes every future session and competes for attention with the task at hand. A
one-off execution error usually does not justify a permanent rule; a pattern
that recurs across sessions does. Say which of the two you are looking at.
