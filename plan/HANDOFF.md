# Handoff — how an implementing session (Sonnet-class) works here

## Boot sequence (every session, in this order; about 15 minutes of reading)

1. `AGENTS.md` (repo root) — roles and rules.
2. `plan/GOALS.md` — goal, success, non-goals, decision rights.
3. `plan/STATUS.md` — newest entry: what is done, next, blocked.
4. `plan/TASKS.md` — pick the first `todo` task whose dependencies are `done`.
5. `plan/ARCHITECTURE.md` sections the task touches; `plan/CONTROL_LAYER.md` for the R-ids.
6. `plan/OWNER_INPUTS.md` when the task touches intent, taste, time or movement.
7. The reference implementation for the pattern: `director/tools/director.py`,
   `director/tools/tests/test_director.py`, `director/runs/001_bottle_selfie/`.

Do not read the tree (`cpcs/`, `Additional/`) wholesale. Open a card or manual only when a
treatment's `from:` or `backs:` points to it, or when writing a new treatment.

## Working loop for a task

1. Write the RED test first (in `director/tools/tests/`), citing the requirement id.
2. Implement in `director/tools/director.py` (split into modules only when a file passes about
   800 lines; keep one CLI).
3. `python3 -m unittest discover -s director/tools/tests` → green.
4. If the task touches a run: `python3 director/tools/director.py check <run>` then
   `emit <run> --model seedance`; re-run the cold read-back (a separate LLM call that sees only
   `prompt.txt`) and update `readback.md`.
5. Record: `plan/TASKS.md` status; `plan/STATUS.md` entry (done, next, blocked); any decision in
   `plan/DECISIONS.md`; any reasoned choice in `director/gaps.jsonl`.
6. Commit locally on branch `director` with a message that names the task id. Never push.

## Writing a treatment

File: `director/treatments/<pass>/<id>.md`. Frontmatter: `id, pass, triggers (≥ 3), not_when,
backs (card ids), from (manual § or card), origin, importance`. Body headings exactly:
`## Wording` with fenced blocks ```` ```prompt core ```` and optionally ```` ```prompt core short ````
and ```` ```prompt dialect=<model> ````; `## Failure signs`; `## Effects` (one line per claim:
claim · evidence_status · model · runs). Wording describes what the camera sees or hears, never
affect words or framework terms. Placeholders `{key}` are filled from the control's `value` dict;
Laban scales produce `{weight_word}`, `{time_word}`, `{space_word}`, `{flow_word}`.

## Running an ask (as the reasoning LLM)

Follow `director/protocol.md`. Write `ask.md` (ask + intent brief + pass plan summary),
`ir.json`, `decisions.jsonl`; run `check`; fix the IR, never the prompt; run `emit`; cold
read-back; `baseline.txt` with the plain ask for the owner's comparison; leave `verdict.md` for
the owner.

## Conventions

- Python 3.9 compatible (no `X | Y` unions, no `match`). stdlib + pyyaml + jsonschema only.
- Origin tags: `USER_EXPLICIT, SOURCE_EVIDENCE, INFERENCE, CREATIVE_CHOICE, PROJECT_DERIVED,
  PROVIDER_EXPERIMENT, UNVERIFIED, CONTRADICTED, UNKNOWN`.
- Numbers from research are conventions until a render measures them; say so in `min_s_origin`
  and in treatment text.
- Pass names, never numbers. One owner per IR field.
- The prompt-system repo (`/Users/king/ai-video-movement-prompt-system`) is read-only source
  material: `lab/concepts.jsonl` (trigger phrases), `lab/blocks.yaml` (proven wording),
  `lab/registry.yaml` patterns p001–p009, `lab/second_brain/retrieval_benchmark.yaml`.
- The owner's standing rule for navigation in code repos: use `graft` and `graphify` before broad
  reads. Graphs for this tree live in the throwaway worktree `/Users/king/cpcs-director-graft`
  (`graft map`, `graft skeleton <file>`); rebuild there, never in this checkout.

## What exists on disk (2026-10-02)

```
/Users/king/cpcs-director            clone of Kingsley-Cyber/DAG_Kinetic_Movement, branch director
  AGENTS.md, CLAUDE.md, README.md    replaced / pointer / banner
  plan/                              this folder
  director/                          passes.yaml, protocol.md, ir.schema.json, gaps.jsonl,
                                     profiles/seedance.yaml, treatments/<pass>/*.md (7),
                                     tools/director.py (+ tests), runs/001_bottle_selfie/
  cpcs/, Additional/, Research_*     the research (read-only)
/Users/king/cpcs-director-graft      throwaway worktree with graft/ and graphify-out/
/Users/king/Backups/cpcs-director-2026-10-02/   backups of loose research files
```

## Asking the owner

Stop and ask (do not guess) for: Seedance route and limits; render results; anything in
`GOALS.md → Decision rights → must ask`. Put the question in `STATUS.md → Blocked` as well.
