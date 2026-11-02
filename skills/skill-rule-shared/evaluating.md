# Measuring an artifact

How to test whether a skill or a rule changes what the model does. The
desk-check in workflow step 5 tests whether the text is clear to a careful
reader. This file covers the other question: does the artifact change
behavior, and at what cost.

## Contents

- When to measure
- Where eval files go
- Writing the eval set
- The trigger eval (skills only)
- The A/B eval (skills and rules)
- Confounds to record with every run
- Reading the results
- What the numbers cannot tell you

## When to measure

Measuring costs real money and 10–30 minutes. It is required for every
user-wide skill and every user-wide rule, and whenever a pass rewrites a
skill description; run it also when the user disagrees with a judgment about
whether the artifact helps. Skip it only for a wording fix or a
single-project rule, and write the skip and its reason in the pass record — an
unstated skip reads as a run.

The two evals answer different questions, so run whichever the change
touches. A description edit needs the trigger eval. A body or rule edit needs
the A/B eval. A new skill needs both.

## Where eval files go

Keep every eval file outside the artifact's directory and outside the
repository: the eval set, fixtures, checking scripts, an old copy of the
artifact, and the results. Some harnesses walk a skills directory
recursively, so a copy of a `SKILL.md` below a skill's directory loads as a
second skill there. Results also go stale with the next edit, and version
control already keeps every old version.

1. Before the run, create a temporary directory with `mktemp -d`. The
   commands below call it `<eval-dir>`.
2. Put every input and output of the run in `<eval-dir>`. For `--old`, write
   the old version there from version control: `git show <ref>:<path>` for
   one file, or `git archive <ref> <dir> | tar -x -C <eval-dir>` for a skill
   with references.
3. Grade the outputs, then write the result into the pass record: the pass
   counts, the model, the harness version, and the cost.
4. Delete `<eval-dir>` before the pass ends.

The pass record is all that a run leaves behind. The next pass writes its own
eval set.

## Writing the eval set

Write the prompts a real user types, not clean abstractions. Real prompts
carry file paths, product names, background, lowercase, and typos, and the
model keys on that texture. "Format this data" tests nothing.

Start from what step 0 of the workflow recorded. When the artifact has been
in use, real past transcripts are the best eval set available: the queries
carry the texture above, and the old outputs are measured baselines that no
synthetic eval provides. Read them first whenever the artifact has history.

Two traps, each of which voids an eval:

- Do not reuse an eval query as a worked example inside the artifact. The
  with-arm is then testing on training data, and the result says nothing.
  The fixture's own identifiers count too: a flag, key, or function name
  from the fixture used as an example hands the with-arm the fixture's
  facts. Grep the artifact for the fixture's names before a suite.
- `ab_eval.py --mode rule` gives the model no slash-command framing. An eval
  query that only makes sense as a skill invocation ("refine this prompt")
  gets answered as an ordinary question in both arms and measures nothing.
  Phrase rule-mode queries as the bare task.

Three evals is the working minimum. Each needs expected behavior stated as
observable outcomes, not impressions:

```json
{
  "artifact": "my-skill",
  "evals": [
    {
      "id": "capture-during-work",
      "query": "quick note: the b2 bucket lifecycle rule was hiding the backups, keep-only-last-version was set. took me an hour to find",
      "files": [],
      "expected_behavior": [
        "Writes one file under the configured output directory",
        "Adds a line to INDEX.md",
        "Does not ask which project the note belongs to"
      ]
    }
  ]
}
```

For the trigger eval, half the queries should be near-misses — prompts that
share vocabulary with the skill but need something else. Obvious negatives
("write a fibonacci function" against a PDF skill) measure nothing. The
useful negative is the one you have to think about.

A third trap: a should-trigger query that refers to attached material
("look at these three ads and tell me...") measures nothing in this
text-only harness, because nothing is attached — the model can correctly
ask for the material before it loads any skill, and the query then scores
0.00 for a behavior that is right. Phrase trigger queries so the
observable activity is in the prompt text itself, or pass real files via
the eval's `files` field.

## The trigger eval (skills only)

```bash
python3 ~/.claude/skills/skill-rule-shared/scripts/trigger_eval.py --skill <name> --eval-set <eval-dir>/queries.json --json <eval-dir>/result.json
```

The script runs each query in a scratch directory and reports how often the
skill loaded. Read three numbers: the pass count, the trigger rate on
should-trigger queries, and the trigger rate on near-misses. A rate near 0.5
is a coin flip, not a pass — the description is ambiguous for that query.

An unscoped rule loads every session, so there is no trigger to measure. A
rules file with `paths:` frontmatter does have a loading condition. The
trigger script cannot see it (it detects Skill calls and SKILL.md reads), so
check it by hand:
in a fresh session, open a file that matches the glob and one that does not,
and ask which rules are loaded, or read the rule text back. Do this once per
`paths:` edit.

## The A/B eval (skills and rules)

```bash
python3 ~/.claude/skills/skill-rule-shared/scripts/ab_eval.py --evals <eval-dir>/evals.json --out <eval-dir>/run --mode skill
```

For a rule, pass `--mode rule --rule-file <path>`. The script runs every eval
in both arms, several times each, and writes per-run outputs, transcripts,
and costs plus a `summary.md`. It deliberately does not grade. Grade the
outputs yourself against `expected_behavior`, and write a checking script for
anything mechanical — "the file exists", "the frontmatter parses" — because a
script is repeatable across iterations and eyeballing is not.

How the arms are built matters for what the result means:

- `--mode skill` removes only the skill under test from the baseline arm
  (`--disallowed-tools "Skill(<name>)"` plus a `skillOverrides` setting),
  so every other skill, rule, and hook stays loaded in both arms and the
  comparison isolates one artifact. The script checks that the with-arm
  actually loaded the skill and reports a run where it did not.
- `--mode rule` starts both arms from `--safe-mode`, which loads no CLAUDE.md,
  skills, or hooks, and injects the rule text into the with arm through
  `--append-system-prompt`, with the frontmatter and HTML comments stripped
  as Claude Code strips them. This is an approximation: a real rule arrives
  as a `<system-reminder>` in the user turn, not as system-prompt text, and
  a real session carries the user's other rules and skills. A rule that
  competes with other loaded rules will look better here than in practice.
- A rule that governs a tool the eval harness does not have cannot be
  measured this way at all. Both `--mode rule` arms run as `claude -p
  --safe-mode`. Read that session's tool list before you write the eval
  set — `claude -p --safe-mode --output-format stream-json --verbose "say
  hi"` prints it in the `init` event. If the governed tool is absent (for
  example a desktop-only or MCP-only tool), the rule has nothing to change
  in either arm and the run measures noise: desk-check instead and record
  the skip with that reason.
- `--old` / `--new` compares two versions of the same artifact in the same
  arms; use it when the question is "did the edit help", not "does the
  artifact help".

Each run gets its own throwaway directory, so work that stays in the working
directory is contained. Work that writes to an absolute path is not: an
artifact that saves into a real vault, repository, or config directory will
write there for every run in both arms. Check what the artifact writes before
you launch a suite, and point it at a scratch copy if it writes outside the
working directory. Two mechanics of the script help: a directory listed
in an eval's `files` is copied
recursively into the run dir under its own name (so a query about "this
project" must name that directory, for example `./logsift`, or the model
works in the empty run root), so a nested fixture tree
(for example a tracker directory an artifact discovers by relative path)
seeds cleanly and isolates every run; and the harness writes its own
`metrics.json`, `transcript.jsonl`, and `output.md` into every run dir, so
a mechanical check script diffing run dirs against fixtures must exclude
those three names or it false-positives on all runs.

The same check applies to the trigger eval when the skill launches something
expensive. `dontAsk` denies Bash and edits, but `claude -p` starts a
dynamic workflow with no prompt at all, so a skill whose body invokes the
Workflow tool can start the real run from inside an eval. Set
`CLAUDE_CODE_DISABLE_WORKFLOWS=1` in the environment for every eval of such
a skill; the runtime reads it at startup and removes the tool. Before you
launch any suite, ask what the loaded skill will try to do in its first
turns and which of those actions `dontAsk` does not stop.

More hazards to check before you trust a run:

- A skill's reference files live in its own directory, outside the
  throwaway run directory, so a `Read` of them needs a permission that a
  non-interactive run denies. `ab_eval.py --mode skill` pre-allows
  `Read(//<abs skill dir>/**)` in both arms for that reason. When the
  artifact reads files anywhere else, check the transcripts for
  "requested permissions to read".
- A with-arm run where the skill did not load is a baseline run, whatever
  the model's output says. Read the `artifact_loaded` flag and the Skill
  call's result in the transcript; a Skill call that returned an error
  did not load the skill.
- A run with zero turns and an empty result is a failed invocation, not a
  model that chose silence. Find the cause before you grade — one cause to
  check is an injected shell command (`` !`command` ``) that matched no
  allow rule.
- Web tools and Bash prompt for permission, so a non-interactive run
  denies them. Pass `--allowed-tools WebSearch WebFetch "Bash(curl *)"`
  (and the exact script the skill runs) to `ab_eval.py` so both arms can
  do the task; `--effort` sets the effort level.
- Before a suite with file fixtures, confirm that one run can read each
  fixture (a PDF may need `pdftoppm`, from poppler), or convert the
  fixture to text. Exclude from grading any run that could not read a
  fixture; do not count it against either arm.

Read the transcripts, not only the outputs. The pass rate says whether the
run ended well; the transcript says how, and that is where the fixable
problems are — a script reinvented in every run belongs in `scripts/`, a
detour repeated in every run means the text sends the model the wrong way.

## Preflight checks

Each of these can fail every run in a suite for a reason that has nothing
to do with the artifact under test:

- **Python version.** The scripts use `str | None` annotations, which need
  Python 3.10 or later; an older `python3` fails at import. Run them with
  Python 3.10 or later.
- **Login state.** A run that fails to authenticate can look finished.
  Before a suite, run a one-word `claude -p` and expect a non-zero
  `total_cost_usd`. If it fails, sign in to the terminal CLI with
  `claude auth login`.
- **Slash-command queries.** In `--mode skill`, a query that begins with
  `/<skill>` gives the baseline arm nothing to run, because the skill is
  disabled there. The with-arm loads the body by slash expansion, which
  the `artifact_loaded` detector cannot see, so it reports "did not load"
  for runs that did. Phrase skill-mode queries as prose that the
  description should catch, and let the trigger eval tell you whether it
  does.
- **Artifacts that write to a fixed absolute path.** A skill whose default
  target is a real directory (`~/projects/<name>`) reaches for it from a
  scratch run directory. Check `ls` on the real target after a suite, and
  phrase the eval so the working directory is the target.

## Confounds to record with every run

A result is only comparable to another result if both say what ran. The
scripts write these into every result file; check them before you compare
runs from different days:

- **Claude Code version.** The scripts call the `claude` on `PATH`, which
  can lag the desktop app by several releases. Results carry `claude
  --version`; a comparison across versions is a comparison across two
  harnesses.
- **Resolved model.** `--model` unset means the account default, which can
  change between passes. Results carry the model the `init` event reports,
  not the string "default".
- **Injected context.** Every `claude -p` session outside `--safe-mode`
  loads the user's rules, skills, and plugin hooks. A SessionStart hook can
  inject text that changes the behavior under test — for example a plugin
  hook that tells the model it must invoke any skill with a 1% chance of
  applying, which inflates every trigger rate measured under it. Before a
  trigger eval, list the active hooks (`~/.claude/settings.json`,
  `~/.claude/plugins/`) and record them; if one pushes on the behavior you
  are measuring, disable it for the run or state that the rate is
  conditioned on it.
- **Skill roster.** The skills `claude -p` loads on the CLI can differ from
  the desktop app's, so a trigger eval may not see a competitor that only
  exists there. Name the roster the eval ran against.

## Reading the results

Compare the arms on three axes, in this order:

1. **Did behavior change?** If both arms pass everything, the artifact is not
   earning its context. Either the task was already easy, or the expected
   behavior is too loose to discriminate. Tighten the evals before concluding
   the artifact works.
2. **Did it change for the better?** Grade against expected behavior. Count a
   run as passing only when every stated behavior holds.
3. **What did it cost?** `summary.md` carries cost, duration, and turns per
   arm with a standard deviation. An artifact that lifts quality and doubles
   cost is a trade-off to report to the user, not a win to announce.

When the two arms land within a standard deviation of each other, the run
measured noise. Raise `--runs` or accept that the effect is too small to see
at this sample size, and say which.

## What the numbers cannot tell you

Published benchmarks find that skills help by wildly different amounts
depending on the domain and the model — a fleet average hides swings from a
few points to fifty. That variance is the argument for measuring the artifact
in front of you rather than assuming the average applies to it.

Three limits worth stating to the user rather than hiding:

- A few evals cannot prove generality. They can only show that the artifact
  fails to help on the cases tested, which is still the finding that matters.
- Grading with the same agent that wrote the artifact is not independent. For
  a close call, have a subagent grade the outputs without telling it which arm
  produced which.
- Results are model-specific. An artifact tuned against one model can carry
  guidance that a weaker model needs spelled out, or that a stronger model
  over-follows. Re-run the eval with `--model` set to the other models the
  artifact will meet.
