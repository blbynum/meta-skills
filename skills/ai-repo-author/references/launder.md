# Launder

How to find and replace personal identifiers and the user's own research
subjects in everything that will be committed. Read this for step 4, and
run the scan again in step 9.

## Contents

- What to search for
- Build the term list
- Run the scan
- Replace what it finds
- What stays
- History of an existing repository

## What to search for

- **Identity**: the user's name, email addresses, account names, and the
  name of their home directory. The script adds git's `user.name`,
  `user.email`, and the home directory name unless you pass
  `--no-identity`.
- **Machine and network**: home directory paths (also in the slug form
  `-Users-<name>-` that some tools build from a path), private host names
  (`.home.arpa`, `.local`, `.lan`, `.internal`), IP addresses, ssh
  remotes, email addresses. These are built into the script.
- **The user's own research subjects**: entity names, aliases, ids, case
  slugs, and assessment names taken from the user's data stores, and the
  places those records name. These are the leaks that a search for the
  user's name misses: an earlier setup shipped a contract whose examples
  were real records, with a real person's name and employer, until a
  search by the store's own entity names found them.
- **Anything else the user names**: an employer, a city, a project, a
  client. Ask once, in the step 1 message or before the scan.

## Build the term list

For each data store found in step 1, pass its records and names to the
script:

```sh
python3 scripts/launder_scan.py <dir>... \
  --jsonl <store>/data/entities.jsonl:name,aka,id \
  --names-from <store>/cases --names-from <store>/assessments \
  --terms-file <scratch>/extra-terms.txt
```

- `--jsonl FILE:FIELDS` takes the named fields of each record; a list
  field adds each item, and an id such as `person:pat-example` also adds
  `pat-example`.
- `--names-from DIR` adds each entry name in the directory without its
  extension: case slugs, assessment names.
- `--terms-file` takes one term per line; keep that file in a scratch
  directory, never in the repository.

Terms shorter than `--min-length` (default 3) are not searched; the
script lists them so you can check them by hand.

A store with no record file, such as a notes vault, has no list of
subjects to read. Its note titles are mostly topics, not people, so do
not pass the whole vault: take the titles that name a person, an
organization, or a place, and ask the user for the rest.

## Run the scan

Before the move, scan the input directories. After the move, scan the
repository root: with `.gitignore` in place, `git ls-files` lists exactly
what the commit will hold, and the script reads that list.

The first line of the output says how many files the script read, from
which source. Check it against the number you expect. Then:

- **COUNTS**: hits per term or pattern.
- **HITS**: `path:line: [term] line`.
- Exit status 0: no hits. 1: hits. 2: the scan did not run or read no
  file, which is a failed scan, not a clean one.

Use the script, not a shell loop. An earlier scan built its directory
list in a shell variable that zsh did not split into words, so grep
looked for one directory with a long name, read no file, sent its errors
to the null device, and reported nothing. A corrected rerun found the
hits. If you must search by hand, pass each directory as its own
argument and print how many files the search read.

## Replace what it finds

- **A path**: replace the personal part so the line still works:
  `/Users/<name>/vault` becomes `~/vault` in prose or `<user>` in a path
  pattern.
- **A real record used as an example**: write a fictional record of the
  same shape: the same fields, the same id pattern, an obviously
  fictional name ("Pat Example", "Example Strategies LLC", jurisdiction
  `XX`). Keep the schema unchanged.
- **A real organization in an eval prompt**: use a fictional one of the
  same kind. Put a fictional place in front of a generic name, so that the
  name does not match a real group ("Exampleton Citizens for Clean Water").
  Then rerun the trigger eval through the migrate skill so that the
  committed results match the committed prompts. When no migrate skill is
  configured, leave the old result file out of the commit and list it in
  the report.
- **A design note about the user's own sessions, cases, or region**:
  generalize it ("cases from one region's politics") and drop links into
  the data store.
- **A log or a result file with a machine path**: regenerate it, or
  replace the path as above.

Rerun the scan with the same arguments after the edits. Show its counts
in the report. Each remaining hit is either replaced or named in the
report with its reason.

## What stays

- **Public subject matter that a skill teaches from**, with its source in
  the ledger: a nationally reported organization used as a textbook
  example. Check that the term is not in the user's data store; if it is
  there, the user researched it, and it is the user's subject.
- **The license holder's name** on the copyright lines of `LICENSE` and of
  the notice in `link.sh`. Pass `--allow-line 'Copyright \(c\)'`.
- **The account in the clone URL** of the README, which names where the
  repository lives.
- **The `/Users/you` placeholder** in captured output. The script already
  ignores it.

Use `--allow <term>` for a public term that would otherwise appear in
every rerun, and name it in the report.

## History of an existing repository

A scrub of the files does not remove a term from the commits that added
it. In an existing repository, add `--history`: the script then also
scans every line that any commit added, in every branch. For each hit in
history, tell the user the commit and whether a remote holds it
(`git branch -r --contains <commit>`). A history rewrite changes every
later commit and breaks every clone. It is the user's decision; never do
it without their explicit yes.
