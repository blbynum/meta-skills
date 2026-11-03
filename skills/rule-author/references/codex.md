# Codex

Rule files as Codex's documentation stated them on the date in this
skill's `sources.md`; re-read its AGENTS.md page before you write one.

- Global: `~/.codex/AGENTS.override.md` if it exists, otherwise
  `~/.codex/AGENTS.md`; only the first non-empty file at this level.
- Project: in each directory from the project root down to the working
  directory, the first of `AGENTS.override.md`, `AGENTS.md`, then the
  names in `project_doc_fallback_filenames`; at most one file per
  directory, concatenated root-down, nearer files overriding earlier
  guidance.
- Cap: files stop being added once the combined size reaches
  `project_doc_max_bytes`, 32 KiB by default; raise it or split across
  nested directories.
- Scoping: none by file pattern; nearer directories override.
- No non-interactive runner the shared script knows: step 5b records "not
  measured: no runner in Codex".

Step 1's file set is the chain above; step 4's budget is the byte total
against the cap; step 4's scoping is by directory only.
