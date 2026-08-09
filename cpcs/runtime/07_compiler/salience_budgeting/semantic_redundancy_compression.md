---
id: cpcs.mx.semantic_redundancy_compression
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §32, §100]
primary_route: cpcs/runtime/07_compiler/salience_budgeting/
interfaces: [cpcs.compiler.control_priority_attention_budget]
---

# Semantic Redundancy Compression and Minimum Sufficient Control

Do not emit `fast`, `rapid`, `sudden`, `explosive`, `quick`, `accelerated`,
`high-energy` as seven independent controls when they target one mechanism.

## Compression

```json
{
  "control_composition": {
    "group": "rapid_onset",
    "members": ["fast", "sudden", "rapid_acceleration"],
    "projection": { "max_equivalent_controls": 1 }
  }
}
```

The compiler should select the strongest provider-compatible representation.

## Minimum sufficient control

The compiler should solve: what is the smallest set of controls required to
preserve the requested intent? Not: how many motion concepts can be retrieved?

```yaml
control_selection:
  required:
    - target_contact
    - side
    - action_identity
  optional:
    - elbow_path
    - torso_style
  omitted:
    - exact_joint_angles
```

This follows from the motor-abundance problem and from motion-matching systems
that explicitly weight feature channels and select among many possible motion
samples rather than prescribing every degree of freedom.

## Verification

`test_redundant_controls_compressed`,
`test_minimum_sufficient_set_identified`.
