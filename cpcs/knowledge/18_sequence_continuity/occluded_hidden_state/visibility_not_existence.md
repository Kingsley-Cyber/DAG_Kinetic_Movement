---
id: cpcs.continuity.visibility_not_existence
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §10.1–§10.10, §28, SRC-002 L2.§27]
primary_route: cpcs/knowledge/18_sequence_continuity/occluded_hidden_state/
secondary_routes:
  - cpcs/knowledge/18_sequence_continuity/reentry_state/
  - cpcs/knowledge/18_sequence_continuity/identity_state/
interfaces: [state_x_continuity, causality_x_editing]
---

# Continuity Semantics: Visibility Change ≠ Existence Change

## Principle

State continuity through partial observability is a semantic dimension of its
own — not reducible to motion (HOW), phase (WHEN), or interaction (WITH
WHOM):

```text
STATE(t0) → STATE TRANSITION → PARTIALLY/UNOBSERVABLE INTERVAL → STATE(t1)
```

A visibility change must **not** automatically become an existence change:

```text
visibility = partial/occluded · existence = continuous · identity = actor_B
· trajectory = continuing
```

is semantically different from `existence = ended · identity = unknown`.

## Six-state visibility vocabulary (SRC-002 L2.§27)

```text
visible · partially_visible · occluded · out_of_frame ·
unobservable · unknown
```

`occluded` does not mean `absent`. Every important property should declare
its persistence lifetime (SRC-002 L2.§27.3): `frame · instant ·
action_phase · action · shot · scene · sequence · project`. Defaults (CPCS
policy, overridable by explicit authored intent): identity→project/scene; AU
activation→event/interval; Laban Effort→event/phrase; wardrobe→scene/project;
gaze target→interval/event.

## Proposed kernel objects (PROJECT_DERIVED, SRC-001 v1.1)

- **ContinuityState** — invariants that must remain true across an interval
  even when full visual state is unavailable (visibility, existence,
  identity, actor_count, trajectory_continuity, pose_continuity,
  action_generation). It constrains what may change; it does not assert an
  unobserved exact pose.
- **StateTransition** — semantic bridge between accepted states
  (type/onset/offset/path/pre_state_ref/post_state_ref/continuity_ref). Must
  not invent exact hidden coordinates merely because a provider requires text.
- **OcclusionInterval** — a **continuity constraint**, not an observation
  annotation: cause, visibility, identity/trajectory preservation flags,
  `exact_pose.status: unobservable`, and `forbidden_generation`
  (`teleport`, `clone`, `pose_reset`, `identity_swap`,
  `new_unmotivated_action`). Uncertainty about hidden state is not
  permission to invent a new state.
- **PersistenceConstraint** — per-entity persistence policy (identity,
  count, wardrobe, topology, existence, visibility may_change, position
  continuous_trajectory). Applies to actors, props, clothing, held objects,
  vehicles, environmental structures.

Schema drafts: `cpcs/schemas/world_model/universal_kernel_family.md`.

## Compiler behavior

Continuity constraints compile **before** provider projection:

```text
accepted entity/state → continuity + persistence constraints
→ causal dependencies → motion/phase/interaction controls
→ provider capability negotiation → provider projection
```

Responses when a provider cannot preserve a required continuity constraint:
`native_continuity_control · semantic_prompt_constraint · shot_decomposition ·
visibility_bridge · reference_conditioning · explicit_compilation_loss ·
reject`. (`shot_decomposition` is a routing/compilation strategy, not a new
semantic primitive.) Never silently treat a descriptive prompt as successful
control.

## Verification

Continuity is a first-class verification dimension:
identity_consistency, actor_count_consistency, existence_continuity,
trajectory_continuity, wardrobe_continuity, prop_continuity,
occlusion_transition_error, forbidden_event_rate. A continuity failure is not
equivalent to a generic motion-adherence failure.

## Complexity interaction

`occlusion_burden` and `continuity_burden` join the complexity feature
vector; do not collapse to a scalar before calibration.
