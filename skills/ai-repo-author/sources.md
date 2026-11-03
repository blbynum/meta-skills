# Sources — ai-repo-author

Provenance ledger for the ai-repo-author skill: every subject-matter claim it
makes, with the source, the date it was last verified, and the models or
vintage a finding was measured on. SKILL.md does not link this file, so it
never loads with the skill. The authoring skill reads it at its research
step and refreshes the "Last verified" dates of the sources it re-checks.
Moved out of the shared ledger on 2026-11-03; entries keep their original
wording and dates.

## ai-repo-author skill subject-matter sources

Provenance for the skill created 2026-11-01. Its procedure comes from the
user's own practice, not from vendor guidance; its few harness facts are
grounded in entries above.

### ai-repo-author — the treatment, from two repository setups (2026-11-01)
- Sources: the transcripts of the sessions that set up this repository
  (2026-10-31 to 2026-11-01) and a second skills repository of three
  research skills (2026-11-01), session
  69abbd20-032e-4c0c-9880-3d4c6ea3e444 and its forks, read for step 0 of
  the create pass; the user's request that specified the treatment. This
  repository's `AGENTS.md` at version 1.2.0 is the reference text for the
  agents-rule template; the step for a copied `link.sh` comes from the
  second repository's `AGENTS.md`.
- Last verified: 2026-11-01.
- Supports: each failure the skill names: a README written without the
  writing skill's README contract that carried a false claim; `link.sh`
  copied from a working tree that predated the license notice; changelog
  entries appended after the changelogs were removed; scripts that crashed
  under the system Python 3.9 on `dict | None` annotations; a usage line
  written from memory without the data-path argument; contract examples
  that were real records; eval prompts that named real organizations; a
  scan whose directory list zsh did not split, so it read no file and
  reported nothing; a config key that held a value that differs by
  harness; a portable claim made before the portability check existed; a
  first commit under the account name because git had no user name set;
  `git merge -F -` failing with "could not read file '-'".

### ai-repo-author — the definition of a major version (2026-11-02)
- Sources, read 2026-11-02: SemVer 2.0.0, https://semver.org/ and its
  source text in the semver/semver repository (rules 1, 3, 4, 5, 8, 11 and
  the FAQ); the Agent Skills specification and
  https://github.com/agentskills/agentskills/issues/46; Claude Code
  https://code.claude.com/docs/en/plugins/loading.md and
  https://code.claude.com/docs/en/plugins/dependencies.md. Read through an
  extraction prompt only: EffVer, https://jacobtomlinson.dev/effver/; the
  Cargo guide, https://doc.rust-lang.org/cargo/reference/semver.html; Go,
  https://go.dev/doc/modules/version-numbers; GitHub Actions,
  https://docs.github.com/en/actions/how-tos/create-and-publish-actions/manage-custom-actions;
  `gh skill`, https://cli.github.com/manual/gh_skill_publish.
- Last verified: 2026-11-02.
- Supports: the major test in `references/repository.md` and in this
  repository's `AGENTS.md`. SemVer defines major by the public API that a
  project declares, so the project sets the scope. Cargo leaves runtime
  behavior and applications to the maintainer's judgment. No source read
  defines a major version for a skill: the specification has no version
  field, and issue #46 is open. The test is the user's decision of
  2026-11-02, not a vendor rule.

### ai-repo-author — instruction-file imports
- Grounded in "Claude Code memory and rules documentation" (an
  `@AGENTS.md` import in `CLAUDE.md`; re-fetched 2026-11-01: "Keeping the
  import never makes Claude read `AGENTS.md` twice", and Claude Code reads
  `AGENTS.md` directly from v2.1.277, by default "only when you have no
  `CLAUDE.md` in your working directory or above it") and "Gemini CLI
  context files" (imports with `@file.md`; verified 2026-11-01).
- Supports: the one-line `CLAUDE.md` and `GEMINI.md` in
  `references/repository.md`, "The agents rule".

### ai-repo-author — link.sh 1.0.0 interface
- Source: `./link.sh --help` and `--list`, and two runs from a scratch home
  directory, 2026-11-01 (link.sh 1.0.0, this repository at 2.1.0).
- Supports: the repository shape; that the script links only from inside
  a git repository; `--harness`; the second run printing `no changes`; the
  MIT notice in the header, which each copy of the script keeps.
