---
id: cpcs.mx.repair_strategy
kind: method
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §41, SRC-004 §15]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/runtime/04_synthesis/
interfaces: [cpcs.verification.failure_mode_catalog, cpcs.verification.verification_expectation_model]
---

# RepairStrategy

The operational loop should be:

```text
target → compile → generate → observe → verify → failure signature →
responsible layer → smallest localized repair → regenerate
```

## Canonical repair

```json
{
  "repair_strategy": {
    "failure": "foot_slide",
    "preferred_repairs": [
      "strengthen_support_constraint",
      "preserve_root_trajectory",
      "recompute_retarget"
    ],
    "regeneration_scope": "affected_action_interval"
  }
}
```

Never automatically rewrite the whole shot for a local failure.

## Failure-directed repair (SRC-004 §15)

### Repair object

```json
{
  "repair_id": "repair.001",
  "failure_id": "failure.camera.001",
  "validator_id": "validator.camera_continuity",
  "base_digest": "sha256:...",
  "responsible_layer": "scene_control",
  "affected_paths": ["/camera/events/2"],
  "cause_candidates": [
    {"layer": "decision", "confidence": 0.41},
    {"layer": "compiler", "confidence": 0.37},
    {"layer": "provider", "confidence": 0.22}
  ],
  "protected_invariants": ["action_identity", "duration", "subject_identity"],
  "patch": [],
  "status": "proposed"
}
```

### Repair algorithm

```text
observed failure
→ classify failure
→ locate earliest responsible layer
→ load only affected object slice
→ propose smallest patch
→ test expected base
→ apply patch
→ rerun failed validator
→ rerun dependent validators
→ recompile
→ reverify
```

Use JSON Patch (RFC 6902) for canonical changes. The `test` operation should
protect the expected base before mutation.

### Escalation

```text
repair 1 fails → second bounded repair if policy permits
repair limit reached → blocked / needs_escalation
```

Never: validator failure → silently rewrite canonical data.

## Verification

`test_repair_targets_responsible_layer`,
`test_regeneration_scope_local`,
`test_no_wholesale_rewrite_for_local_failure`,
`test_repair_requires_base_test`,
`test_repair_preserves_invariants`,
`test_repair_bound_escalates`.
