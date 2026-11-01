# skill-rule-shared

Not a skill. This directory has no `SKILL.md`, so Claude Code ignores it.
It holds the files that the two
authoring skills, one for skills and one for rules, share, so that each
stays pointed at one artifact kind while the record-keeping stays in one
place:

| File | What it is | Who reads and writes it |
|---|---|---|
| `sources.md` | The provenance ledger for the authoring sources (skill and rule guidance, the spec, harness docs, research) and for the subject matter of the skills that live beside this directory. Every other skill keeps its own `sources.md` in its directory, never linked from its SKILL.md. | Both skills, at their research and self-maintenance steps. Re-read an entry immediately before you edit it: another session may have written to it in between. |
| `evaluating.md` | How to measure an artifact: eval sets, the trigger eval (skills only), the A/B eval (skills and rules), the confounds to record, how to read results. | Both skills at their measure step. |
| `scripts/trigger_eval.py` | Measures how often a skill loads across should-trigger and near-miss prompts. | The skills author. |
| `scripts/ab_eval.py` | Runs task prompts with and without an artifact (`--mode skill`, `--mode rule`, `--old/--new`). | Both skills. |
| `skill-vs-rule.md` | The decision framework: skill or rule, decided on loading behavior. A request may need it before either skill is chosen, so it belongs to neither. | Both skills at their confirm-the-mechanism step; either skill answers a pure choice question from it. |
| `guidance-style.md` | Prose style and deprecated patterns that apply to both artifact kinds. | Both skills at their draft step. Each skill keeps the format rules for its own kind in its own `references/`. |
| `retired/skill-rule-creator.SKILL.md` | The last `SKILL.md` of the single skill, as it stood when it was split. Kept so the working tree records what the two bodies were cut from. | Read only; not a skill (not at `<name>/SKILL.md`). |

Both skills link these files from their `SKILL.md`, one level deep, by
the relative path `../skill-rule-shared/<file>`. Any tool that copies one
of the two skills to another machine must copy this directory with it.
