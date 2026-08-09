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

## Typed part–connection–region schema (SRC-013 EXTEND)

> **Source:** SRC-013 (user research return, staged) — gap_answer_02
> §typed object-part schema + §sling-bag instance; evidence E1 (OpenUSD),
> E2 (NVIDIA deformables), E3 (PDDL2.1).

Objects that change state through manipulation are typed part graphs, not
single labels:

- **Part body_model:** `rigid · articulated_rigid · surface_deformable ·
  volume_deformable · distributed_closure · unknown` — e.g. zipper slider =
  rigid, zipper teeth = distributed_closure, side gussets = surface
  deformable, cavity = volume.
- **Connection kinds:** `seam · zipper_path · fold_line · hinge · gusset ·
  adhesive · constraint_surface` — each carries `closure_state` and a
  `topology_rule` (`must_persist · may_release · may_break`).
- **Region:** named geometry with `visibility_state` — occlusion ≠ absent,
  unknown ≠ false (see interaction_lifecycle SRC-013 EXTEND).
- **Design rules:** state changes name the part, connection, and region
  they affect; no untyped "bag opens" label; a part's body_model constrains
  legal transitions (a rigid part cannot stretch).

## Mechanism vocabulary for closure manipulation (SRC-015 EXTEND)

> **Source:** SRC-015 (user research return, staged) — gap_answer_04
> §2 mechanism and state vocabulary (YKK structure + usage manual, Eagle
> Flexible, Arsutoria); evidence class: source evidence.

UNZIP, OPEN, CLOSE, and ZIP are **separate state-changing events over
parts**, never one phrase like "open the bag":

- **Slider motion is a local closure-state operation:** teeth join or
  separate only where the slider passes; the region ahead of the slider
  keeps its prior state (direction determines passed-teeth state).
- **ZIP requires seated halves:** zipping while the panel is misaligned is
  mechanically invalid — seated/aligned zipper halves are a precondition of
  slider motion (YKK usage manual).
- **Gusset expansion follows panel displacement**, never precedes it
  (side-gusset pouch mechanics).
- **Deformation is material-specific:** coil stringers can stretch and
  change pitch; do not overfit a perfectly rigid zipper model.
- **Anatomy vocabulary names parts separately** — front panel, rear
  shell/panel, bottom hinge/base, side gussets, zipper halves (bag
  construction vocabulary).

## Verification

`test_affordance_geometry_present`,
`test_environment_constraints_consumed`,
`test_collision_class_distinguished`,
`test_part_body_model_typed`,
`test_connection_kind_with_topology_rule`,
`test_region_visibility_state_declared`,
`test_slider_passage_local_closure_state`,
`test_zip_requires_seated_halves`,
`test_gusset_follows_panel_displacement`.
