---
id: cpcs.runtime.reasoning_atom
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.1, §11.2]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/verification/
interfaces:
  - cpcs.adrg.decision_record
  - cpcs.adrg.reasoning_trace
  - cpcs.runtime.execution_reasoning_state_schema
  - cpcs.runtime.continuity_capsule
---

# Executor-Relative Reasoning Atom

> **Source:** SRC-006 §4.1 — "Executor-relative reasoning atom"

## Definition

A `reasoning_atom` is the smallest versioned execution-reasoning unit that
one named consumer can independently accept, reject, verify, replace, or
depend upon without changing unrelated meaning.

## What it is not

- not necessarily one sentence, token, frame, shot, or ontology triple;
- not a copy of a full scene object;
- not a provider prompt fragment by default;
- not a reusable research concept;
- not atomic merely because it has one ID.

## Atomicity test (all conditions)

1. It has exactly one primary semantic purpose.
2. It has one owning executor/view.
3. It has one primary verification contract or one explicit unverified status.
4. It can be rejected or replaced without implicitly modifying another
   independent axis.
5. Its preconditions and postconditions can be stated without hidden prose.
6. Its semantic delta can be expressed against one or a tightly coupled set
   of canonical paths.

If staging and camera can vary independently, split them. If a handoff
requires approach, contact, transfer, release, and reaction, represent those
as composed event atoms linked by temporal and causal edges — do not
collapse them into a string.

## Atom types

| Type | Purpose | Typical owner | Canonical destination |
| --- | --- | --- | --- |
| `state_assertion` | current world/character/camera/audio fact or belief | continuity projector | world/execution state |
| `event_decision` | one authored or chosen event/phase | motion/performance/narrative | canonical score event |
| `relation_decision` | spatial, temporal, causal, ownership, knowledge relation | shared semantic kernel | canonical relation object |
| `control_decision` | camera, performance, editing, audio, VFX, style control | relevant directing view | canonical score control |
| `constraint` | hard/soft prohibition, requirement, invariant | policy/director | constraint set |
| `verification_condition` | observable pass/fail or metric definition | verifier | verification plan |
| `provider_realization` | candidate mapping of a canonical control to a provider | compiler/adapter | execution IR/provider plan |
| `failure_claim` | evidence-bound claim about a failed output | evaluator | failure record |
| `repair_operation` | minimal proposed change to execution state | repair planner | patch set |

## Required dimensions

```text
atom_id · atom_type · schema_version · owner · consumer
scope: project/sequence/scene/shot/event/provider-run
canonical_paths · subject_refs / object_refs
time_ref and timebase_id when temporal
coordinate_frame_id when spatial
laterality when side-specific
value · preconditions · postconditions
dependencies · conflicts
verification_ref or verification_status
origin_class · confidence and uncertainty
evidence_refs / provenance · status
```

## Authority and lifecycle

The atom lives in execution reasoning state, not in the reusable research
KG. An accepted atom value may map into the canonical score; a rejected atom
does not. Owner/consumer/path/origin and applicable frames/timebase must be
valid before acceptance.

## Verification

`test_atom_one_primary_purpose`, `test_atom_single_owner_consumer`,
`test_atom_rejected_without_collateral_axis_change`,
`test_atom_split_fixture_catches_independent_axes` (SRC-006 §11.2).
