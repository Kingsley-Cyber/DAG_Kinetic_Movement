# Status

Newest first. One entry per working session or phase exit.

## 2026-10-02 — Handoff pack written

The owner asked for a folder that holds the plans, goals and intent control layer so a
Sonnet-class model can implement from it. Added `GOALS.md`, `CONTROL_LAYER.md` (R-01…R-33),
`OWNER_INPUTS.md`, `TASKS.md` (T00–T80 with acceptance tests), `HANDOFF.md`; `README.md` now gives
the reading order. The phase 0–1 slice stays as the reference implementation.

Next: the implementing session starts at `HANDOFF.md` and takes T10. The owner's part is the
Seedance renders for run 001 (T13).

## 2026-10-02 — Phase 1 done (vertical slice, Reason tier); Phase 2 waits on renders

Done:
- `director/passes.yaml` (16 passes by name, tiers, owners, activation, order), `protocol.md`,
  `ir.schema.json`, `profiles/seedance.yaml`, 7 treatments (interaction ×2, continuity,
  performance, camera, style, time), `tools/director.py` (`check`, `emit`; 580 lines),
  20 unit tests, run `runs/001_bottle_selfie`.
- Exit tests: RED → GREEN on two-hand twist while a hand holds the camera; jump straight to
  "open"; effect with no stated reaction; overloaded beats (with options); reaction before cause;
  disposition inconsistent with capability; locked exact request text cannot enforce; field
  written by a non-owner; style-tier pass writing beats; missing camera grammar. Emit within
  budget with a complete receipt, deterministic, locked content never dropped; blocked with the
  R3 "one clip per causal event" option when only locked content remains.
- Run 001: check GREEN (fit FITS, 6.4 s of 8 s). Emit 1,896 of 2,000 chars after compressing to
  short wording and dropping `c_pace` and `c_negatives` (18 loss records). Cold read-back by a
  separate Haiku call: beat order MATCH, state changes MATCH, camera MATCH (`readback.md`).
- Seedance profile: prompt limit 2,000 chars from third-party API docs (not ByteDance's page);
  recommended 60–100 words per third-party guides; everything else unknown.

Findings worth acting on later (not now; evidence first):
- The emitted prompt restates the action sequence (beats, then grip and chain controls) and
  repeats "deep focus" and "no cuts". Needs a suppression step `already_encoded_by_stronger_control`.
- 475 words vs 60–100 recommended. Phase 2 must render full vs lean vs baseline.
- Every line had to be compressed to fit 2,000 chars; the full wording needs about 3,000.

Next (Phase 2, owner's part): render `prompt.txt` and `baseline.txt` on Seedance with the same
settings; fill `verdict.md`; one line in `director/runs/ledger.jsonl`. I will add a lean variant
(beats + camera + capture only, about 150 words) before the renders if the owner wants three arms.
Then four more asks (product handling with hands, thrown into a pool, two-person action,
camera-only).

Blocked: renders need the owner. Seedance route still unconfirmed.

## 2026-10-02 — Phase 0 done

- Backed up to `/Users/king/Backups/cpcs-director-2026-10-02/`: 7 untracked root manuals from the
  local tree copy, 8 extra files from `Downloads/Additional/Completed MD`, 4 newer
  `MORE_CONTROL` cards.
- Cloned `Kingsley-Cyber/DAG_Kinetic_Movement` (`13a236f`) to `/Users/king/cpcs-director`,
  branch `director`. The 5 manuals are in `Additional/` on the remote; `PROJECT_INSTRUCTIONS.md`
  exists only in the backup.
- Moved the old `AGENTS.md`/`CLAUDE.md` to `plan/legacy/`; wrote the replacement `AGENTS.md`, a
  pointer `CLAUDE.md`, and a banner on `README.md`.
- Wrote `plan/` (README, ARCHITECTURE, PHASES, STATUS, DECISIONS).
- Built graft (44 Python files in the research packages: 488 nodes) and graphify (22,138 nodes,
  code graph only) in the throwaway worktree `/Users/king/cpcs-director-graft`.
- The prompt-system repo and `New project` were not touched.
