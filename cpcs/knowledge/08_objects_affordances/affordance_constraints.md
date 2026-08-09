---
id: cpcs.mx.affordance_constraints
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §37, §91, §92, §93]
primary_route: cpcs/knowledge/08_objects_affordances/
secondary_routes:
  - cpcs/knowledge/03_world_scene/
interfaces: [cpcs.mx.interaction_coupling, cpcs.mx.motion_realization]
---

# Affordance, Environment, and Collision

Motion reasoning needs to know what the environment permits. Affordance is not
just categorical — it includes interaction geometry.

## Affordance with geometry

```yaml
affordance:
  type: grasp
  target_region: handle
  approach:
    direction: actor_relative
  required_orientation:
    mode: aligned
```

Examples: handle → graspable; chair → support/sittable; ground → supportable;
water → penetrable; wall → blocking; door → hinge rotation.

## Environment as constraint field

Instead of `environment = background`, allow:

```text
support surfaces · obstacles · clearance regions · interaction surfaces ·
hazards · occlusion regions · navigation corridors
```

Environment-aware motion generation explicitly couples trajectory, pose, and
environmental collision constraints.

## Collision classes

At least distinguish:

```text
self_collision · actor_actor_collision · actor_object_collision ·
actor_environment_collision · object_environment_collision
```

```text
collision_policy: forbidden · allowed · intentional
```

This prevents a meaningful impact from being treated the same as an accidental
body intersection.

## Verification

`test_affordance_geometry_present`,
`test_environment_constraints_consumed`,
`test_collision_class_distinguished`.
