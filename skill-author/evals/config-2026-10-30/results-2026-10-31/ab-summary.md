# A/B eval: skill-author

Mode: skill (old-vs-new) | Model: claude-opus-5-5[1m] | Claude Code: 2.1.287 | Runs per arm: 3
Plugins loaded: cc-plugin-agents-md@builtin, cc-plugin-plugin-authoring@builtin, cc-plugin-telemetry@builtin

## photo-backup-path

> make me a skill that copies my Lightroom catalog backups onto the external drive at /Volumes/Photos-Backup and prunes copies older than 90 days. Draft only: skip the observation runs, the web research, the eval scripts, and the changelog, and write the skill into ./skills/ in this directory.

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.611 ± 0.109 | 109 ± 22 | 12.0 ± 2.0 | 0 | 0 | 3/3 |
| new | 0.518 ± 0.063 | 89 ± 9 | 13.7 ± 1.5 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- SKILL.md has a ## Config table as its first section with a required key for the backup drive directory
- The body and description do not contain /Volumes/Photos-Backup
- The Config section ends with the read instruction: read config.local.yaml, stop and offer set-up on a missing required key, stop on a missing directory
- A .gitignore containing config.local.yaml exists in the skill directory; no config.yaml, no config.example.yaml, no scripts/config.py
- The 90-day prune age is a named default in the body or an optional key, not a required key
- Frontmatter uses only name, description, and metadata

## commit-style-no-config

> make a skill that rewrites my staged commit message into conventional commits format (type(scope): subject, subject under 50 characters, body wrapped at 72). Draft only: skip the observation runs, the web research, the eval scripts, and the changelog, and write the skill into ./skills/ in this directory.

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.396 ± 0.175 | 63 ± 27 | 9.0 ± 7.2 | 0 | 0 | 2/3 |
| new | 0.420 ± 0.052 | 58 ± 9 | 9.3 ± 1.5 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- No ## Config section, no config.local.yaml, and no .gitignore for it
- No key is invented for commit types, scopes, or line lengths
- If the report mentions config at all, it says in one line that the skill has no config keys

## minutes-companion-skill

> make a skill that files meeting minutes into my Obsidian folder after a call and has my summarize skill write the TL;DR at the top first. Draft only: skip the observation runs, the web research, the eval scripts, and the changelog, and write the skill into ./skills/ in this directory.

| arm | cost $ | duration s | turns ± sd | timeouts | API errors | artifact loaded |
|---|---|---|---|---|---|---|
| old | 0.369 ± 0.030 | 55 ± 6 | 9.0 ± 1.0 | 0 | 0 | 3/3 |
| new | 0.420 ± 0.031 | 60 ± 9 | 11.3 ± 2.1 | 0 | 0 | 3/3 |

Expected behavior to grade against:

- The Config table has a required key for the Obsidian folder
- The summarize skill is an optional key with default summarize, not only a name in prose
- No key is added for anything else, such as the file name pattern or the TL;DR length
- The body names actions, not harness tool names
