---
id: cpcs.gaps.outstanding_actions
kind: gap_register
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012]
primary_route: cpcs/research/gaps/
---

# Outstanding Actions Tracker

> **BOOT-CRITICAL FILE.** A new session or agent MUST read this file to know what
> work remains. The DIST ledgers are audit trails (what was planned); this file
> is the action tracker (what has been executed and what hasn't). Update this
> file every time an EXTEND is applied, a gap is closed, or a source is
> distilled.

## 1. Unapplied EXTENDs

EXTENDs are documented in DIST ledgers but not all have been applied to the
target card files. Status is tracked here so a new agent can see the state at
a glance.

### SRC-003 EXTENDs (18 total)

| # | Target file | SRC-003 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/06_canonical/field_policies/control_scope.md` | MX-specific scope dimensions (body_region, interaction, action, phase) | PENDING |
| E2 | `runtime/06_canonical/control_envelopes.md` | MX envelope types; temporal phase shaping | PENDING |
| E3 | `runtime/07_compiler/salience_budgeting/control_priority_attention_budget.md` | Hardness levels (already present from SRC-002); conflict records; precedence chain | PARTIAL — hardness levels present, conflict records + precedence chain pending |
| E4 | `verification/semantic/verification_expectation_model.md` | MX verification expectations with experimental thresholds | PENDING |
| E5 | `verification/failures/failure_mode_catalog.md` | MX failure signatures (foot_slide, identity_swap, body_penetration, water_effect_detached, whole_clip_fast, left_right_swap) | PENDING |
| E6 | `knowledge/00_foundations/uncertainty/evidence_two_axis_model.md` | Orthogonality: 4 dimensions (knowledge basis x acquisition x epistemic state x confidence), not 1 enum | PENDING — SRC-004 E6 added ADRG evidence classes to this file, but the 4-dimension orthogonality expansion is NOT applied |
| E7 | `knowledge/18_sequence_continuity/occluded_hidden_state/visibility_not_existence.md` | Visibility constraints, line-of-sight as control constraint, uncertainty-aware hidden-state | PENDING |
| E8 | `knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md` | ContactStateMachine (approach->near->onset->sustained->slip/roll/stick->release->separation); stick/slip; semantic/geometric split | PENDING |
| E9 | `runtime/06_canonical/control_registry/generative_realization_layer.md` | MotionRealization with observable/mechanical/hidden target split; action-conditioned mapping | PENDING — SRC-003 created new `motion_realization.md` in same directory; E9 is a cross-reference/bridge into the existing file |
| E10 | `knowledge/06_body_motion/biomechanics/body_topology_support_bridge.md` | SupportState with COM/BOS/COP/ground_reaction; dynamic balance state; surface/friction | PENDING — SRC-003 created new `support/support_state.md` in same directory; E10 is a cross-reference/bridge |
| E11 | `knowledge/00_foundations/causality/causal_event_semantics.md` | Contact outcome -> reaction causality; event preconditions/postconditions/failure outcomes | PENDING — SRC-004 E4 added design causality to this file, but contact outcome causality is NOT applied |
| E12 | `runtime/07_compiler/carrier_planner/carrier_role_semantics.md` | ControlCarrier (16 non-text carriers); carrier selection as semantic decision | PENDING |
| E13 | `runtime/08_provider_negotiation/text_fallback/provider_fallback_ladder.md` | MX-specific 8-rung fallback strategy | PENDING |
| E14 | `runtime/04_synthesis/director_decision_procedure.md` | ControlDecision provenance; abstention outcomes | APPLIED — SRC-004 E1 applied the same content (DecisionRecord provenance + abstention) |
| E15 | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | Provider reliability distinction (supported vs dependably supported); empirical reliability matrix | PENDING — SRC-004 E7 added realization statuses + compile loss->decision linkage to this file, but provider reliability distinction is NOT applied |
| E16 | `runtime/06_canonical/temporal_tracks/temporal_coupling.md` | Coupled timing/relative phase; timing profiles distinct from duration | APPLIED — SRC-012 E1 applied the same content (master clock doctrine, relative phase/phase lock, sync vocabulary) |
| E17 | `knowledge/00_foundations/invariants/bilateral_side_semantics.md` | Symmetry/asymmetry modes; laterality semantics | PENDING |
| E18 | `knowledge/06_body_motion/phase_grammar/evidence_vs_engineering_phases.md` | Motion phase organizations (narrative/action/kinematic distinction) | APPLIED — SRC-012 E2 applied the same content (seven-phase production grammar + BML sync-point mapping) |

**Summary: 14 PENDING + 1 PARTIAL + 3 APPLIED = 18 total**

### SRC-004 EXTENDs (8 total — ALL APPLIED)

| # | Target file | SRC-004 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/04_synthesis/director_decision_procedure.md` | DecisionRecord provenance; abstention outcomes | APPLIED |
| E2 | `verification/repair_strategy.md` | JSON Patch repair (RFC 6902); base_digest; cause_candidates; repair algorithm; escalation policy; repair bound | APPLIED |
| E3 | `verification/verification_layers.md` | 4-level verification separation; planner metrics cross-ref | APPLIED |
| E4 | `knowledge/00_foundations/causality/causal_event_semantics.md` | design_causes vs causal_claim distinction; causal design chain | APPLIED |
| E5 | `knowledge/00_foundations/invariants/epistemic_firewall.md` | Structured-output caution (parse != schema != decision != render) | APPLIED |
| E6 | `knowledge/00_foundations/uncertainty/evidence_two_axis_model.md` | ADRG evidence classes (PACKAGE_ESTABLISHED, REPO_OBSERVED, etc.) | APPLIED |
| E7 | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | Realization statuses (8); compile loss -> decision linkage | APPLIED |
| E8 | `runtime/07_compiler/salience_budgeting/control_priority_attention_budget.md` | Decision-aware routing features (impact/uncertainty/coupling/irreversibility/validator_strength) | APPLIED |

### SRC-005 EXTENDs (6 total — ALL APPLIED)

| # | Target file | SRC-005 additions | Status |
| --- | --- | --- | --- |
| E1 | `knowledge/00_foundations/uncertainty/evidence_two_axis_model.md` | 7 CPCS-MX evidence classes; 6 research-status labels; provenance/conflict resolution | APPLIED |
| E2 | `knowledge/00_foundations/numerical_representation/motion_field_separation.md` | Primary vs derived tracks; authority order | APPLIED |
| E3 | `knowledge/00_foundations/causality/causal_event_semantics.md` | Action graph edges (before/overlaps/causes/requires/targets/interrupts); typed contact taxonomy | APPLIED |
| E4 | `knowledge/16_style_visual_language/style_mechanics.md` | Style transform vector; 5 profiles; cross-style invariants | APPLIED |
| E5 | `verification/verification_layers.md` | 8 verification metric vectors; layer-localized error diagnosis | APPLIED |
| E6 | `knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md` | 8-type contact taxonomy; contact record fields; fight-shot causal bundle | APPLIED |

### SRC-006 EXTENDs (3 total — ALL APPLIED)

| # | Target file | SRC-006 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | Compiler semantics: temporal_precision_unenforceable; compile_key; provider outputs never overwrite; loss reported in feasibility | APPLIED |
| E2 | `research/sources/experiments/carrier_effect_experiment_design.md` | Representation policy; controlled carrier experiment (IVs, controls, 13 outcomes) | APPLIED |
| E3 | `research/sources/experiments/adrg_experiments.md` | F1–F14 fixtures; 7 exact mode implementations; budget tiers B0–B3; randomization; 6 adoption criteria | APPLIED |

### SRC-007 EXTENDs (6 total — ALL APPLIED)

| # | Target file | SRC-007 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/05_strategy/constraints/constraint_feasibility.md` | 5 typed outcomes; 9 checks; unknown-prerequisite ordering rule | APPLIED |
| E2 | `knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md` | 9-stage lifecycle; event/relation/derived classification | APPLIED |
| E3 | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | Exactly-once accounting; 6 terminal dispositions; 5 invariants | APPLIED |
| E4 | `verification/measurement_record_form.md` | Target/observation join contract; 4 confidence layers; 4 required exemplars | APPLIED |
| E5 | `runtime/04_synthesis/failure_repair_contract.md` | Diagnosis as ranked, evidence-linked hypotheses | APPLIED |
| E6 | `research/sources/experiments/carrier_effect_experiment_design.md` | Format boundary doctrine; meaning_id across variants | APPLIED |

### SRC-008 EXTENDs (4 total — ALL APPLIED)

| # | Target file | SRC-008 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/06_canonical/canonical_schema_design.md` | Concrete field catalog (20 top-level fields); 4 authority values; authoring→canonical mapping | APPLIED |
| E2 | `runtime/06_canonical/constraint_resolution_compilation.md` | Reference implementation contract: deep merge, ID-based list matching, profile URI resolution, 4 exit codes | APPLIED |
| E3 | `research/sources/rag_ingestion_architecture.md` | RAG record schema (10 record types, sha256 verification, evidence_labels preservation) | APPLIED |
| E4 | `runtime/04_synthesis/text_to_score_compilation.md` | Agent prompt contract: 4 prompts (text-to-structure, verifier, style-transfer, XML envelope) | APPLIED |

### SRC-009 EXTENDs (5 total — ALL APPLIED)

| # | Target file | SRC-009 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/06_canonical/canonical_schema_design.md` | v1.2 schema fields: VOG schema, cross-format canonical fields, style domain registry, observation record contract | APPLIED |
| E2 | `runtime/06_canonical/constraint_resolution_compilation.md` | Typed merge algebra: 10 data kinds, 9 merge policies, candidate resolution tuple, authority precedence | APPLIED |
| E3 | `knowledge/00_foundations/uncertainty/evidence_two_axis_model.md` | VOG 5 evidence classes; confidence fusion 5 rules; precedence chains | APPLIED |
| E4 | `verification/observation_record_contract.md` | VOG observation schema: clock required, evidence array, extractor parameters_digest, contradiction records | APPLIED |
| E5 | `research/sources/rag_ingestion_architecture.md` | v1.2 RAG corpus structure: 179 records, document + paper_chunk types, 10 record types, 4 new types | APPLIED |

### SRC-010 EXTENDs (6 total — ALL APPLIED)

| # | Target file | SRC-010 additions | Status |
| --- | --- | --- | --- |
| E1 | `knowledge/06_body_motion/action_primitives/combat_action_coding.md` | Combat math metrics layer: two-document architecture, frame budget identity, 4-phase ratios, per-beat kinematics, contact geometry tolerance, 10 constraints, camera math | APPLIED |
| E2 | `knowledge/04_character_performance/facs/facs_au_catalog.md` | UGC + combat usage patterns: intensity B–C vs C–E, genuine/fake combos, 8 AU fight combos, plastic-skin failure note | APPLIED |
| E3 | `knowledge/06_body_motion/laban_bess/laban_numeric_calibration_contract.md` | Combat float encoding as typed proxies (weight/time/space 0–1, flow −1–1, 9 Effort signatures); v005 lab_control render-validated as control channel | APPLIED |
| E4 | `knowledge/12_camera_image_formation/camera_three_layer_semantics.md` | Fight camera math: 7 parameters (focal_length_mm, shake_frequency_hz 8–15, whip_pan_speed_deg_s 120–240), patterns by beat type | APPLIED |
| E5 | `knowledge/16_style_visual_language/anime_sakuga_representation.md` | Combat style notes: shonen/wuxia/MMA/superhero parameterization, naruto worked example | APPLIED |
| E6 | `knowledge/09_evaluation/evaluation_framework.md` | Lab scorecard as empirical instantiation: 4 manual dims vs 6 families, hard-gate analog (v006 0 failures), ablation analog, honesty gap | APPLIED |

### SRC-011 EXTENDs (7 total — ALL APPLIED)

| # | Target file | SRC-011 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/04_synthesis/decision_record.md` | Decision-ledger doctrine: 3 risks of raw CoT (false provenance, retrieval contamination, token/privacy overhead); what may be retained; compact ledger form | APPLIED |
| E2 | `runtime/04_synthesis/decision_aware_routing.md` | Weighted router D = w_I·I + w_U·U + w_C·C + w_R·R − w_V·V; 6 operator rules; 5 branch-admission conditions; 6 early-pruning conditions; 100-unit budget ledger; escalation record | APPLIED |
| E3 | `runtime/05_strategy/constraints/director_invariant.md` | Variant lattice: incompatibilities, maximum_simultaneous_deltas 2, J(S) diversity selection, prompt-vs-shot optimization, model-scaled variant counts | APPLIED |
| E4 | `runtime/07_compiler/format_ownership.md` | Per-format contracts: NL director-language pattern + 8-step compression; YAML 9 safety rules; JSON 4 validation levels + constrained generation; XML envelope/namespaces/security | APPLIED |
| E5 | `runtime/07_compiler/cross_format_compiler_reference.md` | Polyglot compiler: carrier ownership table, one-authority rule, 3 valid dual-format patterns, direct multi-format = text_interpretation_only, 15 cross-format passes | APPLIED |
| E6 | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | Compile-loss ledger entry (control_id/decision_id/status/retained/lost/verification); 3 verifier roles; checkpoints A–I; bounded repair empty-patch escalation | APPLIED |
| E7 | `research/sources/experiments/adrg_experiments.md` | Package experimental program: 7 RQs, factors, causal discipline, ADRG-PKG-E1..E5 (renamed to avoid E-ADRG collision), collision mapping table, 5 promotion criteria | APPLIED |

### SRC-012 EXTENDs (6 total — ALL APPLIED)

| # | Target file | SRC-012 additions | Status |
| --- | --- | --- | --- |
| E1 | `runtime/06_canonical/temporal_tracks/temporal_coupling.md` | Master clock doctrine (seconds authoritative; frame/musical grid derived); timing profiles vs durations; relative phase/phase lock; sync vocabulary — also fulfills SRC-003 E16 | APPLIED |
| E2 | `knowledge/06_body_motion/phase_grammar/evidence_vs_engineering_phases.md` | Seven-phase production grammar; map_phase_bml_v1 BML projection; optionality; role-based stroke — also fulfills SRC-003 E18 | APPLIED |
| E3 | `knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md` | ~40-predicate vocabulary; predicate record (phase_links); contact topology modes (stick/slide/roll/impact/separate); two-person sync patterns; timing metrics | APPLIED |
| E4 | `knowledge/06_body_motion/bartenieff/bartenieff_six_patterns.md` | Basic Six vs patterns separation; primitive encoding (sequencing_delay_ms 55); composition table; 5 compiler ops | APPLIED |
| E5 | `knowledge/05_action/combat/combat_math_metrics_layer.md` | Impact decomposition (4 stages); force production priors; measurement-status precedence; 4-phase ↔ 7-phase mapping; strike rhythm alignment | APPLIED |
| E6 | `runtime/08_provider_negotiation/provider_capability_snapshots.md` | 7-status vocabulary; dated model matrix (2026-07-30); canonical downcasting; adapter contract fields; loss report | APPLIED |

### Files with EXTENDs from multiple sources

| File | SRC-003 | SRC-004 | SRC-005 | SRC-006 | SRC-007 | SRC-009 | SRC-010 | SRC-011 | SRC-012 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `director_decision_procedure.md` | E14 (APPLIED via SRC-004 E1) | E1 (APPLIED) | — | — | — | — | — | — | — |
| `control_priority_attention_budget.md` | E3 (PARTIAL) | E8 (APPLIED) | — | — | — | — | — | — | — |
| `evidence_two_axis_model.md` | E6 (PENDING) | E6 (APPLIED) | E1 (APPLIED) | — | — | E3 (APPLIED) | — | — | — |
| `causal_event_semantics.md` | E11 (PENDING) | E4 (APPLIED) | E3 (APPLIED) | — | — | — | — | — | — |
| `capability_classes_and_loss_records.md` | E15 (PENDING) | E7 (APPLIED) | — | E1 (APPLIED) | E3 (APPLIED) | — | — | E6 (APPLIED) | — |
| `interaction_lifecycle.md` | E8 (PENDING) | — | E6 (APPLIED) | — | E2 (APPLIED) | — | — | — | E3 (APPLIED) |
| `carrier_effect_experiment_design.md` | — | — | — | E2 (APPLIED) | E6 (APPLIED) | — | — | — | — |
| `combat_action_coding.md` | — | — | base (§17) | — | — | — | E1 (APPLIED) | — | — |
| `facs_au_catalog.md` | — | — | — | — | — | — | E2 (APPLIED) | — | — |
| `laban_numeric_calibration_contract.md` | — | — | — | — | — | — | E3 (APPLIED) | — | — |
| `camera_three_layer_semantics.md` | — | — | — | — | — | — | E4 (APPLIED) | — | — |
| `anime_sakuga_representation.md` | — | — | base (§18) | — | — | — | E5 (APPLIED) | — | — |
| `evaluation_framework.md` | — | — | — | — | — | base (§24) | E6 (APPLIED) | — | — |
| `decision_record.md` | — | base | — | — | — | — | — | E1 (APPLIED) | — |
| `decision_aware_routing.md` | — | base | — | — | — | — | — | E2 (APPLIED) | — |
| `director_invariant.md` | — | base | — | — | — | — | — | E3 (APPLIED) | — |
| `format_ownership.md` | — | base | — | — | — | — | — | E4 (APPLIED) | — |
| `cross_format_compiler_reference.md` | — | — | — | — | — | base (App G) | — | E5 (APPLIED) | — |
| `adrg_experiments.md` | — | base | — | E3 (APPLIED) | — | — | — | E7 (APPLIED) | — |
| `temporal_coupling.md` | E16 (APPLIED via SRC-012 E1) | — | — | — | — | — | — | — | E1 (APPLIED) |
| `evidence_vs_engineering_phases.md` | E18 (APPLIED via SRC-012 E2) | — | — | — | — | — | — | — | E2 (APPLIED) |
| `bartenieff_six_patterns.md` | — | — | — | — | — | — | — | — | E4 (APPLIED) |
| `combat_math_metrics_layer.md` | — | — | — | — | — | — | base (SRC-010-U21) | — | E5 (APPLIED) |
| `provider_capability_snapshots.md` | — | — | — | — | base (G007/G008/G021) | — | — | — | E6 (APPLIED) |

## 2. Open Research Questions (consolidated across all sources)

155 open questions across 12 sources. None carries a closed answer. All require
experiments, fixtures, or provider evaluations before becoming hard CPCS rules.
Full detail per source: `src005_open_research_questions.md`,
`src006_open_research_questions.md`, `src007_dmr_runtime_gaps.md`,
`src008_open_research_questions.md`, `src009_open_research_questions.md`,
`src010_open_research_questions.md`, `src011_open_research_questions.md`,
`src012_open_research_questions.md`.

### SRC-001 (14 questions)

| # | Question | Priority | Cross-source link |
| --- | --- | --- | --- |
| 1 | What phase boundaries are reproducible across annotators? | P0 | SRC-003 phase grammar (E18) |
| 2 | Which motion quantities justify schema complexity? | P0 | SRC-004 Q3 (DecisionRecord cost) |
| 3 | Which kinematic controls survive provider compilation? | P1 | SRC-002 Q10, SRC-004 Q4 |
| 4 | Which camera controls are native vs prompt-sensitive per provider? | P1 | SRC-002 Q2, SRC-004 Q4 |
| 5 | Can complexity features predict generation failures? | P2 | SRC-003 Q6 (control density) |
| 6 | Does carrier choice change motion adherence? | P2 | SRC-003 Q5, SRC-004 E-ADRG-006, Q7 |
| 7 | What is the minimum useful style invariant vocabulary? | P1 | SRC-003 style_mechanics |
| 8 | Which force/dynamics estimates are reliable for VOG evidence? | P1 | SRC-003 momentum_impulse |
| 9 | What calibration is needed for a scalar complexity score? | P2 | SRC-001 Q5 |
| 10 | How to represent uncertainty with multiple 3D pose hypotheses? | P1 | SRC-003 observation_provenance |
| 11 | Which continuity constraints reduce identity/teleport failures? | P0 | SRC-003 Q7 |
| 12 | Which occlusion types require visibility bridges? | P1 | SRC-003 E7 |
| 13 | Can causal-event constraints improve generation? | P2 | SRC-003 E11, SRC-004 causal_design_chain |
| 14 | Which continuity failures need compiler decomposition? | P2 | SRC-003 Q7 (shot decomposition) |

### SRC-002 (25 questions — Layer 1: 10, Layer 2: 15)

| # | Question | Layer | Priority | Cross-source link |
| --- | --- | --- | --- | --- |
| L1-1 | Which FACS AU subset: native vs semantic projection? | 1 | P1 | SRC-004 Q4 |
| L1-2 | Which providers honor AU identifiers? | 1 | P1 | SRC-001 Q4 |
| L1-3 | Which providers preserve bilateral/asymmetric? | 1 | P1 | SRC-003 E17 |
| L1-4 | Provider response to ordinal vs NL intensity? | 1 | P1 | — |
| L1-5 | Can Laban proxy features predict CMA labels? | 1 | P2 | — |
| L1-6 | Which Bartenieff patterns detectable from monocular? | 1 | P2 | SRC-001 Q10 |
| L1-7 | How to estimate breath without audio? | 1 | P2 | — |
| L1-8 | Which temporal carrier yields highest adherence? | 1 | P2 | SRC-001 Q6, SRC-004 Q7 |
| L1-9 | How much FACS/Laban/Bartenieff structure improves output? | 1 | P2 | SRC-004 Q3 |
| L1-10 | Minimum controls per provider profile? | 1 | P1 | SRC-001 Q3 |
| L2-1 | FACS temporal tolerance windows across frame rates? | 2 | P2 | SRC-003 temporal precision |
| L2-2 | Which AU detectors sufficiently calibrated? | 2 | P2 | — |
| L2-3 | Project-normalized FACS intensity across subjects? | 2 | P2 | — |
| L2-4 | Which Laban qualities have measurable proxies? | 2 | P2 | SRC-003 Q4 |
| L2-5 | Which Laban-to-kinematic mappings generalize? | 2 | P2 | — |
| L2-6 | Which Bartenieff patterns reliably classified? | 2 | P2 | SRC-002 L1-6 |
| L2-7 | Which cross-framework interactions are research vs hypotheses? | 2 | P2 | — |
| L2-8 | How much do realization primitives improve adherence? | 2 | P2 | SRC-003 MotionRealization |
| L2-9 | How much semantic compression before adherence degrades? | 2 | P2 | SRC-003 semantic_redundancy_compression, SRC-004 Q2 |
| L2-10 | What attention budget maximizes adherence per model? | 2 | P2 | SRC-003 Q6, SRC-004 E8 |
| L2-11 | Which shot-scale observability heuristics generalize? | 2 | P2 | — |
| L2-12 | Can verification detect Laban adherence automatically? | 2 | P2 | SRC-003 verification_layers |
| L2-13 | Which continuity constraints measurable from VOG? | 2 | P2 | SRC-001 Q11 |
| L2-14 | Actor-to-actor temporal: causal vs authored? | 2 | P2 | SRC-003 E11, SRC-004 causal_design_chain |
| L2-15 | How should stylized/anime modify realization? | 2 | P2 | SRC-003 style_mechanics |

### SRC-003 (10 questions)

| # | Question | Cross-source link |
| --- | --- | --- |
| 1 | Which primitive decompositions produce most consistent provider motion? | SRC-002 L1-9 |
| 2 | Which action-conditioned realization features improve video adherence? | SRC-002 L2-8 |
| 3 | What contact distance/velocity thresholds distinguish convincing contact? | SRC-004 verification_metrics |
| 4 | Which support metrics correlate with perceived physical grounding? | SRC-003 support_state |
| 5 | Which carriers best preserve trajectory vs identity vs interaction? | SRC-001 Q6, SRC-004 E-ADRG-006 |
| 6 | What control density causes provider degradation? | SRC-001 Q5, SRC-004 Q2 |
| 7 | When does shot decomposition improve vs reduce continuity? | SRC-001 Q14, SRC-001 Q11 |
| 8 | Which semantic redundancy rules improve adherence? | SRC-002 L2-9 |
| 9 | What retargeting errors are perceptually acceptable? | SRC-004 Q4 |
| 10 | What provider-specific temporal precision is real vs nominal? | SRC-002 L2-1 |

### SRC-004 (10 questions)

| # | Question | Cross-source link |
| --- | --- | --- |
| 1 | Numeric thresholds for impact/uncertainty/coupling? | SRC-003 Q6 |
| 2 | How much state contraction before quality degrades? | SRC-003 Q6, SRC-002 L2-9 |
| 3 | Does DecisionRecord improve compile success enough for cost? | SRC-001 Q2 |
| 4 | Which providers preserve which controls natively? | SRC-001 Q3, Q4, SRC-002 L1-2 |
| 5 | Which variant-distance metric correlates with creative diversity? | SRC-003 controlled_variability |
| 6 | When does self-consistency outperform deterministic validator? | — |
| 7 | Which carrier best preserves semantic under equal tokens? | SRC-001 Q6, SRC-003 Q5 |
| 8 | Which failures attributable to planning vs compilation vs provider? | SRC-003 failure signatures |
| 9 | What evidence threshold promotes reasoning into durable knowledge? | SRC-001 Q1, promotion_rules |
| 10 | How should human overrides interact with soft scores? | — |

### SRC-005 (10 questions)

| # | Question | Priority |
| --- | --- | --- |
| 1 | Does explicit phase and contact coding improve temporal compliance over text-only prompting? | P0 |
| 2 | Do Laban and mannerism layers improve perceived specificity without reducing action correctness? | P1 |
| 3 | Does separating anatomical motion from stylized deformation reduce rig failures in superhuman clips? | P1 |
| 4 | Do dense pose controls outperform key poses for fight-scene contact timing? | P1 |
| 5 | Does a canonical score improve choreography transfer across characters and morphologies? | P2 |
| 6 | Does re-extraction enable targeted correction with fewer full regenerations? | P1 |
| 7 | Which fields remain unsupported by current generation adapters? | P1 |
| 8 | Targeted director questions vs named batch defaults for ambiguity resolution? | P2 |
| 9 | What phase-labeled smoothness thresholds distinguish intended discontinuity from artifact? | P1 |
| 10 | What calibration produces predictive Laban proxy profiles without collapsing concepts? | P1 |

### SRC-006 (10 questions + 7 future items + 6 hypotheses)

| # | Question | Priority |
| --- | --- | --- |
| 1 | Which CPCS files own executor-state, capsule, branch, graph, failure, repair, budget, equivalence semantics? | P0 |
| 2 | Which executors are genuinely distinct policies vs duplicated prompt wrappers? | P1 |
| 3 | What minimal capsule passes long-horizon continuation-equivalence tests? | P0 |
| 4 | Which task features predict benefit from branching, graph aggregation, or repair? | P1 |
| 5 | Which provider controls are exact, approximate, semantic, or unsupported by version? | P0 |
| 6 | Which automatic verifiers are calibrated against CPCS human judgments? | P0 |
| 7 | What materiality tolerances are valid for time, camera, motion, space, audio? | P1 |
| 8 | When does verifier uncertainty make further search wasteful? | P1 |
| 9 | Does any format advantage replicate per model/provider profile? | P1 |
| 10 | Can repair improve the failed requirement without protected-invariant regressions? | P0 |

Future research (§13.5): calibrated difficulty/solvability models · provider-specific
control reliability · causal and physical verification beyond semantic VLM judgment ·
uncertainty propagation from VOG into repair decisions · long-horizon capsule
sufficiency · human preference models preserving domain/cultural specificity · active
selection of when human review is worth its cost.

Experiment-only hypotheses (§13.3): AoT prompting improves planning at lower call
count · graph aggregation outperforms a single structured Director pass · a specific
carrier improves a specific model/provider profile · viewer-guidance modeling improves
camera/edit adherence · learned complexity estimates outperform deterministic triggers
· more test-time renders monotonically improve CPCS outcomes.

### SRC-007 (19 gaps — G010/G018/G022 undefined in prompt)

| Gap | Domain | Status | Distilled to |
| --- | --- | --- | --- |
| G001 | Canonical ScenePlan reconciliation | requires_experiment | sceneplan_authority_projection |
| G002 | Temporal solver (Allen/STN/STNU) | requires_experiment | temporal_solver_semantics |
| G003/G004 | Action preconditions/effects, persistent state | implementable_now | state_variable_catalog |
| G005 | Typed contact lifecycle | implementable_now | interaction_lifecycle EXTEND |
| G006 | Feasibility validator | implementable_now | constraint_feasibility EXTEND |
| G007/G008 | Provider contracts and adapters | unknown (needs docs) | provider_capability_snapshots |
| G009 | Exactly-once compilation-loss report | implementable_now | capability_classes_and_loss_records EXTEND |
| G010 | **undefined in prompt** | unknown | recover from register |
| G011–G013 | Measurement stack and evaluator | requires_experiment | measurement_record_form EXTEND |
| G014/G015 | Failure taxonomy and minimal patch | implementable_now | failure_repair_contract EXTEND |
| G016/G017 | Benchmark and experiment harness | requires_experiment | benchmark_harness_contract |
| G018 | **undefined in prompt** | unknown | recover from register |
| G019 | Format doctrine | requires_experiment | carrier_effect_experiment_design EXTEND |
| G020 | FACS/Laban scale calibration | requires_experiment | numeric_scale_calibration |
| G021 | Provider lifecycle | implementable_now | provider_capability_snapshots |
| G022 | **undefined in prompt** | unknown | recover from register |

### SRC-008 (10 questions)

| # | Question | Category |
| --- | --- | --- |
| 1 | Does the reference compiler pass all 4 example YAMLs through authoring validation, profile resolution, canonical validation, with zero unresolved items? | Implementation |
| 2 | Does `validate_cpcs_mx_package.py` pass on the shipped package without warnings? | Implementation |
| 3 | Do compiled JSON examples round-trip independently against the canonical schema? | Implementation |
| 4 | Are the 80 source references [S001]–[S080] all reachable at their listed URLs? | Link rot |
| 5 | Do the observation schema's 7 evidence classes align with SRC-006 measurement_record_form taxonomy? | Cross-source |
| 6 | Should the RAG schema's 10 record types be adopted as canonical across all sources? | Cross-source |
| 7 | What additional profiles are needed for SRC-006 reasoning scenarios or SRC-007 DMR runtime? | Cross-source |
| 8 | How should the compiler's capability_report format change when production adapters are built? | Cross-source |
| 9 | Should the DMR execution kit be distilled as SRC-009 or is it subsumed by SRC-007? | Package completeness — RESOLVED: SRC-009 is the papers + extraction package |
| 10 | Should the Failure-Aware package be distilled as its own source? | Package completeness |

### SRC-009 (15 questions)

| # | Question | Category |
| --- | --- | --- |
| 1 | Does the reference pipeline pass all 4 commands (probe, prepare, init-record, validate) on a test video? | Implementation |
| 2 | Does `validate_video_observation_graph.py` pass on the shipped example graph? | Implementation |
| 3 | Does `merge_video_observations.py` produce a valid VOG from example observations? | Implementation |
| 4 | Are the 92 source references [S001]–[S092] all reachable? | Link rot |
| 5 | Does the RAG corpus (179 records) pass schema validation with correct hashes? | Implementation |
| 6 | Should the VOG schema's 5 evidence classes be extended to all 7 observation classes? | Cross-source |
| 7 | Pipeline config has 7 capability statuses vs paper's 8 — intentional or gap? | Cross-source |
| 8 | Extraction guide's 12 failure modes vs paper's 15 — which 3 omitted? | Cross-source |
| 9 | Pegasus fight layers add 3 new layers not in SRC-005 combat coding — extend? | Cross-source |
| 10 | Paper's 10 style domains vs extraction guide's 11 tracking dimensions — aligned? | Cross-source |
| 11 | What is the minimum viable experiment for H3 (Laban distinct motion)? | Empirical |
| 12 | Similarity budget defaults are authored — what calibration protocol? | Empirical |
| 13 | Round-trip verification 10 metrics — what soft thresholds? | Empirical |
| 14 | 4-tier MVP — expected extraction quality at each tier? | Empirical |
| 15 | Confidence fusion precedence — empirically validated? | Empirical |

### SRC-010 (19 questions)

| # | Question | Category |
| --- | --- | --- |
| 1 | e001 (30 fps vs 24 fps) isolated A/B — does 30 fps still read UGC? | Implementation |
| 2 | e003 needs a quantitative variance metric before p009 leaves `low` | Implementation |
| 3 | v005 vs v006 same-seed A/B — does the YAML layer add anything? | Implementation |
| 4 | Verification loop post-render half: re-measure a render against a canon (50 ms / 0.05 m) | Implementation |
| 5 | All 8 profiles unvalidated — render one profile per domain | Implementation |
| 6 | blk_facs_au_track (frontier #1) isolated A/B design | Implementation |
| 7 | Tier-2 pose lane never exercised end-to-end; Tier 3/4 unbuilt | Implementation |
| 8 | p008 rests on single run r005 — replicate or demote | Implementation |
| 9 | TOL_REACH 0.35 m / 50 ms / 0.05 m calibrated by one v006 pass — defensible set? | Implementation |
| 10 | Low-confidence bundled patterns (p002, p003, p005) need isolated A/Bs or demotion | Implementation |
| 11 | Bridge 4 manual score dims to the paper's 6 metric families | Cross-source |
| 12 | Should failure taxonomy gain a plastic-skin/plastics class (v004 lab-original)? | Cross-source |
| 13 | Which lab artifact exercises paper Mode B (agent compose)? | Cross-source |
| 14 | p006 vs p008 joint experiment: prose vs JSON vs hybrid fight content | Cross-source |
| 15 | Run the 7-condition style ablation (validates paper's 8-condition design) | Cross-source |
| 16 | What is TOL_REACH's true detection floor (0.18 m deficit case)? | Empirical |
| 17 | Replicate 30 fps cadence + 0.28 s speech pause on LTX-2.3 | Empirical |
| 18 | Second observer re-scoring e002 runs to bound observer effect | Empirical |
| 19 | Do finer sample rates (0.25 s / 24 fps) change validation outcomes? | Empirical |

### SRC-011 (21 questions)

| # | Question | Category |
| --- | --- | --- |
| 1 | Run ADRG-PKG-E1 (mini fixed graph vs one-shot JSON) — gates every mini-profile default | Implementation |
| 2 | ADRG-PKG-E2: quantify 3 CoT risks (false provenance, retrieval contamination, token overhead) | Implementation |
| 3 | ADRG-PKG-E3: validate graph expansion bounds (depth 2, 24 nodes) + coverage contract | Implementation |
| 4 | ADRG-PKG-E4 vs E-ADRG-006: one shared carrier/ownership protocol instead of two runs | Implementation |
| 5 | Router weights for D = w_I·I + w_U·U + w_C·C + w_R·R − w_V·V — calibrated? | Implementation |
| 6 | Calibrate model-scaled profile numbers (top_k, branch widths, repairs) per model stack | Implementation |
| 7 | Tooled measurement for the 11 planner metrics (e.g., decision_trace_faithfulness) | Implementation |
| 8 | Adopt package's 15 concept cards + graph-builder extension (6 node kinds, 12 edges) in lab repo | Implementation |
| 9 | Checkpoint H (post-generation adherence) depends on the unclosed post-render loop (SRC-010 gap 4) | Implementation |
| 10 | Teacher-student decision distillation has no training/exemplar dataset | Implementation |
| 11 | E-ADRG naming collision: renumber to one namespace or keep both registries? | Cross-source |
| 12 | Reconcile package 6 evidence labels vs SRC-004's 5 ADRG classes into one vocabulary | Cross-source |
| 13 | Should the ADRG schema gain adapter-version fields (compile_key, SRC-006 §8)? | Cross-source |
| 14 | Weighted router D vs budget-router vector doctrine — resolution needs ADRG-PKG-E1 | Cross-source |
| 15 | Package 5 promotion criteria vs tree 6 adoption criteria — unify after first results? | Cross-source |
| 16 | Build concept-card crosswalk (package 15 cards ↔ tree cards) before lab import | Cross-source |
| 17 | Small-model limits (mini profile) — CAUTION-grade until ADRG-PKG-E1 measures failure rates | Empirical |
| 18 | Self-critique limits: quantify residual failure rate of intrinsic critique passes | Empirical |
| 19 | Graph complexity: measure actual large-profile graph sizes vs 24-node bound | Empirical |
| 20 | Creative homogenization: human-judged diversity vs J(S) ranking experiment | Empirical |
| 21 | Prompt injection / format security: adversarial authoring test set | Empirical |

### SRC-012 (8 questions)

| # | Question | Priority | Cross-source link |
| --- | --- | --- | --- |
| 1 | Which phase boundaries are reproducible across annotators well enough to become canonical? | P0 | SRC-003 E18 |
| 2 | Which rhythm metrics (beat-alignment error, IOI CV, phase-ratio error, contact-causality error, snappiness/floatiness proxies, cut-rhythm divergence) correlate with expert judgment on real video-model outputs? | P0 | SRC-010 (only empirical source) |
| 3 | Should the KB `rhythm` object (profile + contact_s + setup_strike_recovery 3-split) become a canonical scene field, or remain an authoring convenience reconciled by the compiler? | P1 | canonical_schema_design |
| 4 | Do the KB's 5 evidence classes warrant tree-wide adoption, or stay package-local? (Compare SRC-005 7, SRC-009 VOG 5, SRC-011 6) | P1 | evidence_two_axis_model |
| 5 | Which provider surfaces natively carry timing/phase/contact controls? (KB downcasting: phase_timing/FACS/BESS high-loss in prose) | P1 | provider_capability_snapshots |
| 6 | Can a real-time BESS detector reach production confidence for Weight/Flow using target-response + contact evidence? | P2 | laban_proxy_measurement_contract |
| 7 | Should `sequencing_delay_ms`-style per-pattern lag values be calibrated per actor/technique via immutable experiments? (KB 55 ms is one CPCS_CONVENTION sample) | P2 | bartenieff_six_patterns |
| 8 | Do the KB 5 phase presets or SRC-010 4-phase strike ratios predict viewer readability better? | P1 | combat_math_metrics_layer |

## 3. Pending distillation sources

6 sources remain in the distillation queue (control plane reference §14 —
reconciled 2026-08-09; both files list the same 6 PENDING sources):

| # | File | Lines | Priority |
| --- | --- | --- | --- |
| 04b | `04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE.md` | 4,668 | P1 — larger version of SRC-004 (completed) |
| 07 | `07 CPCS World Model _ Causal State _ Attention Gap Closure.md` | 676 | P2 |
| 08 | `15-kinetic_motion_direction_prompting_manual.md` | 2,479 | P2 |
| 09 | `Continous Combat State.md` | 1,834 | P2 |
| 10 | `Granular Motion Control for AI Video Generation.md` | 1,978 | P2 |
| 11 | `Polyglot Compiler.md` | 532 | P2 |

## 4. Other outstanding items

- **Frozen ZIP packages**: not supplied for SRC-001 or SRC-002; package-level
  claims are not verifiable from supplied files (control plane reference §11.1).
- **FACS 2002 manual**: proprietary/licensed; secondary AU lists must not be
  treated as the manual (§11.2).
- **E-ADRG-001 through E-ADRG-006**: 6 controlled experiments defined but not
  executed. All ADRG policies remain `unexplored` until experiments are run
  (promotion_rules.md).
- **New experiment families (designed, not executed)**: CPCS-MX experimental
  program (7 RQs, ablation conditions A–G — `cpcs.research.cpcs_mx_experiments`);
  carrier factorial with representation policy (`carrier_effect_experiment_design`,
  SRC-006 E2 + SRC-007 E6); reasoning-mode suite (7 modes, budget tiers B0–B3,
  F1–F14 fixtures — `adrg_experiments`, SRC-006 E3); benchmark harness with gold
  fixture chain and falsification slice (`benchmark_harness_contract`).
- **SRC-007 G010/G018/G022**: undefined in the prompt itself; must be recovered
  from the attached DMR register — never inferred from numbering
  (`src007_dmr_runtime_gaps.md`).
- **DIRECTORY.md route count**: regenerated after SRC-010 distillation;
  the count in the control plane reference §2 is the live value.
- **SRC-009 answered SRC-008 Q9**: The DMR execution kit was NOT SRC-009.
  SRC-009 is the CPCS paper v1.2 + extraction guide + Pegasus paper + v1.2
  package. The DMR kit remains a candidate for a separate source.
- **SRC-010 distilled (2026-08-09)**: lab/ (40 files) + references/ (4 files)
  → 9 new cards + 6 EXTENDs (all applied) + 19 questions + DIST-010 ledger.
  The lab is the only empirically validated source in the corpus
  (PROVIDER_EXPERIMENT); its scores are single-observer/single-session.
- **SRC-011 distilled (2026-08-09)**: ADRG Research Package v1.0 (the primary
  package behind SRC-004, its U01) → 3 new cards (model_scaled_reasoning_policy,
  adrg_reasoning_graph_schema, graph_aware_rag_bundle) + 7 EXTENDs (all
  applied) + 21 questions + DIST-011 ledger. All profile numbers, weights, and
  bounds are proposed defaults until ADRG-PKG experiments run.
- **E-ADRG naming collision (SRC-011)**: the package's §21 E-ADRG-001..005 are
  different experiments from SRC-004's E-ADRG-001..006; package experiments
  are registered as ADRG-PKG-E1..E5 with a mapping table in
  `adrg_experiments.md` (SRC-011 EXTEND).
- **ADRG-PKG-E1..E5**: 5 package-defined controlled experiments (mini graph vs
  one-shot; ledger vs verbose rationale; dense vs graph-bundle retrieval;
  dual-format ownership; selective ToT camera) added to the experiment
  families — designed, not executed. All ADRG policies remain `unexplored`
  until experiments are run (promotion_rules.md).
- **SRC-012 distilled (2026-08-09)**: the frozen KB (`CPCS_AI_Video_Motion_Direction_KB_v1.0.0`)
  → 4 new cards (rhythm_metrics_contract, beat_syncpoint_alignment,
  phase_timing_presets, camera_impact_sync — the `10_time_rhythm/` tree
  section was previously empty) + 6 EXTENDs (all applied, including
  SRC-003 E16/E18) + 8 questions + DIST-012 ledger + identity. Sync/alignment
  emphasis: master clock doctrine, phase/rhythm preset families, BML
  sync-point mapping, camera impact binding chain, all with DAG edge
  representations.
- **DMR execution kit DEFERRED**: `director_motion_reasoning_execution_kit`
  remains a candidate for a separate source (SRC-013 candidate); not distilled
  in the SRC-012 pass by user decision. A future pass should audit
  kit-vs-tree overlap before distillation.
- **Understanding gap register LIVE (2026-08-09)**: `understanding_gap_register.md`
  holds the agent's student gaps (UG-001 … UG-007, WHAT/WHY/HOW/WHEN/APPLY/BLEND,
  nested). The user does deep research on UG ids and returns it via
  `Research_return_folder/` or chat; the agent ingests per doctrine D9 and
  closes/refines with evidence. Session continuity lives in
  `00_governance/agent_logs/working_agent_log.md` (H6).

## How to use this file

1. **Before starting work**: read this file to know what's pending.
2. **After applying an EXTEND**: change the status from PENDING to APPLIED.
3. **After closing a research question**: mark it with a closure note.
4. **After distilling a new source**: add its EXTEND table and gap questions.
5. **After adding a new boundary**: add it to §4.
6. **Governance decisions**: resolve via the automation doctrine's decision
   tree (`cpcs/00_governance/policies/control_plane_automation_doctrine.md`,
   D1–D7) and record outcomes in its §5 applied-decisions register. The user
   is consulted only on the doctrine's §6 brief triggers.
