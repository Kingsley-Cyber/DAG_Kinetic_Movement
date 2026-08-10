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

## Unobserved transitions and hard-cut discipline (SRC-013 EXTEND)

> **Source:** SRC-013 (user research return, staged) — gap_answer_02
> §durative causal transitions + §hard-cut discipline; evidence E7 (TAP-Vid).

A cut is a **sampling boundary, not a state reset**: the state recorded at
the end of shot N is the state assumed at the start of shot N+1.

- Durative transitions declare start / over-all / end phases (PDDL2.1
  style); a cut may land only on a declared phase boundary, never on an
  interpolated mid-transition.
- A cut that hides a transition does not authorize the model to invent the
  unseen mechanism — declare it `unobserved` with assumed start/end states,
  or forbid the cut.
- Cut edges carry their own state contract: `preserve_state` for hard cuts
  (e.g. `closure_released`), `changed_field` for match cuts (only the named
  field may change across the cut).
- Identity persists across occlusion and frame exit: a hand/object that
  leaves and returns is the same entity unless a state record says
  otherwise.

## Verification

`test_identity_persistence_across_cut`,
`test_spatial_relation_persistence_within_shot`,
`test_object_holder_persistence`,
`test_persistence_release_on_scope_boundary`,
`test_cut_boundary_is_declared_phase`,
`test_unobserved_transition_declared_not_interpolated`,
`test_cut_edge_preserves_declared_state`,
`test_identity_persists_across_frame_exit_reentry`.
