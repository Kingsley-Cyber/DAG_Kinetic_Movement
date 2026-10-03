# Status

Newest first. One entry per working session or phase exit.

## 2026-10-03 — Queue execution started: WO-01 done

- WO-01 (T16, R-16, R-59): `anchors[]` and beat `relative` deltas in the schema; IR-level checks
  (unknown anchor, anchor not earlier, one escalation per quality, quality mismatch, anchor on
  unknown beat); emitter writes the anchor once after its beat and the delta as a comparison;
  lint warnings for bare magnitude words (named techniques allowed, sentences with "than" pass)
  and vague style words. 11 new tests, RED first; 61 total green; run 001 `check` GREEN and its
  prompt byte-identical.
- Implementation detail recorded: the allowed-phrase list also holds camera terms that contain a
  flagged word (wide shot, wide lens, wide angle, hard cut, hard light, big close-up).
- The tool passed 800 lines and was split: `dircheck.py`, `diremit.py`, `director.py` (CLI).

Next: WO-02 (physics causal events).

## 2026-10-03 — TwelveLabs client refreshed (WO-10) and DMR triage

- **TwelveLabs:** `director/tools/tlclient/` + launcher `director/tools/tl.py`; 24 new unit tests
  (50 total, green on Python 3.9 and 3.11). What was stale in the old client: exact SDK pin 1.3.1
  (latest 1.3.5); `marengo3.0` as a constant while Marengo 3.5 shipped 2026-08-31 with a different
  sync body (`multi_input`); no function to list or find assets; local uploads refused above
  200 MB with no multipart; the key reachable only through an untracked wrapper. Live checks
  passed: `doctor` ready (key from keychain), `assets list` (1 video in the library:
  `x_video2.mp4`), `assets find x_video`. Live uploads (one image, one short video) and one
  analyze and embed call wait for the owner to name the files.
- **DMR ingest:** `plan/ingest/DMR_triage.md` written from the package's real gap register; the
  Seedance 2.0 facts found there are in `profiles/seedance.yaml`.

Next: owner names an image and a short video for the live upload test; then the queue from WO-01.

## 2026-10-03 — Implementation folder written; branch pushed

`implementation/`: `START_HERE.md` (one kickoff prompt to paste), `QUEUE.md` (WO-01…WO-09 with
GATE A for the owner's renders), `OWNER_ACTIONS.md` (route, renders and verdicts, push), and nine
work orders with decisions already made, exact schema fields, error-message substrings, test
names, commands, acceptance and stop conditions. Order follows the external review: enforce
contracts (anchors, causal events, coupling), handoff test (run 002), runs 003–005, first ingest
(DMR) with run 004, experiment arms, then the render gate and the kill check. Phase 3 work orders
are written only if the kill check passes.

Also this session: relative prompting hard at IR level and lint at wording level; explicit-vs-open
contract; passes connect; terminology fixed; `EXPERIMENTS.md` E1–E6.

Next: an implementing session pastes the kickoff prompt and takes WO-01.
Blocked: Seedance route (owner); renders at GATE A (owner).

## 2026-10-03 — External review (FAIL) and remediation

Review: `/Users/king/Documents/Codex/2026-10-02/short-verdict-the-plan-matches-the/outputs/compiler-review.md`
(Codex, against `f2f478c`). Verdict FAIL on compiler requirements, not on video quality. Verified
holes, all now closed with RED→GREEN tests (T09; 26 tests green, the original 20 untouched):

- Retargeting run 001 to Hailuo dropped the locked 8 s duration silently (no native field, no
  loss). Now: a native control the route cannot carry is emitted as text with a
  `native_field_unsupported_by_route` loss and `compressed_to_text` in the receipt, or blocks when
  locked with no text form.
- The checker accepted one hand listed twice for a two-hand stage. Now: distinct (actor, hand)
  pairs only.
- The checker accepted a disconnected within-pathway state chain. Now: each stage must start where
  the previous one ended.
- Hailuo emphasis levers were stored but unused. Now: `emit` applies the best-evidence lever for
  an agnostic `emphasis` intent and records it in the receipt; a model without a lever emits core
  wording and a `provider_attention_loss` when the intent mattered.
- Receipt hash now covers the prompt file bytes as written.

Handoff contradictions the review listed were fixed where they were plain errors (STATUS next
task, ingest-is-not-a-phase, `treatment` key name, camera runs after interaction and physics,
conditional-pass closure rule, synthesis runs twice, read-back raw artifact, 1,000 vs 2,000,
decision rights, "one clip per beat" as hypothesis, T12 asks fixed with run 004 = the glass
fixture). Its "where to cut" was adopted: T10 optional, T11 and T14 deferred; the 55 requirements
are a backlog, not obligations before the first render.

Rejected by the review and left to the owner: taste-first sequencing and restoring reference
images (the owner's recorded intent says "ship Reason first" and excludes references for now).

Next: (1) owner renders run 001 compiled vs baseline on the confirmed route; (2) an independent
LLM runs the first T12 ask from `HANDOFF.md` alone (handoff test); (3) T36 first ingest.

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
