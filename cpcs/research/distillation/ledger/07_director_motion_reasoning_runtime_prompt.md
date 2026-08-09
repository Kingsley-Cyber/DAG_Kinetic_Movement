---
distillation_id: DIST-007
source_id: SRC-007
status: complete
coverage: full
---

# Distillation Ledger — SRC-007

`06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md` →
CPCS knowledge tree. Distilled 2026-08-09. All objects below were written
into their primary routes; this ledger is the audit trail.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-007_director_motion_reasoning_runtime_prompt.md`.
Deep-research prompt for the DMR (Director Motion Reasoning) runtime gap
closure (539 lines, 17 source units U01–U17). **Artifact type: prompt, not
a completed report.** Distilled objects are research requirements, not
verified findings. G010, G018, G022 undefined in the prompt; recovery from
the attached register is mandatory.

## PASS 1 — Structural map

Mission + decision-path requirement → 19 defined gaps (G001–G009,
G011–G017, G019–G021) in 13 gap groups → shared application fixture → six
required packet sections → standards anchors → research execution rules.

## PASS 2 — Existing-knowledge search

G005 lifecycle overlaps `interaction_lifecycle` (SRC-001/002/005) — EXTEND
with stage classification, not a new card. G006 checks overlap
`constraint_feasibility` (SRC-003) — EXTEND with typed outcomes. G009 loss
accounting extends `capability_classes_and_loss_records` (SRC-001/004/006)
— EXTEND with exactly-once model. G011–G013 join contract extends
`measurement_record_form` (SRC-006) — EXTEND. G014/G015 extends
`failure_repair_contract` (SRC-006) — EXTEND. G019 extends
`carrier_effect_experiment_design` (SRC-001/006) — EXTEND.

## PASS 3 — Semantic map

6 new objects: `sceneplan_authority_projection` (G001),
`temporal_solver_semantics` (G002), `state_variable_catalog` (G003/G004),
`provider_capability_snapshots` (G007/G008/G021),
`benchmark_harness_contract` (G016/G017), `numeric_scale_calibration`
(G020).

## PASS 4 — Numerical/formal map

9 feasibility checks with 5 typed outcomes; 9 contact lifecycle stages
classified as event/relation/derived; 6 value-status origins
(authored/solved/derived/observed/measured/unknown); 6 ScenePlan lifecycle
stages; 7 state categories; 4 solver tiers (interval algebra/STN/STNU/none);
4 provider evidence kinds; 5 provider lifecycle states; 6 terminal loss
dispositions; 5 loss invariants; 5 format boundaries; 4 scale types;
4 confidence layers in the join contract.

## PASS 5 — Representation map

ScenePlan as execution projection over four structures (Universal Score,
CPCS-MX, VOG, DMR) with field-ownership matrix; versioned dated provider
snapshots instead of code constants; schedule-origin labeling; exactly-once
terminal dispositions per provider request.

## PASS 6 — Interface map

New cards interface with `cpcs.runtime.*` (canonical_schema,
execution_reasoning_state_schema, reasoning_atom, continuity_capsule,
failure_repair_contract, state_equivalence_keys, sceneplan_authority_projection),
`cpcs.compiler.capability_classes_loss_records`, `cpcs.verification.*`,
`cpcs.mx.continuity_state`, `cpcs.adrg.experiments`,
`cpcs.experiment.carrier_effect_design`, `cpcs.found.*`.

## PASS 7 — Contradiction scan

No contradictions with existing cards. G005 stage vocabulary aligns with
SRC-005 §10.2 contact taxonomy (types) as a complementary lifecycle model
(stages). The prompt's "do not redesign CPCS" constraint is consistent with
the existing authority hierarchy.

## PASS 8 — Placement decisions

6 CREATEs across `cpcs/runtime/04_synthesis/`, `cpcs/runtime/06_canonical/`,
`cpcs/knowledge/18_sequence_continuity/`,
`cpcs/runtime/08_provider_negotiation/`,
`cpcs/research/sources/experiments/`,
`cpcs/knowledge/00_foundations/epistemology/`. 6 EXTENDs (see PASS 2).
No REUSE/MERGE needed.

## PASS 9 — Dedup audit

`state_variable_catalog` complements `continuity_state` (persistence
constraints) and `continuity_capsule` (execution projection) without
duplication. `provider_capability_snapshots` complements
`capability_classes_and_loss_records` (classification) with the versioned
snapshot contract. `numeric_scale_calibration` complements
`evidence_two_axis_model` and `exactness_taxonomy`.

## PASS 10 — Operationalization

Every card lists executable verification tests (`test_sceneplan_*`,
`test_negative_cycle_*`, `test_contact_identity_*`, `test_join_contract_*`,
etc.). G007/G008 remain `unknown` pending official provider documentation —
no capability claim is made.

## PASS 11 — Coverage audit

All 17 source units covered: U01–U13 → cards/EXTENDs per registration
table; U14 shared fixture → gaps file; U15 required outputs → gaps file;
U16 standards anchors → temporal_solver_semantics + numeric_scale_calibration;
U17 execution rules → registration + gaps file.

## Objects written

- `cpcs/research/source_registry/identities/SRC-007_director_motion_reasoning_runtime_prompt.md`
- `cpcs/runtime/04_synthesis/sceneplan_authority_projection.md`
- `cpcs/runtime/06_canonical/temporal_solver_semantics.md`
- `cpcs/knowledge/18_sequence_continuity/state_variable_catalog.md`
- `cpcs/runtime/08_provider_negotiation/provider_capability_snapshots.md`
- `cpcs/research/sources/experiments/benchmark_harness_contract.md`
- `cpcs/knowledge/00_foundations/epistemology/numeric_scale_calibration.md`
- `cpcs/research/gaps/src007_dmr_runtime_gaps.md`
- EXTEND: `cpcs/runtime/05_strategy/constraints/constraint_feasibility.md`
- EXTEND: `cpcs/knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md`
- EXTEND: `cpcs/runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md`
- EXTEND: `cpcs/verification/measurement_record_form.md`
- EXTEND: `cpcs/runtime/04_synthesis/failure_repair_contract.md`
- EXTEND: `cpcs/research/sources/experiments/carrier_effect_experiment_design.md`
