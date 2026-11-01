# Data and provenance

How to keep the user's data out of the repository while the code that
reads it goes in, and how to split provenance ledgers so that each one
travels with what it describes. Read this for step 3.

## Contents

- What counts as data
- Data stays out; its code goes in
- Move code out of a data directory
- Provenance splits by owner

## What counts as data

Data is material that grows with use and belongs to the user: research
data, a notes vault, a findings store, case files, assessments, an inbox
of downloads. It holds the user's subjects, so it never enters a
repository that other people can clone, and it changes on every run, so
it does not belong in version history either.

## Data stays out; its code goes in

- **The skill names the data through a required config key**, for
  example `| findings-store | yes | | directory of the findings store |`.
  The value lives in `config.local.yaml`, which git ignores. No body,
  reference, or script names the path.
- **The code that serves the data goes into a shared directory** in the
  repository, `skills/<name>-shared/`: the data's contract (layout,
  record schemas, the read and write protocol), the scripts that read or
  write the data, and an init script that creates an empty copy for a new
  machine. A shared directory, not one skill's directory, when more than
  one skill reads the data: otherwise the other skills read that skill's
  files, and step 2 removed exactly that kind of dependency.
- **Every script takes the data path as an argument**, such as
  `--store <path>` or a positional path. No script assumes that it runs
  from inside the data directory, and no script holds a default path to
  the user's data.
- **The contract names roles, not skills**: "a skill that writes cases",
  not a skill's name. A shared directory names no consumer.
- **Examples in the contract are fictional records of the same shape.**
  Step 4 checks this.
- **The README gets a section on data setup** (step 8): the init command,
  then the config key to set.

## Move code out of a data directory

When the contract and scripts live inside the data directory today:

1. Back up the data directory first, as an archive in a scratch
   directory. Record its record counts with the data's own check script.
2. Move the contract, the scripts, and any design notes into the shared
   directory. Leave the data, and a short README in the data directory
   that says where the code now lives, by role and not by path.
3. Change each script to take the data path as an argument, and each
   usage line in the contract and the README to pass it.
4. Run each script under the oldest declared interpreter against a copy
   of the data, from a working directory outside the data directory.
5. Run the data's check script on the real data and compare the counts
   with step 1. Run the init script into a scratch path, then the check
   script on the result.
6. Run one fresh session through a skill that reads the data, and
   confirm that it found the contract in the shared directory and passed
   the data path to the scripts.

## Provenance splits by owner

A provenance ledger (`sources.md`) records the sources behind a skill's
guidance, with the date each was last verified.

- The ledger of the authoring skills, the one that the migrate skill and
  the rule skill share, keeps its core sources and the sections for the
  skills in the same repository as itself.
- Every other skill keeps its sections in a `sources.md` in its own
  directory. Its `SKILL.md` never links that file, so the file costs no
  context when the skill loads.
- Sections for skills that exist nowhere any more go to one file outside
  the repository, in a place the user names.
- Split before the move, so that the move carries the right sections.
  Count the lines of each ledger before and after: every line lands in
  exactly one place.
- When a ledger outside the input, for example in another repository,
  holds sections for the skills that move, a change there is a change
  outside the new repository: propose it and apply it on the user's yes.
