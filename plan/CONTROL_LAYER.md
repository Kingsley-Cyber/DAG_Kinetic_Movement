# Control layer — checkable requirements

The control layer emits and validates; it never decides. Each requirement has an id so tests can
cite it. The reference implementation of R-01…R-20 is `director/tools/director.py` with tests in
`director/tools/tests/test_director.py`; the rest are to build. Vocabulary is the research's own
(see `ARCHITECTURE.md` §3 and §12 for sources).

## A. Controls and dispositions

| Id | Requirement | Status |
|---|---|---|
| R-01 | A control has `id, pass, field, value, importance 0..1, lock, origin, capability, disposition`, optional `treatment, exactness, expected_visual_effect, check, clause` (`ir.schema.json`) | done |
| R-02 | `field` has exactly one owner pass (`passes.yaml → owns`); a control written by another pass fails | done |
| R-03 | `capability` ∈ native, approximate, semantic, unsupported, unknown; `disposition` ∈ native, approximated, semantic, omitted, unsupported, unknown; the pair must be consistent | done |
| R-04 | A locked control is never omitted; a locked `exactness: exact` request on a semantic/unknown/unsupported capability blocks with a reason | done |
| R-05 | `native` applies only to fields the model profile lists as `native_fields`; native controls become settings, not prose, unless a treatment gives wording | done |
| R-06 | A Style- or Render-tier pass may not write `beats`, `pathways` or `hands` | done |
| R-07 | Camera grammar is mandatory: at least one camera control covering motion and one covering framing or optics | done |
| R-08 | A phrase is never upgraded to native because it sometimes works (no code path may promote capability from evidence alone) | done by construction |

## B. Validators over the IR (never over the ask)

| Id | Requirement | Status |
|---|---|---|
| R-09 | Hand ledger: one state per (actor, hand, beat); a stage needing N hands lists N hands that are `free` or holding the pathway's object or parts; a `camera` hand cannot be used | done |
| R-10 | Action pathway: stages in causal order; at least anticipation, one action stage, one aftermath stage; last stage ends in `end_state`; any state change after contact needs prior contact and transfer (no magic jump) | done |
| R-11 | Every `effect` stage has a non-empty stated `reaction`; every `contact` has a later effect with a reaction (impact-and-physics language) | done |
| R-12 | Beats: order 1..n; `after` and `caused_by` point to earlier beats; a reaction cannot precede its cause | done |
| R-13 | Fit: `load = Σ min_s`; `load ÷ duration` → FITS ≤ 0.85, TIGHT ≤ 1.0, OVERLOADED > 1.0 with options (cut lowest importance, overlap non-causal pairs, split, lengthen); no duration → UNDERSPECIFIED, no seconds invented | done |
| R-14 | Speech capacity: words ≤ duration × 190 / 60 for any `audio.dialogue` control | done |
| R-15 | Anti-arcade detectors on power actions: plane transition present; anticipation present; weight-transfer path recorded; Flow alternates | to build (phase 3) |
| R-16 | Relative prompting is a compile invariant at the IR level: `anchors[]` (visible-fact description on a named beat); later scaled qualities and causal-event force carry `relative_to` + step + direction; one escalation per quality per anchor; the emitter writes the anchor once, then comparisons, and never two absolutes from scaled values. At the wording level a bare magnitude word with no anchor in scope is a **lint warning** (named techniques such as "slow motion" allowed) until the T18 A/B supports promoting it to a failure | done 2026-10-03 (WO-01); promotion of the lint waits on E2 |
| R-56 | Explicit-versus-open contract (ARCHITECTURE §2.7): the explicit column is validated per pass (contact surface, hand, reaction, event order, end state, camera grammar present); open choices carry CREATIVE_CHOICE or INFERENCE | partly done (R-07, R-09…R-11); trigger actor and part enforced (WO-03); the rest of the explicit column is covered by R-07, R-09…R-11, R-42 |
| R-57 | Passes connect: `reads` per pass in `passes.yaml`; coupling checks (camera vs contact state per beat; Effort direction vs causal-event force delta; timing covers pathway stages; no later-tier control contradicts a Reason lock) | done 2026-10-03 (WO-03): `reads` on 11 passes; checks for camera vs contact state per beat, beat time vs pathway stages, control on unknown beat. Effort-vs-force direction is by protocol until a run needs the check |
| R-34 | FACS event record in the IR: `aus, laterality, intensity (A–E ordinal), onset/apex_start/apex_end/offset (s), combination, head_pose, gaze, visibility, origin`, bound to a beat | to build (T27) |
| R-35 | FACS validators: onset < apex start ≤ apex end < offset, inside the beat span; laterality stated when asymmetric; occluded events are never verification targets; intensity never stored as 0–1 | to build (T27) |
| R-36 | FACS emission: AUs and combinations compile to visible facial behaviour in plain words; no AU codes and no emotion claims in the prompt; intensity emitted relative to the anchor expression | to build (T27) |
| R-37 | Bartenieff connectivity record `action.connectivity[]` (pattern, side_relationship, initiator, receiver_sequence, intensity, range); a power action records Upper-Lower and Cross-Lateral; Body-Half names its side; Basic Six exercises never mixed in | to build (T28) |
| R-38 | Shape record `beats[].shape` (plane_path over Door/Table/Wheel, form, three scaled qualities); a power action changes plane at least once; single-plane motion is flagged | to build (T28) |
| R-39 | Affect record `performance.affect` (experienced and optional displayed trajectories of valence, arousal, dominance; monotonic t; declared scale); affect is never derived from AUs; `displayed` required when a masking decision exists | to build (T29) |
| R-41 | Causal event record `physics.events[]` (trigger, contact_surface, contact_state, force relative_to, primary_reaction, secondary, settle, depends_on, must_not_imply, risk); at most one event per beat | done 2026-10-03 (WO-02) |
| R-42 | Edge admission: every reaction in the IR belongs to an event with a named trigger and contact surface; `force.relative_to` and `depends_on` reference earlier events or beats; settle named for ground or water endings | done 2026-10-03 (WO-02: edge admission, depends_on order, force anchor); the ground-or-water settle rule is by protocol, not code |
| R-43 | Contact-risk capability check: profile `contact_risk` per dialect (reliable, unreliable, unknown) per risk class; unreliable medium/high events are downgraded to `occluded_contact` or `editorial_impact` with a loss record; unknown emits in full and flags the event for the eval log | to build (T35) |
| R-44 | Causal event emission: one sentence per event in the order cause → contact → reaction → settle with connectors; force resolved to relative words; `must_not_imply` never emitted as prompt text | done 2026-10-03 (WO-02) |
| R-45 | Eval log fields per render: IR hash, prompt hash, dialect version, seed, access path, per-event yes/no for contact happened, reaction followed, end pose sane; ≥ 3 seeds per prompt before a verdict | to build (T35) |
| R-46 | Failures registry `director/failures.jsonl`: failure, run, event, class (vocabulary gap vs ceiling), hypothesis status | to build (T35) |
| R-47 | Intent catalog: intents (emphasis, hold, camera move, speech line, order and timing, exclusion, identity anchor, shot settings) are written in the IR in agnostic form only; model syntax in the IR is a schema error | to build (T53) |
| R-48 | Dialect levers live only in `profiles/<model>.yaml → dialect.levers[] {intent, syntax, evidence, caveats, runs}`; `owner_observed` is never promoted without a logged run | profiles done (hailuo, seedance); validator to build (T53) |
| R-49 | Lever application happens at emission; each application is written to the receipt as `lever: <intent>`; an intent with no lever and importance ≥ 0.7 produces a `provider_attention_loss` record | to build (T53) |
| R-50 | The IR is an execution projection, never a second semantic authority: every control cites a treatment, a card, an owner input or an INFERENCE tag; no field is treated as knowledge after the run | to build (T36) |
| R-51 | Every validator returns a typed outcome: pass · fail · indeterminate · not_applicable · unobservable; an unknown prerequisite is never treated as a pass downstream | to build (T36; current checks return pass/fail only) |
| R-52 | Profile facts and levers carry a lifecycle state (unverified → verified → stale → reprobe_due → invalidated) with dates; reprobe_due and invalidated block native dispositions for that fact | to build (T36) |
| R-53 | Camera move controls reference a `director/vocab/camera_moves.yaml` id (or `custom` with a decision record); the control's layer matches the catalog (an optics entry cannot be emitted as camera motion); one move per shot unless beats order them | catalog and treatment done; validator to build (T38) |
| R-54 | Profile completeness: format, section order, phrase map (levers/prefer/avoid), supported/unsupported facts, defaults_to_counter, access_path, version, evidence, date_tested, lifecycle status; `check`/`emit` warn on missing fields and block native dispositions when status is reprobe_due or invalidated | fields present in seedance and hailuo; validator to build (T36) |
| R-55 | Camera control covers at least Where (shot scale or angle), Movement (type) and Lens (focal length or focus); the research's three image layers map onto these groups | to build (T39; R-07 stays as the minimum until then) |
| R-58 | Scratchpad: `ir.json` holds accepted state only; a contribution is accepted through `check --pass`; `open.jsonl` records alternatives, conflicts and revision requests (`from_pass, to_pass, field, reason`); `emit` refuses while an open conflict or revision request is unresolved; `check_report.json` is saved with typed outcomes; replay = saved IR + profile + treatments | to build (WO-03b) |
| R-59 | Vague-word lint: `cinematic, epic, beautiful, stunning, dramatic, dynamic, professional, high quality` in LLM-written free text → warning naming the variables to state instead; treatment wording is exempt | done 2026-10-03 (WO-01) |
| R-60 | Spacing: optional `spacing` (`ease_in, ease_out, ease_in_out, even`) and `pose_role` on beats; all moving beats `even`, or none declared when the action pass is active → "constant motion" warning; emitted as visible behaviour | to build (WO-03b) |
| R-61 | Emission order leads with the main idea (shot, subject, ordered action first); a "first 20–30 words" rule is a hypothesis (E7), not a requirement | order done (R-18); experiment to run |
| R-40 | Affect and Shape and Bartenieff emission: compiled to visible behaviour (face, breath, posture, travel of the movement, voice), never framework terms or affect words; emitter word list for affect words is a recorded convention | to build (T28, T29) |

## C. Emitter

| Id | Requirement | Status |
|---|---|---|
| R-17 | `emit` runs `check` first and is blocked by any error | done |
| R-18 | Assembly order is the profile's `clause_order` (default `[SHOT] [SUBJECT AND ACTION] [PERFORMANCE] [TIMING] [CAMERA] [NEGATIVES]`); entities first, then beats in order, then controls by importance | done |
| R-19 | Budget: compress to `short` wording (lowest importance first), then drop unlocked lines (lowest importance first), then block with options including "one clip per causal event" when more than one pathway changes state; locked content is never squeezed | done |
| R-20 | Receipt: every prompt line → source (entity, beat, or control + treatment) with origin; `prompt_sha256`; `emit_report.json` with chars, limit, settings, dispositions, drops, compressions, four validity levels | done |
| R-21 | Loss record per non-exact realization with the research fields (`loss_id, canonical_field, requested, provider, capability, projection, replacement, loss{type, severity}, accepted`) and `loss_code` where applicable | done |
| R-22 | Same inputs and profile → byte-identical prompt | done |
| R-23 | Dialects: a treatment's `dialect=<model>` block overrides `core` for that model; dialect changes wording only, never order | parsing done; profile rules to build (phase 6) |
| R-24 | Negatives: positive-language invariants first; a dedicated negative field when the profile has one, otherwise one short "Avoid:" line | done |
| R-25 | Suppression reason codes on anything not emitted: `low_observability · provider_unsupported · redundant · conflicting · lower_priority · already_encoded_by_stronger_control · token_budget` | token_budget done; others to build (phase 3) |
| R-26 | Redundancy: a control whose wording is already carried by beats or a stronger control is suppressed with `already_encoded_by_stronger_control` | to build (phase 3; run 001 read-back found the duplication) |
| R-27 | Strength-scaled emission: profile `strength: strong | weak`; weak → minimal core (3–5 highest-leverage lines) + camera/continuity compensation | to build (phase 5) |
| R-28 | Structured carriers (YAML/JSON/XML/hybrid) from the same IR, each with a loss report; promoted only on render evidence | to build (phase 7) |

## D. Model profiles

| Id | Requirement | Status |
|---|---|---|
| R-29 | `director/profiles/<model>.yaml`: every fact tagged `documented | documented_thirdparty | measured | guess | unknown` with source and date | done (seedance) |
| R-30 | Profiles for Kling, Hailuo, Veo, Wan from the tree's provider findings plus current docs | to build (phase 9) |

## E. Records

| Id | Requirement | Status |
|---|---|---|
| R-31 | `decisions.jsonl` per run: bridge chain + DecisionRecord subset; `selected ∈ alternatives` | written by the LLM; validator to build (phase 4) |
| R-32 | `director/gaps.jsonl`: every INFERENCE decision appended | written by the LLM; validator to build (phase 4) |
| R-33 | `director/runs/ledger.jsonl`: one line per render verdict; treatments' `## Effects` updated from it | to build (phase 2) |

## IR schema

`director/ir.schema.json` is the contract. Rule: a field exists only if a check or the emitter
reads it. Current top-level keys: `schema_version, run_id, ask, model, clip, pass_plan, entities,
hands, pathways, beats, controls, notes`. Example instance: `director/runs/001_bottle_selfie/ir.json`.
