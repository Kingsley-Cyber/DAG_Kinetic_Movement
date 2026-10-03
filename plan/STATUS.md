# Status

Newest first. One entry per working session or phase exit.

## 2026-10-02 — WO-05 done: run 003 thrown into the pool (world reactions)

- Run folder `director/runs/003_pool_shove/`: `ask.md`, `ir.json`, `decisions.jsonl` (d001–d011), `baseline.txt`, `prompt.txt`, `receipt.json`, `loss.jsonl`, `emit_report.json`, `check_report.json`, `readback_raw.md`, `readback.md`, `verdict.md`. No `open.jsonl` (nothing open).
- `check`: GREEN at the first run, no repair round; fit FITS (5.6 s of 8 s, ratio 0.7). Six beats: step up and nudge, plant and shove, loses balance and falls, water entry, surfaces, settles laughing. Three pathways (`p_nudge`, `p_shove`, `p_water`), two physics events (`ev_shove` b2 with force "much more intense than the first nudge", `ev_water` b4), one anchor (`a_nudge`, intensity).
- `emit --model seedance`: 1,967 / 2,000 characters; dropped for budget: `c_laugh`, `c_pace`, `c_negatives`; twelve lines compressed; 15 loss records; no warnings.
- Read-back (Haiku subagent, no tools): beat order MATCH, causal order and state changes MATCH (splash after the entry, wet state after surfacing), camera MATCH. Findings in `readback.md`: "arriving fast and settling" and "easing in and out" read as ambiguous.
- New treatments: `world.water_entry` (from `material_response.md`, `affordance_constraints.md`; PROJECT_DERIVED) and `continuity.wet_state` (from the World Model gap-closure document §1 and `material_response.md`; PROJECT_DERIVED). Reused: `interaction.contact_causal_chain`, `camera.move_from_catalog`, `time.beat_schedule_ugc`.
- Tests: 87 green, none changed; runs 001 and 002 untouched (git shows no change under them).
- Guesses (what the protocol, a treatment or a tool did not specify; file and line of the gap):
  1. Whether the nudge may be added when seconds allow but characters are tight. `implementation/work_orders/WO-05_run003_pool.md` line 28–29 says "only if the 8 s fit allows the extra beat" (seconds); the 2,000-character limit is the real constraint. Added the nudge (load 5.6 s) and it fit, with three unlocked controls dropped (d001, d011).
  2. How to model a contact that is only the force baseline (the nudge). `protocol.md` line 203 ("one pathway per contact cycle") and line 108–111 (physics events) do not say whether such a tap needs a physics event. Chose a pathway (`p_nudge`) and the anchor sentence; no event (d002).
  3. A first anchor's `description` as a contact-plus-reaction sentence. `protocol.md` line 217 asks anchors to be visible facts and not restate the beat; the nudge fact is a cause, contact and reaction in one sentence.
  4. Which actor id owns the hand ledger for a person-to-person push. `protocol.md` line 94–97 covers hands on objects and the camera; used state `free` for the pusher's hands on the contact beats and no ledger rows for the friend who is pushed.
  5. The pathway `object` for a body that is pushed or falls. `protocol.md` line 90–92 defines `object` for things; used the actor id (`friend_b`) as the object of all three pathways.
  6. Whether effect stages may carry no hands when the event is a body-on-water contact. `dircheck.py` line 362 onward lets `hands_required: 0`; used it for the water contact, transfer and effect.
  7. The `action` pass closed although its condition holds (a body falls). Used the protocol section 2 override (reason names interaction and physics); `protocol.md` line 16–18 gives only the run-001 example.
  8. Aspect ratio 16:9 and no capture or look (style closed): the ask is silent and `protocol.md` has no rule (d010).
  9. Camera pass: "lens" has no field in the catalog or the treatment. Put "standard lens" in `phrase` and "deep focus" in `framing`; `director/treatments/camera/move_from_catalog.md` has no optics key.
  10. Staging has no treatment and no template: wrote `staging.screen_direction` as a plain-text control (CREATIVE_CHOICE) with no `short` form, so it cannot be compressed.
  11. Where the splash lives. Event, world control and continuity control could all state it; `protocol.md` says "one owner per field" but not how to split wording across three passes. Split by d006: event = splash and bubbles; world = where displaced water goes; continuity = wet clothes, hair and the moving surface. Words still overlap ("rocking", "settles").
  12. Intensity comparison wording. The brief says "much harder than the nudge"; `diremit.py` `COMPARATIVES` renders intensity as "much more intense than the first nudge" ("hard" is a banned magnitude word). Accepted the tool's wording.
  13. Spacing clauses on three beats. `protocol.md` line 157 asks for spacing on every moving beat; the tool prints "arriving fast and settling" and "easing in and out" after the beat text, which the reader found ambiguous. Kept three clauses (ease_out on the shove, ease_in on the fall, ease_in_out on the surfacing) and left the finding open.
  14. Reading times for a fall and a water entry: no source. Reused run-001 conventions (0.8 / 1.0).
  15. Dates in records: used 2026-10-02, the session's local date (`protocol.md` line 225); STATUS entries for WO-04 carry 2026-10-03.
- Tool behaviour that differed from the documents: none blocking. `pack` prints the pass view but not the treatments; the emit report's `chars` (1,967) is the prompt without its trailing newline, `prompt.txt` is 1,968 bytes.

Next: WO-06 (first ingest: DMR package; typed outcomes, camera move validator, profile lifecycle, CI workflow; run 004 glass fixture). Blocked: owner renders of runs 001–003.

## 2026-10-03 — Handoff test reviewed (WO-04) and the tool defects it found are fixed

Run 002 was executed by a Sonnet session from the repository's instructions alone: `check` GREEN
(fit TIGHT, 7.2 s of 8 s), prompt 1,987 of 2,000 characters, independent read-back MATCH, three new
treatments, 24 guesses listed in the entry below. What the guesses showed, and what changed:

| Finding | Fix |
|---|---|
| First beat printed as "First, He…" | emitter lowercases common sentence openers after the lead word and keeps names (test) |
| The catalog camera treatment's keys did not satisfy the camera-grammar check | check accepts `move`, `movement`, `phrase` as the motion part (test) |
| The OVERLOADED cut suggestion still overloaded | `check` now lists as many lowest-importance beats as it takes to fit (test) |
| `emit` blocked with "only locked content remains" and no hint what to shorten | the message names the five longest locked lines (test) |
| The pace treatment said "before the drink" | wording made generic |
| Protocol silent on: one pathway per contact cycle, `holding:` ids, folding effect-read beats, where to record an OVERLOADED resolution, beat vs event vs anchor repeating the same action, anchor labels, catalog camera value keys, sentence case, budget repair | `director/protocol.md` §4·3 |
| `emit_report.json` changed on every emit (timestamp) | timestamp removed; the file is stable |

Still open from the handoff (not tool defects): reading-time conventions have no source; which
existing treatment "fits" is a judgement; the same action is still stated more than once when a
beat, an anchor and an event describe it (redundancy suppression is T21, after the kill check);
acting direction was dropped for budget in run 002.

Verdict on the handoff: a second model produced a valid, readable run from the documents, with
guesses concentrated in the places listed above. "Any LLM" is not proven; one Sonnet run is.

Next: WO-05 (run 003, pool).

## 2026-10-03 — WO-04 done: run 002 earbuds unboxing (handoff test)

- Run folder `director/runs/002_earbuds_unbox/`: `ask.md`, `ir.json`, `decisions.jsonl` (d001–d009), `open.jsonl` (o001 resolved), `baseline.txt`, `prompt.txt`, `receipt.json`, `loss.jsonl`, `emit_report.json`, `check_report.json`, `readback_raw.md`, `readback.md`, `verdict.md`.
- `check`: GREEN, fit TIGHT (7.20 s of 8.00 s, ratio 0.9). The first draft (12 beats, 9.80 s) was OVERLOADED; resolved in the open (d001, o001) by cutting the establishing beat and folding the three effect-read-only beats into the action beats. No `min_s` was changed.
- `emit --model seedance`: 1,987 / 2,000 characters; dropped for budget: `c_pace`, `c_negatives`, `c_register`; 20 loss records. First emit blocked at 2,014 characters; repaired in the IR (guess 15).
- Read-back (Haiku subagent): beat order MATCH, state changes MATCH, camera MATCH. Findings for the emitter in `readback.md` (case opening stated three times; comparison far from its anchor; awkward occluded-contact wording).
- New treatments: `interaction.grip_case_and_earbud`, `style.capture_iphone_rear_handheld`, `performance.casual_product_handling` (reused: `interaction.contact_causal_chain`, `continuity.object_locks`, `camera.move_from_catalog`).
- Tests: 83 green, none changed; run 001 `ir.json` untouched.
- Guesses (what the protocol, a treatment or a tool did not specify; file and line of the gap):
  1. Whether an effect-read beat (run-001 convention 0.6 s) stays separate when a physics event already carries cause, reaction and settle on one beat. `director/protocol.md` line 84–86 (Beat) and line 108–112 (Physics event) are silent. Chose to fold the three effect-read beats into their action beats; recorded in d001.
  2. Which printed OVERLOADED option to take when the printed cut still overloads (b1+b12 gives 8.2 s) and `overlap_non_causal_pairs` is empty. `implementation/work_orders/WO-04_run002_product_hands.md` line 27–28 lists the options but not what to do when none suffices alone. Combined a cut with a fold.
  3. Whether folding beats counts as "shrinking min_s". The work order (line 27–28) forbids shrinking `min_s` only; no rule on merging beats. Kept every remaining `min_s` at the run-001 value.
  4. Reading times for opening a box, lifting a case, a hinge push and an earbud pinch: no source. Reused run-001 conventions (0.8 / 1.0 / 0.6 / 0.8). `director/treatments/time/beat_schedule_ugc.md` line 9–11 only says they are conventions.
  5. Whether an off-screen friend holding the camera belongs in the hand ledger or the entities. `director/protocol.md` line 96–97 covers only the actor's own hands on the camera. Chose: no ledger rows for the friend; an entity of kind `camera` (later emptied for budget).
  6. Which state strings may appear in the hand ledger for a hand that grips a part (lid, case). The schema pattern allows `holding:<id>`, but the check (`dircheck.py` line 362 and 422) only accepts ids equal to the pathway's `object` or `parts`; `protocol.md` line 94–97 does not say so. Declared `parts` on every pathway.
  7. A pathway may not repeat stage kinds (`dircheck.py` line 365–367 requires sorted kinds), so grip + lift-out + lid-open could not be one pathway. `protocol.md` line 86–91 ("one per physical task") does not say how to split. Used four pathways (unbox, take out, open, ear).
  8. Which field name the catalog camera control takes. `protocol.md` line 160–168 and `camera/move_from_catalog.md` do not name it; the check needs a `motion` key or a `camera.motion` field (`dircheck.py` line 513), while the treatment's keys are `movement`, `phrase`, `speed`, `framing`, `end`. Used field `camera.motion`.
  9. First beat description casing. `diremit.py` line 173 lowercases every beat except the first, so a first description starting with a capital prints "First, He ...". Wrote the first description in lowercase.
  10. Which treatments fit. No rule defines "fit"; judged by wording (existing `performance.casual_register`, `style.capture_iphone_selfie` and `time.beat_schedule_ugc` name a bottle, a cap, a front camera and a drink) and wrote three new treatments instead of editing the run-001 ones (editing would change run 001's prompt).
  11. Pace control with no treatment (`beat_schedule_ugc.md` line 20 mentions "the drink"). Plain text, origin INFERENCE.
  12. Where an OVERLOADED resolution is recorded "in the open". The work order says to resolve it in the open and record in `decisions.jsonl`; `protocol.md` line 143–148 defines `open.jsonl` items for revision requests only. Wrote an `alternative` item with status `resolved` (does not block emit) and decision d001.
  13. How to reference an anchor for a physics event's force. `protocol.md` line 108–114 allows `relative_to` an earlier weight or intensity anchor; chose intensity on the thumb push, consumed by the ear-press force, and no beat delta (avoids saying it twice). The first event has no `force` because a first `force` with `relative_to: null` would need its own anchor and emits no comparison.
  14. Insertion into the ear as `occluded_contact` with `risk: high`. `HANDS_CONTACT_MANIPULATION.md` §2.3/§5 say conceal or commit short; no earbud-specific guidance, and `contact_risk` in `profiles/seedance.yaml` is all `unknown`.
  15. The budget repair path. `emit` blocked at 2,014 / 2,000 with only locked content left; the options printed ("shorten locked content in the IR") do not say what to shorten. Shortened the chain list, the lock sentence, the anchor sentence, the camera phrase, one box line and removed four spacing clauses; rejected locking `c_capture`. Dropped by the emitter: `c_register`, `c_pace`, `c_negatives`.
  16. Whether spacing is required on every moving beat (`protocol.md` line 157 says so) when the budget cannot carry it. Kept one spacing clause (b5) and dropped the rest as a budget trade; the warning rule in `dircheck.py` (line 306) only fires when `action` is active, which it was not.
  17. Aspect ratio 9:16 (the ask is silent; `protocol.md` has no rule). Same as run 001.
  18. Which ear and which hand: "his right ear" with the right hand; handedness assumed.
  19. Device wording for a rear camera: the old treatment says "front camera"; `CAPTURE_SURFACE_REALISM.md` §4 gives one `iphone_recent` row with no front/rear split. Used "main camera held by a friend" and kept the 30 fps / HDR phrases from the old treatment even though `fps_assumed` is 24 (the same mismatch exists in run 001).
  20. New-treatment `from` for the performance treatment cites `LIVING_PERFORMANCE_REALISM.md` §4, §8, §9, which the work order's Read-first list does not include; read only those sections.
  21. Date of records: used 2026-10-03 (UTC, as the tool's `emitted_at`) although the session clock said 2026-10-02.
  22. Read-back: launched a Haiku general-purpose subagent through the Agent tool with the five instructions and `prompt.txt`; the harness reports one tool use (its hand-back). Assumed this counts as "a separate call".
  23. Whether to run `pack` and `check --pass` (WO-03b) during the run; the work order says nothing. Ran `pack` and `check --pass` for time, physics and camera after the IR existed; no change resulted.
  24. Whether `ledger.jsonl` is touched now; left for the owner (verdict.md says after renders).
- Owner: render `prompt.txt` and `baseline.txt` and fill `runs/002_earbuds_unbox/verdict.md` (gate A).

Next: WO-05 (run 003, thrown into the pool).

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

- WO-02 (T35 first slice; R-41, R-42, R-44): `physics_events[]` in the schema; checks for one
  event per beat, unknown beat, `depends_on` order, force anchor (weight or intensity, earlier),
  edge admission (non-empty contact surface, reaction, settle), near-contact warning; emitter
  writes cause → contact → reaction → settle after the beat with wording variants per
  `contact_state`; `must_not_imply` is never emitted. 8 new tests, RED first; 69 total green; run
  001 unchanged. Not in this slice: risk-based degradation, eval-log fields, failures registry.

- WO-03 (T17; R-56, R-57): `reads` on 11 passes in `passes.yaml`; optional `beat` scope on
  controls; coupling checks (camera close-up on a hidden contact, camera cut-away on a confirmed
  contact, beat shorter than 0.2 s per pathway stage, control on an unknown beat) and the explicit
  rule that an event's trigger names actor and part. 6 new tests, RED first; 75 total green; run
  001 unchanged.

- WO-03b (R-58, R-60): `director.py pack <run> <pass>` (the pass's view: entry, reads, locked
  controls, treatments, open items; camera also gets the 48 moves with function hints);
  `check --pass <pass>` (only the rules that pass owns; others `not_applicable`); full `check`
  writes `check_report.json` (typed outcomes per rule group, IR hash); `open.jsonl` with open
  conflicts or revision requests blocks `emit`; beat `spacing` and `pose_role`; the
  "constant motion" warning when the action pass is active and nothing declares spacing; spacing
  emitted as visible behaviour. 8 new tests, RED first; 83 total green; run 001 unchanged.
  Deviation from the work order: the report carries the IR hash, not a timestamp, so the file
  does not change between identical runs.

Next: WO-04 (run 002, the handoff test).

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
