# Antigravity

Rule files as Antigravity's documentation stated them on the date in the
shared ledger; re-read its rules and discovery pages before you write one.

- Per directory, in the workspace and each parent up to the repository
  root: `AGENTS.md` or `GEMINI.md`; `.agents/AGENTS.md` or
  `.agents/GEMINI.md`; and `.agents/rules/*.md` (legacy `.agent/rules/`).
- Global: `~/.gemini/AGENTS.md`, `~/.gemini/GEMINI.md`, or the same names
  under `~/.gemini/config/`, plus `~/.gemini/config/rules/*.md`.
- `AGENTS.md` and `GEMINI.md` have no frontmatter and are always on. A
  file in a `rules/` directory needs `trigger:` frontmatter, or
  Antigravity silently discards it. `AGENTS.md` support dates from v1.20.5.
- The agent's terminal runs in a sandbox limited to the workspace and
  temporary directories, with no network by default; files outside the
  workspace need approval.
- No non-interactive runner the shared script knows: step 5b records "not
  measured: no runner in Antigravity".

Step 1's file set is the chain above; step 4's scoping is `trigger:`.
