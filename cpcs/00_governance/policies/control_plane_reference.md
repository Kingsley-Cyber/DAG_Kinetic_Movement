---
id: cpcs.gov.control_plane_reference
kind: policy
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012, CPCS operating prompt]
primary_route: cpcs/00_governance/policies/
secondary_routes:
  - cpcs/00_governance/
interfaces:
  - cpcs.gov.automation_doctrine
  - cpcs.gaps.outstanding_actions
---

# CPCS Control Plane Reference

> **BOOT FILE for new sessions and agents.** Read this first. It captures the
> live state of the ontology, all controlled vocabularies, the authority
> hierarchy, and the distillation queue. Update it after every distillation.

## 1. Purpose

This document is the single source of truth for:

- What has been distilled and what remains
- Which controlled vocabularies are in force
- Where every canonical object lives
- What rules govern object creation, extension, and naming
- How a new session or agent achieves continuity

The companion script `cpcs_ontology_check.ps1` (workspace root) validates every
`.md` file under `cpcs/` against the schema defined here. Run it after any
change to the knowledge tree.

## 2. System state (live)

| Property | Value |
| --- | --- |
| Last updated | 2026-08-09 |
| Sources distilled | 12 (SRC-001 … SRC-012) |
| Sources pending | 6 (see §14) |
| Total knowledge objects | 178 cards + 5 system files = 183 |
| Routes (directories) | 1,124 (1,011 leaves) — regenerated after agent-log + gap-register addition |
| DIRECTORY.md status | LIVE — regenerated after SRC-012 |
| Operating prompt | `CPCS Research Distillation Agent — Persistent Operating Prompt.md` |
| Distillation folder | `Research_distillation_folder/` |
| Automation doctrine | `00_governance/policies/control_plane_automation_doctrine.md` — agent-automated control plane (§15) |
| Working agent log | `00_governance/agent_logs/working_agent_log.md` — session continuity, append per H6 (§16) |
| Understanding gaps | `research/gaps/understanding_gap_register.md` — student-gap register, automated capture D8 (§16) |
| Research return | `Research_return_folder/` — deep-research intake for gap ingestion D9 (§16) |

### Distillation history

| ID | Source file | Status | Objects written | Ledger |
| --- | --- | --- | --- | --- |
| SRC-001 | `01_AI_VIDEO_MOTION_DIRECTION_KB_GAP_CLOSURE_RESEARCH.md` | COMPLETE | 25 new + 0 EXTEND | `ledger/01_...md` |
| SRC-002 | `02_FACS_LABAN_BARTENIEFF_GAP_CLOSURE_COMPLETED.md` | COMPLETE | 37 new + 9 EXTEND | `ledger/02_...md` |
| SRC-003 | `03_MX_HIERARCHICAL_MOTION_GRAMMAR_GAP_CLOSURE_RESEARCH.md` | COMPLETE | 30 new + 18 EXTEND | `ledger/03_...md` |
| SRC-004 | `04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md` | COMPLETE | 12 new + 8 EXTEND | `ledger/04_...md` |
| SRC-005 | `04.5-CPCS_MX_Hierarchical_Motion_Grammar_Research_Paper.md` | COMPLETE | 14 new + 6 EXTEND | `ledger/05_...md` |
| SRC-006 | `05_VIDEO_TEST_TIME_REASONING_GAP_CLOSURE.md` | COMPLETE | 10 new + 3 EXTEND | `ledger/06_...md` |
| SRC-007 | `06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md` | COMPLETE | 6 new + 6 EXTEND | `ledger/07_...md` |
| SRC-008 | `CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0` (frozen package) | COMPLETE | 6 new + 4 EXTEND | `ledger/08_...md` |
| SRC-009 | `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2` + Pegasus v1.0 + Extraction Guide v1.2 | COMPLETE | 12 new + 6 EXTEND | `ledger/09_...md` |
| SRC-010 | CPCS Prompt Lab `lab/` + `references/` (44 files) | COMPLETE | 9 new + 5 EXTEND | `ledger/10_...md` |
| SRC-011 | `CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0` | COMPLETE | 3 new + 6 EXTEND | `ledger/11_...md` |
| SRC-012 | `CPCS_AI_Video_Motion_Direction_KB_v1.0.0` (frozen KB) | COMPLETE | 4 new + 6 EXTEND | `ledger/12_...md` |

## 3. Architecture

Three planes under `cpcs/`:

```
cpcs/
  00_governance/          ← policies, priorities, control-plane reference
  knowledge/              ← KNOWLEDGE PLANE — domain taxonomy
    00_foundations/       ← invariants, causality, uncertainty, numerical rep
    04_character_performance/  ← FACS, affect
    05_action/combat/     ← fight analysis, combat metrics
    06_body_motion/       ← Laban, Bartenieff, biomechanics, kinematics, phases
    07_interaction_contact/ ← actor-object lifecycle
    09_force_physics/     ← dynamics fail-closed
    09_evaluation/        ← framework, experimental program, pattern registry
    10_time_rhythm/       ← rhythm metrics, beat syncpoints, timing presets
    12_camera_image_formation/
    16_style_visual_language/
    18_sequence_continuity/ ← occluded/hidden state
    19_generation_complexity/
  runtime/                ← RUNTIME PLANE — director pipeline
    00_request/intent/
    03_retrieval/
    04_synthesis/         ← decision procedure, composition
    05_strategy/constraints/
    06_canonical/         ← control registry, envelopes, scope, temporal
    07_compiler/         ← carrier, semantic mapping, salience budgeting
    08_provider_negotiation/text_fallback/
  evaluation/             ← EVALUATION PLANE — benchmark runs, reference-video distillation
    benchmark_runs/
    reference_video/
  verification/           ← semantic contracts, failure modes
  schemas/world_model/    ← canonical object family + performance event
  research/               ← RESEARCH PLANE
    source_registry/identities/  ← SRC-001, SRC-002
    distillation/ledger/         ← DIST-001, DIST-002
    sources/experiments/         ← carrier-effect, model-conditioning
    gaps/                        ← open questions per source
  providers/              ← provider-specific findings (runway, veo, kling)
```

## 4. Authority hierarchy

Binding priority — apply from the first knowledge object onward:

```text
REUSE > EXTEND > SUPPORT > SPECIALIZE > MERGE > CREATE
```

- **REUSE** — an existing object already covers the meaning; cite it, do not
  duplicate.
- **EXTEND** — add a section or field to an existing canonical owner.
- **SUPPORT** — add evidence or a secondary source to an existing owner.
- **SPECIALIZE** — create a child of an existing owner when the parent is too
  broad.
- **MERGE** — combine two existing objects into one (rare; requires ledger
  note).
- **CREATE** — only when no existing object can absorb the meaning.

## 5. YAML frontmatter schema (canonical)

Every `.md` file under `cpcs/` MUST begin with YAML frontmatter:

```yaml
---
id: cpcs.<domain>.<concept_name>     # dot-separated, snake_case leaf
kind: <kind_value>                    # from controlled vocabulary §6
epistemic_status: <status_value>      # from controlled vocabulary §6
acquisition: <acquisition_value>      # from controlled vocabulary §6
sources: [SRC-001 §N, SRC-002 §N]    # bracket list; system files use [SRC-001]
primary_route: cpcs/<path>/           # must match actual file directory
secondary_routes:                      # optional list
  - cpcs/<other_path>/
interfaces: []                         # cross-department relationships
---
```

### Registration and ledger files

Source registrations use `id: SRC-NNN` (no `cpcs.` prefix).
Distillation ledgers use `id: DIST-NNN`.
These are the only IDs that deviate from the `cpcs.*` convention.

### Optional fields

```yaml
status: <human-readable status>        # e.g., "designed, not executed"
curation_status: proposal              # for schema drafts
```

## 6. Controlled vocabularies

### 6.1 Valid `kind` values

```text
agent_log · catalog · contract · doctrine · experiment_design · fixture_set ·
gap_register · mechanism · method · metric_contract · policy ·
principle · provider_finding · schema_draft · vocabulary
```

New kind values may only be added by updating this reference and the
deviation checker (doctrine D4 — one change, recorded in the doctrine §5).
Do not invent kind values per-card.

### 6.2 Valid `epistemic_status` values

```text
SOURCE_EVIDENCE       directly supported by the supplied source
INFERENCE             logically derived from source evidence but not explicitly stated
CREATIVE_CHOICE       a possible directorial application rather than research fact
PROJECT_DERIVED       a CPCS-created representation or scale
PROVIDER_EXPERIMENT   observed behavior for a specific provider/model/version
UNVERIFIED            requires further confirmation
CONTRADICTED          source evidence conflicts with another admitted claim
UNKNOWN               research does not resolve it
```

### 6.3 Valid `acquisition` values

```text
authored · observed · detected · measured · estimated ·
inferred · derived · interpreted · simulated · creative_choice
```

### 6.4 Valid `id` patterns

| Pattern | Used by | Example |
|---------|---------|---------|
| `cpcs.<domain>.<concept>` | Knowledge cards | `cpcs.facs.intensity_ordinal_contract` |
| `cpcs.<domain>.<sub>.<concept>` | Nested cards | `cpcs.found.numeric.rotation_representation_contract` |
| `SRC-NNN` | Source registrations | `SRC-001`, `SRC-002` |
| `DIST-NNN` | Distillation ledgers | `DIST-001`, `DIST-002` |

- `id` must be unique across the entire `cpcs/` tree.
- Leaf segment must be `snake_case`.
- No dots in leaf segment (dots are separators).

### 6.5 Route naming

- Directories: `snake_case`, numbered prefixes preserved (e.g., `00_foundations`,
  `04_character_performance`).
- Files: `snake_case.md`.
- Interface directories: `domain_x_domain` (e.g., `motion_x_camera`).
- Deprecation preferred over deletion.

## 7. Card bootstrap convention

A knowledge card is a single `.md` file with:

1. YAML frontmatter (§5 schema).
2. A level-1 heading matching the card title.
3. Prose sections with source evidence.
4. Code blocks for YAML/JSON examples.
5. No invented precision — qualitative terms stay qualitative unless the source
   provides calibrated numerics.
6. `epistemic_status` field preserves the evidence boundary — never disguise
   one category as another.

## 8. Source registry

| ID | File | Units | Status |
| --- | --- | --- | --- |
| SRC-001 | `01_AI_VIDEO_MOTION_DIRECTION_KB_GAP_CLOSURE_RESEARCH.md` | 16 (U01–U16) | COMPLETE |
| SRC-002 | `02_FACS_LABAN_BARTENIEFF_GAP_CLOSURE_COMPLETED.md` | 13 (U01–U13) | COMPLETE |
| SRC-003 | `03_MX_HIERARCHICAL_MOTION_GRAMMAR_GAP_CLOSURE_RESEARCH.md` | 8 (U01–U08) | COMPLETE |
| SRC-004 | `04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md` | 14 (U01–U14) | COMPLETE |
| SRC-005 | `04.5-CPCS_MX_Hierarchical_Motion_Grammar_Research_Paper.md` | 28 (U01–U28) | COMPLETE |
| SRC-006 | `05_VIDEO_TEST_TIME_REASONING_GAP_CLOSURE.md` | 21 (U01–U21) | COMPLETE |
| SRC-007 | `06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md` | 17 (U01–U17) | COMPLETE |
| SRC-008 | `CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0` | 28 (U01–U28) | COMPLETE |
| SRC-009 | `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2` + Pegasus v1.0 + Extraction Guide v1.2 | 31 (U01–U31) | COMPLETE |
| SRC-010 | CPCS Prompt Lab (`lab/` + `references/`, 44 files) | 24 (U01–U24) | COMPLETE |
| SRC-011 | `CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0` | 22 files (refs [S001]–[S042]) | COMPLETE |
| SRC-012 | `CPCS_AI_Video_Motion_Direction_KB_v1.0.0` (frozen KB) | 13 (U01–U13, sources [S001]–[S076]) | COMPLETE |

Registrations live at `cpcs/research/source_registry/identities/`.

## 9. Canonical object registry

178 knowledge objects + 5 system files = 183 `cpcs.*` objects (verified by id
scan, 2026-08-09; checker confirms 209 files with frontmatter). Each has a
unique `cpcs.*` ID. The deviation checker validates all IDs. New objects added
during distillation MUST be recorded here. The by-domain table below is an
approximate guide (rows ending in "and N more" are placeholders); the
authoritative census is `cpcs_ontology_check.ps1` + DIRECTORY.md.

### By domain

| Domain | Count | IDs |
| --- | --- | --- |
| foundations | 15 | epistemic_firewall, evidence_two_axis_model, motion_field_separation, rotation_representation_contract, bilateral_side_semantics, causal_event_semantics, relation_vocabulary, simulation_provenance, multimodal_sync, exactness_taxonomy, layer_architecture, timebase_systems, numeric_scale_calibration, and 2 more |
| foundations/epistemic_policy | 1 | cpcs_ethics_and_governance (SRC-009) |
| character_performance/facs | 8 | descriptive_not_emotion, intensity_ordinal_contract, versioning_rule, au_catalog, relation_layer, autodetection_contract, bilateral_asymmetry, temporal_event |
| character_performance/affect + gaze | 2 | vad_trajectory, gaze_body_coupling |
| character_performance (root) | 1 | ugc_realism_reference (SRC-010) |
| body_motion/action_primitives | 3 | action_template, typed_primitive_taxonomy (SRC-003), combat_coding (SRC-005) |
| body_motion/combat | 2 | pegasus_fight_analysis (SRC-009), combat_math_metrics_layer (SRC-010) |
| body_motion/laban | 4 | layering_not_canonical, proxy_measurement_contract, numeric_calibration_contract, reliability_contract |
| body_motion/bartenieff | 1 | six_patterns |
| body_motion/biomechanics | 3 | body_topology_support_bridge, support_state (SRC-003), skeleton_topology (SRC-005) |
| body_motion/coarticulation | 1 | motor_synergy (SRC-003) |
| body_motion/root_motion | 4 | retarget_contract, root_local_motion (SRC-003), superhuman_transform (SRC-005), and 1 more |
| body_motion/phase | 2 | evidence_vs_engineering, phase_timing_presets (SRC-012) |
| body_motion/kinematics | 1 | measurement_contract |
| body_motion (root) | 5 | spatial_state, relative_motion, transition_compatibility, motion_smoothness, controlled_variability (SRC-003) |
| interaction_contact | 2 | interaction_lifecycle, interaction_coupling (SRC-003) |
| objects_affordances | 1 | affordance_constraints (SRC-003) |
| sequence_continuity | 3 | visibility_not_existence, continuity_state (SRC-003), state_variable_catalog (SRC-007) |
| force_physics | 3 | fail_closed_dynamics, noise_sensitivity, momentum_impulse (SRC-003) |
| vfx_secondary_motion | 1 | material_response (SRC-003) |
| camera | 3 | three_layer_semantics, camera_subject_parallax (SRC-003), camera_impact_sync (SRC-012) |
| style | 3 | constraint_model, style_mechanics (SRC-003), anime_sakuga (SRC-005) |
| complexity | 1 | feature_vector |
| observation | 2 | monocular_ambiguity, observation_provenance (SRC-003) |
| time_rhythm | 2 | rhythm_metrics_contract, beat_syncpoint_alignment (SRC-012) |
| evaluation (knowledge/09_evaluation) | 4 | evaluation_framework, cpcs_experimental_program (SRC-009), empirical_pattern_registry, prompt_lab_architecture (SRC-010) |
| runtime/request | 1 | intent_to_control_mapping |
| runtime/retrieval | 2 | agent_retrieval_contract, graph_aware_rag_bundle (SRC-011) |
| runtime/synthesis | 23 | director_decision_procedure, cross_framework_composition, long_form_scheduler (SRC-003), decision_record, execution_edge_vocabulary, decision_aware_routing, state_contraction, causal_design_chain, reasoning_trace (SRC-004), reasoning_atom, continuity_capsule, selective_tree_search, typed_reasoning_graph, bounded_local_search, failure_repair_contract, reasoning_budget_router, state_equivalence_keys, execution_reasoning_state_schema, sceneplan_authority_projection, text_compilation, mx_workflow_recipes (SRC-005/006/007/008), model_scaled_reasoning_policy (SRC-011), adrg_reasoning_graph_schema (SRC-011) |
| runtime/strategy | 5 | applicability_contraindication, observability_conditioned_selection, semantic_guardrails, constraint_feasibility (SRC-003), director_invariant (SRC-004) |
| runtime/canonical | 14 | control_envelopes, control_scope, director_control_ir, generative_realization_layer, temporal_coupling, control_lifetime (SRC-003), motion_realization (SRC-003), canonical_schema, constraint_compilation (SRC-005), temporal_solver_semantics (SRC-007), mx_compiler, mx_roadmap, mx_profiles (SRC-008), typed_merge_algebra (SRC-009) |
| runtime/compiler | 14 | carrier_role_semantics, capability_classes_loss_records, control_priority_attention_budget, risk_profile (SRC-003), semantic_redundancy_compression (SRC-003), format_ownership (SRC-004), interchange_manifests, motion_matching (SRC-005), agent_prompts (SRC-008), structured_prompting_architecture, capability_negotiation_protocol, cross_format_compiler_reference, information_transfer_protocol (SRC-009), kinematic_validation_tooling (SRC-010) |
| runtime/provider | 2 | provider_fallback_ladder, provider_capability_snapshots (SRC-007) |
| verification | 9 | verification_contract, verification_expectation_model, failure_mode_catalog, repair_strategy (SRC-003), verification_layers (SRC-003), measurement_form (SRC-004), verification_metrics (SRC-004), measurement_record_form (SRC-006), observation_contract (SRC-008) |
| schemas | 2 | universal_kernel_family, performance_expression_event |
| governance | 7 | distillation_priority, operational_knowledge_model, reasoning_completeness_score, control_plane_reference, promotion_rules (SRC-004), automation_doctrine, working_agent_log |
| gaps | 13 | src001, src002, src003 (SRC-003), src004 (SRC-004), src005 (SRC-005), src006 (SRC-006), src007 (SRC-007), src008 (SRC-008), src009 (SRC-009), src010 (SRC-010), src011 (SRC-011), src012 (SRC-012), understanding_register |
| research/sources | 2 | rag_ingestion (SRC-005), concept_kitchen (SRC-010) |
| experiments | 5 | carrier_effect_design, src002_model_conditioning, adrg_experiments (SRC-004), cpcs_mx_experiments (SRC-005), benchmark_harness_contract (SRC-007) |
| fixtures | 1 | src002_fixture_set |
| providers | 3 | runway, veo, kling (SRC-001 findings) |
| evaluation/benchmark_runs | 2 | lab_ab_test_protocol, variant_lineage (SRC-010) |
| evaluation/reference_video | 4 | reference_video_distillation, video_observation_graph, extraction_pipeline_stages (SRC-009), lab_runbooks (SRC-010) |

## 10. Rules and policies

| Rule | Location | Scope |
| --- | --- | --- |
| DIRECTORY.md live-sync | `.qoder/rules/directory-md-sync.md` | ALWAYS ON — regenerate after any cpcs/ route change |
| Authority hierarchy | This file §4 | All object creation |
| Epistemic discipline | Operating prompt §6 | All knowledge claims |
| Distillation priority | `00_governance/policies/distillation_implementation_priority.md` | P0/P1/P2 triage |
| Epistemic firewall | `knowledge/00_foundations/invariants/epistemic_firewall.md` | Qualitative→numeric collapses forbidden |
| Outstanding actions | `research/gaps/outstanding_actions.md` | BOOT-CRITICAL — unapplied EXTENDs, open questions, pending sources |
| Evidence model | `knowledge/00_foundations/uncertainty/evidence_two_axis_model.md` | Acquisition × epistemic state |
| Operational knowledge model | `00_governance/policies/operational_knowledge_model.md` | Six strata; no parallel ontologies |
| Reasoning completeness | `00_governance/policies/reasoning_completeness_score.md` | RCS scoring |
| Control plane automation | `00_governance/policies/control_plane_automation_doctrine.md` | Agent-automated governance — decision tree D1–D7; user consulted only on decision briefs (§6) |
| Working agent log | `00_governance/agent_logs/working_agent_log.md` | Session continuity — append an entry after every session/batch (H6); read latest entries on boot |
| Understanding gaps | `research/gaps/understanding_gap_register.md` | Student-gap register — automated capture while working (D8); research-return ingestion (D9) |

## 11. Known boundaries (do not overclaim)

1. **Frozen ZIP packages** — not supplied for SRC-001 or SRC-002; package-level
   claims are not verifiable from supplied files.
2. **FACS 2002 manual** — proprietary/licensed; secondary AU lists must not be
   treated as the manual.
3. **Layer-2 operational objects** — CPCS proposals (`cpcs_proposed` /
   `source_supported_interpretation`), not externally established facts.
4. **Force from monocular video** — estimation under a model, never measurement.
5. **FACS detector output** — `detected ≠ measured`; detector-continuous [0,1]
   ≠ A–E ordinal.
6. **Laban reliability** — weak-to-acceptable (Krippendorff α); CMA proxy without
   calibration forbidden.
7. **No carrier superiority** — no representation format is universally
   superior; experiment required.
8. **No parallel ontologies** — operational layer extends existing routes; do
   not create a parallel "FACS runtime" or "Laban runtime".

## 12. Session continuity checklist

A new session or agent MUST perform these steps before operating on the tree:

1. **Read this file** (`cpcs/00_governance/policies/control_plane_reference.md`).
2. **Read the automation doctrine** (`cpcs/00_governance/policies/control_plane_automation_doctrine.md`)
   — resolves governance decisions without user consultation; raise a brief
   only on the §6 triggers.
3. **Read the working agent log** (`00_governance/agent_logs/working_agent_log.md`)
   — what previous sessions did, what is in flight, what to pick up; and the
   **understanding gap register** (`research/gaps/understanding_gap_register.md`)
   — open student gaps awaiting research (take one on if the user asks).
4. **Read the operating prompt** (`CPCS Research Distillation Agent — Persistent
   Operating Prompt.md`).
5. **Check DIRECTORY.md** (workspace root) — confirms current route tree.
6. **Run the deviation checker**: `pwsh -NoProfile -File .\cpcs_ontology_check.ps1`
   — confirms the tree is clean before any work begins (doctrine D3).
7. **Check the distillation queue** (§14 below) — identifies the next source.
8. **Read the most recent ledger** (`cpcs/research/distillation/ledger/`) —
   captures the last completed distillation's PASS outputs.
9. **Read the outstanding actions tracker** (`research/gaps/outstanding_actions.md`)
   — identifies unapplied EXTENDs, open research questions, and cross-source
   dependencies that need action.
10. **Verify no orphan files** — every `.md` under `cpcs/` should have valid
   frontmatter and a known ID in §9.

## 13. Distillation workflow (summary)

Full workflow defined in the operating prompt (PASS 0–11):

```text
PASS 0  — read full source
PASS 1  — source identity + structural map
PASS 2  — existing-knowledge search (REUSE/EXTEND candidates)
PASS 3  — semantic extraction
PASS 4  — numerical extraction
PASS 5  — representation/compiler extraction
PASS 6  — interface extraction
PASS 7  — contradictions/boundaries
PASS 8  — placement (primary_route assignment)
PASS 9  — dedup (against existing canonical owners)
PASS 10 — operationalization (compiler/verification implications)
PASS 11 — coverage audit (every section dispositioned)
```

Output: structured A–L report ending with `SOURCE DISTILLATION COMPLETE`.

Then:
- Write source registration → `research/source_registry/identities/`
- Write knowledge cards → primary routes
- Write distillation ledger → `research/distillation/ledger/`
- Write gaps → `research/gaps/`
- Write experiments → `research/sources/experiments/`
- Regenerate DIRECTORY.md → `pwsh -NoProfile -File .\update_directory_md.ps1`
- Run ontology check → `pwsh -NoProfile -File .\cpcs_ontology_check.ps1`
- Update this control plane reference (§2 state, §8 registry, §9 objects, §14 queue)
- Apply housekeeping H1–H7 (automation doctrine §4) in order H5 → H1 → H2 → H3 → H4 → H6 → H7
- Record every governance decision in the automation doctrine §5 applied-decisions
  register (rule + status) — no decision is taken silently

## 14. Distillation queue

Distillation queue — sources in `Research_distillation_folder/` (6 pending):

| # | File | Lines | Status |
| --- | --- | --- | --- |
| 03 | `03_MX_HIERARCHICAL_MOTION_GRAMMAR_GAP_CLOSURE_RESEARCH.md` | 4,405 | COMPLETE |
| 04 | `04.5-CPCS_MX_Hierarchical_Motion_Grammar_Research_Paper.md` | 4,181 | COMPLETE |
| 04b | `04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE.md` | 4,668 | PENDING |
| 04c | `04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md` | 2,208 | COMPLETE |
| 05 | `05_VIDEO_TEST_TIME_REASONING_GAP_CLOSURE.md` | 2,168 | COMPLETE |
| 06 | `06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md` | 538 | COMPLETE |
| 07 | `07 CPCS World Model _ Causal State _ Attention Gap Closure.md` | 676 | PENDING |
| 08 | `15-kinetic_motion_direction_prompting_manual.md` | 2,479 | PENDING |
| 09 | `Continous Combat State.md` | 1,834 | PENDING |
| 10 | `Granular Motion Control for AI Video Generation.md` | 1,978 | PENDING |
| 11 | `Polyglot Compiler.md` | 532 | PENDING |

> When a source is distilled, mark its row COMPLETE, update §2 counts, add
> objects to §9, and regenerate DIRECTORY.md + run the ontology checker.

This queue is reconciled with `outstanding_actions.md` §3 — both list the same
6 PENDING sources. Candidate outside this queue: the DMR execution kit
(`director_motion_reasoning_execution_kit`) is an SRC-013 candidate pending an
overlap audit against SRC-007 before distillation (decision
D-2026-08-09-04).

## 15. Automation doctrine

`control_plane_automation_doctrine.md` (same directory) governs HOW this
reference is maintained: the control plane is agent-automated. A new session
resolves every governance decision through its decision tree D1–D7 (source
intake, placement, vocabulary conformance, vocabulary extension, preset/delta
conflicts, open questions, error handling) and records outcomes in its §5
applied-decisions register. The user is consulted only on the five decision-brief
triggers (§6 of the doctrine). When the operating prompt and the doctrine
conflict on decision-making, the doctrine wins and the difference is recorded.

## 16. Understanding gaps and agent continuity

Two files complete the boot set:

- `00_governance/agent_logs/working_agent_log.md` — append-only session
  journal (doctrine H6). New sessions read the latest entries to pick up
  open threads; entries link decisions (doctrine §5) and gaps (UG ids).
- `research/gaps/understanding_gap_register.md` — the automated student-gap
  register (doctrine D8): WHAT/WHY/HOW/WHEN/APPLY/BLEND gaps captured while
  working, nested for research alignment. The user performs deep research on
  open UG ids and returns it (chat or `Research_return_folder/`); the agent
  ingests it per D9 and closes/refines the gap with evidence.
