# Style for guidance prose

Quality bars that apply to both artifact kinds — skills and rules — and to
the files of the two authoring skills themselves. Each
skill's own standards file (`skill-standards.md`, `rule-standards.md`) holds
the format rules for its kind; this file holds what they share.

## Contents

- Style for guidance prose (both kinds)
- Old patterns (deprecated techniques)

## Style for guidance prose (both kinds)

- Explain why for anything non-obvious: "the output feeds a text-to-speech
  engine, so never use ellipses" outlives and outperforms a bare
  prohibition. Models generalize from the motivation.
- Say what to do rather than what to avoid, wherever possible.
- In a portable skill, name actions, not tools: "read the file", "run the
  command", "search the web", never a harness's tool names. A model maps
  the action to whatever tool it has, and a tool name ties the skill to one
  harness. A harness-specific skill (`metadata: {harness: <id>}`) may name
  that harness's tools; a portable skill keeps tool behavior in its
  harness references, not in the body.
- Prefer the calm imperative: "Use this when...". Pressure words (ALL-CAPS,
  MUST) are documented to over-trigger tools and skills on Opus 4.5 and 4.6;
  on later models the effect is undocumented either way, and Anthropic's own
  sample prompts still use them. Treat emphasis as a lever the trigger eval
  can test, not as a default and not as an error in itself.
- When an artifact pushes against a behavior, bound the opposite failure in
  the same artifact. Models overshoot corrections: Anthropic's Sonnet 5
  system card says a rise in dismissive "wet blanket" replies is
  "potentially linked" to the sycophancy reduction, and cross-model
  measurement finds newer models resisting confirmation-fishing where older
  ones folded — the strongest resister, Fable 5, does it by hedging rather
  than contradicting. State what the wanted behavior costs when overdone,
  not only what it replaces.
- Write for the least capable model that will run the artifact — Haiku needs
  steps spelled out where Opus needs a sentence — but not below what the
  strongest target tolerates: skills written for prior models can be too
  prescriptive for Fable 5 and degrade its output. When the artifact will
  meet both ends, test on both. Fable 5.1 "already formats less than
  earlier models", so a block that restricts formatting "can suppress
  structure the content needs" there (its prompting page, read
  2026-10-28); write formatting guidance as what to use when, not as a
  ban.
- Every specific figure an artifact states — a rate, an effect size, a
  threshold, a version number — must trace to an entry in
  [sources.md](sources.md), checked against the primary source rather than
  recalled. Statistics degrade as they are relayed: an interval gets dropped,
  a null result reads as positive, a subgroup number becomes a headline rate.
  A 2026-08-15 audit of one artifact's numeric claims found five of seven
  wrong or absent from the cited paper, including a figure that reversed a
  null finding. When a figure resists verification, either cut it or mark it
  unverified in the artifact — an artifact that states numbers confidently is
  trusted on exactly those numbers. Prefer a reported interval to a bare point
  estimate wherever the artifact has room.

## Old patterns (deprecated techniques)

Standard through the Claude 4 era; strip these when updating older
artifacts and do not introduce them in new ones, except where a bullet
states a measured exception. Where a bullet names a model, that is the
extent of the evidence:

- ALL-CAPS pressure ("CRITICAL: you MUST use this tool") — documented to
  over-trigger tools and skills on Opus 4.5 and 4.6; undocumented for later
  models. Replace with plain conditions ("Use this tool when...") unless a
  trigger eval on the target shows under-triggering.
- Anti-laziness prompting ("if in doubt, use the tool") — documented to
  over-trigger on Claude 4.6 models; replace with a targeted condition.
- Manual chain-of-thought scaffolding ("think step by step", hand-written
  reasoning plans) — native adaptive thinking outperforms it on thinking
  models; steer depth with the effort setting. Still a documented fallback
  when thinking is off or the target is small.
- "Verify your answer" instructions aimed at a model whose vendor page says
  it self-verifies (Opus 5 today) — there the instruction buys
  over-verification and token cost. Fable 5 is not such a model: its page
  asks for explicit self-verification at intervals in long runs. Self-check
  instructions still help on smaller and older models; this pattern is
  model-dependent, not universally deprecated.
- Instructions telling the model to echo, transcribe, or explain its internal
  reasoning in the response — can trigger reasoning-extraction refusals on
  Fable 5. Read the API's thinking blocks instead.
- Prefilled assistant responses — removed from the API on Claude 4.6 and
  later (requests error). Use structured outputs or direct instructions.
- XML tags wrapping simple prompts — headings and clear language work as
  well; reserve XML for complex mixed-content prompts.
- Elaborate personas used to raise task quality ("you are a world-class
  engineer") — state the desired perspective directly instead. This applies
  to personas as a performance trick. It does not apply when the voice itself
  is the deliverable, such as a character, an NPC, or a product's house voice;
  there a dense persona spec is the working technique, and a
  persona-writing skill covers it, where one exists.
