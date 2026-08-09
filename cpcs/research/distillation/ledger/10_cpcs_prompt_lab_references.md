---
distillation_id: DIST-010
source_id: SRC-010
status: complete
coverage: full
---

# Distillation Ledger — SRC-010

`lab/` (40 files) + `references/` (4 files) from `ai-video-movement-prompt-system - Copy` → CPCS knowledge tree. Distilled 2026-08-09.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-010_cpcs_prompt_lab_references.md`. The lab is the empirical component of the CPCS ecosystem: render results, user verdicts, pattern attributions with honest confidence. 24 source units U01–U24. Epistemic class: PROVIDER_EXPERIMENT — the ONLY source in the corpus whose claims rest on actual renders.

## PASS 1 — Structural map

**Lab core:** `registry.yaml` (single source of truth: 13 levers, 7 variants, 9 patterns, 3 experiments), `blocks.yaml` (13 tested modular blocks + 7 composition rules), `AGENTS.md` (agent operating procedure: compose/recommend/log, format discipline law), `CONTROL_SURFACE.md` (2 control paradigms, A/B channel catalog with status, 8 unexplored frontier channels, v005→v006 precision lesson), `FORMAT_CONTROL_MAP.md` (format↔control assignment, production flow, 3-format rationale, honesty nuances), `UNIVERSAL_MOTION_SKELETON.md` (14 layers × 3 formats, full field dictionary, coverage audit vs all 3 papers), `CONCEPT_INDEX.md` (complete concept catalog of all 3 papers mapped to lab status), `concepts.jsonl` (semantic retrieval cards with nl_triggers).

**Lab experiments:** `experiments/e001-e003` (30fps vs 24 hypothesis, skin isolated_confirmed, format variance hypothesis), `runs/results.csv` (r001-r006), `schema/records.schema.json` (variant/run/experiment/pattern shapes).

**Lab tooling:** `scripts/validate_kinematics.py` (8 check families: frame math, velocities, position/velocity coherence, contact geometry, closing speed, foot contacts, monotonic time, near-miss clearance), `extract_pose_tier2.py` (MediaPipe multi-person 2D pose → schema-valid observation records), `validate_repo.py` (pre-commit gate), `sync_repo.py` (E2E sync, 4 checks S1-S4), `build_graph.py` + `graph.py` (derived knowledge graph), `concepts.py` (query/card/stats/validate).

**Lab variants:** v001 (champion, iPhone12 raw UGC YAML-in-XML, 5/5/4/5), v002 (same content YAML+JSON, format-neutral proof), v003 (scored FACS/Laban cinematic, "too movie like" → raw pivot), v004 (smooth skin ANTI-PATTERN, 2/1/4/5), v005 (JSON canon truth alone, new paradigm, 5/5/5), v006 (hybrid YAML+JSON, reach-fixed, 0 failures on validate_kinematics), naruto_sasuke_rooftop_clash (10s shonen anime, authoring-layer worked example).

**References:** `combat_choreography.md` (two-document architecture, kinematics metrics, frame timing, spatial geometry, tempo BPM, power curves, character profiles, combat FACS, combat Laban, constraints with tolerances, camera math, style notes), `facs_laban_reference.md` (UGC AU table, intensity A–E, genuine vs fake combos, Laban effort/shape, plain-language cheat sheet, body catalog), `iphone_rawugc_realism.md` (2 failure modes + cures, iPhone-12 signature, formats that worked), `method_details.md` (looks-real lock list, reference-still pattern, multi-clip assembly, verification checklist, reverse path, per-model notes).

**Runbooks:** `RUNBOOK_pegasus_extraction.md` (semantic lane: passes, provenance pinning, time conversion, normalization mapping), `RUNBOOK_reference_to_kinematic_truth.md` (8-step breakdown→reconstruction loop, 4-tier ladder), `RUNBOOK_cross_style_switching.md` (4-layer separation, invariants, typed transform vector, style ablation), `RUNBOOK_format_mixing_and_tinkering.md` (mixing compiler, merge laws, combo recipes, 14-row tinkering map, growth protocol).

## PASS 2 — Existing-knowledge search

SRC-001–SRC-009 already distilled: FACS AU catalog, Laban contracts (layering, numeric calibration, proxy measurement, reliability), combat_action_coding (SRC-005 §17), anime_sakuga_representation, camera_three_layer_semantics, style_mechanics, evaluation_framework, canonical_schema_design, constraint_resolution_compilation, evidence_two_axis_model, observation_record_contract, rag_ingestion_architecture.

**Major gaps found:**
1. Prompt Lab architecture (levers→variants→runs→experiments→patterns model; registry as single source of truth) — not in tree
2. Empirical pattern registry (p001–p009 with confidence levels) — not in tree
3. A/B test protocol (one-lever discipline, experiment record schema, promotion rules) — not in tree
4. Variant lineage (v001–v006 render history, the v005→v006 reach-deficit lesson) — not in tree
5. Kinematic validation tooling (8 check families, pre-render self-consistency gate) — not in tree
6. Lab runbooks (4 operational procedures with trigger phrases) — not in tree
7. Combat math metrics layer (kinematics units, frame budgets, BPM, power curves, tolerances) — combat_action_coding has the ontology but no math layer
8. UGC realism reference (anti-cinematic block, microtexture recipe, iPhone-12 signature, lock list) — not in tree
9. Concept kitchen (concepts.jsonl retrieval, CONCEPT_INDEX crosswalk, profiles, growth protocol) — not in tree

## PASS 3 — Semantic map

9 new objects:
- `prompt_lab_architecture` — lab model, 2 control paradigms, 13 levers, channel catalog, format discipline law, honesty rule
- `empirical_pattern_registry` — p001–p009: statements, confidence, evidence chains, recommend_when guards
- `lab_ab_test_protocol` — one-lever A/B, record schema, run ledger, promotion/demotion rules, experiment statuses
- `variant_lineage` — v001–v006 + naruto: render history, verdicts, lineage edges, anti-pattern v004
- `kinematic_validation_tooling` — validate_kinematics 8 check families; pose Tier-2 lane; honest bounds
- `lab_runbooks` — 4 runbooks as operational procedures (triggers, steps, gates)
- `combat_math_metrics_layer` — two-document architecture, kinematics metrics, frame timing, spatial geometry, tempo, power curves, tolerances, camera math, style notes
- `ugc_realism_reference` — lock list, anti-cinematic, microtexture, iPhone-12 signature, FACS/Laban cheat sheet, verification checklist, per-model notes
- `concept_kitchen` — concepts.jsonl retrieval, CONCEPT_INDEX paper crosswalk, 8 profiles, graph, growth protocol

## PASS 4 — Numerical/formal map

13 levers · 7 variants · 9 patterns · 3 experiments · 6 runs · 4 score dims (realism/skin/motion/adherence, 1–5) · 13 blocks · 8 profile bases · 8 check families in validate_kinematics (with tolerances: TOL_SPEED 0.05 m/s, TOL_FRAME 0, TOL_REACH 0.35 m) · Laban float ranges (weight/time/space 0–1, flow −1–1) · 9 named Effort float signatures · 10 contact types (5 in v005 + combat reference taxonomy: impact/near_miss/block/grasp/grasp_and_shove) · frame budget identity (beat_frames = (end−start)×fps) · 4-phase strike timing ratios (anticipation 25–35%, contact 10–15%, follow-through 25–35%, recovery 15–30%) · 6 engagement ranges by style (0.3–2.5 m) · BPM table (6 beat types, 40–220) · 10 required combat constraints with tolerances · 7 camera fight parameters · 5 fighting archetypes → Laban baselines.

v005→v006 defect: 1.60 m separation vs 1.42 m combined reach = 0.18 m deficit — the canonical numeric contradiction that cost precision.

## PASS 5 — Representation/compiler map

The lab empirically validates the paper's representation claims: v001/v002 (format-neutrality, p006: identical content in YAML-in-XML vs YAML+JSON → identical 5/5/4/5), v005 (JSON canon truth alone sufficient — Mode A with canonical JSON), v006 (dual-parse YAML+JSON, JSON ⊂ YAML). FORMAT_CONTROL_MAP: YAML=intent/readability/inheritance, JSON=precision/hash, XML=ordered mixed content/namespaces/triggers, JSONL=evidence stream, media=dense assets. Merge laws: one authority per quantity; YAML resolves DOWN into JSON; XML owns order+triggers only; JSON wins on conflict, reported not averaged; resolution order profile < scope < local override < human lock; typed merges only; two-document clock agreement.

UNIVERSAL_MOTION_SKELETON: 14 layers (intent, action graph, phase, root & balance, joint kinematics, contact & interaction, dynamics, Laban/BESS, face & affect, mannerism, secondary motion, stylization/VFX, presentation, verification) × 3 formats, with SPINE (identity/time/coords/authority/rights). Coverage audit: every MX Appendix A.1–A.16 field family has a named home.

## PASS 6 — Interface map

New cards interface with: combat_action_coding, facs_au_catalog, laban_numeric_calibration_contract, laban_proxy_measurement_contract, anime_sakuga_representation, camera_three_layer_semantics, style_mechanics, evaluation_framework, canonical_schema_design, constraint_resolution_compilation, evidence_two_axis_model, video_observation_graph, reference_video_distillation, extraction_pipeline_stages, information_transfer_protocol, cross_format_compiler_reference, observation_record_contract, failure_taxonomy, controlled_variability, motion_smoothness.

## PASS 7 — Contradiction scan

No contradictions within SRC-010. Cross-source tensions documented:
- Lab p006 ("format ≠ realism for look") vs paper §19.1 "serialization is not control" — consistent; p008 refines it (numeric structure IS control for motion).
- Lab's 2 control paradigms vs paper's 4 modes: lab has proven Mode A only; Mode B partial (agent compose); C/D unexplored — consistent, complementary.
- e002 isolated_confirmed but single-observer/single-session — honest bound noted in both sources.
- Lab's 15 named paper failures vs observed: v004 plastic-skin is a **lab-original failure the paper does not name** (paper's 15 include foot skating, floating, premature reaction, etc.).
- v005 hard constraints authored but enforcement never verified post-render — the paper's verification loop remains unexercised in the lab.
- combat reference Laban float ranges (weight 0–1) vs SRC-002 §1.6 "no universal numeric conversion" — resolved by the numeric calibration contract: combat floats are typed proxies for authoring (v005 `lab_control` proved as control channel), not universal measurements.

## PASS 8 — Placement decisions

9 CREATEs across: knowledge/09_evaluation (2), evaluation/benchmark_runs (2), runtime/07_compiler (1), evaluation/reference_video (1), knowledge/05_action/combat (1), knowledge/04_character_performance (1), research/sources (1). 6 EXTENDs: combat_action_coding, facs_au_catalog, laban_numeric_calibration_contract, camera_three_layer_semantics, anime_sakuga_representation, evaluation_framework. No REUSE/MERGE.

## PASS 9 — Dedup audit

empirical_pattern_registry vs evaluation_framework: the former is empirical (render-derived); the latter is the paper's proposed framework. Complementary — the lab is the empirical instantiation of the paper's multi-objective scorecard (4 manual dims vs 6 metric families).
variant_lineage vs evaluation/benchmark_runs: lineage is the only populated run history in the tree — placed in benchmark_runs as the empirical ground truth.
combat_math_metrics_layer vs combat_action_coding: the former adds the quantitative layer (units, budgets, tolerances) to the latter's ontology (atoms, coupled score). Complementary; linked via EXTEND.
kinematic_validation_tooling vs verification/* : the former is the pre-render self-consistency gate (tooling), the latter the post-render measurement contracts. Different phases; linked.
concept_kitchen vs rag_ingestion_architecture: the former is the lab's retrieval corpus (concepts.jsonl, nl_triggers), the latter the paper's RAG record schema. Same idea at different scales; complementary.

## PASS 10 — Operationalization

All patterns, levers, blocks, check families, runbook steps, and tolerance values are enumerable and testable. validate_kinematics.py and extract_pose_tier2.py are executable with documented exit codes. The 10-item verification checklist (method_details §4) is a deterministic pass/fail. Experiment statuses (hypothesis → qualitative_confirmed → isolated_confirmed → refuted) are tracked in schema. The growth protocol (cannibalize flow) is a defined procedure with a gate (sync_repo.py).

## PASS 11 — Coverage audit

All 24 source units dispositioned: U01–U06 → CREATE prompt_lab_architecture + EXTENDs; U07–U09 → CREATE concept_kitchen; U10 → CREATE lab_ab_test_protocol; U11 → CREATE variant_lineage; U12 → CREATE lab_ab_test_protocol; U13–U14 → CREATE kinematic_validation_tooling; U15 → CREATE concept_kitchen; U16 → CREATE variant_lineage; U17–U20 → CREATE lab_runbooks; U21 → CREATE combat_math_metrics_layer + EXTEND combat_action_coding; U22–U24 → CREATE ugc_realism_reference + EXTEND facs_au_catalog.

## Objects written

- `cpcs/research/source_registry/identities/SRC-010_cpcs_prompt_lab_references.md`
- `cpcs/research/distillation/ledger/10_cpcs_prompt_lab_references.md`
- `cpcs/research/gaps/src010_open_research_questions.md`
- `cpcs/knowledge/09_evaluation/prompt_lab_architecture.md`
- `cpcs/knowledge/09_evaluation/empirical_pattern_registry.md`
- `cpcs/evaluation/benchmark_runs/lab_ab_test_protocol.md`
- `cpcs/evaluation/benchmark_runs/variant_lineage.md`
- `cpcs/runtime/07_compiler/kinematic_validation_tooling.md`
- `cpcs/evaluation/reference_video/lab_runbooks.md`
- `cpcs/knowledge/05_action/combat/combat_math_metrics_layer.md`
- `cpcs/knowledge/04_character_performance/ugc_realism_reference.md`
- `cpcs/research/sources/concept_kitchen.md`
- EXTEND: `cpcs/knowledge/06_body_motion/action_primitives/combat_action_coding.md`
- EXTEND: `cpcs/knowledge/04_character_performance/facs/facs_au_catalog.md`
- EXTEND: `cpcs/knowledge/06_body_motion/laban_bess/laban_numeric_calibration_contract.md`
- EXTEND: `cpcs/knowledge/12_camera_image_formation/camera_three_layer_semantics.md`
- EXTEND: `cpcs/knowledge/16_style_visual_language/anime_sakuga_representation.md`
- EXTEND: `cpcs/knowledge/09_evaluation/evaluation_framework.md`
