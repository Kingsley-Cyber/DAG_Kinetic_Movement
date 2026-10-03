# Tasks (ordered; one task per session is fine)

Each task names its files, its acceptance test, and what it depends on. Status: todo · doing ·
done · blocked. Update this file and `STATUS.md` when a task changes state. Requirement ids
(R-xx) are in `CONTROL_LAYER.md`.

## Done (reference implementation, 2026-10-02)

| Id | Task | Evidence |
|---|---|---|
| T00 | Phase 0 set-up: clone, branch `director`, `AGENTS.md`, `plan/`, backups, graphs | `STATUS.md` 2026-10-02 |
| T01 | Pass registry, protocol, IR schema, Seedance profile | `director/passes.yaml`, `protocol.md`, `ir.schema.json`, `profiles/seedance.yaml` |
| T02 | `check` (R-01…R-14) and `emit` (R-17…R-22, R-24, R-29) with 20 tests | `director/tools/director.py`, `tests/test_director.py` |
| T03 | Run 001 bottle selfie: IR, decisions, prompt, receipt, losses, cold read-back MATCH | `director/runs/001_bottle_selfie/` |

## Ingest (runs alongside every phase; the engine that makes knowledge grow)

| Id | Task | Files | Acceptance | Depends | Status |
|---|---|---|---|---|---|
| T36 | First ingest by `plan/INGEST.md`: the DMR gap-closure package (`Research_distillation_folder/research/continue_detail/director_motion_reasoning_complete_package/`, prompt `Additional/06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md`). Triage G001–G022 into the six statuses; implement the `implementable_now` rows in INGEST §4 (typed validator outcomes R-51, IR-not-authority invariant R-50, provider lifecycle states in profiles, state-variable continuity treatments); trace the shared fixture (glass strike) as run 004 | `plan/`, schema, `director.py`, profiles, treatments, run 004 | every gap has a status with a reason; run 004 `check` GREEN and read-back MATCH; no new field without a consumer | T02 | todo |
| T37 | Second ingest: one of the owner's `Completed MD` returns chosen by the gap log (e.g. `07 CPCS World Model _ Causal State _ Attention Gap Closure.md` for the world, attention and continuity passes) | same | world and attention passes gain treatments a run uses | T36 | todo |

## Phase 2 — evidence (owner renders; implementer prepares)

| Id | Task | Files | Acceptance | Depends | Status |
|---|---|---|---|---|---|
| T10 | Lean variant emitter mode: `emit --variant lean` keeps entities, beats, camera and capture only; records omitted controls as `lower_priority` losses | `director.py`, tests | lean prompt ≤ 150 words for run 001; receipt complete; test RED→GREEN | T02 | todo |
| T11 | Ledger writer: `director.py log-verdict <run> --model --prompt compiled|lean|baseline --scores '{...}' --verdict --notes` appends to `director/runs/ledger.jsonl`; `verdict.md` template already exists | `director.py`, tests | one line per call; malformed scores rejected | — | todo |
| T12 | Four more asks, each a full run folder (ask, IR, decisions, prompt, baseline, read-back): product handling with hands (two hands + object), "he gets thrown into the pool" (world reactions), two-person action (staging + contact + reaction), camera-only (no performer; performance pass inactive) | `director/runs/00[2-5]_*` | each `check` GREEN; read-back MATCH; new treatments only where an ask needed them | T02 | todo |
| T13 | Owner renders compiled, lean and baseline for each run on Seedance; verdicts logged | `verdict.md`, `ledger.jsonl` | 5 runs × 3 arms scored | T10–T12 | blocked on owner |
| T14 | Effects update: a script reads `ledger.jsonl` and rewrites `## Effects` lines in the treatments used (evidence_status supported / contradicted / unverified per model) | `director.py effects`, tests | treatments reflect ledger; idempotent | T13 | todo |
| — | **Kill check**: compiled beats baseline on most runs? If not, stop and write up in `STATUS.md` | | | T13 | — |

## Phase 3 — Style and Render tiers

| Id | Task | Files | Acceptance | Depends | Status |
|---|---|---|---|---|---|
| T20 | Per-beat priority weights in the IR (`beats[].weights: {silhouette, anticipation, impact, …}`) read by `emit` to order and size wording | schema, `director.py`, tests | weights change word share, never beat order (R-06 test extended) | T02 | todo |
| T21 | Redundancy suppression (R-26): a control whose wording tokens are ≥ 70 % covered by beats or a higher-importance control is suppressed with `already_encoded_by_stronger_control`; threshold recorded as a convention | `director.py`, tests | run 001 loses the duplicated grip/chain sentences; receipt shows the reason code | T02 | todo |
| T22 | Suppression reason codes (R-25) for every non-emitted line | `director.py`, tests | no omitted control without a reason | T21 | todo |
| T23 | Timing profiles as treatments: `time/profile_snappy.md`, `profile_floaty.md`, `profile_anime_limited.md`, `profile_ugc_natural.md` (conventions, origin tagged) and the six-question procedure in `protocol.md` | treatments, protocol | a combat ask and an emotional ask select different profiles with recorded decisions | — | todo |
| T24 | Sakuga and UGC texture treatments; the fusion case (sakuga beats, UGC render) as run 006 | treatments, run 006 | `check` shows Reason order unchanged after Style/Render controls | T20 | todo |
| T25 | Anti-arcade detectors (R-15) on IR fields `action.plane_transitions`, `action.weight_transfer_path`, `performance.laban.flow` per beat, pathway anticipation | schema, `director.py`, tests | each of the four signatures has a RED→GREEN test on a fight run | T12 | todo |
| T26 | Relative-prompting validator (R-16): anchor before escalation; no two absolute magnitude words for one quality in one clause | `director.py`, tests | RED→GREEN | — | todo |
| T28 | Bartenieff six patterns and Shape planes (R-37, R-38, R-40): schema fields `action.connectivity[]` and `beats[].shape`; validators (power action → Upper-Lower + Cross-Lateral, side named, plane change); treatments `action/connectivity_pathways.md` (six patterns as visible travel wording, UNVERIFIED) and `performance/shape_planes.md` (three planes, forms, scaled qualities); proven on a fight run | schema, `director.py`, treatments, tests, run | RED→GREEN on each validator; prompt names no pattern or plane terms; read-back reports the power path and the plane change | T12, T25 | todo |
| T29 | Affect layer (R-39, R-40): `performance.affect` with experienced and displayed trajectories; validators (monotonic t, scale, displayed when masking); treatment `performance/affect_to_behaviour.md` mapping affect to FACS combinations, breath, posture, Effort scaling (hypothesis) and voice presets; affect-word blocklist in the emitter; proven on run 007 "smiles subtly while hiding disappointment" | schema, `director.py`, treatment, tests, run | RED→GREEN; prompt contains no affect words; read-back sees a smile that does not reach the eyes and a held breath | T27 | todo |
| T27 | FACS as a spatiotemporal event (R-34…R-36): `performance.face_events[]` in the schema; validators for phase order, beat span, laterality, occlusion, ordinal intensity; emitter maps AU combinations to plain visible wording via a `performance/facs_combinations.md` treatment (AU6+12, AU1+12, AU4+5+7, AU4+7 from `cpcs/knowledge/04_character_performance/facs/`); a dialogue or reaction run uses it | schema, `director.py`, treatment, tests, run | RED→GREEN on each validator; prompt contains no AU codes or emotion words; read-back lists the facial event at the right beat | T12 | todo |

## Phase 4 — widen on demand, records

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T30 | World treatments (water, sand, glass, mud, wall, smoke responses) from `cpcs/knowledge/08_objects_affordances`, `material_response`, the pool example | run 003 uses them; each cites a source | T12 | todo |
| T31 | Camera three-layer treatments; light_color and attention first treatments | runs cite them | T12 | todo |
| T32 | Decision and gap validators (R-31, R-32): `selected ∈ alternatives`, every INFERENCE control has a gap line | tests | T02 | todo |
| T33 | `director.py index`: builds `director/index.json` (pass → sub-module → treatment ids, triggers) once there are > 30 treatments; `pack <pass>` prints a pass pack | tests; load path unchanged for small asks | T30 | todo |
| T35 | Specialized physics layer (R-41…R-46): `physics.events[]` in the schema; validators (edge admission, one event per beat, relative force anchor, settle for ground/water endings, contact_state consistent with risk and dialect); `contact_risk` in profiles; downgrade with loss record; emitter template cause → contact → reaction → settle with connectors; eval-log fields and `director/failures.jsonl`; A/B/C design for the stomp (plain vs causal vs prop) as run 008 and the pool throw (run 003) using it | schema, `director.py`, profiles, tests, runs | RED→GREEN on each validator; run 003 prompt reads cause → contact → reaction → settle in order; unreliable dialect produces `editorial_impact` wording and a loss record | T12 | todo |
| T38 | Camera move validator (R-53): `check` loads `director/vocab/camera_moves.yaml`; a camera control with `move` must name a catalog id or `custom`; layer consistency (optics never as motion); one move per shot; a run (e.g. the glass fixture: reframe to B, then reveal) uses two ordered moves | `director.py`, tests, run 004 | RED→GREEN; run 004 emits both moves in the four-part grammar in beat order | T36 | todo |
| T39 | Camera 12 sub-layers (R-55): vocab files for Where (shot scale, angle, position), Lens (focal length, focus/DoF, composition), Time (slow motion, ramps, blur), Connection (cuts, start/end states), stance and shot function; `camera.grammar` control value gains these keys; validator for minimum coverage; `locked_off_control` used as the A/B control in Phase 2 | vocab, schema, `director.py`, treatments, tests | RED→GREEN; run 004 states where, movement and lens explicitly | T38 | todo |
| T34 | Trigger-matching test set (`director/tests/asks.yaml`, seeded from the prompt-system repo's `lab/second_brain/retrieval_benchmark.yaml` and owner asks) scored against `lab/scripts/concepts.py` as baseline | hit rate recorded in `STATUS.md` | T33 | todo |

## Phase 5 — validators and calculators that runs needed

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T40 | `director.py calc`: beat frames, phase ratios × duration, exposure time, apparent image velocity (qualitative), speech words from seconds, strike phase split; output carries the origin of its inputs | tests per formula; a run uses at least one | T12 | todo |
| T41 | Strength-scaled emission (R-27): `strength` in profiles; weak → minimal core + camera/continuity compensation | run emitted twice, strong and weak, both receipts complete | T20 | todo |
| T42 | World bundle fields in the IR and their use by anti-arcade and fit | tests | T25, T30 | todo |

## Phase 6 — steering, diversity, dialects

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T50 | Steering profile (`director/steering/default.yaml`, per user, per ask) merged later-wins with locks; dials per `ARCHITECTURE.md` §8 | same seed → same prompt; locked content never varies | T20 | todo |
| T51 | Variants: `emit --n 3 --seed S --variation 0.5` → labelled variants differing only in free fields | labels list what differs; test | T50 | todo |
| T52 | Dialect rules in profiles (R-23): prefer/avoid vocabulary, clause order per model; `dialect=` blocks in treatments | a treatment with a dialect block emits differently per model, same order | T13 | todo |
| T53 | Intent catalog and lever application (R-47…R-49): `emphasis`, `hold`, `pause_s` fields in the schema; a schema check that rejects model syntax in IR strings (`<i>`, `<emphasis>`, `*word*`, API field names); `emit` applies `dialect.levers` and writes `lever:` into the receipt; loss record when a mattering intent has no lever; first test on Hailuo emphasis (three forms, one run, ≥ 3 seeds each) | schema, `director.py`, profiles, tests, run | RED→GREEN; same IR emits `<i>not</i>` for hailuo and plain "not" for seedance; receipt shows the lever; ledger compares the three forms | T52 | todo |

## Phase 7 — structured carriers (experiment)

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T60 | `emit --carrier yaml|json|xml|hybrid` from the same IR with loss reports; prose stays default | owner renders prose vs structured on two runs; promoted only on evidence | T13 | todo |

## Phase 8 — research ingest

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T70 | Revise `plan/INGEST.md` from what T36 and T37 taught; prove it by adding a new sub-module and a new pass from a return with no code edit | a new sub-module and a new pass added with no code edit | T36, T37 | todo |
| T71 | Gap log → research prompts: `director.py gaps --prompts` groups `gaps.jsonl` into research questions | owner receives a list | T32 | todo |

## Phase 9 — more models

| Id | Task | Acceptance | Depends | Status |
|---|---|---|---|---|
| T80 | Profiles for Kling, Hailuo, Veo, Wan from `cpcs/providers/*` findings and current docs, every fact tagged | runs emitted per model; dialect differences recorded | T52 | todo |
