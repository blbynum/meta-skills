# meta-skills: instructions for agents

<!-- last-verified: 2026-11-02 -->

These instructions are for agents that work on this repository. They do
not ship to users: keep this file at the repository root, never in
`skills/` or `rules/`, and never link it into a harness. `CLAUDE.md` and
`GEMINI.md` import this file for the harnesses and versions that do not
read `AGENTS.md` directly.

## Versioning

`VERSION` at the repository root holds the version as
`major.minor.snapshot`. `master` is the development branch. Keep this
section and the "Versioning" section of `README.md` in agreement.

1. Give every change that merges into `master` one new version. Set it in
   `VERSION` on the change's branch. A helper branch that merges into a
   change's branch gets no version of its own.
2. Pick the level from the change's effect on a person who already has
   the repository linked into a harness. If more than one level fits, use
   the highest.
   - Major: after `git pull` and a new run of the link script, something
     the person had stops working. Examples: a skill or rule removed or
     renamed; a config key renamed or made required.
   - Minor: the install keeps working and gains something. Examples: a
     new skill or rule; a new optional config key; a skill that does a
     new kind of task.
   - Snapshot: every other change: guidance edits, fixes, references,
     documentation, changes to the options of the link script.
3. Immediately before the merge, check the version again; another change
   can take the number first. Fetch, read `VERSION` on `master`, and set
   the branch's `VERSION` to master's version plus one step at the
   change's level:
   - Snapshot: `X.Y.S` becomes `X.Y.(S+1)`. If the branch's snapshot is
     less than or equal to master's snapshot, it must change to master's
     snapshot plus one.
   - Minor: `X.Y.S` becomes `X.(Y+1).0`.
   - Major: `X.Y.S` becomes `(X+1).0.0`.
   Commit that change before the merge.
4. Before the merge, leave a branch named after master's current version
   at master's tip:
   - For a snapshot change, make sure the branch `X.Y.S` (for example
     `1.4.2`) exists there. Create it if it does not exist.
   - For a minor or major change, create the branch `X.Y` for the old
     minor version (for example `1.4`). For a major change, also create
     the branch `X` (for example `1`). Then delete the snapshot branches
     of the old minor version (`1.4.0`, `1.4.1`, and so on). Each one is
     an ancestor of `X.Y`, so no commit is lost.
5. Never delete or move a major or minor branch. When `master` is
   pushed, push the new version branches and the deletions with it.
6. In the commit that sets `VERSION`, write the version and level as the
   first paragraph after the title: "Version 1.4.3 (snapshot)." When the
   change merges into `master`, finish steps 3 and 4 first, and step 7 if
   the change edits `link.sh`. Then merge with `git merge --no-ff`, and
   give the message with two `-m` options:

   ```sh
   git merge --no-ff <branch> -m "Merge X.Y.Z: <change>" -m "X.Y.Z: <change>"
   ```

7. `link.sh` has a version of its own, `LINK_SH_VERSION` near the top of
   the script, because people copy the script alone into other
   repositories. It is independent of `VERSION` and gets no branches.
   - If a change edits `link.sh`, set `LINK_SH_VERSION` too, in the same
     `major.minor.snapshot` form. Pick the level from the change's effect
     on a person who runs the script: major when a command that worked
     before now fails; minor for a new option or harness; snapshot for
     fixes and help text.
   - A change to the options of `link.sh` counts only toward
     `LINK_SH_VERSION`. For `VERSION`, it is a snapshot change unless it
     also fits a higher level in step 2.
   - Immediately before the merge, read `LINK_SH_VERSION` on `master`.
     Set the branch's value to master's value plus one step at the
     script level, as in step 3. Two branches that both change 1.0.0 to
     1.0.1 merge with no conflict, so without this check the second
     change gets no new version.
