# CPCS-MX — Heaviest P0 Research Closure
## Operational Motion Reasoning, Control Composition, Spatial State, Continuity, Support, Contact, Carrier Selection, and Verification

**Purpose:** deepen the 03_MX packet specifically where a coding/reasoning agent would otherwise have to invent behavior.

**Scope:** this document does not attempt to add more motion terminology. It closes the highest-impact semantic and operational gaps identified in the 03_MX critique.

**Primary architectural rule:** 03_MX owns hierarchical motion grammar and motion mechanics. Universal objects already owned by 01/02 must be referenced, not recreated.

---

# 1. Executive verdict

The strongest existing parts of MX are:

- kinematic representation;
- coordinate-frame discipline;
- explicit timebases;
- phase representation;
- contact as a concept;
- morphology/retargeting;
- measurement;
- provider compilation;
- verification metrics.

The heaviest missing layer is:

```text
DIRECTOR INTENT
    ↓
ACTION SELECTION
    ↓
ACTION TEMPLATE
    ↓
BRANCH / OUTCOME
    ↓
MOTION PRIMITIVES + MODIFIERS + PHASES
    ↓
SPATIAL / SUPPORT / CONTACT / CONTINUITY STATE
    ↓
REALIZATION
    ↓
CONTROL COMPOSITION
    ↓
CARRIER SELECTION
    ↓
PROVIDER
    ↓
OBSERVATION
    ↓
VERIFICATION
    ↓
FAILURE SIGNATURE
    ↓
LOCAL REPAIR
```

The important conclusion is:

> **MX should not merely describe motion. It must encode how a director-level request is transformed into a constrained motion plan.**

The 03 critique identifies the most important P0 gaps as operational knowledge, action templates, spatial state, continuity/persistence, control scope/lifetime/envelopes, support, contact geometry, realization, control priority, carrier selection, attention budgeting, verification expectations, and localized repair. Those are treated here as one integrated control system rather than as unrelated additions.

---

# 2. Cross-package ownership is non-negotiable

## Universal kernel — 01

Owns reusable cross-domain contracts such as:

```text
SpatialState
ContinuityState
StateTransition
PersistenceConstraint
CameraState
CausalEvent
CapabilityMatch
CompilationLoss
evidence/provenance axes
control scope/lifetime/priority where universal
```

## Performance semantics — 02

Owns:

```text
FACS
Laban
Bartenieff
performance-expression semantics
facial/gaze expressive interpretation
```

## MX — 03

Owns:

```text
hierarchical motion grammar
ActionTemplate
MotionPrimitive
MotionModifier
MotionPhase
SupportState
ContactSemantic
ContactGeometry
kinematics
dynamics
morphology
retargeting
secondary/material motion
motion observation
motion-specific verification
motion realization
```

The critique correctly identifies duplicated FACS/Laban and evidence semantics as architectural conflicts. MX should reference those canonical definitions.

---

# 3. The central new object: ActionTemplate

A primitive is too low-level to answer:

> What should happen when the director asks for a particular action?

Use an `ActionTemplate`.

## Definition

```text
ActionTemplate =
    action identity
    + preconditions
    + applicability
    + phases
    + primitive composition
    + modifiers
    + spatial requirements
    + support requirements
    + interaction requirements
    + outcome branches
    + invariants
    + realization candidates
    + verification expectations
```

## Example: strike

```yaml
action_template:
  id: strike
  preconditions:
    actor_present: true
    target:
      required: true

  phases:
    - anticipation
    - execution
    - interaction
    - follow_through
    - recovery

  composition:
    anticipation:
      - primitive: shift_weight
      - primitive: retract
    execution:
      - primitive: reach
      - modifier: accelerate
    interaction:
      - event: contact
    follow_through:
      - modifier: continue
    recovery:
      - primitive: stabilize

  outcomes:
    - contact
    - blocked_contact
    - near_miss
    - complete_miss
    - interrupted
    - deflected

  invariants:
    - actor_identity
    - side
    - action_identity
```

This is the missing decision layer between director intent and primitives.

---

# 4. Primitive taxonomy must be typed

The existing list mixes fundamentally different semantic classes.

## Primitive

An operation that produces a movement:

```text
translate
rotate
reach
retract
shift_weight
grasp
release
jump
land
turn
redirect
stabilize
oscillate
gesture
gaze_shift
```

## Modifier

A property/process applied to motion:

```text
accelerate
decelerate
direct
curved
large_amplitude
small_amplitude
fast_onset
slow_onset
```

## Phase

A temporal organization:

```text
anticipation
initiation
acceleration
apex
contact
deceleration
follow_through
recovery
```

## Interaction state/event

```text
near_contact
contact
impact
support
grasp
release
separation
collision
```

## Support/stability behavior

```text
plant
brace
stabilize
transfer_support
```

Do not make these peer members of one `primitive` enum.

---

# 5. Primitive applicability must be researched and encoded

Every reusable primitive needs operational knowledge:

```yaml
primitive:
  id: shift_weight

  meaning:
    concise: transfer support/load between body regions

  applies_when:
    - locomotion_initiation
    - directional_change
    - grounded_strike
    - landing_absorption
    - push_pull
    - balance_recovery

  less_relevant_when:
    - fully_airborne
    - isolated_facial_action

  modifies:
    - support_state
    - center_of_mass_relation
    - root_motion
    - downstream_chain_behavior

  visible_expectations:
    - support changes before or during action

  contraindications:
    - no_support_available

  verification:
    - support_transition
    - root_com_consistency
```

The purpose is to move primitive selection out of the model's private prior knowledge and into retrievable research/application knowledge.

---

# 6. Action branching is essential for generative video

A motion plan cannot assume the desired interaction succeeds.

## Canonical branch model

```text
Action
 ├── intended path
 └── outcome
       ├── success
       ├── blocked
       ├── near_miss
       ├── miss
       ├── interrupted
       ├── deflected
       ├── caught
       └── cancelled
```

## Example

```json
{
  "action_template": "strike",
  "selected_branch": "near_miss",
  "branch_contract": {
    "requires": [
      "visible_separation",
      "no_impact_deformation"
    ],
    "produces": [
      "evasive_reaction"
    ],
    "forbids": [
      "impact_recoil_as_collision"
    ]
  }
}
```

This prevents a generator from converting "near miss" into an accidental hit.

---

# 7. SpatialState is distinct from coordinate frames

A coordinate frame answers:

> Where is a point numerically?

SpatialState answers:

> How are entities arranged for the director?

## Required distinction

```text
numeric:
    actor_B.position = [0.4, 1.2, -2.8]

semantic:
    actor_B is right_of actor_A
    actor_B remains behind table
    weapon remains between actors
    hand passes outside face
    actor remains above water
```

## Canonical structure

```json
{
  "spatial_state": {
    "frame": "shot_world",
    "relations": [
      {
        "subject": "actor_B",
        "predicate": "right_of",
        "object": "actor_A",
        "persistence": "shot"
      },
      {
        "subject": "actor_A",
        "predicate": "above_surface",
        "object": "water"
      }
    ],
    "action_axes": [
      {
        "id": "fight_axis",
        "orientation": "actor_relative"
      }
    ]
  }
}
```

---

# 8. Direction must always carry a reference frame

Never emit ambiguous:

```text
forward
right
left
up
down
advance
retreat
```

without a frame.

Use:

```json
{
  "direction": {
    "value": "forward",
    "frame": "actor_root"
  }
}
```

or:

```json
{
  "direction": {
    "value": "right",
    "frame": "screen"
  }
}
```

Possible semantic frames:

```text
world
camera
screen
actor_root
target
surface
object
```

This is separate from the numeric coordinate frame.

---

# 9. ActionAxis and screen-space continuity

Many cinematic interactions are governed by a semantic axis rather than raw coordinates.

Examples:

```text
fight axis
conversation axis
travel direction
screen-left/right relationship
approach vector
retreat vector
camera-to-subject axis
```

Represent:

```json
{
  "action_axis": {
    "id": "fight_axis",
    "reference": "actor_A_to_actor_B",
    "persistence": "shot",
    "allow_crossing": false
  }
}
```

This provides a deterministic place for "don't cross the line" style directing constraints.

---

# 10. ContinuityState

Observation continuity and directing continuity are different.

Observation asks:

> Did the tracker maintain identity?

Directing asks:

> What must remain invariant across generation?

Use:

```json
{
  "continuity_state": {
    "entity": "actor_B",
    "identity": "invariant",
    "existence": "continuous",
    "actor_count": {
      "value": 1,
      "constraint": "exact"
    },
    "trajectory": "continuous",
    "visibility": "may_occlude",
    "hidden_state": {
      "pose": "unspecified"
    },
    "forbidden_transitions": [
      "teleport",
      "identity_change",
      "clone"
    ]
  }
}
```

A hidden state should not be invented merely because visibility is lost.

---

# 11. PersistenceConstraint

Apply continuity to more than actors.

Objects need:

```text
identity
existence
holder
attachment
state
location relation
```

Example:

```json
{
  "persistence": {
    "entity": "sword",
    "identity": "invariant",
    "existence": "continuous",
    "holder": "actor_A",
    "holder_until": "release_01"
  }
}
```

This prevents the common class of:

```text
visible object
→ occluded
→ different object/state appears
```

from being treated as acceptable.

---

# 12. ControlScope

Every control needs an explicit scope.

```json
{
  "scope": {
    "shot": "shot_03",
    "actor": "actor_A",
    "action": "strike_01",
    "phase": "acceleration",
    "body_region": "right_arm"
  }
}
```

Valid dimensions may include:

```text
scene
shot
beat
actor
body_region
joint
action
primitive
phase
interaction
environment
camera
secondary_effect
```

This prevents:

```text
"fast during acceleration"
```

from accidentally becoming:

```text
everything in the clip is fast
```

---

# 13. ControlLifetime

Scope answers where.

Lifetime answers how long.

```json
{
  "lifetime": {
    "start": "phase_start",
    "end": "phase_end",
    "persists_until": null,
    "decay": "none"
  }
}
```

Examples:

```text
identity lock → scene/sequence
foot plant → support phase
contact constraint → contact interval
motion accent → short interval
wind response → shot
```

This prevents local controls from contaminating later motion.

---

# 14. ControlEnvelope

Continuous controls should not be static labels.

```json
{
  "control_envelope": {
    "target": "motion_speed",
    "values": [
      {"phase": "anticipation", "value": "low"},
      {"phase": "acceleration", "value": "rising"},
      {"phase": "apex", "value": "high"},
      {"phase": "recovery", "value": "low"}
    ]
  }
}
```

The same applies to:

```text
camera_shake
motion_blur
effort
amplitude
tempo
recoil
secondary_motion
```

This makes temporal localization executable.

---

# 15. SupportState is a core whole-body representation

Support should be explicit rather than scattered across contact, balance and weight shift.

```json
{
  "support_state": {
    "actor": "actor_A",
    "contacts": {
      "left_foot": "planted",
      "right_foot": "planted"
    },
    "base_of_support": "bilateral",
    "load_distribution": {
      "left": "dominant",
      "right": "secondary"
    },
    "center_of_mass": {
      "relation": "inside_base"
    },
    "transfer": {
      "from": "rear_leg",
      "to": "right_arm",
      "path": [
        "pelvis",
        "torso",
        "shoulder"
      ]
    }
  }
}
```

This is high-value because:

```text
strike
kick
jump
land
turn
push
pull
run
recoil
balance
```

all depend on whole-body support organization.

---

# 16. Support verification

For a planted foot:

```text
foot_height ≈ support_surface
foot_velocity ≈ 0
contact persists during support interval
```

Do not use visual prose as the acceptance test.

Example:

```json
{
  "verification_expectation": {
    "target": "left_foot_support",
    "metrics": [
      "foot_height_error",
      "foot_velocity"
    ],
    "threshold": {
      "status": "experimental",
      "foot_velocity_max": null,
      "height_error_max": null
    },
    "verdict": "fail_if_exceeded"
  }
}
```

Thresholds must be calibrated against the intended capture/generation regime rather than invented universally.

---

# 17. Contact must split semantic and geometric layers

## ContactSemantic

```text
grasp
support
impact
brush
slide
near_contact
release
collision
```

## ContactGeometry

```text
site_a
site_b
surface_a
surface_b
distance
normal
relative_velocity
penetration
slip
duration
approach_direction
```

Example:

```json
{
  "contact_semantic": {
    "type": "near_contact",
    "interaction_intent": "evasion"
  },
  "contact_geometry": {
    "site_a": "right_fist",
    "site_b": "face_region",
    "minimum_separation": {
      "value": null,
      "status": "semantic_only"
    },
    "penetration_allowed": false
  }
}
```

This prevents "near contact" from becoming a vague enum.

---

# 18. Contact outcome must control reaction

A reaction must be causally linked.

```text
impact
→ target_reaction
```

versus:

```text
near_miss
→ evasive_reaction
```

versus:

```text
blocked
→ redirected_motion
```

Never leave:

```text
contact
reaction
```

as two unrelated events.

---

# 19. MotionRealization

This is the most important addition for autonomous direction.

A semantic request such as:

```text
heavy
```

is not itself executable motion.

Use:

```json
{
  "motion_realization": {
    "semantic_control": "heavy",
    "action_class": "strike",
    "observable_targets": [
      "grounded_preparation",
      "visible_weight_transfer",
      "proximal_to_distal_acceleration",
      "sharp_contact_accent",
      "recoil",
      "deliberate_recovery"
    ],
    "does_not_require": [
      "exact_force_value"
    ],
    "evidence_status": "candidate_action_conditioned_mapping"
  }
}
```

The critical point:

> `heavy × strike` is not the same realization as `heavy × landing` or `heavy × walk`.

---

# 20. Action-conditioned realization

Formalize:

```text
semantic_control
× action_class
× body_scope
× phase
× environment
→ realization
```

Examples:

```text
heavy × strike
→ grounded preparation + sharp transfer + recoil

heavy × landing
→ increased pre-contact preparation + strong support absorption + settling

heavy × walk
→ greater support commitment + reduced lightness + deliberate transfer

light × gesture
→ reduced amplitude + quick recovery + low visible effort
```

These should be research-backed mappings or explicitly marked hypotheses.

Do not encode them as universal biomechanical laws.

---

# 21. Realization must distinguish observable from hidden mechanics

A provider generally cannot be expected to reproduce:

```text
exact torque
exact center-of-pressure trajectory
exact joint moment
```

from prose.

It can potentially reproduce:

```text
visible weight transfer
clear preparation
abrupt contact accent
visible recoil
deliberate settling
```

Therefore realization should have:

```text
observable_targets
mechanical_targets
optional_internal_targets
```

and should never require an unobservable internal value when an observable proxy is available.

---

# 22. MaterialResponse

Secondary motion is not enough.

Interactions with materials/environment need a causal response object.

```json
{
  "material_response": {
    "material": "water",
    "trigger": {
      "event": "foot_contact"
    },
    "origin": {
      "bind_to": "contact_site"
    },
    "immediate_response": [
      "local_displacement",
      "splash"
    ],
    "secondary_response": [
      "ripples"
    ],
    "persistence": {
      "mode": "decay"
    }
  }
}
```

This turns:

```text
splash
```

from arbitrary decorative VFX into a consequence of an event.

The same pattern applies to:

```text
dust
mud
snow
sand
cloth
hair
rope
debris
smoke
liquid
glass
```

---

# 23. SecondaryMotion contract

At minimum:

```json
{
  "secondary_motion": {
    "asset": "coat",
    "driver": "torso_turn",
    "behavior": {
      "lag": "moderate",
      "overshoot": "slight",
      "damping": "natural"
    },
    "constraints": {
      "attached_at": [
        "left_shoulder",
        "right_shoulder"
      ],
      "avoid_body_interpenetration": true
    }
  }
}
```

Exact simulation parameters can remain in a simulation artifact rather than canonical semantic IR.

---

# 24. Retargeting must preserve semantic identity

Mechanical validity is insufficient.

A retarget is successful only if required semantic invariants survive.

```json
{
  "retarget_contract": {
    "required_invariants": [
      "action_identity",
      "actor_identity",
      "side",
      "target_relation",
      "phase_order",
      "contact_intent"
    ],
    "adaptable": [
      "joint_angles",
      "trajectory_amplitude",
      "root_height"
    ]
  }
}
```

---

# 25. Retargeting needs a reachability policy

When a target is unreachable:

```text
target unreachable
```

the system must not improvise.

Possible bounded adjustments:

```text
root translation
stance adjustment
torso lean
bounded limb extension
```

Potentially forbidden:

```text
target substitution
side change
identity change
semantic action change
```

Example:

```json
{
  "retarget_failure_policy": {
    "condition": "target_unreachable",
    "allowed_adjustments": [
      "bounded_root_translation",
      "bounded_stance_adjustment"
    ],
    "forbidden": [
      "change_target",
      "change_side"
    ],
    "otherwise": "fail"
  }
}
```

---

# 26. Provider capability and empirical reliability are different

A provider may technically support a control but perform it poorly.

Use:

```json
{
  "provider_control_profile": {
    "provider": "X",
    "control": "multi_actor_contact",
    "support": "semantic",
    "empirical": {
      "attempts": 100,
      "success_rate": 0.37,
      "common_failures": [
        "penetration",
        "actor_merge",
        "missed_contact"
      ]
    }
  }
}
```

This lets routing distinguish:

```text
supported
```

from:

```text
dependably supported
```

---

# 27. ControlCarrier

Text formats are not the complete carrier space.

A motion compiler may need:

```text
natural language
structured text
reference image
identity reference
first frame
last frame
first + last frame
pose
skeleton
depth
mask
trajectory
control video
reference video
audio timing
postproduction
```

Use:

```json
{
  "control_carrier": {
    "semantic_control": "exact_hand_trajectory",
    "preferred": "pose_or_control_video",
    "fallbacks": [
      "reference_video",
      "natural_language"
    ],
    "reason": "trajectory precision exceeds reliable text expression"
  }
}
```

The exact supported carrier set must be populated from current provider documentation and empirical tests, not assumed universally.

---

# 28. FallbackStrategy

Recommended general ladder:

```text
native structured control
↓
native reference/conditioning
↓
semantic text
↓
behavioral realization text
↓
shot decomposition
↓
postproduction
↓
provider substitution
↓
unsupported
```

This should be capability- and reliability-aware.

A failure at one carrier should not immediately mean unsupported if another carrier can express the same semantic requirement.

---

# 29. Shot decomposition

The compiler should split a request when control complexity exceeds reliable provider capacity.

Risk signals:

```text
actor_count
simultaneous_primitive_count
contact_count
causal_depth
occlusion_burden
camera_complexity
identity_burden
retargeting_complexity
secondary_motion_complexity
```

Example:

```json
{
  "risk_profile": {
    "actor_count": 3,
    "contact_count": 4,
    "camera_complexity": "high",
    "identity_burden": "high"
  },
  "strategy": "decompose"
}
```

Preferred split boundaries:

```text
stable state
interaction outcome
camera reset
identity/visibility bridge
```

---

# 30. Control priority and conflict

Use explicit hardness:

```text
locked
required
high
medium
low
optional
```

Recommended default precedence:

```text
explicit locked user constraint
>
identity/continuity invariant
>
world/physical safety invariant
>
required action semantics
>
explicit shot direction
>
profile rule
>
research recommendation
>
style preference
>
provider embellishment
```

This is a CPCS policy, not an external scientific law.

Conflicts should produce a structured record:

```json
{
  "control_conflict": {
    "controls": [
      "exact_contact",
      "no_penetration"
    ],
    "resolution": "preserve_no_penetration",
    "reason_code": "geometry_safety_overrides_exact_site"
  }
}
```

---

# 31. Attention-budget compiler

Canonical MX may be extremely detailed.

Provider input should be minimal sufficient information.

```text
canonical motion graph
    ↓
locked constraints
    ↓
salience
    ↓
observability
    ↓
provider capability
    ↓
provider reliability
    ↓
semantic redundancy collapse
    ↓
attention/token budget
    ↓
minimal sufficient carrier
```

This is not merely token optimization.

It is semantic prioritization.

---

# 32. Semantic redundancy compression

Do not emit:

```text
fast
rapid
sudden
explosive
quick
accelerated
high-energy
```

as seven independent controls when they target one mechanism.

Create:

```json
{
  "control_composition": {
    "group": "rapid_onset",
    "members": [
      "fast",
      "sudden",
      "rapid_acceleration"
    ],
    "projection": {
      "max_equivalent_controls": 1
    }
  }
}
```

The compiler should select the strongest provider-compatible representation.

---

# 33. Evidence taxonomy must be orthogonal

Do not use one enum containing:

```text
measured
derived
authored
unknown
```

These describe different dimensions.

Use:

## Knowledge basis

```text
source_established
source_supported
cpcs_policy
experimental_hypothesis
```

## Acquisition/derivation

```text
authored
observed
detected
measured
estimated
inferred
derived
simulated
```

## Epistemic state

```text
known
uncertain
unknown
unobservable
contradictory
```

## Confidence

A separate field:

```json
{
  "confidence": {
    "value": 0.91,
    "basis": "detector_probability",
    "calibration_status": "uncalibrated"
  }
}
```

This must be shared across 01/02/03.

---

# 34. Derived measurements must remain derived

If:

```text
pose estimator
→ position
→ numerical differentiation
→ velocity
```

then velocity is not independently "measured" merely because the source system is a detector.

Use:

```json
{
  "velocity": {
    "acquisition": "derived",
    "source_acquisition": "detected",
    "derivation": "central_difference"
  }
}
```

The same applies to:

```text
velocity
→ acceleration
→ force estimate
```

Uncertainty should propagate rather than disappear.

---

# 35. Uncertainty propagation

Conceptually:

```text
position uncertainty
    ↓
velocity uncertainty
    ↓
acceleration uncertainty
    ↓
dynamic estimate uncertainty
```

Store derivation references:

```json
{
  "uncertainty": {
    "basis": "propagated",
    "source_refs": [
      "position_uncertainty_01",
      "timebase_uncertainty_01"
    ]
  }
}
```

Do not allow a high-confidence position detector to produce a falsely precise acceleration merely because differentiation returns a number.

---

# 36. Simulation provenance

If a quantity is simulated:

```json
{
  "simulation_ref": {
    "solver": "solver_id",
    "timestep": 0.008333,
    "mass_model": "mass_profile_01",
    "contact_model": "contact_model_02",
    "gravity": [0, -9.81, 0],
    "friction_model": "model_03",
    "initial_conditions_ref": "ic_01"
  }
}
```

Exact simulation parameters need not all live in canonical motion IR, but reproducibility metadata must remain accessible.

---

# 37. Affordance constraints

Motion reasoning needs to know what the environment permits.

```json
{
  "affordance": {
    "entity": "door",
    "capabilities": [
      "graspable",
      "hinge_rotatable"
    ],
    "constraints": {
      "axis": "vertical",
      "rotation_range": "model_defined"
    }
  }
}
```

Examples:

```text
handle → graspable
chair → support/sittable
ground → supportable
water → penetrable
wall → blocking
door → hinge rotation
```

This prevents semantically valid movement from becoming physically nonsensical interaction.

---

# 38. Complexity/risk vector

Use a vector rather than an unexplained scalar:

```json
{
  "risk_profile": {
    "actor_count": 3,
    "simultaneous_primitives": 5,
    "causal_depth": 4,
    "contact_count": 3,
    "occlusion_burden": "high",
    "camera_complexity": "high",
    "identity_burden": "high",
    "retargeting_complexity": "medium",
    "secondary_motion_complexity": "low"
  }
}
```

Risk drives strategy:

```text
high contact + high camera
→ simplify camera

high identity + high occlusion
→ stronger reference/conditioning

high action density
→ shot decomposition

high retarget complexity
→ stronger target constraints / pre-solve
```

---

# 39. VerificationExpectation

Metrics alone are not acceptance rules.

Use:

```json
{
  "verification_expectation": {
    "target": "right_hand_contacts_handle",
    "expectation": {
      "contact_distance": "near_zero",
      "identity": "same_actor",
      "side": "right"
    },
    "metrics": [
      "contact_distance",
      "identity_continuity"
    ],
    "threshold": {
      "status": "experimental",
      "contact_distance_max": null
    },
    "priority": "required",
    "fail_if_exceeded": true
  }
}
```

Thresholds should be measured/calibrated.

---

# 40. FailureSignature

Verification should identify the mechanism of failure.

```json
{
  "failure_signature": {
    "type": "foot_slide",
    "observations": [
      "support_contact_present",
      "foot_velocity_above_threshold"
    ],
    "likely_owners": [
      "support_state",
      "contact_constraint",
      "retargeting"
    ]
  }
}
```

Examples:

```text
foot_slide
→ support/contact/retarget

identity_swap
→ continuity/identity/reference

body_penetration
→ contact_geometry/IK

water_effect_detached
→ material_response/causal_binding

whole_clip_fast
→ scope/lifetime/envelope

left_right_swap
→ side/mirror mapping
```

---

# 41. RepairStrategy

The operational loop should be:

```text
target
→ compile
→ generate
→ observe
→ verify
→ failure signature
→ responsible layer
→ smallest localized repair
→ regenerate
```

Example:

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

---

# 42. ControlDecision

Record structured decision provenance, not hidden reasoning.

```json
{
  "control_decision": {
    "intent_ref": "intent_42",
    "action_template": "strike",
    "selected_branch": "near_miss",
    "selected_controls": [
      "shift_weight",
      "reach",
      "sharp_contact_accent"
    ],
    "rejected_controls": [
      "impact_deformation"
    ],
    "provider_profile": "provider_X_v7",
    "rationale_codes": [
      "near_miss_branch",
      "provider_contact_unreliable"
    ]
  }
}
```

This makes the system auditable.

---

# 43. Abstention

The reasoner must be able to decline a semantic mapping.

```json
{
  "decision": {
    "outcome": "abstain",
    "reason": "unsupported_mapping",
    "missing_evidence": [
      "target_geometry"
    ]
  }
}
```

Valid outcomes:

```text
select
degrade
decompose
fallback
abstain
reject
```

Forcing a primitive selection when evidence is insufficient is worse than returning `unknown`.

---

# 44. Carrier selection is a semantic decision

Carrier selection should be based on:

```text
control precision required
+
provider support
+
provider empirical reliability
+
observability
+
attention budget
```

Examples:

```text
identity preservation
→ identity/reference carrier

exact pose
→ pose/reference/control video where supported

trajectory shape
→ trajectory/control video where supported

general movement quality
→ behavioral NL

timing relationship
→ structured timing + NL if supported

complex choreography
→ decomposition
```

Do not assume prose is the universal carrier.

---

# 45. Text-format experiment must be separated from carrier experiment

The previous five-format test should be split.

## Semantic representation test

```text
YAML
JSON
XML
NL
```

Test:

```text
semantic preservation
validation
ordering
ambiguity
token cost
model adherence
```

## Observation stream

```text
JSONL
```

is not part of semantic round-trip equivalence.

It belongs to:

```text
render
→ observe
→ audit
```

pipeline.

## Control-carrier test

```text
NL
reference image
pose
control video
first/last frame
etc.
```

Test:

```text
motion fidelity
identity fidelity
spatial fidelity
temporal fidelity
```

---

# 46. Temporal precision must be provider-qualified

Do not automatically emit:

```text
1.20 seconds
1.70 seconds
1.78 seconds
```

to every provider.

Represent:

```text
exact_timestamp
approximate_timestamp
relative_phase
sequence_only
unsupported
```

Then compile according to empirical provider behavior.

If exact timestamps are unreliable:

```text
1.20–1.30
```

may become:

```text
early preparation
```

and:

```text
1.50–1.70
```

may become:

```text
late deceleration before contact
```

The semantic target remains intact while the carrier becomes provider-compatible.

---

# 47. Provider reliability matrix

For each provider/control pair:

```text
support class
empirical success
sample size
failure classes
tested versions
carrier
conditions
```

Example:

```json
{
  "provider": "X",
  "control": "multi_actor_contact",
  "support": "semantic",
  "carrier": "text",
  "empirical": {
    "attempts": 100,
    "success_rate": 0.37
  },
  "failure_classes": [
    "penetration",
    "identity_merge"
  ]
}
```

This becomes a routing input.

---

# 48. What should NOT be added

Do not respond to these gaps by creating:

```text
another graph database
another ontology
another motion dictionary
another prompt DSL
another universal numeric style scale
another LLM-only reasoning layer
```

The missing capability is primarily **typed operational knowledge + control composition + execution state + verification**, not more storage infrastructure.

---

# 49. P0 implementation order

## P0-A — shared contracts

1. Shared evidence taxonomy.
2. Shared `ControlScope`.
3. Shared `ControlLifetime`.
4. Shared `ControlPriority`.
5. Shared `SpatialState`.
6. Shared `ContinuityState`.
7. Shared `PersistenceConstraint`.

## P0-B — MX grammar

8. Typed primitive/modifier/phase/event classes.
9. `ActionTemplate`.
10. `ActionBranch`.
11. `MotionRealization`.
12. `SupportState`.
13. `ContactSemantic`.
14. `ContactGeometry`.

## P0-C — compilation

15. `ControlEnvelope`.
16. `ControlComposition`.
17. `ControlCarrier`.
18. provider reliability profile.
19. fallback strategy.
20. attention-budget projection.
21. shot decomposition.

## P0-D — verification

22. `VerificationExpectation`.
23. `FailureSignature`.
24. `RepairStrategy`.
25. `ControlDecision`.
26. localized regeneration.

---

# 50. Required fixtures for the P0 layer

The fixture corpus should explicitly test:

1. heavy punch with successful contact;
2. heavy punch near-miss;
3. blocked punch;
4. punch with camera movement;
5. left/right mirrored strike;
6. two actors maintaining screen sides;
7. actor occlusion with identity persistence;
8. object occlusion with object persistence;
9. planted foot during root motion;
10. weight transfer into strike;
11. unreachable target during retargeting;
12. retargeted short-limb actor;
13. hand-object grasp/release;
14. water impact and causal splash;
15. cloth lag from torso rotation;
16. multi-actor contact plus complex camera;
17. provider with unreliable contact control;
18. exact timestamp unsupported by provider;
19. semantic redundancy overload;
20. local foot-slide repair.

---

# 51. Required acceptance tests

## Action selection

```text
input:
"character throws a heavy punch"

expected:
ActionTemplate = strike
branch = unresolved until target outcome specified
realization = action-conditioned heavy mapping
```

## Near miss

```text
input:
"punch narrowly misses"

expected:
near_miss branch
no impact deformation
evasion/avoidance response allowed
```

## Spatial continuity

```text
input:
"A remains screen-left of B"

expected:
persistence across the shot unless explicitly changed
```

## Support

```text
input:
"plant the left foot and pivot"

expected:
left foot support persists through pivot phase
```

## Scope

```text
input:
"accelerate the right arm during execution"

expected:
no global actor-speed modification
```

## Lifetime

```text
input:
"brief recoil"

expected:
recoil does not persist into unrelated later action
```

## Retarget

```text
input:
shorter actor reaches handle

expected:
bounded adaptation or explicit failure
never silent target substitution
```

## Verification repair

```text
failure:
foot_slide

expected:
repair targets support/contact/retarget layer
not entire prompt rewrite
```

---

# 52. Research questions that remain genuinely empirical

These should not be filled with invented constants.

1. Which primitive decompositions produce the most consistent provider motion?
2. Which action-conditioned realization features actually improve video adherence?
3. What contact-distance/velocity thresholds distinguish convincing contact from near-contact for each media regime?
4. Which support metrics correlate with perceived physical grounding?
5. Which carriers best preserve trajectory versus identity versus interaction?
6. What control density causes provider degradation?
7. When does shot decomposition improve results versus reduce continuity?
8. Which semantic redundancy rules improve adherence?
9. What retargeting errors are perceptually acceptable?
10. What provider-specific temporal precision is real rather than nominal?

Each should have a fixture and measurable outcome before becoming a hard CPCS rule.

---

# 53. Primary evidence anchors

The following external sources support the mechanical boundaries used in this closure:

### Unreal Engine Control Rig / Full Body IK

Epic documents Full Body IK as a procedural adjustment system using effectors, root behavior, stiffness, preferred angles and joint limits, including ground alignment and reaching. This directly supports treating support, effectors, limits and retargeting as explicit controls rather than prose-only intent.

### Unreal Engine IK Retargeting

Epic documents retargeting across skeletal meshes with different bone counts, names and orientations and describes preserving precise hand/foot contact through IK. This supports semantic invariants plus morphology-dependent recomputation.

### MediaPipe Pose Landmarker

Google documents both image-space and 3D world landmarks and identifies visibility/landmark semantics. This supports preserving source coordinate semantics rather than collapsing all detections into generic world coordinates.

### Human-video generation research

Recent research continues to identify identity consistency, motion controllability, semantic consistency and inter-shot consistency as separate problems. This supports making identity/continuity, motion control and shot decomposition explicit rather than treating them as one prompt property.

---

# 54. Final P0 closure matrix

| Gap | Why it matters | Required representation | Owner | Verification |
|---|---|---|---|---|
| Action selection | prevents primitive guessing | `ActionTemplate` | MX | selected template |
| Primitive typing | prevents semantic category mixing | typed grammar | MX | schema |
| Branching outcomes | prevents accidental impacts/misses | `ActionBranch` | MX | outcome fidelity |
| Spatial state | preserves directorial geometry | `SpatialState` | universal/MX reference | relation persistence |
| Direction frame | prevents ambiguous forward/right | typed direction | universal | frame preservation |
| Continuity | prevents identity disappearance | `ContinuityState` | universal | identity continuity |
| Object persistence | prevents prop replacement | `PersistenceConstraint` | universal | object identity |
| Scope | prevents control contamination | `ControlScope` | universal | scope isolation |
| Lifetime | prevents temporal leakage | `ControlLifetime` | universal | interval isolation |
| Envelope | enables temporal shaping | `ControlEnvelope` | universal/MX | profile similarity |
| Support | grounds whole-body motion | `SupportState` | MX | foot/COM metrics |
| Contact semantics | defines interaction meaning | `ContactSemantic` | MX | branch consistency |
| Contact geometry | defines physical relation | `ContactGeometry` | MX | distance/penetration |
| Realization | converts adjectives into mechanics | `MotionRealization` | MX | observable target adherence |
| Material response | binds effects causally | `MaterialResponse` | MX | effect origin/persistence |
| Retarget invariants | preserves action identity | `RetargetContract` | MX | semantic equivalence |
| Reachability | prevents silent semantic changes | `RetargetFailurePolicy` | MX | failure behavior |
| Provider reliability | distinguishes support from success | reliability profile | provider adapter | empirical success |
| Carrier selection | avoids prose-only control | `ControlCarrier` | compiler | carrier fidelity |
| Fallback | prevents premature failure | `FallbackStrategy` | compiler | degradation record |
| Decomposition | controls complexity | `RiskProfile` + policy | compiler | shot-level success |
| Priority | resolves conflicts | `ControlPriority` | universal | deterministic arbitration |
| Attention budget | prevents overloading provider | `ControlComposition` | compiler | adherence vs density |
| Verification | converts metrics into gates | `VerificationExpectation` | verifier | pass/fail |
| Failure localization | identifies responsible layer | `FailureSignature` | verifier | owner accuracy |
| Repair | closes runtime loop | `RepairStrategy` | execution | localized recovery |
| Decision provenance | makes routing auditable | `ControlDecision` | execution | decision trace |

---

# 55. Final architecture

The target MX architecture is:

```text
                 CREATIVE INTENT
                       │
                       ▼
              DIRECTOR CHARACTERIZATION
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      action        spatial        constraints
      intent         state
        │              │
        └──────────────┼──────────────┘
                       ▼
                ACTION TEMPLATE
                       │
                       ▼
                 BRANCH SELECT
                       │
                       ▼
                MOTION GRAMMAR
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   primitives       phases        modifiers
        │              │              │
        └──────────────┼──────────────┘
                       ▼
          SUPPORT / CONTACT / CONTINUITY
                       │
                       ▼
              MOTION REALIZATION
                       │
                       ▼
             CONTROL COMPOSITION
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      scope         lifetime       envelope
        │              │              │
        └──────────────┼──────────────┘
                       ▼
             PRIORITY / CONFLICT
                       │
                       ▼
                RISK ASSESSMENT
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          compile             decompose
             │                   │
             └─────────┬─────────┘
                       ▼
                CARRIER SELECT
                       │
                       ▼
              PROVIDER COMPILER
                       │
                       ▼
                    RENDER
                       │
                       ▼
                    VOG
                       │
                       ▼
                 MEASUREMENT
                       │
                       ▼
                 VERIFICATION
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
           PASS             FAILURE SIGNATURE
                                  │
                                  ▼
                            REPAIR STRATEGY
                                  │
                                  ▼
                         LOCAL REGENERATION
```

---

# Final verdict

The heaviest research conclusion is not "add more motion concepts."

It is:

> **CPCS-MX needs to become a motion decision-and-control grammar, not merely a motion representation grammar.**

The highest-value additions are therefore:

1. `ActionTemplate`
2. typed primitive/modifier/phase/event system
3. `SpatialState`
4. `ContinuityState` / persistence
5. `SupportState`
6. `ContactSemantic` + `ContactGeometry`
7. `MotionRealization`
8. `ControlScope` + `ControlLifetime` + `ControlEnvelope`
9. priority/conflict/composition
10. `ControlCarrier` + empirical provider reliability
11. complexity/risk + shot decomposition
12. verification expectation → failure signature → repair

Those twelve close the path from:

```text
"I want a heavy punch that narrowly misses while
the camera tracks around both actors"
```

to:

```text
action selection
→ branch = near_miss
→ heavy × strike realization
→ support/weight-transfer plan
→ right/left spatial invariants
→ contact geometry = near-contact
→ camera/actor complexity assessment
→ carrier/fallback selection
→ generation
→ objective verification
→ localized repair
```

That is the level at which 03 becomes genuinely useful to an autonomous coding/reasoning agent rather than simply being a sophisticated motion schema.


---

# 56. Due-diligence expansion: concepts that were still missing

The first P0 closure was still too compiler-centric. A deeper cross-check against biomechanics, motor-control literature, current animation systems, and current controllable human-motion generation reveals several additional concepts that should be explicitly represented or at least made first-class reasoning primitives.

These are not "more ontology for ontology's sake." They answer specific questions that the previous P0 layer still could not answer deterministically.

---

# 57. Task-space vs joint-space is a foundational distinction

MX currently represents joints, trajectories, contacts and primitives, but the architecture needs an explicit distinction between:

```text
TASK SPACE
what must happen in the world

JOINT SPACE
how the body realizes it
```

Example:

```text
task:
    right hand reaches handle

task-space constraints:
    hand contacts handle
    handle identity preserved
    approach direction acceptable

joint-space realization:
    shoulder rotation
    elbow flexion
    wrist orientation
    torso compensation
    pelvis adjustment
```

This matters because there are usually many valid joint configurations for one task outcome. Human motor-control literature explicitly treats motor redundancy/abundance as a central property of movement rather than assuming one unique joint solution. citeturn1search3turn1search7

### Required representation

```yaml
task_constraint:
  target: right_hand
  objective:
    type: reach
    target_entity: handle

  task_space:
    position: required
    orientation: preferred
    contact: required

  joint_space:
    solution: adaptable
```

**Key rule:**

> Do not over-specify joint motion when the director only specified a task-space outcome.

This is a major missing principle.

---

# 58. Null-space / allowable variation needs representation

If:

```text
hand must reach target
```

there are many acceptable:

```text
elbow angles
torso angles
wrist configurations
pelvis adjustments
```

The compiler therefore needs to distinguish:

```text
locked variables
required task variables
preferred variables
free variables
```

This is more precise than a generic priority enum.

```yaml
constraint:
  variable: elbow_orientation
  status: free
  reason: task_outcome_unaffected
```

The purpose is to prevent the compiler from accidentally eliminating physically plausible solutions.

This is directly aligned with research on motor abundance and synergies, where multiple joint configurations can preserve task performance. citeturn1search3turn1search14

---

# 59. Constraint hierarchy needs feasibility, not just priority

Priority alone is insufficient.

Suppose:

```text
hand must touch handle
foot must remain planted
knee has joint limit
torso must remain upright
```

The system needs to determine whether the constraints can be jointly satisfied.

Therefore add:

```text
ConstraintSet
ConstraintHardness
ConstraintFeasibility
ConstraintRelaxation
```

Example:

```yaml
constraint_set:
  hard:
    - actor_identity
    - required_contact
    - no_penetration

  soft:
    - torso_upright
    - stylistic_arm_path

  relaxation_order:
    - stylistic_arm_path
    - torso_upright

  infeasible:
    action: reject_or_decompose
```

This is different from simply saying one control has priority over another.

---

# 60. Feasibility must precede provider compilation

The pipeline should contain:

```text
semantic target
→ constraint compilation
→ feasibility analysis
→ adaptation/decomposition
→ provider compilation
```

not:

```text
semantic target
→ provider prompt
→ discover impossibility afterward
```

Feasibility checks can include:

```text
reachability
joint limits
collision
support
contact geometry
actor spacing
camera visibility
trajectory bounds
provider capability
```

A semantically impossible request should be rejected, adapted, or decomposed before expensive generation.

---

# 61. Motor synergies should be a first-class reasoning concept

The current primitive model is still too atomized.

Human movement is often coordinated through multi-joint patterns rather than independent joint commands. Research on motor synergies describes hierarchical coordination across levels and task-dependent combinations. citeturn1search6turn1search14

For MX, this suggests:

```text
MotionPrimitive
    ↓
CoordinationPattern / Synergy
    ↓
joint realization
```

Example:

```yaml
coordination_pattern:
  id: strike_chain
  purpose: transfer movement through body

  components:
    - pelvis_rotation
    - trunk_rotation
    - shoulder_rotation
    - elbow_extension
    - wrist_alignment

  coupling:
    type: proximal_to_distal

  task_invariant:
    hand_velocity_at_contact: required
```

This is far more useful than independently selecting six joint actions.

---

# 62. Proximal-distal sequencing needs explicit status

The earlier "heavy punch" example uses:

```text
proximal → distal
```

but MX should distinguish:

```text
research-supported coordination principle
```

from:

```text
CPCS stylistic realization
```

This matters because not every movement is best described by one universal proximal-distal chain.

Use:

```yaml
coordination_rule:
  id: proximal_distal_transfer
  applicability:
    action_classes:
      - strike
      - throw
  status:
    evidence: source_supported
    universality: conditional
```

That prevents an illustrative choreography pattern from becoming a false universal law.

---

# 63. Anticipatory and compensatory control should be separated

"Anticipation" currently exists as a phase, but there is a deeper distinction:

```text
anticipatory postural adjustment
vs
compensatory postural adjustment
```

APAs occur before predictable perturbations and help prepare or initiate movement; compensatory adjustments respond after perturbation. citeturn1search0turn1search1turn1search2

Therefore:

```text
anticipation
```

as a narrative phase is not equivalent to:

```text
APA
```

Add:

```text
PosturalStrategy:
    anticipatory
    reactive
    mixed
```

Example:

```yaml
postural_strategy:
  type: anticipatory
  trigger: upcoming_strike
  objective:
    - preserve_balance
    - prepare_weight_transfer
```

This is a high-value distinction for realistic whole-body motion.

---

# 64. Center of pressure is missing from SupportState

The first closure added COM and support, but a deeper biomechanics review shows that COM alone is insufficient.

For standing balance, COM, base of support and center of pressure interact; postural adjustments actively manipulate these relationships. citeturn1search1turn1search11

Add:

```text
COM
BOS
COP
ground_reaction
```

at least semantically.

```yaml
support_state:
  center_of_mass:
    relation: inside_base

  center_of_pressure:
    movement: forward

  base_of_support:
    geometry: bilateral

  ground_reaction:
    status: inferred
```

Do not require exact force-platform measurements for ordinary video generation. The semantic variables are sufficient when the underlying evidence is absent.

---

# 65. Dynamic balance needs a state model

Static:

```text
COM inside BOS
```

is not enough for walking, running, jumping or directional changes.

The system needs:

```text
stable
controlled_instability
transition
recovery
loss_of_balance
```

Example:

```yaml
balance_state:
  state: controlled_instability
  phase: initiation
  recovery_plan:
    required: true
```

Current motor-control research describes dynamic movement as repeated transitions involving anticipatory and compensatory control rather than static balance alone. citeturn1search10turn1search11

---

# 66. Momentum and impulse are missing

The MX model currently discusses acceleration and force, but a motion director often needs:

```text
momentum
impulse
angular momentum
deceleration
energy transfer
```

These are different from instantaneous force.

For example:

```text
heavy
```

may be visually realized through:

```text
large momentum
rapid momentum transfer
strong deceleration
visible recoil
longer settling
```

rather than an arbitrary numeric force.

The canonical model should therefore allow:

```yaml
dynamic_intent:
  momentum:
    qualitative: high

  impulse:
    qualitative: sharp

  angular_momentum:
    qualitative: high

  force_value:
    status: unspecified
```

This keeps dynamics conceptually correct without fabricating physical measurements.

---

# 67. Inertia and mass distribution matter for retargeting

Two characters with identical joint angles can look very different because:

```text
segment lengths
mass distribution
limb proportions
center of mass
moment of inertia
```

differ.

The retargeting model currently focuses heavily on skeletal geometry.

Add:

```text
mass_profile
inertial_profile
center_of_mass_profile
```

when dynamics or grounded motion are being modeled.

If unavailable:

```text
status: unknown
```

not an invented human default.

---

# 68. Friction and surface properties are missing

Support is not determined solely by contact.

Walking, stopping, sliding, pushing and landing depend on surface conditions.

At minimum:

```text
surface_type
support
friction_class
compliance
slope
roughness
```

Example:

```yaml
surface:
  id: wet_floor
  support: yes
  friction:
    class: low
  slope:
    status: unknown
```

This is especially important for:

```text
sliding
running stops
foot planting
falls
pushing
pulling
```

Do not invent a coefficient of friction unless the source or simulation supplies one.

---

# 69. Contact is not binary; contact state machines are needed

The earlier semantic/geometry split is still insufficient.

A contact evolves:

```text
approach
→ near_contact
→ contact_onset
→ sustained_contact
→ slip/roll/stick
→ release
→ separation
```

Use:

```text
ContactStateMachine
```

This is particularly important for:

```text
grasp
push
pull
carry
sit
stand
climb
land
impact
```

Example:

```yaml
contact_state:
  current: sustained
  transitions:
    sustained:
      - release
      - slip
      - separation
```

---

# 70. Stick/slip behavior is a major missing interaction concept

For object interactions:

```text
hand moves with object
```

is different from:

```text
hand slides along object
```

Add:

```text
contact_mode:
    stick
    slip
    roll
    detach
```

This provides a much stronger basis for:

```text
grasp
drag
push
pull
slide
climb
```

than a generic `contact` event.

---

# 71. Object state must be coupled to actor state

The earlier closure added object persistence but not full interaction coupling.

For a held object:

```text
actor hand
↔ object transform
↔ contact
↔ object response
```

should be one coupled execution relationship.

CVPR work on human-object interaction generation explicitly models human motion, object motion and contact as interdependent rather than independent streams. citeturn2search2

Therefore add:

```text
InteractionCoupling
```

Example:

```yaml
interaction_coupling:
  actor: A
  effector: right_hand
  object: hammer

  coupling:
    mode: grasped

  object_motion:
    source: actor_motion

  release_event:
    unlocks_object_motion: true
```

---

# 72. Moving targets require prediction semantics

A target can move while an actor reaches toward it.

The MX model needs:

```text
target_state
target_velocity
target_prediction_horizon
interception_point
```

Examples:

```text
catch ball
hit moving target
grab moving object
follow another actor
```

This is a distinct reasoning class from static reachability.

```yaml
target:
  state: moving
  predicted_position:
    horizon: relative_time
  interaction:
    mode: interception
```

---

# 73. Relative motion should be first-class

For multi-actor choreography, absolute positions are often less useful than:

```text
relative distance
relative velocity
relative heading
relative orientation
relative phase
```

Example:

```yaml
relative_motion:
  subject: actor_A
  reference: actor_B

  distance:
    trend: decreasing

  relative_heading:
    trend: converging

  phase_relation:
    value: synchronized
```

This is essential for:

```text
chase
fight
dance
conversation
passing
catching
group movement
```

---

# 74. Multi-actor coordination needs role semantics

Do not treat actors as independent motion graphs when the action is relational.

Add:

```text
leader
follower
target
initiator
responder
counterpart
observer
```

Example:

```yaml
interaction_roles:
  initiator: actor_A
  responder: actor_B
  target: actor_B
```

Then:

```text
A strikes
→ B reacts
```

becomes a causal coupled action rather than two unrelated actions.

---

# 75. Coupled timing needs relative phase

Two actors can be:

```text
simultaneous
offset
counterphase
leader-follow
reaction-delayed
```

Use:

```yaml
coordination:
  actor_A:
    phase: execution

  actor_B:
    phase_relation:
      type: delayed_response
      offset: relative
```

Do not force all synchronization into exact timestamps.

---

# 76. Gaze/head/body coordination is still under-specified

02 may own expressive/gaze semantics, but MX needs to consume the control mechanically.

A motion can require:

```text
eyes target
head follows
torso follows partially
body remains oriented elsewhere
```

That is a coordination pattern.

Example:

```yaml
gaze_body_coupling:
  gaze_target: actor_B
  head_follow: partial
  torso_follow: delayed
  lower_body_orientation: independent
```

This is particularly important for believable dialogue, surveillance, pursuit and reaction shots.

---

# 77. Visibility and line-of-sight are control constraints

Spatial state needs:

```text
visible
occluded
partially_occluded
line_of_sight
screen_overlap
depth_order
```

Example:

```yaml
visibility_constraint:
  subject: actor_B
  observer: camera
  requirement: face_visible
  interval: reaction_phase
```

This converts camera composition from a separate concern into a constraint on motion.

---

# 78. Camera-subject coupling needs parallax semantics

Camera and actor motion are correctly separated, but they also interact perceptually.

The same actor trajectory can look different under:

```text
locked camera
dolly
tracking
orbit
handheld
zoom
```

Therefore MX needs a semantic relation:

```text
camera_motion
↔ subject_motion
```

Example:

```yaml
camera_subject_relation:
  subject: actor_A
  camera_mode: tracking
  framing:
    preserved: medium_shot
  relative_screen_motion:
    target: stable
```

Current human-video motion research explicitly treats camera trajectories and human pose as joint spatio-temporal control variables rather than unrelated signals. citeturn1academia85

---

# 79. Root trajectory and body pose must be separately controllable

This distinction is important enough to be explicit:

```text
root trajectory
≠
local body motion
```

A character can:

```text
run forward
while upper body rotates
```

or:

```text
stand in place
while performing a large gesture
```

Current Motion Matching systems explicitly query both pose and trajectory features, including position, velocity and phase, and weight trajectory separately from pose. citeturn2search0

Therefore:

```text
RootMotionPlan
+
LocalMotionPlan
```

should be separate but coordinated.

---

# 80. Trajectory needs history and prediction

A single current position is inadequate for motion control.

Motion Matching explicitly uses trajectory samples at offsets in the past/future and pose history to select motion. citeturn2search0

MX should support:

```text
past trajectory
current state
future intent trajectory
```

Example:

```yaml
trajectory:
  history:
    required: true

  current:
    pose_ref: current

  prediction:
    horizon: relative
    samples:
      - early
      - middle
      - late
```

This is much stronger than one `trajectory` object.

---

# 81. Motion phase should not be only narrative phase

There are at least three temporal organizations:

```text
narrative phase
action phase
kinematic phase
```

Example:

```text
narrative beat:
    attack

action:
    punch

kinematic:
    preparation
    acceleration
    contact
    deceleration
```

These must be linked, not conflated.

Motion Matching also treats phase as a searchable motion feature, reinforcing that phase can be computationally useful rather than merely narrative. citeturn2search0

---

# 82. Transition compatibility is missing

Every action should specify:

```text
allowed predecessors
allowed successors
transition cost
required bridge
```

Example:

```yaml
transition:
  from: run
  to: strike

  compatibility:
    status: valid

  bridge:
    required:
      - deceleration
      - support_adjustment
```

This prevents impossible concatenations such as:

```text
airborne spin
→ instantaneous planted strike
```

without a transition state.

---

# 83. Motion blending is not the same as semantic transition

A numerical blend can produce a visually smooth interpolation while semantically destroying the action.

Therefore distinguish:

```text
geometric blend
semantic transition
```

A valid transition needs:

```text
identity continuity
support continuity
contact continuity
action phase compatibility
trajectory continuity
```

---

# 84. Loop closure is missing

For repeated actions:

```text
walk
run
idle
breathing
gestures
cyclic dance
```

the compiler needs:

```text
cycle_start
cycle_end
phase_alignment
state_equivalence
closure_error
```

Example:

```yaml
cycle:
  mode: loop
  closure:
    required:
      - root_continuity
      - phase_continuity
      - support_continuity
```

---

# 85. Motion smoothness needs multiple levels

Do not collapse smoothness into one metric.

At least distinguish:

```text
position continuity
velocity continuity
acceleration continuity
jerk continuity
semantic continuity
```

A movement can be geometrically smooth but semantically wrong.

Example:

```text
hand trajectory smooth
but contact occurs too early
```

Therefore verification should identify which continuity layer failed.

---

# 86. Curvature and path shape are missing

Trajectory is not only:

```text
position + velocity
```

For directing:

```text
straight
arc
spiral
hook
S-curve
approach-and-retreat
```

can matter.

Use:

```yaml
path_geometry:
  family: arc
  curvature:
    qualitative: moderate
  direction_change:
    count: 1
```

Avoid exact curvature unless measured or authored.

---

# 87. Timing profile is distinct from duration

Two actions can have identical duration but different temporal profiles:

```text
constant
early burst
late burst
ease-in
ease-out
symmetric pulse
hold-release
```

Use:

```yaml
timing_profile:
  duration: relative
  velocity_profile: late_burst
```

This is especially important for "snappy", "deliberate", "hesitant", and "explosive."

---

# 88. Variability should be controlled, not eliminated

Realistic motion is not perfectly identical on every repetition.

Motor-control research describes "repetition without repetition": task outcomes can remain stable while kinematic details vary. citeturn1search18turn1search3

Therefore MX should distinguish:

```text
required invariant
from
allowed variation
```

Example:

```yaml
variation_policy:
  invariant:
    - target_contact
    - actor_identity

  variable:
    - elbow_path
    - torso_micro_adjustment

  variability:
    level: moderate
```

This is a major anti-overconstraint principle.

---

# 89. Symmetry and asymmetry need explicit semantics

A motion can be:

```text
bilateral symmetric
bilateral asymmetric
alternating
mirrored
same-side
cross-body
```

Use:

```yaml
laterality:
  mode: unilateral
  side: right
  mirror_allowed: true
```

and:

```yaml
symmetry:
  type: asymmetric
  relationship: complementary
```

Do not treat mirror as simple text replacement.

---

# 90. Motion style needs mechanics, not adjective accumulation

Style controls should map into measurable/observable dimensions:

```text
amplitude
tempo
onset sharpness
duration
path curvature
symmetry
effort
stability
variability
settling
```

Then:

```text
snappy
```

can become:

```text
short onset
high acceleration
low dwell
rapid recovery
```

rather than a stack of synonyms.

---

# 91. Affordance should include interaction geometry

The previous affordance object is still too categorical.

For an object:

```text
graspable
```

is not enough.

You may need:

```text
grasp region
approach direction
hand orientation
clearance
support region
interaction side
```

Human-object interaction research increasingly uses explicit interaction/contact geometry as an intermediate control signal. citeturn2search2turn1academia85

Example:

```yaml
affordance:
  type: grasp
  target_region: handle
  approach:
    direction: actor_relative
  required_orientation:
    mode: aligned
```

---

# 92. Environment must be represented as a motion constraint field

Instead of:

```text
environment = background
```

MX should allow:

```text
support surfaces
obstacles
clearance regions
interaction surfaces
hazards
occlusion regions
navigation corridors
```

This is supported by recent environment-aware motion matching work, which explicitly couples trajectory, pose and environmental collision constraints. citeturn2academia52

---

# 93. Collision needs self-collision and inter-entity collision

At least distinguish:

```text
self_collision
actor_actor_collision
actor_object_collision
actor_environment_collision
object_environment_collision
```

Then:

```text
collision_policy:
    forbidden
    allowed
    intentional
```

This prevents a meaningful impact from being treated the same as an accidental body intersection.

---

# 94. Occlusion needs an uncertainty-aware hidden-state model

The system should distinguish:

```text
not visible
not present
unknown
estimated behind occluder
```

A hidden hand is not necessarily a missing hand.

The observation layer therefore needs:

```yaml
visibility:
  state: occluded
  hidden_state:
    identity: known
    pose: uncertain
```

This should feed verification without forcing false precision.

---

# 95. Observation filtering must be separated from measurement

A pose pipeline may perform:

```text
detection
→ tracking
→ smoothing
→ interpolation
→ derivative
```

These are not one acquisition event.

Store:

```text
raw_observation
tracked_observation
filtered_observation
derived_measurement
```

This makes velocity/acceleration provenance much stronger.

---

# 96. Time synchronization across modalities is missing

For:

```text
video
audio
pose
camera
object tracking
motion capture
```

the system needs a shared temporal reference.

At minimum:

```text
source_timebase
canonical_timebase
offset
drift
synchronization confidence
```

This is essential when action timing is inferred across heterogeneous observations.

---

# 97. Multi-camera / multi-view fusion should preserve source provenance

If multiple cameras observe the same motion:

```text
camera A
camera B
camera C
```

do not simply merge them into one observation.

Preserve:

```text
source camera
calibration
view confidence
occlusion state
fusion method
```

Otherwise verification cannot determine whether an apparent disagreement is actual motion or viewpoint uncertainty.

---

# 98. Perceptual verification and geometric verification must be separate

A trajectory can be geometrically accurate but visually wrong.

Use at least:

```text
geometric_verification
temporal_verification
interaction_verification
continuity_verification
perceptual_verification
semantic_verification
```

Example:

```text
hand reached mathematically correct point
BUT
motion looked hesitant
```

This is not a geometry failure.

---

# 99. Verification needs invariant vs preference distinction

Some checks should be hard:

```text
identity preserved
no impossible penetration
required contact occurs
side preserved
```

Others are preferences:

```text
graceful
natural
dramatic
fluid
stylized
```

Do not let aesthetic preference failures invalidate a physically valid action unless explicitly requested.

---

# 100. The system needs a "minimum sufficient control" principle

The compiler should solve:

> What is the smallest set of controls required to preserve the requested intent?

Not:

> How many motion concepts can be retrieved?

This follows from the motor-abundance problem and from current motion-matching systems that explicitly weight feature channels and select among many possible motion samples rather than prescribing every degree of freedom. citeturn1search3turn2search0

Representation:

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

---

# 101. The compiler needs a constraint budget and a freedom budget

A good motion specification should contain both:

```text
what must not vary
```

and:

```text
what is intentionally free
```

Example:

```yaml
freedom_budget:
  free:
    - elbow_configuration
    - micro_torso_adjustment

  bounded:
    - root_translation
    - hand_path

  locked:
    - target_identity
    - side
    - contact_outcome
```

This is arguably as important as the control budget.

---

# 102. Current AI-video research reinforces decomposition

Recent work on controllable human video generation separates:

```text
subject
background
trajectory
action
```

and other work explicitly combines camera trajectories and human poses as separate but interacting spatio-temporal controls. citeturn1academia84turn1academia85

This means MX should not collapse:

```text
action
trajectory
camera
appearance
interaction
```

into one "motion prompt."

They need independent controls with explicit coupling.

---

# 103. Long-form motion needs a scheduler

For multi-beat sequences:

```text
beat 1
beat 2
beat 3
...
```

the compiler needs a stateful scheduler that maintains:

```text
actor state
object state
spatial state
support state
continuity state
camera state
active contacts
pending outcomes
```

A long-form motion generator cannot independently solve every beat from scratch.

---

# 104. State transition should be explicit

Use:

```yaml
state_transition:
  from:
    support: bilateral
    object_holder: actor_A
    actor_relation: left_of

  event:
    type: release

  to:
    support: bilateral
    object_holder: none
    object_state: airborne
```

This is much stronger than storing disconnected events.

---

# 105. Event causality needs preconditions and postconditions

Every significant event should support:

```text
preconditions
trigger
effects
postconditions
failure outcomes
```

Example:

```yaml
event:
  id: release_object

  preconditions:
    - object_held_by_actor

  trigger:
    type: hand_open

  effects:
    - remove_hold_constraint

  postconditions:
    - object_no_longer_attached

  failure:
    - grip_persists
```

This turns motion into an executable state-transition system.

---

# 106. Motion should be modeled as constrained state evolution

The deepest architectural formulation is:

```text
STATE_t
+
ACTION_t
+
CONTROL_t
→
STATE_t+1
```

where state contains:

```text
actor pose
actor root
support
contact
object transforms
spatial relations
camera
continuity
phase
```

This is stronger than a simple hierarchy:

```text
scene → shot → beat → action → primitive
```

The hierarchy organizes the content.

The state-transition system governs execution.

Both are required.

---

# 107. Final expanded MX architecture

After the deeper due-diligence sweep, the architecture should be:

```text
CREATIVE INTENT
        ↓
DIRECTOR CHARACTERIZATION
        ↓
TASK MODEL
 ├── actors
 ├── objects
 ├── environment
 ├── goals
 ├── affordances
 ├── spatial relations
 ├── camera relation
 └── constraints
        ↓
ACTION TEMPLATE
        ↓
ACTION BRANCH / OUTCOME
        ↓
STATE + STATE TRANSITION MODEL
 ├── actor state
 ├── object state
 ├── support state
 ├── contact state
 ├── spatial state
 ├── continuity state
 ├── camera state
 └── environment state
        ↓
MOTION GRAMMAR
 ├── primitives
 ├── modifiers
 ├── phases
 ├── synergies
 ├── coordination patterns
 └── trajectories
        ↓
TASK-SPACE CONSTRAINTS
        ↓
JOINT-SPACE REALIZATION
        ↓
FEASIBILITY / REDUNDANCY / FREEDOM ANALYSIS
        ↓
MOTION REALIZATION
        ↓
CONTROL COMPOSITION
 ├── scope
 ├── lifetime
 ├── envelope
 ├── hardness
 ├── priority
 ├── conflict
 └── freedom budget
        ↓
RISK / COMPLEXITY ANALYSIS
        ↓
RETARGET / MORPHOLOGY ADAPTATION
        ↓
CARRIER SELECTION
        ↓
PROVIDER COMPILATION
        ↓
RENDER
        ↓
OBSERVATION
 ├── raw
 ├── tracked
 ├── filtered
 └── derived
        ↓
VERIFICATION
 ├── geometric
 ├── temporal
 ├── semantic
 ├── interaction
 ├── continuity
 └── perceptual
        ↓
FAILURE SIGNATURE
        ↓
LOCAL REPAIR
        ↓
STATE UPDATE
        ↓
NEXT ACTION / BEAT
```

---

# 108. Newly identified P0/P1 boundary

The earlier P0 list should therefore be expanded.

## P0 — must exist before reasoning closure

```text
ActionTemplate
ActionBranch
typed motion grammar
TaskSpaceConstraint
JointSpaceRealization
SpatialState
ContinuityState
PersistenceConstraint
StateTransition
SupportState
BalanceState
ContactStateMachine
ContactSemantic
ContactGeometry
InteractionCoupling
MotionSynergy / CoordinationPattern
ControlScope
ControlLifetime
ControlEnvelope
ConstraintHardness
ConstraintFeasibility
FreedomBudget
MotionRealization
RootMotionPlan
LocalMotionPlan
RelativeMotion
TrajectoryHistoryPrediction
ControlCarrier
ProviderReliability
RiskProfile
VerificationExpectation
FailureSignature
RepairStrategy
```

## P1 — should follow immediately

```text
COM/COP semantics
momentum/impulse
mass/inertia profiles
surface/friction
moving-target prediction
multi-actor roles
relative phase
gaze-body coupling
camera-subject coupling
transition compatibility
loop closure
path curvature
timing profiles
controlled variability
affordance geometry
environment constraint fields
collision classes
observation provenance
multimodal time synchronization
multi-view fusion
perceptual verification
long-form scheduler
```

---

# 109. What the due-diligence changed

The earlier closure treated MX primarily as:

```text
motion representation
+
compiler
+
verification
```

The deeper review shows that the correct model is:

```text
MOTION KNOWLEDGE
+
TASK MODEL
+
STATE MODEL
+
CONSTRAINT MODEL
+
COORDINATION MODEL
+
REALIZATION MODEL
+
COMPILATION MODEL
+
OBSERVATION MODEL
+
VERIFICATION / REPAIR
```

That distinction is important.

The largest remaining conceptual risk was not another missing primitive such as `throw`, `catch`, or `pivot`.

It was that the system still lacked a formal answer to:

> **How does a director-level goal become a feasible task-space constraint, how does MX choose among the many valid body configurations, how does it preserve state across time and actors, and how does it know what it is allowed to leave unspecified?**

The motor-control literature strongly supports treating movement as a redundant, hierarchical coordination problem rather than a one-to-one mapping from intent to joint angles. citeturn1search3turn1search6turn1search14

Current production animation systems independently reinforce several of the same architectural distinctions: trajectory and pose are separate searchable signals; phase is a useful feature; multiple goals/effectors and per-bone constraints coexist; retargeting preserves contact through IK; and animation warping is used to compensate for missing coverage. citeturn2search0turn0search0turn0search2turn2search3

Current human-motion generation research likewise reinforces explicit trajectory, action, camera, object and contact representations rather than relying on unconstrained text alone. citeturn1academia84turn1academia85turn2search2

Therefore the next revision of 03 should **not** be another incremental list of motion concepts. It should close these underlying control abstractions and then populate them with research-backed concepts.
