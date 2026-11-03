# Gemini CLI

Rule files as Gemini CLI's documentation stated them on the date in this
skill's `sources.md`; re-read its context-file page before you write one.

- Global: `~/.gemini/GEMINI.md`.
- Project: `GEMINI.md` in the workspace directories and their parent
  directories, loaded at start; a file in a subdirectory loads when a tool
  first touches that directory.
- File names: `GEMINI.md` by default; `context.fileName` in
  `settings.json` takes one name or a list, for example
  `["AGENTS.md", "GEMINI.md"]`.
- Imports: an `@file.md` line imports another file, by a relative or an
  absolute path. A root `GEMINI.md` that holds only `@AGENTS.md` serves an
  `AGENTS.md` rule to Gemini CLI without a settings change.
- Scoping: by directory only; no file-pattern scoping is documented.
- Limits on import depth or file size: not stated on the page.
- No non-interactive runner the shared script knows: step 5b records "not
  measured: no runner in Gemini CLI".

Step 1's file set is the chain above; step 4's scoping is by directory.
