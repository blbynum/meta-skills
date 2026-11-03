# GitHub Copilot

Rule files as GitHub's documentation stated them on the date in this
skill's `sources.md`; re-read its custom-instructions page before you
write one.

- Repository-wide: `.github/copilot-instructions.md`.
- Path-specific: `NAME.instructions.md` under `.github/instructions/`,
  with an `applyTo` glob in its frontmatter; supported for the cloud agent
  and code review only.
- Agent instructions: `AGENTS.md` anywhere in the repository, nearest file
  wins; or a single `CLAUDE.md` or `GEMINI.md` at the root.
- Precedence: personal instructions, set in the UI, outrank repository
  instructions, which outrank organization instructions; when a
  path-specific file matches and a repository-wide file exists, both apply.
- Code review reads instructions from the head branch, not the base.
- No non-interactive runner the shared script knows: step 5b records "not
  measured: no runner in Copilot".

Step 1's file set is the three kinds above; step 4's scoping is `applyTo`.
