# Sources — prompt-author

Provenance ledger for the prompt-author skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

## Tier 1: Anthropic official

### Prompting Claude Fable 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Last verified: 2026-08-18 (re-fetched; byte-identical to the 2026-08-15
  copy; full page read)
- Supports: give the reason behind the request ("I'm working on X for Y...");
  state assess-vs-act boundaries; brief brevity instructions outperform
  enumerating verbosity patterns; ground progress claims in tool results;
  reasoning-echo instructions can trigger reasoning-extraction refusals;
  skills written for prior models are often too prescriptive and can degrade
  Fable 5 output.
- Self-verification, verbatim (section "Recommended scaffolding changes"):
  "Make self-verification explicit in long-run prompts. Separate,
  fresh-context verifier subagents tend to outperform self-critique. For
  long-running tasks, instruct: `Establish a method for checking your own
  work at an interval of [X] as you build. Run this every [X interval],
  verifying your work with subagents against the specification.`" This is
  the reverse of the Opus 5 guidance to remove verification instructions,
  and it is why refine-prompt must not strip self-checks from a Fable 5
  long-run prompt. Also verbatim: "Skills developed for prior models are
  often too prescriptive for Claude Fable 5 and can degrade output quality.
  Review and consider removing older instructions if default performance
  is better." The page has no guidance on caps, MUST, emphasis, or skill
  over-triggering, and does not mention Opus 4.5 or 4.6.

### Prompting Claude Opus 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Last verified: 2026-08-17 (re-fetched, full page read)
- Supports: default responses run longer than prior Opus models and effort
  does not control visible length, so prompt for conciseness; readier
  narration during agentic work; longer written deliverables; removal of
  verification instructions because the model verifies its own work
  ("removing them reduces wasted tokens with no loss in quality"); scope
  expansion on narrow tasks; readier subagent delegation; more correction
  narration; artifacts when thinking is disabled. Also: literal compliance
  with "only report high-severity issues" in review prompts reduces reported
  findings.
- Read in full 2026-08-17 for the refine-prompt scope pass. The "Task scope
  and over-verification" section states, verbatim: "Claude Opus 5 can also
  expand the scope of a task, adding steps that weren't requested or applying
  its own judgment about what the task should be. For narrow tasks, constrain
  scope explicitly", followed by a sample clamp whose operative lines are
  "Deliver what was asked, at the scope intended" and "stop short of actions
  that are clearly beyond what was asked". Two things follow. First, scope
  expansion is a documented model behavior, not an artifact defect, so an
  artifact that produces text on the user's behalf needs its own clamp.
  Second, the documented remedy is an explicit clamp in the prompt, which is
  the design refine-prompt's Scope section adopts.
- Re-read 2026-08-18: the "Self-correction" section adds "Claude Opus 5
  catches and fixes its own mistakes well without prompting. Avoid
  instructing re-checks it already performs". The page has no guidance on
  caps, MUST, emphasis, or skill over-triggering, and never mentions Opus
  4.5 or 4.6 (comparisons are against Opus 4.8 only). "Positive examples of
  the communication style you want tend to be more effective than
  instructions about what not to do" is the page's positive-framing line.

### Prompting Claude Sonnet 5
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
- Last verified: 2026-08-15 (fetched)
- Supports: length calibrated to task complexity rather than a fixed
  verbosity; adaptive thinking on by default (a change from Sonnet 4.6);
  `temperature`, `top_p`, and `top_k` return 400; manual extended thinking
  removed; readier tool use and self-verification loops; more literal
  instruction following, so state scope explicitly; code-review harnesses
  tuned for earlier models lose recall. Read together with the Opus 5 page,
  this is the evidence that two models in one generation need different
  prompt changes.
- Re-read 2026-08-18: no guidance on caps, MUST, emphasis, or skill
  over-triggering; the "Tool use triggering" section frames the risk as
  under-triggering with thinking off ("add an explicit nudge in the system
  prompt"). The page's one ALL-CAPS "NEVER" sits inside a recommended
  frontend sample prompt. Comparisons are against Sonnet 4.6 only.

### Console prompting tools (prompt generator and improver)
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools
- Last verified: 2026-08-15 (fetch redirects to the consolidated
  best-practices page; improver behavior per the 2024 announcement at
  https://www.anthropic.com/news/prompt-improver and search summaries)
- Supports: the improver's classic transformations (chain-of-thought
  enrichment, prefill addition) target older model generations and are now
  deprecated techniques on current models — grounds refine-prompt's rule to
  strip what automated improvers added rather than emulate them.

## Tier 1: other vendor documentation

Primary documentation for models other than Claude. Rank it as tier 1 for
claims about its own models only.

### OpenAI GPT-5.1 and GPT-5.2 prompting guides
- URLs: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide ,
  https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide
- Last verified: 2026-08-15 (fetched)
- Supports: GPT-5.1 errs toward excessive concision, so prompt for
  persistence and completeness; new `none` reasoning mode; tool-eagerness
  guidance; a metaprompting section that uses the model on its own prompts.
  GPT-5.2 is lower-verbosity with stronger instruction adherence, and the
  guide adds explicit length clamps, scope constraints ("EXACTLY and ONLY
  what the user requests"), and a `minimal → none` effort migration.
  Corroborates that per-release deltas are real outside Anthropic, and that
  each release ships its own prompt changes.

### Gemini 3 developer guide
- URL: https://ai.google.dev/gemini-api/docs/gemini-3
- Last verified: 2026-08-15 (fetched)
- Supports: verbatim, Gemini 3 "may over-analyze verbose or overly complex
  prompt engineering techniques used for older models"; replace
  chain-of-thought scaffolding with `thinking_level: "high"` and simplified
  prompts; remove explicit `temperature` and use the 1.0 default, since low
  values cause "looping or performance degradation on complex tasks"; less
  verbose by default; put the question after the data. Third independent
  vendor stating that prompts tuned for older models over-steer newer ones.

## Tier 2: research

### To CoT or not to CoT (Sprague et al., arXiv 2409.12183, ICLR 2025)
- URL: https://arxiv.org/abs/2409.12183
- Last verified: 2026-08-18 (abstract and full text fetched and read; v3 of
  7 May 2025)
- Models: 14 instruction-tuned models of 2023–2024 vintage (Llama 2 7B,
  Mistral 7B, Llama 3.1 8B/70B, Gemma 2 9B, Phi-3, Qwen 7B/72B, gpt-4o-mini
  and gpt-4o 2024 releases, Gemini 1.5 Flash/Pro, claude-3-haiku,
  claude-3-5-sonnet-20240620) over 20 datasets, plus "a quantitative
  meta-analysis covering over 100 papers using CoT".
- Supports, verbatim: "CoT gives strong performance benefits primarily on
  tasks involving math or logic, with much smaller gains on other types of
  tasks"; "On MMLU, directly generating the answer without CoT leads to
  almost identical accuracy as CoT unless the question or model's response
  contains an equals sign". The finding is about prompt-based CoT on
  pre-reasoning-era models; the vault note that paraphrased it as "minimal
  or negative" overstated it. Cited by the vault's CoT note; not a basis
  for any artifact claim beyond "CoT gains concentrate in math and
  symbolic tasks".

### The Prompt Report (Schulhoff et al., arXiv 2406.06608)
- URL: https://arxiv.org/abs/2406.06608
- Last verified: 2026-08-15 (via vault)
- Supports: standard vocabulary and taxonomy of prompting techniques.

### Prompt underspecification (Yang et al., arXiv 2505.13360, ACL Findings 2026)
- URL: https://arxiv.org/abs/2505.13360
- Last verified: 2026-08-18 (abstract re-fetched, v3 of 24 Apr 2026; full
  HTML text read for the model list)
- Models tested (Sec 3.2): Llama-3.3-70B-Instruct, gpt-4o-2024-08-06, and
  o3-mini; the model-update study adds gpt-4o 05-13/11-20 and Llama-3/3.1
  70B; the optimizer study runs on Llama3.3-70b-instruct only; Appendix D
  reports the pattern also holds on gemini-2.5-flash. No Claude model is
  tested. Treat every percentage below as a 2024–2025 open-weight and
  GPT-4o-era measurement.
- Supports: the both-sided constraint on any anti-addition guidance. Models
  infer unstated requirements correctly about 41.1% of the time, so gaps are
  real and consequential: under-specified prompts are "2x as likely to
  regress across model or prompt changes, sometimes with accuracy drops
  exceeding 20%". But the paper also finds that "simply specifying all
  requirements does not consistently help, as models have limited
  instruction-following ability and requirements can conflict. Standard
  prompt optimizers likewise provide little benefit." Its remedy is
  requirements discovery, evaluation, and monitoring with the human in the
  loop — requirements-aware optimization "improve[s] performance by 4.8% on
  average over baselines". Also: "stronger LLMs are more likely to guess
  requirements: o3-mini can guess 44.7% of unspecified requirements, a
  20.2% increase compared to Llama3.3-70b-instruct". Grounds refine-prompt's
  design: surface the gap to the user as an offer rather than filling it
  silently, and do not overcorrect into stripping. Tasks studied are code
  explanation, trip advisory, and product description, so treat the
  percentages as directional outside those domains.

### PromptBridge: cross-model prompt transfer (arXiv 2512.01420)
- URL: https://arxiv.org/html/2512.01420
- Last verified: 2026-08-15 (fetched)
- Supports: "model drifting" — a prompt tuned for one model transfers badly
  to another, measured across GPT-4o, o3, o4-mini, GPT-5, Llama-3.1-70B,
  Qwen3-32B, and Gemma3-27B (December 2025). A GPT-5-optimized prompt scored
  99.39 percent on GPT-5 and 68.70 percent on Llama-3.1-70B; cross-model
  adaptation beat direct transfer by 27.39 percent relative on SWE-Bench
  Verified and 39.44 percent on Terminal-Bench. Caveat: single-group
  preprint, not replicated. Grounds refine-prompt's re-check-on-target-change
  line. Note what it does not show: the gains come from optimizing against
  the target with measurements, not from the refiner sharing the target's
  identity.

### Prompt sensitivity does not track scale (JudgeSense, arXiv 2604.23478)
- URL: https://arxiv.org/html/2604.23478v2
- Last verified: 2026-08-18 (abstract and full v2 text fetched and read;
  v2 dated 7 May 2026; 13 judge models run April 2026: GPT-5.5, GPT-4o,
  GPT-4o-mini, Claude Opus 4.7, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini
  2.5 Flash, Llama-3.1-70B, Mistral small, Qwen-2.5-72B, DeepSeek-R1, Qwen
  3.6 Flash, DeepSeek-V4 Flash)
- Supports: the paper's stated finding, verbatim from the abstract:
  "Crucially, we find that model scale is not a reliable proxy for
  consistency; notably, as an interesting result in our analysis, the
  largest and newest models are not the most consistent." Within-vendor
  inversions: "Claude Opus 4.7 below Claude Haiku 4.5; GPT-5.5 below
  GPT-4o" on coherence-judgment stability (Opus–Haiku directional with
  overlapping CIs; GPT-5.5–GPT-4o statistically separated). The 8.5%
  (GPT-4o) and 61.3% (gemini-2.5-flash) flip rates are the introduction's
  motivating example, not a capability ordering. Correction recorded
  2026-08-18: an earlier version of this entry, written from a search
  summary, cited these two numbers as corroboration that "weaker models ...
  are more sensitive to wording"; the paper says the opposite, and its
  authors add that reasoning-tuned judges ran at a different token budget
  ("an uncontrolled confound"). What survives for refine-prompt: prompt
  sensitivity is model-specific and must be measured on the target, not
  inferred from its tier. Judge setting only.

### Model-specific prompting strategies (VMware, arXiv 2402.10949)
- URL: https://arxiv.org/pdf/2402.10949.pdf
- Last verified: 2026-08-18 (abstract and full text fetched and read; v2
  of 20 Feb 2024; Battle & Gollapudi, VMware NLP Lab)
- Models: Mistral-7B-Instruct-v0.1, Llama-2-13b-chat-hf, Llama-2-70b-chat-hf
  on GSM8K; 60 system-message combinations with and without CoT; DSPy as
  the optimizer. Commercial models were named as not tested ("financially
  prohibitive").
- Supports, verbatim: "results do not universally generalize across models"
  and "employing an automated prompt optimizer emerges as the most effective
  method for enhancing performance, even when working with smaller
  open-source models"; conclusion: "the automatically generated prompts
  perform better and generalize better than hand-tuned 'positive thinking'
  prompts", with the caveat that "Mistral-7B struggled to optimize its own
  prompt until it had 100 questions to work with". Grounds the model-and-
  dataset specificity of prompts. Caveat: 2023–2024 open-weight models of
  7–70B, so directional for current models rather than current evidence.

## Tier 3: community (corroborated or labeled)

### Community prompt-refinement skills (prompt-architect, prompt-improver)
- URLs: https://github.com/ckelsoe/prompt-architect ,
  https://github.com/wagnersza/prompt-improver
- Last verified: 2026-08-15 (fetched)
- Supports (unverified community practice): delivery shape of diagnosis +
  improved prompt + model-settings note (adopted in refine-prompt);
  prompt-architect's 31-framework menu and progressive questioning were
  reviewed and rejected as conflicting with tier-1 minimum-necessary-
  structure and one-default-with-escape-hatch guidance.

## prompt-author skill subject-matter sources

### Claude Code `/goal` (2026-10-29)
- URLs: https://code.claude.com/docs/en/goal (fetched in full as raw
  markdown, `goal.md`, 2026-10-29) ; https://code.claude.com/docs/en/commands
  (`commands.md`, the `/goal` row and the table preamble) ;
  https://code.claude.com/docs/en/skills (`skills.md`, "Stack several
  skills in one message" and "Restrict Claude's skill access") ;
  https://code.claude.com/docs/en/desktop (`desktop.md`, grep only, no
  `/goal` mention).
- Last verified: 2026-10-29 (first entry; local CLI 2.1.287).
- Supports (verbatim where quoted), goal page: "The `/goal` command sets a
  completion condition and Claude keeps working toward it without you
  prompting each step. After each turn, a model checks whether the
  condition holds. If the model judges it not yet met, Claude starts
  another turn instead of returning control to you. The goal clears
  automatically once the condition is met, if the model judges the
  condition impossible to satisfy, or if a turn fails on an error you have
  to fix"; "Setting a goal starts a turn immediately, with the condition
  itself as the directive. You don't need to send a separate prompt"; "The
  evaluator judges your condition against what Claude has surfaced in the
  conversation. It doesn't run commands or read files independently, so
  write the condition as something Claude's own output can demonstrate";
  a durable condition has "One measurable end state", "A stated check",
  and "Constraints that matter"; "The condition can be up to 4,000
  characters"; "To bound how long a goal runs, include a turn or time
  clause in the condition, such as `or stop after 20 turns`"; "A goal
  doesn't change your permission mode. To let goal turns run unattended,
  run `/goal` in auto mode"; "If Claude keeps answering the evaluator
  without making progress (no tool use for several turns in a row),
  Claude Code stops the loop, prints a warning, and returns control to you
  with the goal still set"; the evaluator is "a wrapper around a
  session-scoped prompt-based Stop hook" on "your configured small fast
  model" and "does not call tools"; `claude -p "/goal <condition>"` "runs
  the loop to completion in a single invocation". Fit examples on the
  page: migrate a module until call sites compile and tests pass,
  implement a design doc until acceptance criteria hold, split a file
  until each piece is under a size budget, drain a labeled issue backlog.
  Version notes on the page, not carried into the skill: check-ins
  v2.1.234+, idle check-ins v2.1.236+, retry/pause notices v2.1.269+,
  restore on every resume route v2.1.239+.
- Built-in, not a skill: commands.md lists `/goal [condition|clear]`
  without the **Skill** marker in a table whose preamble says "Most are
  built-in commands whose behavior is coded into the CLI"; `/loop` in the
  same table is marked **Skill**. skills.md: "A few built-in commands are
  also available through the Skill tool, including `/init` and
  `/security-review`. Other built-in commands such as `/compact` are
  not."
- Placement, skills.md verbatim: "When you type at the Claude Code prompt
  in your terminal, you can stack several skills at the start of one
  message. Through the Agent SDK or `claude -p`, Claude Code loads only
  the first skill, with the rest of the line as its arguments"; "Expansion
  stops at the first token that isn't an inline user-invocable skill. If
  you stack a skill that runs as a forked subagent ... or one whose
  arguments may start with another command, such as `/loop`, expansion
  ends there. That token and everything after it become the argument text
  for every expanded skill." `/goal` is not a skill, so a `/goal` after a
  skill ends expansion and becomes argument text in every mode.
- Inference carried into the skill, not stated on the page: a run with a
  user gate (an approval, rounds of questions) is a poor fit because the
  evaluator starts another turn rather than waiting, and the
  no-tool-use stop then halts the loop. Mechanism-level inference from the
  quoted text; not measured.
