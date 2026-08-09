---
distillation_id: DIST-009
source_id: SRC-009
status: complete
coverage: full
---

# Distillation Ledger — SRC-009

`CPCS_FACS_Laban_AI_Video_Research_Package_v1.2` (33 files, 8,731-line paper + 1,378-line extraction guide) + `Pegasus_Atomic_Video_Deconstruction_and_Modular_AI_Recreation_v1.0` (2,782 lines) → CPCS knowledge tree. Distilled 2026-08-09.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-009_cpcs_facs_laban_paper_v1_2_pegasus_extraction.md`.
Three documents + v1.2 package. 31 source units U01–U31. Paper sections §1-17 overlap with SRC-001–SRC-005; §18-30 + appendices + Pegasus + extraction guide are new.

## PASS 1 — Structural map

CPCS paper: 31 sections + appendices A-H. §19 alone is ~1,900 lines covering structured prompting, 3-representation architecture (ASL→CIR→TEP+VER), 4 modes of structured direction, 6 typed control contracts, 11 style domains, scope cascade, typed merge algebra, 14-pass YAML→JSON compilation, capability negotiation, 3 compilation tiers, backend adapters (Sora 2, Veo, Runway), security, 8 verification checkpoints. §20-23 worked examples. §24 evaluation (6 families). §25 experimental program (6 hypotheses, 8-condition ablation). §26 failure modes (15 types). §27-29 ethics/limitations/future. §30 reference-video distillation (VOG, 5 evidence classes, 15-stage pipeline, temporal pyramid, fight/UGC workflows). Appendices: glossary, directorial crosswalk, authoring template, compilation protocol, RAG protocol, evidence map, cross-format compiler reference, video-to-CPCS operational reference.

Pegasus paper: Part I-II foundations (already in SRC-001–SRC-005). Part III: 8 fight layers, 5 fight passes (F1-F5), 6-step measurement pipeline, JSONL evidence, canonical fight CPCS score, fight transfer YAML, 5 compilation tiers, fight validation. Part IV: 5 transformation stages, XML semantic envelope, compiler resolution order, provider adapter contract, RAG storage (10 record types), 4-phase implementation blueprint, Python SDK patterns, 13 failure modes, verification checklist. Appendices A-E.

Extraction guide: 30 sections. Research question, "extracting the core" (7 properties, 11-level hierarchy), 5 evidence classes, temporal pyramid (7 passes), 15-stage architecture, stages 0-11 detailed (rights, ffprobe, shot/scene/beat, semantic analysis [Gemini/Pegasus/Marengo], face/gaze, pose/3D/camera, coordinate normalization, action atoms/contacts, Laban proxies, camera/editing, audio, VFX, UGC/marketing), confidence fusion, VOG schema, reverse compilation, fight/UGC workflows, provider orchestration, round-trip verification, failure modes (12 types), minimum viable implementation (4 tiers), verification checklist.

v1.2 package: pipeline config (262 lines), 4 JSON schemas (VOG, observation record, extraction record, RAG record), 7 Python scripts (pipeline 859 lines, manifest extractor 398, merge 227, VOG validator 191, RAG builder 923, reference pipeline 858, index builder 41), 5 prompt files, RAG corpus (179 JSONL records), 4 reference indexes, extraction example (615 lines), 2 manifests.

## PASS 2 — Existing-knowledge search

SRC-001–SRC-008 already distilled: FACS AU system, Laban Effort/Shape/Body/Space, Bartenieff connectivity, motion phase grammar, VAD/VAC affect, kinematics, intent vocabulary, interaction predicates, force dynamics, camera grammar, rhythm, motion style transfer, computational Laban, AI video control surfaces, canonical schema design, constraint resolution compilation, text-to-score compilation, RAG ingestion architecture, observation record contract, interchange manifests, MX compiler implementation, agent prompt contracts, workflow recipes, implementation roadmap, MX profile system, anime sakuga, combat coding, evidence two-axis model, failure taxonomy, director reasoning, test-time reasoning.

**Major gaps found:**
1. Structured prompting architecture (4 modes, 3-representation architecture) — not in tree
2. Typed merge algebra (10 data kinds × policies) — only abstract description in constraint_resolution_compilation
3. Capability negotiation protocol (8 statuses, loss budgets) — not in tree
4. Backend adapter pattern (Sora 2, Veo, Runway concrete examples) — not in tree
5. Video Observation Graph (canonical schema, evidence fusion, contradiction management) — not in tree
6. Reference-video distillation pipeline (15 stages, temporal pyramid, provider orchestration) — not in tree
7. Evaluation framework (6 families, detailed metrics, hard gates) — not in tree
8. Fight analysis layers (8 layers, 5 passes, measurement pipeline) — not in tree
9. Information transfer protocol (5 transformation stages, XML envelope, transfer YAML) — not in tree
10. Cross-format compiler reference (pseudocode, acceptance checklist, style domain registry) — not in tree
11. Extraction pipeline scripts (4 CLI tools, merge protocol, validation) — not in tree
12. Ethics and governance framework — not in tree

## PASS 3 — Semantic map

12 new objects:
- `structured_prompting_architecture` — 4 modes, ASL→CIR→TEP+VER, 6 typed contracts, 11 style domains
- `capability_negotiation_protocol` — 8 statuses, loss budgets, degradation ladder
- `typed_merge_algebra` — 10 data kinds, merge policies, scope cascade, candidate resolution tuple
- `video_observation_graph` — VOG schema, evidence classes, temporal pyramid, fusion, contradiction
- `reference_video_distillation` — 15-stage pipeline, provider orchestration, round-trip verification
- `pegasus_fight_analysis` — 8 layers, 5 passes, measurement pipeline, fight JSONL, transfer YAML
- `information_transfer_protocol` — 5 stages, XML envelope, compiler resolution order, adapter contract
- `evaluation_framework` — 6 families, metrics per domain, multi-objective scorecard
- `cpcs_experimental_program` — 6 hypotheses, 8-condition ablation, 10-task suite
- `extraction_pipeline_stages` — operational stages 0-11, confidence fusion, VOG schema, workflows
- `cross_format_compiler_reference` — pseudocode, style domain registry, merge-policy registry
- `cpcs_ethics_and_governance` — identity rights, deepfake, cultural variation, stunt governance

## PASS 4 — Numerical/formal map

Structured prompting: 4 modes (A=text, B=LLM, C=deterministic compiler, D=native conditioning). 3 representations (ASL, CIR, TEP) + 1 evidence stream (VER). 6 domain contracts (FACS, Laban, Combat, Director, VFX, Marketing). 11 style domains. Scope cascade: 7 levels (studio→project→sequence→scene→shot→beat→event). 6 authority classes. Candidate resolution tuple: 9 fields (p,v,a,s,q,ℓ,h,o,r). 10 merge data kinds. 14-pass YAML→JSON compilation. 8 capability statuses. 3 compilation tiers. 8 verification checkpoints.

VOG: 5 evidence classes (measured, detected, inferred, interpreted, authored). 7 temporal pyramid passes. 15 extraction stages. VOG schema: 10 required top-level fields, 21 section types. 7 contradiction types. 4 resolution statuses. 6 provider profile fields.

Evaluation: 6 families (control compliance, temporal/causal, physical, appearance/identity, semantic/cinematic, general quality). 15 failure modes. 6 hypotheses. 8-condition ablation table. 10-task suite.

Fight: 8 layers. 5 passes (F1-F5). 6-step measurement. 9 body landmarks. 5 compilation tiers. 4 validation metric families.

Transfer: 5 transformation stages. 7 capability statuses in pipeline config. 8 review gates.

## PASS 5 — Representation/compiler map

ASL→CIR→TEP+VER is a compilation pipeline, not a prompt-writing exercise. Each representation has distinct validation: ASL allows unresolved inheritance; CIR must be fully resolved with provenance; TEP is model-specific. The compiler is deterministic for translation but the video model remains stochastic.

Typed merge algebra: each data kind has a specific policy — replace (scalar), deep_merge_typed (object), merge_by_id (keyed entity), append_ordered (ordered list), set_union (set), replace_track (temporal track), splice_interval, blend_interval, conjoin_or_conflict (hard constraints). The schema declares which policy applies at each path.

Capability negotiation: for each control field, the adapter reports one of 8 statuses. A loss budget specifies hard_domains, maximum_text_compression, permitted_approximations, forbidden_drops. The compile report records what each control became.

VOG evidence fusion: do not average unlike evidence. Preserve confidence type and calibration scope. Precedence: source timestamps > calibrated geometry > uncalibrated detector > multimodal semantic > free-form description. Contradictions are first-class outputs, not silently resolved.

## PASS 6 — Interface map

New cards interface with: canonical_schema_design, constraint_resolution_compilation, evidence_two_axis_model, observation_record_contract, rag_ingestion_architecture, mx_compiler_implementation, combat_coding, anime_sakuga, camera_grammar, computational_laban, facs, kinematics, failure_taxonomy.

## PASS 7 — Contradiction scan

No contradictions found. The v1.2 pipeline config's 7 capability statuses are a subset of the paper's 8 statuses (pipeline drops `native_exact` distinction). The extraction guide's 12 failure modes are a subset of the paper's 15. The observation record schema's evidence classes align with SRC-005's evidence_two_axis_model EXTEND. The VOG schema's contradiction types are consistent with the paper's §20 contradiction management. The Pegasus paper's fight layers are compatible with SRC-005's combat/action cards but add 3 new layers (anime VFX, camera/edit causality, interaction).

## PASS 8 — Placement decisions

12 CREATEs across: knowledge/00_foundations (1), knowledge/09_evaluation (1), runtime/06_canonical (3), runtime/07_compiler (2), knowledge/05_action (1), knowledge/06_camera (1), evaluation/reference_video (1), research/sources (1), knowledge/00_foundations/epistemic_policy (1). 6 EXTENDs (see PASS 2). No REUSE/MERGE.

## PASS 9 — Dedup audit

structured_prompting_architecture vs text_to_score_compilation: the former defines the 4-mode architecture and 3-representation design; the latter is one specific compilation path. Complementary.
typed_merge_algebra vs constraint_resolution_compilation: the former is the formal algebra with 10 data kinds; the latter describes merge behavior informally. The algebra subsumes and extends.
video_observation_graph vs observation_record_contract: VOG is the canonical fused graph; observation_record_contract is the per-record schema. Different layers.
reference_video_distillation vs extraction_pipeline_stages: the former is the research framework (RVD/RDC theory); the latter is the operational implementation guide. Complementary.
pegasus_fight_analysis vs combat_coding: Pegasus adds 8-layer decomposition and 5-pass measurement; combat_coding covers choreography notation. Different concerns.
cross_format_compiler_reference vs mx_compiler_implementation: the former is the CPCS-paper reference pseudocode; the latter is the MX-specific implementation. Different scopes.

## PASS 10 — Operationalization

All capability statuses, merge policies, evidence classes, contradiction types, review gates, and compilation tiers are enumerable and testable. The extraction pipeline scripts are executable with Python 3.10+, ffprobe, FFmpeg. The VOG schema validates with JSON Schema Draft 2020-12. The 19-item verification checklist is a deterministic pass/fail test.

## PASS 11 — Coverage audit

All 31 source units dispositioned: U01-U02 → EXTENDs; U03 → 4 CREATEs; U04-U06 → 3 CREATEs; U07 → EXTEND; U08 → 2 CREATEs; U09-U10 → 2 CREATEs + EXTEND; U11 → registration; U12-U15 → CREATE + EXTEND; U16-U17 → CREATE; U18-U22 → CREATEs + EXTENDs; U23-U26 → CREATE; U27-U31 → CREATE + registration.

## Objects written

- `cpcs/research/source_registry/identities/SRC-009_cpcs_facs_laban_paper_v1_2_pegasus_extraction.md`
- `cpcs/research/distillation/ledger/09_cpcs_facs_laban_paper_v1_2_pegasus_extraction.md`
- `cpcs/research/gaps/src009_open_research_questions.md`
- `cpcs/runtime/07_compiler/structured_prompting_architecture.md`
- `cpcs/runtime/07_compiler/capability_negotiation_protocol.md`
- `cpcs/runtime/06_canonical/typed_merge_algebra.md`
- `cpcs/runtime/07_compiler/cross_format_compiler_reference.md`
- `cpcs/evaluation/reference_video/video_observation_graph.md`
- `cpcs/evaluation/reference_video/reference_video_distillation.md`
- `cpcs/evaluation/reference_video/extraction_pipeline_stages.md`
- `cpcs/knowledge/05_action/combat/pegasus_fight_analysis.md`
- `cpcs/runtime/07_compiler/information_transfer_protocol.md`
- `cpcs/knowledge/09_evaluation/evaluation_framework.md`
- `cpcs/knowledge/09_evaluation/cpcs_experimental_program.md`
- `cpcs/knowledge/00_foundations/epistemic_policy/cpcs_ethics_and_governance.md`
- EXTEND: `cpcs/runtime/06_canonical/canonical_schema_design.md`
- EXTEND: `cpcs/runtime/06_canonical/constraint_resolution_compilation.md`
- EXTEND: `cpcs/knowledge/00_foundations/uncertainty/evidence_two_axis_model.md`
- EXTEND: `cpcs/verification/observation_record_contract.md`
- EXTEND: `cpcs/research/sources/rag_ingestion_architecture.md`
