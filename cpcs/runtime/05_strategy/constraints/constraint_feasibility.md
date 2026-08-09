---
id: cpcs.mx.constraint_feasibility
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §59, §60, §101]
primary_route: cpcs/runtime/05_strategy/constraints/
secondary_routes:
  - cpcs/runtime/07_compiler/
interfaces: [cpcs.canonical.control_scope, cpcs.compiler.control_priority_attention_budget]
---

# Constraint Feasibility and Freedom Budget

Priority alone is insufficient. The system needs to determine whether
constraints can be jointly satisfied.

## Constraint hierarchy

```text
ConstraintSet · ConstraintHardness · ConstraintFeasibility · ConstraintRelaxation
```

```yaml
constraint_set:
  hard:
    - actor_identity
    - required_contact
    - no_penetration
  soft:
    - torso_upright
    - stylistic_arm_path
  relaxation_order:
    - stylistic_arm_path
    - torso_upright
  infeasible:
    action: reject_or_decompose
```

## Feasibility must precede provider compilation

```text
semantic target → constraint compilation → feasibility analysis →
adaptation/decomposition → provider compilation
```

Not: `semantic target → provider prompt → discover impossibility afterward`.

Feasibility checks: reachability, joint limits, collision, support, contact
geometry, actor spacing, camera visibility, trajectory bounds, provider
capability.

## Freedom budget

A good motion specification should contain both what must not vary and what is
intentionally free.

```yaml
freedom_budget:
  free:
    - elbow_configuration
    - micro_torso_adjustment
  bounded:
    - root_translation
    - hand_path
  locked:
    - target_identity
    - side
    - contact_outcome
```

## Task-space vs joint-space

Do not over-specify joint motion when the director only specified a task-space
outcome. Many valid joint configurations exist for one task outcome (motor
redundancy/abundance).

```yaml
constraint:
  variable: elbow_orientation
  status: free
  reason: task_outcome_unaffected
```

## Verification

`test_feasibility_checked_before_compilation`,
`test_infeasible_rejected_or_decomposed`,
`test_freedom_budget_present`.

## Typed feasibility outcomes (SRC-007 G006)

Every bounded feasibility check must return a typed outcome, never an
implicit pass:

```text
pass | fail | indeterminate | not_applicable | unobservable
```

Checks covered: support, reach, joint limits, root/foot coherence,
penetration, impossible timing, ownership, contact, balance. Deterministic
checks are explicitly distinguished from estimates and unknowns. Each check
declares inputs, assumptions, algorithm, tolerance source, confidence
propagation, evidence, false-positive risk, and repair scope.

Blocking rules: which failures block compilation, warn, cause re-solving, or
require review. A 2D video is insufficient to assert 3D penetration or a
joint-limit failure — those checks return `indeterminate` or `unobservable`,
not `fail`.

Ordering rule: validation is ordered so an **unknown prerequisite cannot be
treated as a pass by downstream checks** — `unknown` propagates as
`indeterminate`, never as success.

`test_unknown_prerequisite_propagates_indeterminate`,
`test_2d_video_cannot_assert_3d_penetration`,
`test_every_check_returns_typed_outcome`.
