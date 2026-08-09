---
id: cpcs.runtime.temporal_solver_semantics
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G002]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/knowledge/00_foundations/numerical_representation/
  - cpcs/runtime/04_synthesis/
interfaces:
  - cpcs.found.timebase_systems
  - cpcs.runtime.execution_reasoning_state_schema
  - cpcs.runtime.failure_repair_contract
  - cpcs.runtime.canonical_schema
---

# Temporal Solver Semantics

> **Source:** SRC-007 G002 — "Temporal solver"

## Scope

Executable temporal semantics for: interval, instant, duration, onset,
deadline, overlap, before/after, during, meets, starts/finishes, equality,
latency. Research anchors: Allen interval relations, OWL-Time, STN/STNU
boundaries, negative-cycle explanations, underconstraint detection, and
uncertainty. Standards are interoperability references, not wholesale
ontology imports.

## Solver selection policy

Specify when CPCS should use:

- **interval algebra** — ordering/overlap reasoning with no metric
  tightness requirement;
- **Simple Temporal Network (STN)** — metric constraints with
  difference constraints;
- **uncertainty-aware extension (STNU-style)** — durations that are not
  controllable;
- **no solver** — purely authored timing with no resolution needed.

## Required solver behavior

- negative cycle in the constraint graph ⇒ inconsistent schedule, with a
  **minimal conflict explanation**, not a bare failure;
- underconstraint detection: multiple valid schedules exist and the choice
  policy must be explicit;
- uncertain durations must never become falsely precise;
- deadline/latency violation triggers repair, not silent rescheduling;
- numeric tolerance, clock/timebase, boundary rules (interval convention),
  unit conversion, and rounding are declared per solve.

## Schedule origin

Record whether a chosen schedule came from **authored timing**,
**deterministic optimization**, or **creative selection** — the origin
label is part of the output, not an afterthought.

## Compilation from authored temporal language

Authored language compiles into solver variables and constraints. Required
demonstrations: one fully specified schedule; one satisfiable but
underconstrained schedule; one inconsistent schedule with minimal conflict
explanation; one uncertain-duration case that must not become falsely
precise; one deadline/latency violation that triggers repair.

## Verification

`test_negative_cycle_yields_minimal_conflict_explanation`,
`test_underconstrained_schedule_explicit_choice_policy`,
`test_uncertain_duration_not_falsely_precise`,
`test_schedule_origin_labeled`,
`test_deadline_violation_triggers_repair`.
