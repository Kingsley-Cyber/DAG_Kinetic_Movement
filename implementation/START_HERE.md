# Implementation — start here

This folder is everything an implementing model needs to execute the plan with almost no owner
involvement. The owner's only jobs are in `OWNER_ACTIONS.md`.

## For the owner: how to run it

1. Open Claude Code (desktop Code tab or terminal) on the folder `/Users/king/cpcs-director`.
2. Pick a Sonnet-class model.
3. Paste the block below as the first message. That is all. Repeat in a new session whenever the
   previous one stops; it picks up from `QUEUE.md`.

```
You are the implementing model for this repository. Read, in order: AGENTS.md,
implementation/START_HERE.md, implementation/QUEUE.md, plan/GOALS.md, plan/HANDOFF.md.
Then execute the first work order in implementation/QUEUE.md whose status is `todo` and whose
dependencies are `done`. Follow that work order exactly: its "Read first" list, steps, tests and
acceptance. When it passes, update its status in QUEUE.md, add an entry to plan/STATUS.md,
commit locally on branch `director`, and continue with the next work order. Stop when you reach
a GATE, when a work order's stop condition fires, or when you would have to guess: in that case
write the question under "Blocked" in plan/STATUS.md and in implementation/OWNER_ACTIONS.md and
stop. Never push. Never edit cpcs/, Additional/ or the research folders. Never modify the
original tests in director/tools/tests/test_director.py; add new tests in new classes.
```

## For the implementing model: the rules of this folder

- **One work order at a time**, in queue order. A work order is self-contained: if it does not
  say it, look in the file it points to; if that does not say it either, stop and ask.
- **Decisions already made** are listed in each work order so you do not have to guess. Do not
  reopen them.
- **Tests first.** Each work order lists the tests to add by name and what they assert. Write
  them, watch them fail, then implement. All existing tests must stay green and unmodified:
  `python3 -m unittest discover -s director/tools/tests`.
- **Python 3.9**, stdlib + pyyaml + jsonschema only. No `X | Y` unions, no `match`.
- **Schema rule:** a field is added to `director/ir.schema.json` only together with the check or
  emit code that reads it, in the same commit. New fields are optional unless the work order says
  otherwise, so existing runs stay valid.
- **Run 001 is a fixture.** Do not change `director/runs/001_bottle_selfie/ir.json`.
- **Runs are written by you as the reasoning LLM** following `director/protocol.md`. Every run
  needs `ask.md`, `ir.json`, `decisions.jsonl`, `baseline.txt`, then `check` GREEN, `emit`, a cold
  read-back by a separate call (a subagent that sees only `prompt.txt`), `readback_raw.md`,
  `readback.md`, and `verdict.md` copied from run 001's template.
- **Records at the end of every work order:** `implementation/QUEUE.md` status;
  `plan/STATUS.md` entry (done, next, blocked); `plan/TASKS.md` status; `plan/DECISIONS.md` for any
  decision; `director/gaps.jsonl` for every INFERENCE; local commit naming the work order.
- **Code layout:** `director/tools/dircheck.py` (validators, loaders, lint), `diremit.py`
  (emitter), `director.py` (CLI; re-exports `check` and `emit`). If a module passes about 800
  lines, split it again keeping the one CLI. Do not add dependencies.
- **Never:** push, touch other repositories, invent model facts, treat a convention or a
  third-party doc as fact, implement the test names cited inside `cpcs/` cards, add a layer or
  requirement that no work order asks for.

## Files here

| File | Purpose |
|---|---|
| `QUEUE.md` | ordered work orders, status, dependencies, gates |
| `OWNER_ACTIONS.md` | the only things the owner must do, in plain steps |
| `work_orders/WO-xx_*.md` | one self-contained brief per unit of work |
