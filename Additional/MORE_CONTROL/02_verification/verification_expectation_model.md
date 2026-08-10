---
id: cpcs.verification.verification_expectation_model
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§37]
primary_route: cpcs/verification/semantic/
secondary_routes:
  - cpcs/verification/performance/
interfaces: []
---

# Verification Expectation Model

A metric alone is insufficient. Every compiled control should resolve to:

```text
target → observable expectation → measurement method → metric → threshold → verdict
```

## Example

```yaml
verification_expectation:
  target: { control: laban.effort.flow.bound }
  observable_expectations: [controlled_progression, reduced_uncontrolled_follow_through, continuous_articulation]
  failure_signatures: [rigid_freeze, robotic_stiffness, excessive_follow_through]
  measurement: { type: mixed_human_kinematic_assessment }
  verdict: { threshold_status: experimental }
```

The threshold remains **experimental** until validated.

## Provider adherence decomposition

Provider adherence must be decomposed, not one opaque score:

```text
identity_adherence · action_adherence · spatial_adherence ·
temporal_adherence · performance_quality_adherence · facial_adherence ·
connectivity_adherence · camera_adherence · continuity_adherence
```

The aggregate is derived from these dimensions and must not hide catastrophic
failure of a high-priority constraint.
