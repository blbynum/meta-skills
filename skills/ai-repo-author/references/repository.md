# Repository mechanics

The commands for steps 6, 7, and 9: the move, the copy of `link.sh`, the
links, git, versions, commits, merges, the agents rule, and the push.

## Contents

- Move
- Copy link.sh
- Link and check
- Initialize git and the identity
- Versions and branches
- Commits and merges
- The agents rule
- Push

## Move

1. The repository directory is the path the user gave in step 1. If it
   exists and is not empty (`ls -A <repo>` prints anything), stop and
   ask. For an input that is already the repository directory, a
   directory or a repository with skills in it, skip this step.
2. Create it and run `git init -b master` there; in place, run
   `git init -b master` only when it is not a repository yet. `link.sh` links only
   from inside a git repository, and git's ignore rules then apply to the
   launder scan and to the README capture. Make no commit yet.
3. Create `skills/` and `rules/` as needed, and `mv` each skill directory
   to `skills/<name>/` and each rule file to `rules/<name>.md`. In place,
   move only the entries that are not in that shape yet. Use `mv`,
   not a copy: `config.local.yaml` and a per-skill `.gitignore` travel
   with the directory, and no second copy stays behind for the harness to
   load twice.
4. Check that each skill with a `config.local.yaml` has a `.gitignore`
   beside it with the line `config.local.yaml`, and add one where it is
   missing.
5. Write the root `.gitignore`:

   ```text
   config.local.yaml
   .DS_Store
   __pycache__/
   ```

   Do not delete `__pycache__` or `.DS_Store` with `rm -rf`; the ignore
   file keeps them out of the commit.

## Copy link.sh

Copy from the default branch of the configured source as committed,
never from its working tree. The source clone can sit on another branch
with an older `link.sh`: one copy taken from a working tree predated the
license notice and had to be replaced.

From a local clone:

```sh
SRC=<link-script-source>
git -C "$SRC" fetch --quiet origin
REF=$(git -C "$SRC" rev-parse --abbrev-ref origin/HEAD)
git -C "$SRC" show "${REF}:link.sh" > <repo>/link.sh
chmod 755 <repo>/link.sh
test -s <repo>/link.sh && git -C "$SRC" show "${REF}:link.sh" | cmp - <repo>/link.sh && echo "link.sh matches $REF"
```

Keep the braces in `${REF}:link.sh`. In zsh, `$REF:l` is a modifier
that lowercases the variable, so `"$REF:link.sh"` asks git for
`origin/masterink.sh`, the copy comes out empty, and a `cmp` of two empty
streams reports a match. The `test -s` and the checks below catch an
empty copy.

If the clone has no remote, set `REF` to its default branch by name
(`master` or `main`), not to the branch it has checked out. From a URL,
download the raw file with `curl -fsSL <url> -o <repo>/link.sh`.

Then check the copy:

```sh
cd <repo> && ./link.sh --version
grep -c 'Permission is hereby granted' link.sh
```

Expect the script's version and `1`. An empty or broken `link.sh` can
run, print nothing, and exit 0, so read the output of each check. Do not
edit the copy, its header
included: the header carries the license notice that the license
requires in each copy, and the source URL that the agents rule points
to. If the repository is itself the source of `link.sh`, skip the copy.

## Link and check

```sh
./link.sh --list
./link.sh --harness <id>
./link.sh --harness <id>
python3 <this skill>/scripts/dep_check.py <repo> --linked <harness skills dir>
```

`<id>` is the user's harness; when the user does not say, use the harness
this session runs in. The first run prints a `linked <name>` line for each
skill. The second run must print `no changes`. A line `skipped <name>:
... exists and is not a symbolic link` on standard error means that a real
directory or file of that name is still in the harness directory, and the
harness keeps loading it instead of the repository's copy. The exit status
is still 0, so read the output. Ask the user whether to move the old one
aside; do not delete it. The dependency check with
`--linked` confirms that each link resolves into the repository and that
each relative path between skills and shared directories resolves through
the links. Add to its arguments any skill that stayed behind and reads a
shared directory that moved.

If the old location is a git repository, for example the harness's own
configuration directory, `git -C <old> status --short` now shows the
moved directories as deleted and the new links as untracked. Tell the
user; those changes are theirs to commit. Do not commit there.

## Initialize git and the identity

Commit as the user's identity:

```sh
git -C <repo> config user.name
git -C <repo> config user.email
```

If either prints nothing, ask the user for the name and email. You can
offer the identity on their own recent commits in another repository,
`git -C <link-script-source> log -1 --format='%an <%ae>'`. Pass the
identity with each commit, `git -c user.name="<name>" -c
user.email="<email>" commit ...`, and do not write it into git's global
configuration. With no name set, git builds one from the account name: an
earlier first commit came out under the account name and had to be
amended. After each commit, `git log -1 --format='%an <%ae>'` must show
the user's identity.

Add a remote only with the URL the user gives:
`git remote add origin <url>`.

## Versions and branches

`VERSION` at the root holds `major.minor.snapshot`. `master` is the
development branch. An existing repository keeps its own default branch,
for example `main`: write its name wherever this file and the template
say `master`. A new repository starts at `1.0.0`, committed
directly on `master`; there is no older version, so no version branch
exists yet. An existing repository with no `VERSION` gets `1.0.0` in the
change that adds versioning.

Every later change that merges into `master` gets one new version. The
level comes from the change's effect on a person who already has the
repository linked into a harness; if more than one level fits, use the
highest:

| Level | The change | Examples |
|---|---|---|
| Major | breaks the install, or needs more than `git pull` and a new run of `link.sh` | a skill or rule removed or renamed; a config key removed, renamed, or made required; a link script command that worked before now fails |
| Minor | adds something the install can use, and breaks nothing | a new skill or rule; a new optional config key; a new link script option |
| Snapshot | every other change | guidance edits, fixes, references, evals, documentation |

A branch named after each version stays at the last state of `master`
before the next version. Snapshot branches (`1.4.2`) are kept only for
the current minor version. When a new minor version is cut, the branch
`1.4` marks the old minor version and its snapshot branches are deleted;
each is an ancestor of `1.4`, so no commit is lost. A new major version
also leaves the branch `1`. Major and minor branches are kept.

## Commits and merges

The commit message names the version and level:

```text
<what the change does, in the imperative>

Version X.Y.Z (<major|minor|snapshot>).

<what changed and why; for this skill's work, the pass record>
```

The first commit says `Version 1.0.0 (first version).`

A change after the first version goes on its own branch, with `VERSION`
set there. Immediately before the merge, check the version again,
because another change can take the number first:

1. `git fetch`, read `VERSION` on `master`, and set the branch's
   `VERSION` to master's version plus one step at the change's level.
   Commit that.
2. Leave the version branch at master's tip: `X.Y.S` for a snapshot
   change; `X.Y` for a minor change, then delete the old snapshot
   branches; `X.Y` and `X` for a major change.
3. Merge without fast-forward:

   ```sh
   git switch master
   git merge --no-ff <branch> -m "Merge X.Y.Z: <change>" -m "X.Y.Z: <change>"
   ```

Give the message with `-m`. An earlier merge given `-F -` with the
message on standard input failed with "could not read file '-'", and
the merge did not run.

## The agents rule

`AGENTS.md` at the root carries the version procedure as steps for agents
that work on the repository. `CLAUDE.md` and `GEMINI.md` each hold one
line, `@AGENTS.md`: Claude Code and Gemini CLI read their own file names
and import another file with `@`. Hand the template below to the rule
skill (`rule-skill`) with the repository's name and its `link.sh` case;
it applies its own standards. When no rule skill is configured, write the
template as it stands and say in the report that the rule checks did not
run. Keep `AGENTS.md` and the README's Versioning section in agreement.

```markdown
# <repo-name>: instructions for agents

These instructions are for agents that work on this repository. They do
not ship to users: keep this file at the repository root, never in
`skills/` or `rules/`, and never link it into a harness. `CLAUDE.md` and
`GEMINI.md` import this file for the harnesses that do not read
`AGENTS.md`.

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
   - Major: the install breaks, or needs more than `git pull` and a new
     run of the link script. Examples: a skill or rule removed or
     renamed; a config key removed, renamed, or made required; a link
     script command that worked before now fails.
   - Minor: the install keeps working and gains something. Examples: a
     new skill or rule; a new optional config key; a new link script
     option; a skill that does a new kind of task.
   - Snapshot: every other change: guidance edits, fixes, references,
     evals, documentation.
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
6. Write the version and level in the commit message: "Version 1.4.3
   (snapshot)." Merge into `master` with `git merge --no-ff`, titled
   "Merge X.Y.Z: <change>", and give the message with `-m`.
7. `link.sh` is a copy of the link script from the repository named in
   its header. It has a version of its own, `LINK_SH_VERSION` near the top
   of the script, which belongs to that source, and it gets no branches
   here.
   - Do not edit `link.sh` in this repository. To update it, replace the
     whole file with the newer version from the source URL in its header,
     and keep the header with the license notice.
   - A change that replaces `link.sh` takes a level for `VERSION` at
     least as high as the script's own change: major when a command that
     worked before now fails; minor for a new option or harness; snapshot
     for fixes and help text.
```

When the repository is itself the source of `link.sh`, step 7 instead
says: if a change edits `link.sh`, set `LINK_SH_VERSION` too, at the
level of its effect on a person who runs the script; the change's level
for `VERSION` is at least that level; and immediately before the merge,
read `LINK_SH_VERSION` on `master` and set the branch's value to master's
value plus one step, because two branches that both raise it from the
same value merge with no conflict.

## Push

Push only when the user says to:

```sh
git push -u origin master
git push origin <new version branches>
git push origin --delete <deleted snapshot branches>
git ls-remote origin
```

The last command confirms that the remote holds what you pushed. Do not
push a change branch unless the user asks.
