# A/B eval: rule-author

Mode: skill (old-vs-new) | Model: claude-opus-5-5 | Claude Code: 2.1.287 | Runs per arm: 3
Plugins loaded: cc-plugin-agents-md@builtin, cc-plugin-plugin-authoring@builtin, cc-plugin-telemetry@builtin

## add-pnpm-rule

> add a rule for this project that we always use pnpm, never npm or yarn. Draft only: skip the observation runs, the web research, the A/B, and the changelog; write the rule file into ./rules/ in this directory and tell me where it would normally live and what else loads alongside it.

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.356 ± 0.022 | 37 ± 6 | 7.3 ± 1.2 | 0 | 0 | 3/3 |
| new | 0.347 ± 0.042 | 41 ± 6 | 8.7 ± 2.3 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- Reads a harness reference or otherwise states the correct file locations for the harness it runs in
- The rule is imperative and concrete, a few lines, with a one-line last-verified comment
- Names the always-loaded set it would sum for the budget check and the contradiction check
- Says where the rule normally lives for this harness and that a file-scoping mechanism exists for narrower rules

## rule-not-followed

> why isn't my rule 'never use em dashes' being followed? it is in my user-level rules. don't edit anything, just diagnose and tell me what to do.

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.219 ± 0.025 | 23 ± 4 | 4.7 ± 1.5 | 0 | 0 | 1/3 |
| new | 0.238 ± 0.042 | 24 ± 0 | 6.0 ± 1.7 | 0 | 0 | 2/3 |

Expected behavior to grade against:

- Diagnoses from the three failure places: always-loaded total, contradictions with other loaded rules, and the gap between a stated policy and enforcement
- Offers an enforcement layer where the harness has one, named generically or by its harness-specific name with the harness named
- Does not edit any file
