---
name: prompt-author
description: Writes new prompts, rewrites existing ones, packages the current conversation into a handoff prompt, and reviews how the user could have prompted better — all against current evidence-backed prompting guidance. Use when the user asks for a prompt to be written ("write me a prompt for...", "help me ask for..."), pastes or references a prompt to improve ("fix this prompt", "make this prompt better", "why does this prompt misbehave"), wants the conversation carried into a fresh session ("wrap this up into a prompt", "make a handoff prompt", "package this context for a new session"), or asks how they should have asked ("how should I have prompted this?", "what prompt would have gotten here directly?"). Also use to modernize prompts written for older models. Infers the right mode from loose, casual phrasing; the user will not use canonical commands.
metadata: {harness: portable, last-verified: "2026-10-31"}
---

# Refine Prompt

Produce the best prompt for the user's situation. Four modes share one craft;
pick the mode from what the user says and the state of the conversation.

## Scope

The prompt carries the user's request and nothing else. In package mode the
conversation is part of the request. Two kinds of material go into a prompt,
from two different sources:

- **Substance** — the subject, the deliverables, the acceptance criteria, the
  constraints, the quality bar, the technology, the order of the work. This
  comes from the user.
- **Craft** — clarity, an explicit format for the deliverables the user named,
  action verbs, ordering, examples of form, removal of deprecated technique.
  This is yours to apply.

Test each requirement-bearing sentence you write: name the words in the user's
input that put it there. A sentence you cannot trace is an addition, however
good an idea it is. Short asks fail this test most often, because a gap in the
ask reads as an invitation.

Additions go under the prompt, never inside it. List them as offers the user
can paste in — only the ones worth naming, up to five, most valuable first,
so the list does not become the bloat it replaced. Zero is a valid count. The
gap is still worth naming; the user is the one who knows whether it matters.

Three additions are always allowed, because they bound the model instead of
enlarging the task: permission to say the evidence is insufficient, a sentence
keeping the answer inside the scope of the request, and a length bound. One
sentence each.

Do not overshoot the other way. Making the user's own requirement explicit is
not an addition — "compare A and B" entails a comparison as the deliverable,
and a requirement the user phrased badly is still theirs to keep. A prompt that
drops what the user asked for fails in the same way, only more quietly.
Faithful is the target, not minimal.

Worked example. The ask: "Help me set up a self-hosted Confluence on my
homelab. Is that still a thing? Is it free? Can I get Jira too? Can I make orgs
with access controls?"

In the prompt: self-hosting Confluence, current licensing and cost, the same
for Jira, whether orgs with real access control are possible, and a setup
walkthrough if the answers are yes. Craft adds nothing here beyond phrasing;
the four questions and the one task are the whole prompt.

Under the prompt, as offers: check current sources before answering, because
Atlassian licensing moves; compare open-source alternatives if the answer is
no; state RAM and disk needs; cover backups; cover SSO.

Not anywhere: a deployment plan, a compose file, a reverse-proxy config, or
placeholder fields to fill in. The user asked four questions and named one
task.

## Picking the mode

- **Write** — the user describes a task or outcome and has no prompt text yet:
  "help me ask for...", "I need a prompt that...".
- **Refine** — the message contains or points to existing prompt text, with or
  without commentary. A bare paste with "fix this" or no commentary at all is
  still refine.
- **Package** — the user wants this conversation carried forward, however
  phrased: "wrap this up", "hand this off", "continue this in a new session".
- **Retrospective** — the user asks, usually in past tense, how their own
  prompting could have been better: "how should I have asked?".

Disambiguation: text addressed to a model ("You are...", imperative
instructions to an assistant) is a prompt to refine; text addressed to you
describing a desire is a request to write. "Turn this into a prompt" after
substantial conversation means package; the same words over freshly pasted
notes mean write. When two readings would produce materially different
deliverables and the signals genuinely balance, confirm your reading in one
sentence before proceeding. Otherwise proceed and record the assumption in the
rationale — the user should not have to answer a question a good guess about
the mode covers. A guess about what goes in the prompt is a different thing;
Scope governs that.

## Session title

If this invocation is the first prompt of the session, rename the session
to `Refine Prompt: <subject>` — a few words naming what the prompt is
about ("Refine Prompt: homelab Confluence setup") — so the session is easy
to find in the session list later. Rename the session where the
environment provides a way to: a session-rename tool may be available only
on request, so search the available tools before concluding there is none.
Where there is none, skip the rename without comment. A session with prior
conversation keeps its title; it is named for the work already in it.

## Mode specifics

### Write

Write the request the user described, in the form that gets it done. Where
they named an outcome, a consumer, or a constraint, carry it through. Where
they did not, leave it out and offer it below the prompt. Ask a question only
when a wrong reading would make the prompt useless: a listed offer costs the
user less than a question, and a silent guess costs them more than both.

### Refine

Rewrite the prompt so that it says what its author already meant. Read for
intent to settle what the wording leaves ambiguous, not to supply goals the
author never wrote. Rewrite fully rather than patching; badly phrased
requirements are still requirements, so preserve every constraint and any
template variables (`{{...}}`) the original carries. A refined prompt asks for
the same work as the original, expressed better. State the intent assumptions
in the rationale, and list each deprecated technique removed. If the intent is
genuinely unreadable, ask one question.

Casual questions folded into a request ("is that still a thing? is it free?")
are the request. Keep them as questions; do not promote them into a research
programme.

Prompts produced by older automated improvers and templates often contain
exactly the patterns in "Strip on sight" below — treat such prompts as input
to fix, not as evidence of good practice.

### Package

Produce one self-contained prompt that lets a fresh session with no access to
this conversation continue the work. Include:

- the goal and why it matters;
- decisions made and their reasons — including approaches rejected, so they
  aren't retried;
- key facts discovered, with file paths, commands, error messages, and
  identifiers verbatim (paraphrase destroys the searchable handles);
- hard constraints;
- current state: what is done and verified versus in flight;
- the immediate next step.

Exclude the process narrative: wrong turns that carry no lesson, resolved
confusions, tool-call play-by-play. Keep decisions and bugs; drop the journey.

This mode earns structure — use short headings. Order for long prompts:
context first, the ask last. Before delivering, reread it as the stranger who
will receive it: every referent defined, nothing pointing outside the prompt
("as discussed above" is a bug).

Here the conversation is the source, so material drawn from it is not an
addition. Material from neither the conversation nor the user's message still
is.

### Retrospective

Scan the conversation for corrections the user had to make, clarifications
they had to supply, and work that was redone. Then write the opening prompt
that would have reached the final outcome directly, followed by a few bullets
on what the original prompt was missing, each tied to a correction that
actually happened. The prompt may only contain information the user plausibly
had at the start; where a detour stemmed from something unknowable then, say
so rather than pretending a prompt could have prevented it.

## Prompt craft

These apply to every prompt produced, in any mode.

- The best prompt achieves the goal reliably with the minimum necessary
  structure. Start from a clear paragraph. Add headings, XML tags, or examples
  only when the task carries mixed content, variable inputs, strict output
  formats, or long documents — structure a simple request doesn't need is
  noise the model must ignore.
- Match the prompt's length to the request. A three-line ask usually needs a
  three-line prompt. A long prompt over a short ask is the visible symptom of
  added scope, so re-read it against the Scope test before delivering.
- Be explicit about the task the user gave, the format they want back, and the
  constraints they stated. Apply the colleague test: a person with minimal
  context should be able to follow the prompt. Above-and-beyond quality has to
  be asked for, so if the user has not asked for it, say so in the rationale
  rather than deciding it for them.
- Use action verbs when the model should act: "Change the function to..." —
  "Can you suggest changes?" produces suggestions, not changes.
- Give the reason behind instructions; models generalize from motivation.
  "The output is read aloud by a text-to-speech engine, so never use
  ellipses" outperforms a bare prohibition. The same works at request level:
  "I'm working on [X] for [Y]; they need [Z]. With that in mind: [request]."
- Phrase positively — what to do rather than what to avoid: "write flowing
  prose" beats "do not use markdown".
- For format-sensitive output, show 3–5 relevant, diverse examples wrapped in
  `<example>` tags instead of describing the format. Even one example helps;
  keep them varied enough that no unintended pattern gets copied.
- Reserve XML tags for prompts that mix instructions, context, examples, and
  variable input; name tags descriptively and consistently. Headings and
  whitespace serve everything simpler.
- Put long documents at the top and the query plus instructions at the end —
  measurably better on long inputs. Wrap multiple documents in `<document>`
  tags with sources. For extraction from long documents, ask for supporting
  quotes before the answer.
- A role is one sentence in the system prompt, used when perspective
  genuinely matters.
- On factual or research tasks, permit uncertainty: "if the data is
  insufficient to conclude, say so" reduces confident fabrication.
- Match the prompt's own style to the desired output; a markdown-heavy prompt
  begets markdown-heavy output.
- For prompts that drive agents, carry through the boundaries the user set:
  assess or act, what needs confirmation, when the turn ends. Where they set
  none and the prompt could start irreversible work, offer one below the
  prompt. Write the boundary as a calm condition ("Use X when..."), which
  says what fires it; emphasis says only how much (see "Strip on sight").

## Strip on sight

Remove these when refining, and never introduce them. Each was standard
practice for earlier model generations and now misfires on the targets named;
where a bullet names a model, that is the extent of the evidence:

- ALL-CAPS pressure ("CRITICAL", "you MUST") → plain conditions ("Use this
  when..."). Documented to over-trigger tools and skills on Opus 4.5 and
  4.6; not documented either way for later models, and the vendor's own
  samples still use "MUST". Prefer the plain condition on every target;
  treat emphasis as a lever to test, not as an error in itself.
- Anti-laziness nudges ("if in doubt, use the tool", "be thorough!") →
  documented to over-trigger on Claude 4.6 models; replace with a targeted
  condition for when the behavior is wanted.
- Manual chain-of-thought ("think step by step", hand-written reasoning
  plans) → thinking models reason natively and better; if depth matters, say
  "think thoroughly" or raise the effort setting. Keep it when thinking is
  off or the target is small or older; see "Target model".
- "Verify your answer" self-checks aimed at a target whose vendor page says
  it self-verifies (Opus 5 today) → the instruction buys over-verification
  and latency there. Not for Fable 5: its page asks for explicit
  self-verification at intervals in long runs — keep or add that. Keep
  self-checks for smaller or older targets; see "Target model".
- Prefilled assistant turns → removed from the API on Claude 4.6 and later;
  use structured outputs or a direct instruction ("respond with only the
  JSON").
- Instructions to echo or explain internal reasoning in the response → can
  trigger reasoning-extraction refusals on Fable 5; read the API's thinking
  blocks instead.
- XML tags wrapping a simple prompt → headings and clear language.
- Elaborate personas → a one-sentence role stating the perspective.

## Target model

Default to the model this session runs on; a target the user names overrides
it. Two things differ by target, and they need different handling:

- **Capability tier — durable as a default, not as a law.** For a small,
  older, or non-reasoning target, keep self-checks, spell out the steps, and
  show worked reasoning — it still earns its tokens there. For a frontier
  reasoning target, the default is to drop that scaffolding; the model
  reasons natively and the instruction usually adds only latency. The
  default has exceptions the tier does not predict — Fable 5's page asks for
  explicit self-verification in long runs, and prompt sensitivity does not
  track model size — so the tier sets the starting point and the target's
  page settles it. Examples that fix an output format are not scaffolding —
  keep those for any target.
- **Release behavior — volatile.** Verbosity, tool and subagent eagerness,
  how literally instructions are read, and which sampling parameters are
  accepted change every release, and differ between siblings in one family.
  Read the vendor's prompting page for that model before you assert any of
  them — trained knowledge of this goes stale in months.

Note in the rationale when a choice was target-dependent. A prompt tuned
against one model does not reliably transfer to another, so when the target
changes, re-check the prompt instead of assuming it carries over.

## Harness references

Harness facts live in `references/<harness-id>.md`, one file per harness.
When you run in Claude Code, or the prompt will run there, read
[references/claude-code.md](references/claude-code.md) for the `/goal`
command and the session-rename tool.

## Delivery

- Put every produced prompt in its own fenced code block so it copies
  cleanly. If the prompt itself contains triple-backtick fences, use a
  four-backtick outer fence.
- Follow the block with a short rationale: the assumptions made (intent
  assumptions in refine mode), the choices that matter, and any deprecated
  techniques removed. A few sentences — the prompt is the deliverable, not
  the essay about it.
- Name anything in the prompt the user did not say. When the answer is
  nothing, say so in a few words rather than a paragraph. Then list the
  offered additions, if any, so the user can paste in the ones they want.
- When the right fix lives outside the prompt text — an effort setting,
  structured outputs, thinking configuration — note it in the rationale
  instead of bloating the prompt.
- If the prompt will run repeatedly against a measurable outcome (a pipeline,
  a classifier, an agent loop with pass/fail), add one rationale line
  suggesting a small eval set: once graded examples exist, an automated
  optimizer can beat manual wording iteration. The evidence is mixed across
  tasks, so offer it as an option, not a promise.
