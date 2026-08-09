---
id: SRC-012
title: CPCS AI Video Motion Direction Knowledge Base v1.0.0 (frozen package)
version: 1.0.0
epistemic_class: research_package
status: COMPLETE
lines: 14 topics (~1600) + canonical model + pipeline + schemas + examples + evidence + evaluation + adapters
file: research/continue_detail/CPCS_AI_Video_Motion_Direction_KB_v1.0.0/CPCS_AI_Video_Motion_Direction_KB/
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-012 — CPCS AI Video Motion Direction Knowledge Base v1.0.0

## Source identity

The frozen **CPCS AI Video Motion Direction KB v1.0.0** — the knowledge base
whose gap closure was distilled as SRC-001. SRC-001 explicitly stated the
package itself was **NOT supplied**; this distillation closes that gap by
processing the package directly. The KB is a self-contained research package:
14 topic files with per-topic source-reference JSONs, a canonical model
(16-layer stack, ontology, unit conventions, provenance model, graph tiers,
6 mappings), 10 pipeline documents, 10 JSON Schemas, 5 worked examples
(canonical scene + intent YAML + beats XML + compiled prompts + expected
checks), an evidence suite (claims.jsonl, sources, evidence matrix,
contradictions, gaps), evaluation (metrics, benchmark plan, acceptance
criteria, annotation protocol, model test matrix), 7 prompts, 10 scripts,
a graph seed (264 entities, 410 relations), 8 provider adapters, manifests,
checksums, and validation report. Sources [S001]–[S076].

Its core doctrine: motion is layered (creative intent → affect → body →
BESS → primitives → phases → kinematics → interaction → force → rhythm →
camera → style → adapter), every number is a typed proxy unless measured,
every preset is `CPCS_CONVENTION` until immutable experiments calibrate it,
and the seven-phase grammar is a production synthesis, **not** a universal
movement law. The adapter layer is a dated snapshot verified 2026-07-30.

## Source structure

| Folder | Contents |
| --- | --- |
| 00_scope/ | research mission, methodology, terminology crosswalk, evidence confidence, corrections and scope gaps |
| 01_topics/ | 14 topics: laban_bess, bartenieff_connectivity, motion_phase_grammar, facs, kinematics, intent_vocabulary, interaction_predicates, force_dynamics, camera_grammar, rhythm, vad_trajectories, motion_style_transfer, computational_laban, ai_video_control_surfaces (+ reference JSON per topic) |
| 02_canonical_model/ | layer_stack, ontology.yaml, graph_tiers, unit_conventions, provenance_model, mappings.jsonl (6 mappings), controlled_vocabulary.csv |
| 03_schemas/ | 10 JSON Schemas (actor, affect_trajectory, camera_track, canonical_scene, experiment_record, facs_track, interaction, model_adapter, motion_primitive, phase_timeline) |
| 04_pipeline/ | architecture, compiler, derived_weights, extraction, immutable_experiments, implementation_roadmap, ingestion, model_adapters, retrieval, validation |
| 05_examples/ | 5 worked scenes (cross_punch, comforting_reach, ugc_product_reveal, anime_block_counter, uncertain_aggression) × (canonical.json, intent.yaml, beats.xml, compiled_prompts.md, expected_checks.md) |
| 06_evidence/ | bibliography, claims.jsonl, claim_source_map.jsonl, contradictions, evidence_matrix.csv, gaps, search_log, source_quality, sources.csv/jsonl |
| 07_prompts/ | critique, experiment_summarizer, intent_planner, model_adapter, motion_compiler, normalizer, source_extractor |
| 08_evaluation/ | acceptance_criteria, annotation_protocol, benchmark_plan, metrics, model_test_matrix.csv, test_cases.jsonl |
| 09_source_notes/ | per-topic source locators |
| 10_scripts/ | compile_example.py, export_graph.py, validate_package.py + demo_compile_output.json |
| 11_graph_seed/ | concepts.csv, entities.jsonl (264), relations.jsonl (410), graph_export.cypher, graph_ingest.md |
| 12_adapters/ | 8 adapters (adobe_firefly_video, kling_3_0, kling_3_0_omni, luma_ray_3_2, runway_act_two, runway_gen_4_5, sora_2_legacy, veo_3_1) |
| root | README, USAGE_NOTICE, CHANGELOG, manifest.json, checksums.sha256, validation_report.json |

## Source units

| Unit | Component | Distilled to |
| --- | --- | --- |
| U01 | 00_scope/* (mission, methodology, crosswalk, confidence, corrections) | DIST ledger, gaps |
| U02 | 01_topics/10_rhythm.md | CREATE rhythm_metrics_contract, beat_syncpoint_alignment |
| U03 | 01_topics/03_motion_phase_grammar.md | CREATE phase_timing_presets; EXTEND evidence_vs_engineering_phases (E18) |
| U04 | 01_topics/09_camera_grammar.md | CREATE camera_impact_sync |
| U05 | 01_topics/02_bartenieff_connectivity.md | EXTEND bartenieff_six_patterns |
| U06 | 01_topics/07_interaction_predicates.md + 08_force_dynamics.md | EXTEND interaction_lifecycle, combat_math_metrics_layer |
| U07 | 01_topics/14_ai_video_control_surfaces.md + 12_adapters/* | EXTEND provider_capability_snapshots |
| U08 | 01_topics/01,04,05,06,11,12,13 (BESS, FACS, kinematics, intent, VAD, style, computational laban) | DIST ledger, gaps (mostly covered by SRC-001/002/003/009/010; deltas noted) |
| U09 | 02_canonical_model/* (layer stack, ontology, units, provenance, mappings, tiers) | DIST ledger, gaps (unit conventions match SRC-010; evidence-class vocabulary delta noted) |
| U10 | 03_schemas/* + 05_examples/* | DIST ledger, gaps; phase_timeline/canonical_scene field deltas |
| U11 | 04_pipeline/* (compiler passes, validation layers, immutable experiments, adapters) | DIST ledger, gaps; compiler order corroborates SRC-003/007 |
| U12 | 06_evidence/* + 08_evaluation/* + 07_prompts/* + 10_scripts/* + 11_graph_seed/* | DIST ledger, gaps (metrics/benchmark/acceptance gates) |
| U13 | manifest.json, README, USAGE_NOTICE, CHANGELOG, validation_report | DIST ledger, identity, gaps |

## Self-declared limitations

- **All numeric presets are `CPCS_CONVENTION`** (production starting points),
  to be learned per action/actor/genre/model through immutable experiments —
  never presented as universal or measured values.
- **Adapters are a dated snapshot (2026-07-30)**; model names, endpoints,
  limits, and UI/API parity change frequently. Every adapter must revalidate
  official documentation; `ttl_days` 21–30.
- **Seven-phase grammar is a CPCS synthesis**; BML's seven sync points
  (start/ready/stroke_start/stroke/stroke_end/relax/end) are a different
  taxonomy and must not be relabeled as a universal phase law.
- **Rhythm presets differ from phase-grammar presets**; both are CPCS
  conventions and the compiler must reconcile them, never silently override.
- **LMA Weight/Flow are not physically measurable from monocular RGB**; no
  validated real-time full-BESS detector exists. Aliases LabanWRML,
  ChoosenMove, and the CMD dataset remain UNVERIFIED (quarantined).
- **Evidence classes** are 5 (ESTABLISHED / EMPIRICAL / PRACTICE /
  CPCS_CONVENTION / UNVERIFIED) with measurement_status precedence
  (measured > annotated > inverse_dynamics_estimate > model_inference >
  visual_proxy > prompt_prior > generated) — related to but not identical
  with tree vocabularies from SRC-005/009/011 (noted in gaps).
- Topic 14 was reconstructed by the KB itself from a truncated query
  (explicitly disclosed in the KB); it is a dated snapshot, not a ranking.

## Distilled object count

4 new cards + 6 EXTENDs (incl. application of pending SRC-003 E16 and E18)
+ 1 gaps file + DIST-012 ledger + source identity registration + sync.
