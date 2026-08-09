---
id: cpcs.runtime.sceneplan_authority_projection
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G001]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.execution_reasoning_state_schema
  - cpcs.compiler.capability_classes_loss_records
  - cpcs.verification.measurement_record_form
---

# ScenePlan Authority Projection

> **Source:** SRC-007 G001 — "Canonical ScenePlan"

## Principle

Define one executable ScenePlan without creating a competing semantic
authority. ScenePlan is an **execution projection** over the four
structures — CPCS Universal Score, CPCS-MX, Video Observation Graph (VOG),
and DMR — never a fifth semantic truth.

## Field-ownership matrix

For every overlapping field across the four structures, state whether DMR:

- references it without copying;
- materializes a resolved execution value;
- derives a temporary solver value;
- records an observation link; or
- is forbidden from owning it.

## ScenePlan lifecycle

```text
creation → resolution → validation → compilation → evaluation → retirement
```

Replanning triggers: an authored score change, an observation mismatch, and
a provider capability change. Where an observed VOG value differs from an
authored target, observation does **not** silently overwrite intent — it
produces a conflict record and a decision.

## Value-status model

Every ScenePlan value carries an origin:

```text
authored · solved · derived · observed · measured · unknown
```

## Required artifact set

- normative field-ownership matrix;
- identity/reference rules for scene, shot, actor, object, event, control,
  and evidence IDs;
- units and frame registry;
- origin/value-status model;
- ScenePlan state machine;
- minimal, realistic, and invalid ScenePlan instances;
- an invariant proving ScenePlan cannot become a second semantic authority.

## Verification

`test_sceneplan_never_second_authority`,
`test_observation_does_not_overwrite_authored_intent`,
`test_replanning_on_authored_score_change`,
`test_replanning_on_observation_mismatch`,
`test_replanning_on_provider_capability_change`.
