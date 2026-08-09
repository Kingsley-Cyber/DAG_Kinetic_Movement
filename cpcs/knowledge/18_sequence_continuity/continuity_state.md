---
id: cpcs.mx.continuity_state
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §10, §11]
primary_route: cpcs/knowledge/18_sequence_continuity/
secondary_routes:
  - cpcs/knowledge/06_body_motion/
interfaces: [cpcs.continuity.visibility_not_existence, cpcs.found.causal_event_semantics]
---

# ContinuityState and PersistenceConstraint

Observations about identity, position, state, and relation must persist across
time within a scope. ContinuityState encodes what must remain true across cuts,
occlusions, and time skips.

## ContinuityState

```json
{
  "continuity_state": {
    "actor_identity": {
      "actor_A": { "persists": true, "scope": "scene" },
      "actor_B": { "persists": true, "scope": "scene" }
    },
    "spatial_relation": {
      "actor_A_left_of_actor_B": { "persists": true, "scope": "shot" }
    },
    "object_held": {
      "weapon": { "holder": "actor_A", "persists": true, "scope": "shot" }
    },
    "support_state": {
      "actor_A_planted": { "persists": true, "scope": "action" }
    }
  }
}
```

## PersistenceConstraint

Not all state should persist indefinitely. PersistenceConstraint declares
lifetimes explicitly:

```yaml
persistence_constraint:
  entity: actor_A
  property: left_of_actor_B
  lifetime: shot
  release_on:
    - explicit_director_override
    - scene_change
```

## Scope hierarchy

```text
explicit local scope > event scope > shot scope > scene scope > project default
```

State changes should persist until another event changes them. This prevents
identity disappearance, prop replacement, and spatial relation flipping.

## Verification

`test_identity_persistence_across_cut`,
`test_spatial_relation_persistence_within_shot`,
`test_object_holder_persistence`,
`test_persistence_release_on_scope_boundary`.
