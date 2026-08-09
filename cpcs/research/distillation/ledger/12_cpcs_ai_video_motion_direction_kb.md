---
distillation_id: DIST-012
source_id: SRC-012
status: complete
coverage: full
---

# Distillation Ledger — SRC-012

`CPCS_AI_Video_Motion_Direction_KB_v1.0.0` (frozen knowledge base; 14 topics,
canonical model, pipeline, 10 schemas, 5 examples, evidence suite, evaluation,
adapters; sources [S001]–[S076]) → CPCS knowledge tree.
Distilled 2026-08-09. Emphasis: **motion sync and alignment formula
representation for the DAG**, with deltas and nuance.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-012_ai_video_motion_direction_kb.md`.
SRC-001 distilled the KB's gap-closure analysis but explicitly lacked the
package; SRC-012 processes the package itself. Epistemic class:
research_package with `CPCS_CONVENTION` provenance on all presets; adapters
are a dated snapshot (2026-07-30).

## PASS 1 — Structural map

**Topics (14):** 01 laban_bess (Effort factors, 6 states, 4 drives, 8 basic
effort actions, Shape modes, Space, digitization systems) · 02
bartenieff_connectivity (Basic Six vs Six Patterns separation, primitive
encoding with sequencing_delay_ms, composition table, 5 compiler ops) · 03
motion_phase_grammar (7-phase CPCS synthesis, 5 timing presets with exact
ratios, action decompositions, state machine, expressive roles, compiler
requirements) · 04 facs (public AU registry, A–E → 0.2–1.0 ordinal, motifs
incl. pain_pspi, onset/apex/offset timing, no micro-expression law) · 05
kinematics (formula table, 9-step video-to-physics pipeline, perceived-quality
params) · 06 intent_vocabulary (20 intents, P(motion|…) priors, multi-scale
compilation) · 07 interaction_predicates (40-predicate vocabulary, contact
topology, two-person patterns) · 08 force_dynamics (4 truth levels, impact
decomposition, kinetic chain as directed graph, perceived-force controls,
combat-style priors) · 09 camera_grammar (pinhole, exposure formula, 12
primitives, impact synchronization, anime devices, canonical camera record) ·
10 rhythm (hierarchy, master clock, 5 rhythm presets, frame profiles, metrics,
combat rhythm, AIST++, dialogue/UGC, editing rhythm) · 11 vad_trajectories
(VAD + confidence/certainty/engagement, 10 seed anchors, trajectory
representation, VAD→motion/face mapping, transition types) · 12
motion_style_transfer (style as transform over protected choreography,
invariants, 8-step compiler order, 7 profiles, anime transform, 7 failure
modes) · 13 computational_laban (no real-time full-BESS detector; systems/
datasets tables; UNVERIFIED aliases; 10-step detector architecture;
observability; learning strategy) · 14 ai_video_control_surfaces (dated
snapshot; 7-status vocabulary; model matrix; downcasting; adapter contract;
loss report).

**Canonical model:** 16-layer stack with precedence (safety > interaction >
measured > estimates > priors); ontology (26 classes, ~22 relations incl.
HAS_PHASE ordered, CONTACTS temporal); graph tiers (Curated / Immutable /
Derived + Promotion); unit conventions (right-handed +x right +y up +z
forward; quaternion [w,x,y,z]; radians; seconds; bipolar [-1,1] u=(x+1)/2;
body_weight_force=force/(mass·g); store continuous, quantize at render);
provenance 5 classes + measurement_status precedence; 6 mappings
(map_phase_bml_v1, map_facs_letter_unit_v1, map_shape_vertical_v1,
map_vad_arousal_motion_v1, map_effort_weight_force_v1 NON_EQUIVALENCE,
map_model_surface_v1).

**Pipeline:** architecture (intent→canonical→adapter→generation→immutable
ledger→derived weights→compiler rerank; storage lanes; 6 control-plane
invariants) · compiler (8 passes; "Solve interaction causality before
camera/style"; "Align phases to clocks/beats… impact sync"; 7-level conflict
priority; determinism) · derived_weights (lineage fields, guardrails,
promotion) · extraction (6 stages, claim records, ontology alignment) ·
immutable_experiments (append-only supersedes; 12 evaluation axes incl.
timing/rhythm + audio sync) · ingestion (8 steps) · model_adapters (adapter
key, 7 capability statuses, 8-step compile, loss report, deprecation) ·
retrieval (5 indexes) · validation (8 layers incl. temporal "synchronized
bindings" + interaction causality rules).

**Schemas/examples:** canonical_scene (required: cpcs_version, scene_id,
title, duration_s, fps, actors; fields: intent, beats, actors, affect_tracks,
phase_timelines, motion_primitives, facs_tracks, interactions, camera_tracks,
style, rhythm, constraints, target_adapters, provenance) · phase_timeline
(phases enum incl. hold/custom; per-phase t_start/t_end, progress_curve,
semantic/force/emotion role, contact_event_ids; interruptions; provenance) ·
motion_primitive (connectivity_pattern enum, initiator, receiver_sequence,
speed m/s|rad/s|normalized, sequencing_delay_ms, grounding, breath_phase,
laterality, support_contact_ids, phase_timeline_id, laban block). Worked
example ex_cross_punch_01 (3.0 s @ 24 fps; phase timeline 1.1 s with
contact_01 bound to stroke+overshoot; interaction int_block 1.13–1.25 s
duration 0.12, compliance 0.25, resistance 0.82; rhythm {explosive,
contact_s 1.18, setup_strike_recovery [0.4,0.18,0.42]}; camera truck 0.65–1.7
subject-locked, impact_bindings [] with expected check "impulse decays within
six frames"; FACS AU4/AU7 with onset/apex/offset; expected checks: reaction at
or after contact, no foot skating, fist recoil by 2.3 s, identity/laterality
stable).

**Evaluation:** metrics (human 0–4 ordinal; automatic: MPJPE/PCK, contact
precision/recall/onset error/drift/penetration/reaction-order violations,
identity, camera, rhythm beat alignment + phase landmark timing + IOI, FACS
AU agreement, style + invariant preservation, physics foot-skate/bone-length/
joint-limit/COM-support, temporal coherence fragmentation/swaps/flicker;
reliability κ/ICC/Krippendorff/Brier/ECE) · benchmark plan (4 conditions
baseline prose / CPCS prose-only / CPCS native-reference / ablations; 9 scene
families; ≥5 scenes/family; co-primary = predicate/action correctness +
contact causality; model×scene interactions reported) · acceptance criteria
(parse 100%, source IDs resolve, no adapter older than TTL, no UNVERIFIED in
Curated; compiler deterministic, no interval outside scene, no invalid phase
order without interruption, loss report completeness, measured/estimated/
prior distinguishable; pilot gate: predicate ≥3/4, contact causality ≥3/4,
identity ≥3/4, zero critical safety violations, κ/ICC ≥0.60, CPCS improves ≥1
co-primary without decline in other) · annotation protocol (blinded, replay/
scrub allowed, no hidden emotion/deception inference, ≥2 annotators +
adjudication, original labels stored).

**Graph seed:** 264 entities (14 topics, 76 sources), 410 relations
(SUPPORTED_BY with locators; Neo4j ingest with reification recommended;
Curated tier only; derived never merged into source claims).

**Adapters:** 8 JSON adapters (veo_3_1_gemini_v2026_07_30 status preview,
native {duration 4/6/8, aspect 16:9/9:16, res 720p/1080p/4k conditional, seed,
native_audio, reference_images max 3 conditional}, prompt_only
[laban_bess, facs_track, phase_microtiming, interaction_predicates, camera
trajectory], validation_rules ["Some reference/extension/high-resolution
operations require duration=8"], loss_risk contact_topology high; kling
3_0_omni status current ttl 21, multi_shot + shot_level_duration +
element_voice, loss_risk contact_causality high; sora_2_legacy status
legacy_deprecating).

## PASS 2 — Existing-knowledge search

Already in tree: FACS AU system (SRC-001/002), Laban Effort/Shape/Body/Space
(SRC-001/002/010), Bartenieff patterns (SRC-002), motion phase grammar
foundations (SRC-001 evidence vs engineering), VAD/VAC affect (SRC-001),
kinematics, intent vocabulary (SRC-001/010), interaction predicates
(SRC-001/003), force dynamics (SRC-001/010), camera grammar (SRC-001/010),
motion style transfer (SRC-003), computational Laban (SRC-001/002), control
surfaces (SRC-007/009), canonical schema design (SRC-005/008/009), compiler
(003/007/011), validation (SRC-006/007), evaluation (SRC-010).

**Major gaps found (sync/alignment emphasis):**
1. **No rhythm layer in tree** — `knowledge/10_time_rhythm/` referenced in
   evidence_vs_engineering_phases frontmatter but EMPTY. Rhythm hierarchy,
   master clock doctrine, presets, frame profiles, metrics absent → CREATE.
2. **BML sync-point mapping absent** — map_phase_bml_v1 (CPCS phases → BML
   sync points) is the only canonical cross-taxonomy sync mapping → CREATE.
3. **Phase timing presets absent** — exact normalized ratio presets, phase
   roles (semantic/force/emotion), action decompositions, pin-contact rule
   not in tree → CREATE; feeds pending SRC-003 E18.
4. **Camera impact synchronization absent** — binding chain, zero-frame
   offset preset, 83 ms impact hold, exposure formula, impact_response
   record not in tree → CREATE.
5. **Contact causality timing metrics absent** — onset error, drift,
   penetration, reaction-order violations; contact topology modes
   (stick/slide/roll/impact/separate); two-person sync patterns (handoff
   shared-support, counter window) → EXTEND interaction_lifecycle.
6. **Bartenieff primitive encoding absent** — sequencing_delay_ms,
   initiator/receiver_sequence, breath_phase, support_contacts, composition
   chains, 5 compiler ops → EXTEND bartenieff_six_patterns.
7. **Force-style priors + impact decomposition + 4-phase/7-phase delta**
   → EXTEND combat_math_metrics_layer.
8. **Adapter 7-status vocabulary + dated capability matrix + downcasting
   table** → EXTEND provider_capability_snapshots.
9. E16 (temporal_coupling coupled timing) PENDING — KB master-clock/relative-
   phase/phase-lock content fulfills it → apply.
10. E18 (evidence_vs_engineering_phases phase organizations) PENDING — KB
    seven-phase grammar + optionality + BML distinction fulfills it → apply.

## PASS 3 — Semantic map

4 new objects:
- `rhythm_metrics_contract` — hierarchy, master clock (seconds authoritative;
  frame clock + musical grid derived), 14 rhythm fields, 5 rhythm presets
  with exact ratios, 3 frame-level profiles, 7 metrics, combat/dance/UGC/
  editing rhythm, reconciliation rule vs phase presets.
- `beat_syncpoint_alignment` — CPCS seven-phase ↔ BML sync points mapping
  (map_phase_bml_v1), gesture-phase taxonomy, beat-alignment semantics
  (initiation leads / apex on beat), feint pattern, dialogue sync.
- `phase_timing_presets` — 7-phase grammar with optionality, 5 timing presets
  (exact ratios), phase roles, action decompositions, state-machine rules,
  compiler requirements (pin contact before warp), worked binding example.
- `camera_impact_sync` — impact binding chain (7 anchor events; subject
  contact authoritative), impact_response record, exposure formula, 83 ms
  hold, anime devices, DAG edge representation.

6 EXTENDs: temporal_coupling (E16), evidence_vs_engineering_phases (E18),
interaction_lifecycle, bartenieff_six_patterns, combat_math_metrics_layer,
provider_capability_snapshots.

## PASS 4 — Numerical/formal map

Phase presets (ratios sum to 1): explosive 0.03/0.09/0.19/0.22/0.14/0.22/0.11;
ballistic 0.03/0.07/0.21/0.22/0.20/0.18/0.09; controlled 0.07/0.17/0.17/0.22/
0.07/0.19/0.11; sustained 0.07/0.14/0.17/0.27/0.06/0.18/0.11; microgesture
0.08/0.10/0.16/0.30/0.04/0.18/0.14. Rhythm presets (DIFFER): explosive
0.05/0.22/0.18/0.10/0.10/0.20/0.15; ballistic 0.04/0.14/0.22/0.12/0.20/0.18/
0.10; controlled 0.08/0.18/0.18/0.18/0.06/0.20/0.12; sustained 0.08/0.12/
0.16/0.28/0.06/0.18/0.12; hesitant 0.12/0.27/0.10/0.12/0.04/0.18/0.17. Frame
profiles: snappy_24fps {onset [2,4], acceleration [2,4], impact_hold [0,2],
settle [3,7]}; floaty_24fps {onset [6,12], acceleration [6,14], impact_hold
[0,1], settle [8,18]}; anime_limited {key_pose_hold [2,12], smear [1,2],
impact [1,3]}. Camera: exposure_time = shutter_angle/(360×fps) (180°@24fps →
1/48 s); pinhole x = fX/Z; impact_response {amplitude 0.22, peak_offset_frames
0, decay_frames 6}; 2-frame impact hold @24fps ≈ 83 ms; handheld_impulse
{amplitude, frequency_hz, impact_sync, decay_s}. Force priors (Preparation/
Peak speed/Recoil/Follow-through/Commitment): boxing_snap 0.25/0.85/0.8/0.35/
0.65; muay_thai_commitment 0.45/0.8/0.45/0.8/0.9; tai_chi_redirection
0.25/0.35/0.25/0.55/0.55; mma_mixed = none. Bartenieff sequencing_delay_ms 55
(cross punch), grounding 0.84–0.86, breath_phase exhale. Interaction record:
duration_s 0.12, compliance 0.25, resistance 0.82 (block example); metrics:
contact onset error, drift, penetration, reaction-order violations. Mapping
unit conventions: bipolar [-1,1], u = (x+1)/2; body_weight_force =
force/(mass·g) — consistent with SRC-010 laban_numeric_calibration_contract
(weight/time/space ∈ [0,1], flow ∈ [−1,1]).

## PASS 5 — Representation/compiler map

KB compiler order (8 passes) corroborates the tree's compiler doctrine:
interaction/contact causality solved **before** camera/style; "Align phases to
clocks/beats… impact sync" is pass 6; determinism required. Phase timeline is
**action-local** (primitive-relative times) and anchored to the scene via beat
start + contact event binding (ex_cross_punch_01: primitive timeline 0–1.1 s,
scene offset 0.7 s, contact event at scene 1.13 s = stroke start 0.43 + 0.7).
The KB's `rhythm` object (profile, contact_s, setup_strike_recovery 3-split)
coexists with the 7-phase timeline — two complementary timing representations
that the compiler reconciles; documented rather than merged. Loss report
(demo_compile_output.json) matches the tree's capability_classes_and_loss
records: preserved_or_native vs lossy_or_prompt_only vs loss_risk +
verification_required + not_executed flag.

## PASS 6 — Interface map

New cards interface with: temporal_coupling (relations precedes/lags/
synchronizes_with/peaks_with/holds_during/releases_after/triggered_by),
multimodal_sync (timebase alignment), temporal_solver_semantics (STN/STNU,
schedule origin), evidence_vs_engineering_phases (phase boundary provenance),
canonical_schema_design (event/interval/track contracts, timebase),
interaction_lifecycle (causal bundle), combat_math_metrics_layer (SRC-010
4-phase ratios, frame budgets, contact tolerances), bartenieff_six_patterns,
provider_capability_snapshots, capability_classes_and_loss_records,
motion_matching_compilation (matching cost + phase-conditioned control),
adrg_reasoning_graph_schema (synchronizes_with edge), cross_format_compiler_
reference.

## PASS 7 — Contradiction scan

- **Rhythm presets vs phase presets (KB-internal, explicit):** Topic 10
  presets ≠ Topic 3 presets; the KB itself declares both CPCS conventions and
  requires the compiler to reconcile rather than silently override. Captured
  in both new rhythm cards + phase_timing_presets; no merge attempted.
- **KB 7-phase vs SRC-010 combat 4-phase:** SRC-010 strike ratios are 4 bins
  (anticipation 25–35% · contact 10–15% · follow-through 25–35% · recovery
  15–30%) with contact as a bin; KB treats contact as an event bound to
  stroke+overshoot phases. Not contradictory (different granularity) but must
  not be silently equated; mapping documented in combat_math_metrics_layer
  EXTEND.
- **KB 7-phase vs tree 10-step engineering grammar** (evidence_vs_engineering_
  phases): 10-step is action-boundary grammar with explicit contact step; KB
  7-phase is normalized profile grammar with contact as event. Complementary;
  relationship documented in E18 application.
- **BML seven sync points ≠ seven-phase law:** KB explicitly warns against
  relabeling (also the execution-kit audit verdict); terminology correction
  captured in beat_syncpoint_alignment + E18.
- **Evidence-class vocabulary:** KB 5 classes (ESTABLISHED/EMPIRICAL/
  PRACTICE/CPCS_CONVENTION/UNVERIFIED) + measurement_status precedence vs
  SRC-005 7 classes / SRC-009 VOG 5 / SRC-011 6 labels. Related, not
  identical; noted in gaps, no tree change (mirrors SRC-011 gap #12).
- **Unit conventions:** KB bipolar [-1,1] u=(x+1)/2 and flow signed matches
  SRC-010 laban_numeric_calibration_contract; KB examples store unit-view
  [0,1] values — consistent via the stated conversion; no conflict.
- **Contact as authoritative anchor:** KB "contact instant remains the causal
  anchor" (force dynamics, camera, interaction) matches interaction_lifecycle
  causal bundle and SRC-010 "contact time error ≤ 50 ms" — consistent, no new
  card needed for the principle itself.
- **No contradictions** with SRC-001/002/003/007/009/010/011 boundaries.

## PASS 8 — Placement decisions

4 CREATEs: knowledge/10_time_rhythm/rhythm_metrics_contract.md,
knowledge/10_time_rhythm/beat_syncpoint_alignment.md,
knowledge/06_body_motion/phase_grammar/phase_timing_presets.md,
knowledge/12_camera_image_formation/camera_impact_sync.md.
6 EXTENDs: temporal_coupling.md (E16 application), evidence_vs_engineering_
phases.md (E18 application), interaction_lifecycle.md, bartenieff_six_patterns.md,
combat_math_metrics_layer.md, provider_capability_snapshots.md.
No REUSE/MERGE/SPECIALIZE beyond the above. (SRC-013 execution-kit
distillation deferred per user decision; candidate note retained in
outstanding_actions.)

## PASS 9 — Dedup audit

- rhythm_metrics_contract vs beat_syncpoint_alignment: metrics/clocks/profiles
  vs cross-taxonomy sync mapping; distinct, cross-referenced.
- rhythm_metrics_contract vs temporal_coupling (E16): contract card owns the
  rhythm layer + metrics; temporal_coupling EXTEND adds coupled timing/
  relative phase/phase-lock edges — complementary, no duplication.
- phase_timing_presets vs evidence_vs_engineering_phases (E18): presets card
  owns the normalized profile grammar + ratios; E18 EXTEND documents the
  relationship between the two engineering grammars and the BML distinction.
- camera_impact_sync vs combat_math_metrics_layer: camera card owns impact
  binding/impulse/decay + exposure; combat card owns SRC-010 camera math
  (shake 8–15 Hz, whip 120–240°/s) — cross-referenced, no overlap.
- interaction_lifecycle EXTEND vs camera_impact_sync: causal bundle vs camera
  binding chain; the bundle already exists in interaction_lifecycle, the
  camera-specific binding is new — cross-referenced.
- provider_capability_snapshots EXTEND vs capability_classes_and_loss_records:
  snapshot matrix/status vocabulary vs realization statuses + loss taxonomy;
  complementary layers (SRC-007 boundary preserved).
- No duplicate of multimodal_sync (observation timebase) — rhythm card is
  authored-clock doctrine for the canonical scene, not observation sync.

## PASS 10 — Operationalization

All presets, ratios, frame ranges, offsets, decays, tolerances, metrics, and
statuses are enumerable and testable. The worked example (ex_cross_punch_01)
is a valid instance of the package's canonical_scene schema with a known
compile output (demo_compile_output.json). Metrics (beat-alignment error,
IOI CV, phase-ratio error, contact-causality error, snappiness/floatiness
proxies, cut-rhythm divergence, contact onset error/drift/penetration/
reaction-order violations) are computable from scene timelines. Acceptance
gates (predicate/contact-causality ≥3/4, κ/ICC ≥0.60, TTL policy) are
declared thresholds, not universal constants.

## PASS 11 — Coverage audit

All 13 units dispositioned: U01, U08–U13 → DIST ledger, identity, gaps;
U02 → CREATE rhythm_metrics_contract + beat_syncpoint_alignment; U03 →
CREATE phase_timing_presets + EXTEND evidence_vs_engineering_phases (E18);
U04 → CREATE camera_impact_sync; U05 → EXTEND bartenieff_six_patterns; U06 →
EXTEND interaction_lifecycle + combat_math_metrics_layer; U07 → EXTEND
provider_capability_snapshots; E16 applied to temporal_coupling.

## Objects written

- `cpcs/research/source_registry/identities/SRC-012_ai_video_motion_direction_kb.md`
- `cpcs/research/distillation/ledger/12_cpcs_ai_video_motion_direction_kb.md`
- `cpcs/research/gaps/src012_open_research_questions.md`
- CREATE: `cpcs/knowledge/10_time_rhythm/rhythm_metrics_contract.md`
- CREATE: `cpcs/knowledge/10_time_rhythm/beat_syncpoint_alignment.md`
- CREATE: `cpcs/knowledge/06_body_motion/phase_grammar/phase_timing_presets.md`
- CREATE: `cpcs/knowledge/12_camera_image_formation/camera_impact_sync.md`
- EXTEND: `cpcs/runtime/06_canonical/temporal_tracks/temporal_coupling.md` (E16)
- EXTEND: `cpcs/knowledge/06_body_motion/phase_grammar/evidence_vs_engineering_phases.md` (E18)
- EXTEND: `cpcs/knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md`
- EXTEND: `cpcs/knowledge/06_body_motion/bartenieff/bartenieff_six_patterns.md`
- EXTEND: `cpcs/knowledge/05_action/combat/combat_math_metrics_layer.md`
- EXTEND: `cpcs/runtime/08_provider_negotiation/provider_capability_snapshots.md`
- Sync: `cpcs/research/gaps/outstanding_actions.md`, DIRECTORY.md regeneration
