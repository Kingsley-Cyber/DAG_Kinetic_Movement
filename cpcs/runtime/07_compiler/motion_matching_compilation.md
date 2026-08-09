---
id: cpcs.runtime.motion_matching
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §22]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/knowledge/06_body_motion/phase_grammar/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.constraint_compilation
  - cpcs.body.retarget_contract
  - cpcs.found.layer_architecture
---

# Procedural Animation, Motion Matching, and Engine Execution

> **Source:** SRC-005 §22 — "Procedural animation, motion matching, and engine execution"

## Principle

A CPCS-MX score can drive an offline DCC pipeline or real-time character
controllers. Game engines demonstrate how root motion, state, trajectory
prediction, IK, animation databases, and procedural constraints can be
composed at runtime.

## Root-motion execution modes

| Mode | Root trajectory authority | Typical use |
| --- | --- | --- |
| `clip_driven` | animation clip | authored attacks, cinematic locomotion |
| `controller_driven` | navigation/gameplay controller | responsive gameplay |
| `constraint_driven` | contacts, target, optimization | exact staging or procedural traversal |
| `hybrid_warped` | clip plus trajectory warp | motion matching and target alignment |

Root policy must be explicit because it changes the meaning of every contact.
A foot planted in the source clip can slide if a controller moves the capsule
independently.

## Motion matching as retrieval plus adaptation

Motion matching selects a pose or frame from a database by comparing current
state and desired future trajectory to feature vectors. A CPCS-MX adapter
compiles fields into query features: current root velocity, facing, joint
positions and velocities, support/contact state, desired future trajectory
samples, desired facing samples, action tag, style/persona tag, and Laban
proxy values.

The matching cost:

\[
C_i = w_p E_{pose,i} + w_v E_{velocity,i} + w_t E_{trajectory,i}
+ w_c E_{contact,i} + w_s E_{style,i} + w_a E_{action,i}.
\]

Weights are project parameters, not universal constants. A combat cinematic
may prioritize contact and action tags; a background crowd controller may
prioritize trajectory and continuity. Determinism depends on database version,
feature normalization, tie-breaking, runtime state, and post-selection
warping — all stored in an execution manifest.

## Procedural IK and full-body adjustment

IK is used for foot placement, hand-to-prop alignment, gaze and head aiming,
seating and bracing, target-aware reaches, combat staging, retarget
correction, and camera-relative framing. Full-body IK distributes error across
a chain rather than moving a single end effector.

```json
{
  "ik_task": {
    "id": "ik.right_hand.prop_handle",
    "interval": [1.42, 2.87],
    "effector": "right_hand",
    "target": {"entity": "prop_sword", "socket": "grip"},
    "position_weight": 1.0,
    "orientation_weight": 0.85,
    "pole_target": "right_elbow_preferred_plane",
    "joint_limit_profile": "rig.actor_a.anatomical",
    "root_translation_limit_m": 0.06,
    "root_rotation_limit_deg": 4.0,
    "failure_policy": "report_and_hold_last_valid"
  }
}
```

If no solver can satisfy the task, the adapter must not silently move the prop
or violate a locked contact.

## Phase-conditioned control

PFNN conditions a locomotion model on a cyclic phase variable and
user/environment controls. Local Motion Phases generalize this by learning
asynchronous phase signals for multiple body parts in multi-contact actions.
These support a CPCS-MX distinction between: global gait phase, limb-local
phase, action-event phase, contact state, and presentation retime.

## Physics-based controllers

A score can be compiled into a trajectory-optimization or
reinforcement-learning objective:

\[
J = \sum_t \left(
w_q E_q(t) + w_{\dot q}E_{\dot q}(t) + w_r E_{root}(t)
+ w_c E_{contact}(t) + w_e E_{effort}(t) + w_u\|u(t)\|^2
\right),
\]

subject to dynamics, joint limits, non-penetration, balance, and task
constraints. Here `effort` is an engineering proxy derived from the authored
performance score.

## Engine execution package

A runtime compiler emits: character rig mapping, animation database or base
clip IDs, root policy and trajectory, state-machine/action graph, phase and
contact streams, IK tasks and priorities, motion-warp targets, physics
profile, facial curves, secondary-motion profile, camera and VFX events, and
verification probes. A capability report declares which fields are
natively supported vs approximated vs unsupported.

## Verification checkpoints

At runtime or in recorded replays, measure: root deviation, transition
discontinuity, contact timing and foot slip, IK residual, joint-limit
violations, collision penetration, action-state sequence, phase continuity,
frame-time dependence, and deterministic replay under a fixed seed and
database hash. The engine is an execution target, not the semantic source of
truth.
