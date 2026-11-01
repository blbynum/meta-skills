# A/B eval: prompt-author

Mode: skill (old-vs-new) | Model: claude-opus-5-5[1m] | Claude Code: 2.1.287 | Runs per arm: 3
Plugins loaded: cc-plugin-agents-md@builtin, cc-plugin-plugin-authoring@builtin, cc-plugin-telemetry@builtin

## goal-fit-long-run

> write me a prompt for claude code. i want it to go through every brewing guide in ~/projects/tea/guides and make each one follow the layout in ~/projects/tea/LAYOUT.md (same section order, same headings, nothing else changed). there's a check script, scripts/check_layout.py <guide>, that exits 0 when a guide conforms. i dont want to babysit it, it should just keep going until every guide passes

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.243 ± 0.003 | 21 ± 3 | 3.0 ± 0.0 | 0 | 0 | 3/3 |
| new | 0.218 ± 0.005 | 20 ± 3 | 3.0 ± 0.0 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- DISCRIMINATOR: the delivered prompt begins with /goal and the condition is the whole prompt (no separate task message after it)
- The condition states the end state as something the agent's output can show: check_layout.py exits 0 for every guide in ~/projects/tea/guides, with the results shown
- The condition keeps the user's constraint that only section order and headings change
- DISCRIMINATOR: the condition carries a turn or time bound, or the rationale offers one
- DISCRIMINATOR: the rationale says the user types /goal themselves and that unattended turns need auto mode (or an equivalent permission note)

## goal-unfit-user-gates

> help me write a prompt that runs /skill-author to build a tea-guide skill in ~/projects/tea. it should grill me first about what the guides need (a few rounds of questions), then show me a draft SKILL.md for approval before writing anything, then write it and run the evals. i want to run it as a /goal so it keeps going until the skill is done

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.178 ± 0.036 | 19 ± 5 | 1.7 ± 1.2 | 0 | 0 | 1/3 |
| new | 0.221 ± 0.003 | 27 ± 12 | 3.0 ± 0.0 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- DISCRIMINATOR: the delivered prompt does not lead with /goal, or the response says plainly that /goal is a poor fit because the grilling rounds and the draft approval need the user, and the goal evaluator starts another turn instead of waiting
- DISCRIMINATOR: offers the split: an ordinary prompt up to the approval gate, then a /goal condition for the unattended remainder (write the skill, run the evals)
- The prompt keeps every stated step: run /skill-author, grilling rounds, draft for approval, write, run evals
- Does not invent requirements the user did not state (no extra deliverables beyond the skill and its evals)

## goal-placement-refine

> this is what i typed in claude code and it never set a goal, it just ran the research skill once and stopped. fix it:

/research /goal Research the best way to brew white tea. Goal: a short brewing guide at ~/projects/tea/guides/white-tea.md with water temp, leaf ratio, and steep times for western and gongfu, sourced from r/tea threads. keep going until the guide exists and every number has a source

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.129 ± 0.015 | 14 ± 2 | 1.0 ± 0.0 | 0 | 0 | 0/3 |
| new | 0.118 ± 0.001 | 12 ± 1 | 1.0 ± 0.0 | 0 | 0 | 0/3 |

Expected behavior to grade against:

- DISCRIMINATOR: explains that only the first slash command ran: /research took '/goal ...' as its argument text, so no goal was set
- DISCRIMINATOR: the rewritten prompt begins with /goal and names the research skill in prose inside the condition, not as a second slash command
- The condition keeps the end state and its proof: the file exists at the given path with water temp, leaf ratio, western and gongfu steep times, each number with an r/tea source, and the agent shows that in its output
- Adds no requirements the user did not state beyond a bound (turn or time clause) and the allowed bounding sentences
- Does not drop the r/tea source preference or the file path

## one-turn-no-goal

> write me a prompt asking claude code to add a Sources section at the end of ~/projects/tea/guides/sencha.md listing the three r/tea threads i used (i'll paste the links in)

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.118 ± 0.016 | 7 ± 2 | 1.0 ± 0.0 | 0 | 0 | 0/3 |
| new | 0.198 ± 0.002 | 10 ± 1 | 3.0 ± 0.0 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- The delivered prompt does not lead with /goal and does not recommend one
- At most one sentence about /goal anywhere in the response, and only to say it is not needed
- The prompt asks for the one edit the user named and nothing more; placeholders for the three links are acceptable
- Short: the prompt is a few lines, matched to the ask
