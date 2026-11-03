# Cursor

Rule files as Cursor's documentation stated them on the date in this
skill's `sources.md`; re-read its rules page before you write one.

- Project rules: `.cursor/rules/*.mdc`, version-controlled; a plain `.md`
  file there is ignored because it has no frontmatter. `AGENTS.md` in the
  project root or a subdirectory is the simpler alternative.
- User rules: set in the app under Customize → Rules, not in a file.
- Team rules come from the dashboard and outrank project rules, which
  outrank user rules.
- Scoping: `alwaysApply: true` loads the rule in every chat and ignores
  `globs` and `description`; `globs` attaches the rule when a matching
  file is in context; `description` alone lets the agent decide.
- Cursor's own caution: "AI guidance should not be your only security
  control."
- No non-interactive runner the shared script knows: step 5b records "not
  measured: no runner in Cursor".

Step 1's file set is the project `.mdc` files and `AGENTS.md`; step 4's
budget sums the `alwaysApply` rules; step 4's scoping is `globs`.
