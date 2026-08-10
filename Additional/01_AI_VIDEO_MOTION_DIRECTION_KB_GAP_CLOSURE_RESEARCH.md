# CPCS AI Video Motion Direction — Research Closure
## 01_AI_VIDEO

**Status:** research closure v1.1 — continuity/causality closure applied
**Revision basis:** the supplied architectural critique in `Pasted markdown(9).md` identified a remaining generative-video failure layer: continuity through ambiguity/occlusion, explicit persistence, and causal event structure. These additions are treated as proposed CPCS representations, not as externally established ontologies.  
**Scope:** motion, phase, bilateral semantics, dynamics, interaction, camera/image formation, style, complexity, representation carriers, compiler behavior, verification  
**Important source limitation:** the uploaded material contains the CPCS research protocol and the `01_AI_VIDEO_MOTION_DIRECTION_KB_GAP_CLOSURE` research prompt, but not the referenced `CPCS_AI_Video_Motion_Direction_KB_v1.0.0.zip`. Therefore this document cannot honestly claim package-by-package coverage of that frozen KB. It treats the prompt as the gap specification and independently verifies important claims against primary/authoritative sources. Package-derived assertions are therefore marked **not verifiable from the supplied files**.

---

# 1. Executive gap closure

## 1.1 What the supplied prompt establishes

The existing AI-video KB is described as already covering:

- intent;
- Laban/BESS;
- Bartenieff connectivity;
- motion phase grammar;
- FACS;
- kinematics;
- interactions;
- force/dynamics;
- camera grammar;
- rhythm;
- VAD;
- style transfer;
- control surfaces;
- adapters;
- examples;
- metrics.

The requested work is explicitly **not** another survey. The gap is the missing precision between those concepts and executable representation.

The master protocol fixes several architectural constraints:

1. one universal semantic kernel;
2. YAML for authored intent/inheritance/profile overrides;
3. resolved JSON as canonical machine meaning;
4. XML only when ordered/namespaced/mixed-content structure provides a real advantage;
5. natural language as provider projection rather than canonical truth;
6. evidence/provenance and evidence-class separation;
7. separate research KG, execution reasoning state, and Video Observation Graph;
8. compact director world/scene model rather than raw observation dumping;
9. canonical controls negotiated against provider capability;
10. fail-closed or explicit degradation for unsupported required controls.

These are the governing constraints for the closure below.

## 1.2 What is externally established

### Motion representation

Human pose systems routinely distinguish root/body translation, articulated joint configuration, and temporal pose sequences. Human3.6M provides millions of 3D human poses for four viewpoints, while VideoPose3D demonstrates temporal modeling of pose sequences rather than treating frames independently. SMPL represents human pose using a kinematic body model whose pose parameters are joint rotations and whose geometry is generated through skinning. These sources support a structured pose/motion representation, but **they do not establish one universal CPCS authoring vocabulary**. That vocabulary remains a CPCS design decision.

3D rotation representation requires care. Zhou et al. show that common four-or-fewer-dimensional Euclidean representations such as Euler angles and quaternions have discontinuity problems for neural-network learning, while continuous 5D/6D representations are more suitable for learned rotation regression. This does **not** mean CPCS must store 6D rotations canonically. A semantic IR should remain representation-independent and define the frame, rotation convention and units; 6D is best treated as a numerical/ML representation where needed.

### Phase structure

Gesture research provides strong evidence for preparation → stroke/action → retraction, with optional holds. The McNeill Lab annotation material explicitly describes preparation, prestroke hold, stroke, poststroke hold and retraction. This supports a phase graph but does **not** prove that every physical action has exactly those phases.

Robotics research also supports multi-phase task representations where phases have different effects and transitions. Therefore CPCS should distinguish:

- **observed phase boundaries**;
- **author-authored phase boundaries**;
- **derived phase boundaries** from kinematic/contact thresholds;
- **provider-oriented phase descriptions**.

The requested `anticipation → initiation → acceleration → peak/action → contact → deceleration → follow-through → recovery` is therefore partly evidence-backed and partly an operational CPCS grammar.

### Monocular-video uncertainty

Monocular 3D pose is fundamentally ambiguous because multiple 3D configurations can project to similar 2D observations. Recent 2026 CVPR work explicitly describes monocular 3D pose as ill-posed due to depth ambiguity and occlusion. Consequently CPCS must not turn an estimated 3D pose into false exact physical truth.

### Force/dynamics

Force, momentum, torque and friction have precise physical meanings. However, recovering them from ordinary monocular video requires assumptions, additional sensing, or physics-informed estimation. Research has demonstrated estimation of forces and torques from monocular video under explicit modeling assumptions, but that is an **estimation problem**, not direct measurement.

The 2026 work on noise propagation in video-based inverse dynamics is especially relevant: numerical differentiation can amplify pose noise dramatically. Therefore `force`, `torque`, `impulse`, `mass`, `friction_coefficient`, and similar quantities must never be silently promoted from visual observation to measured fact.

### Interaction

Human-object interaction research supports explicit contact position/timing representation and shows that contact can be difficult to observe because hands or objects occlude the contact point. Monocular interaction estimation can jointly infer 3D motion, contact and force, but again these are estimates under a model.

### Camera

Camera calibration gives a precise distinction between:

- intrinsic parameters: focal lengths, principal point, distortion;
- extrinsic parameters: camera pose relative to a reference frame.

OpenCV's calibration documentation is a useful authoritative implementation reference for this distinction.

AI-video provider documentation confirms that modern generators expose semantic camera concepts such as locked/static, pan, tilt, zoom, dolly/tracking, handheld and focus-related motion, but provider capabilities differ. Runway explicitly recommends treating subject motion, scene motion, camera motion and style as separate prompt components. Google Veo's guide similarly separates shot framing/motion, style, lighting and character description. Kling documents explicit camera movement controls and displacement parameters.

This supports a universal camera semantic layer with provider adapters rather than a provider-specific camera ontology.

### Style

A style label is not a sufficient executable specification. At minimum, CPCS should separate:

- visual style;
- motion style;
- camera style;
- editing style;
- performance style;
- audio style;
- narrative style.

Each style should carry:

- invariants;
- allowed variation;
- forbidden drift;
- priority;
- evidence/provenance.

This is a **CPCS representation proposal**, not an externally standardized ontology.

### Structured carriers

Current research supports treating structured output reliability as a separate engineering property from semantic correctness. Structured-output benchmarks continue to find gaps between schema compliance and value correctness. Provider-native structured output can enforce schema shape, but schema validity does not prove semantic correctness.

Therefore:

- JSON should remain the resolved semantic authority;
- YAML should remain authoring-oriented;
- XML should be an explicit projection only when ordering/namespaces/mixed content matter;
- NL should be a lossy provider projection;
- round-trip semantic tests should operate against the resolved JSON, not textual equality.

No available evidence justifies a universal claim that JSON, YAML or XML inherently produces better reasoning. Carrier effects must be experimentally measured for the actual director/compiler tasks.

---

# 2. Evidence ledger

| Field/concept | Meaning | Evidence class | Primary/authoritative source | Confidence | Measurement status | CPCS status |
|---|---|---|---|---|---|---|
| `root.position` | Root translation in declared frame | established representation concept + proposed CPCS field | SMPL / Human3.6M | high | measurable when scale/frame are known; otherwise estimated | implementable |
| `root.orientation` | Root orientation in declared frame | established representation concept + proposed field | SMPL; rotation representation literature | high | measured/estimated | implementable |
| `joint.rotation` | Local joint rotation relative to parent | established representation concept | SMPL | high | measured/estimated | implementable |
| `velocity` | First temporal derivative of position/angle | physics/kinematics + proposed field | standard mechanics; pose-video literature | high | derived | implementable |
| `acceleration` | Second temporal derivative | physics/kinematics + proposed field | standard mechanics | high | derived | implementable |
| `jerk` | Third temporal derivative | mathematical/kinematic concept | proposed CPCS use | medium | derived, noise-sensitive | experimental/optional |
| `trajectory` | time-ordered state path | established mathematical concept + proposed field | pose/video literature | high | derived | implementable |
| `phase` | temporal segment with semantic role | research-supported + CPCS grammar | McNeill Lab; robotics phase literature | high for phase concept, medium for exact CPCS labels | observed/inferred/derived | implementable |
| `anticipation` | preparatory movement before primary action | research-supported | gesture and skilled-action literature | high | observed/inferred | implementable |
| `contact` | temporal/spatial interaction event | research-supported | human-object contact literature | high | detected/estimated/observed | implementable |
| `force` | physical interaction force | established physics | OpenStax; inverse-dynamics literature | high | generally estimated, not directly measured in ordinary video | fail-closed by default |
| `mass_class` | qualitative physical mass behavior | proposed semantic abstraction | no universal standard | medium | authored/inferred | experimental |
| `camera.intrinsics` | optical/image-formation parameters | established computer-vision representation | OpenCV calibration | high | measured/calibrated/unknown | implementable |
| `camera.motion` | camera pose/motion semantic | provider + cinematography vocabulary | Runway, Veo, Kling | high | authored/detected/estimated | implementable |
| `style.invariants` | properties style should preserve | proposed CPCS representation | no universal standard | medium | authored/evidence-derived | implementable |
| `complexity_score` | bounded production-risk heuristic | proposed metric | no external calibration | low until benchmarked | derived | experiment required |
| `carrier_effect` | impact of JSON/YAML/XML/NL on adherence/validity | experimental question | structured-output research | medium | requires CPCS benchmark | experiment required |

---

# 3. Canonical semantic representation

## 3.1 Core rule

CPCS should represent **meaning**, not the serialization format and not a provider's prompt dialect.

Recommended conceptual layers:

```text
research/evidence
    ↓
director interpretation
    ↓
canonical scene/world state
    ↓
canonical control intent
    ↓
capability negotiation
    ↓
provider projection
```

A motion control should therefore never be stored as:

```json
{"prompt": "camera slowly moves in"}
```

when the intended meaning is actually:

```json
{
  "camera_motion": {
    "kind": "dolly",
    "direction": "forward",
    "rate": {"value": 0.35, "unit": "normalized"},
    "profile": "ease_in_out",
    "target": "subject:alice",
    "duration": {"value": 2.0, "unit": "s"}
  }
}
```

The latter can be compiled to natural language or a native provider control.

## 3.2 Motion state object

Recommended canonical object:

```json
{
  "motion_id": "motion_001",
  "actor_id": "actor_01",
  "scope": "body",
  "reference_frame": "actor_local",
  "space_mode": "relative",
  "start_time": 0.0,
  "end_time": 1.8,
  "trajectory": {
    "type": "piecewise_cubic",
    "control_points": []
  },
  "root": {
    "translation": {
      "value": [0.0, 0.0, 0.0],
      "unit": "m",
      "frame": "world"
    },
    "orientation": {
      "representation": "quaternion",
      "value": [1.0, 0.0, 0.0, 0.0],
      "frame": "world"
    }
  },
  "joints": [],
  "kinematics": {
    "speed": {"value": 0.8, "unit": "normalized"},
    "acceleration_profile": "ease_in_out"
  },
  "phase_graph": [],
  "evidence_class": "authored",
  "confidence": 1.0,
  "provenance": {
    "source_ref": "director_request"
  }
}
```

### Important design decision

`speed`, `amplitude`, `intensity`, `effort`, and `force` must not be aliases.

- `speed` = temporal rate of movement.
- `amplitude` = spatial/angular extent.
- `acceleration_profile` = how velocity changes through time.
- `effort` = expressive movement quality, not Newtons.
- `force` = physical quantity requiring physical interpretation/measurement/estimation.

This separation is essential.

---

# 4. Rotation representation

## 4.1 Canonical semantic representation

For semantic interchange:

```json
{
  "rotation": {
    "representation": "quaternion",
    "convention": "wxyz",
    "frame": "parent_local",
    "unit": "unitless",
    "value": [0.9239, 0.0, 0.3827, 0.0]
  }
}
```

The exact quaternion convention must be declared. `wxyz` versus `xyzw` cannot be inferred safely.

For authored human-readable direction:

```yaml
rotation:
  axis: y
  angle: 45deg
  frame: parent_local
```

The compiler resolves this to canonical JSON.

For learned ML representations, 6D rotation is a valid adapter representation because Zhou et al. show continuity advantages over Euler/quaternion representations for neural-network learning. It should not replace the semantic rotation contract.

## 4.2 Required validation

Reject or quarantine:

- undeclared axis convention;
- undeclared frame;
- malformed quaternion;
- quaternion with norm outside tolerance;
- Euler angles without axis order;
- angle units omitted when not obvious from schema.

---

# 5. Bilateral and left/right semantics

## 5.1 Rule

Use side-indexed structures whenever left and right are semantically independent.

Preferred:

```json
{
  "hands": {
    "left": {
      "trajectory": "...",
      "contact": "object_01"
    },
    "right": {
      "trajectory": "...",
      "contact": null
    }
  },
  "symmetry": {
    "state": "asymmetric",
    "score": 0.28
  }
}
```

Do not compress this into:

```json
{"hand_position": [...]}
```

if side matters.

## 5.2 Bilateral value

Use `bilateral` only when the source or author explicitly describes a coupled bilateral action:

```json
{
  "arms": {
    "mode": "bilateral",
    "coupling": "symmetric",
    "symmetry": 0.94
  }
}
```

`bilateral` does not mean "average left and right."

For asymmetric behavior, preserve the underlying side-specific observations and derive symmetry/asymmetry metadata.

## 5.3 FACS

FACS is explicitly a descriptive, anatomically based system for visually discernible facial movement and Action Units. The Paul Ekman Group describes AUs as individual components of facial movement. FACS should therefore remain a facial movement description layer rather than an emotion inference layer.

Recommended:

```json
{
  "facs_event": {
    "au_id": "AU12",
    "side": "bilateral",
    "intensity": {
      "scale": "facs_A_E",
      "value": "C"
    },
    "onset": 0.20,
    "apex": 0.65,
    "offset": 1.10,
    "evidence_class": "detected",
    "confidence": 0.91
  }
}
```

If a detector emits continuous intensity rather than FACS A-E, preserve the detector scale:

```json
{
  "intensity": {
    "scale": "detector_continuous",
    "value": 0.73,
    "range": [0, 1]
  }
}
```

Do not silently map detector values to FACS A-E.

---

# 6. Temporal and phase grammar

## 6.1 Canonical phase object

```json
{
  "phase_id": "p3",
  "role": "contact",
  "start": 1.20,
  "end": 1.32,
  "boundary_basis": "detected",
  "confidence": 0.88,
  "preconditions": ["hand_near_target"],
  "postconditions": ["contact_established"]
}
```

## 6.2 Evidence-backed vs engineering phases

### Evidence-backed concepts

- preparation;
- stroke/action;
- retraction;
- holds;
- temporal segmentation;
- contact onset/offset;
- action boundaries.

Gesture research directly supports preparation/stroke/retraction and optional holds. Robotics research supports multi-phase tasks with meaningful phase transitions.

### CPCS engineering grammar

The following is useful as a normalized execution grammar:

```text
precondition
→ anticipation
→ initiation
→ acceleration
→ action/apex
→ contact
→ deceleration
→ follow-through
→ recovery
→ postcondition
```

This must be tagged as `derived` or `authored`, not as a universal law of human movement.

## 6.3 Example: punch

```json
{
  "action": "punch",
  "phase_graph": [
    {"role": "precondition", "state": "stance_stable"},
    {"role": "anticipation", "duration": 0.20},
    {"role": "initiation", "duration": 0.08},
    {"role": "acceleration", "profile": "rapid"},
    {"role": "action_apex", "event": "fist_near_target"},
    {"role": "contact", "event": "target_contact"},
    {"role": "follow_through", "profile": "short"},
    {"role": "recovery", "profile": "rapid_guard_return"}
  ]
}
```

### Important distinction

`action_apex` is not automatically `contact`.

For a near-miss, there may be an apex without contact.

---

# 7. Kinematics and measurement

## 7.1 Canonical measurement object

```json
{
  "measurement": {
    "quantity": "joint_velocity",
    "subject": "actor_01",
    "joint": "right_wrist",
    "value": [0.2, -0.1, 1.4],
    "unit": "m/s",
    "frame": "world",
    "timebase": "pts",
    "timestamp": 2.133,
    "sampling_rate_hz": 30,
    "method": "finite_difference",
    "confidence": 0.84,
    "error": {
      "type": "estimated",
      "value": 0.12,
      "unit": "m/s"
    },
    "missing_data_behavior": "unknown"
  }
}
```

## 7.2 Required measurement fields

Every measured/derived kinematic quantity should carry:

- source;
- timestamp/timebase;
- sampling rate;
- coordinate frame;
- units;
- method;
- confidence;
- uncertainty/error where available;
- missing-data state;
- occlusion state;
- camera-motion compensation state.

## 7.3 Camera-motion contamination

For image-derived motion, `world`, `camera`, and `actor_local` must never be conflated.

A person can appear to move in image coordinates while remaining stationary in world coordinates because the camera moves.

Therefore:

```json
{
  "coordinate_frame": {
    "position": "camera",
    "orientation": "camera",
    "camera_motion_compensated": false
  }
}
```

is materially different from:

```json
{
  "coordinate_frame": {
    "position": "world",
    "orientation": "world",
    "camera_motion_compensated": true
  }
}
```

---

# 8. Dynamics and force: fail-closed model

## 8.1 Evidence model: acquisition vs epistemic state

The previous flat evidence list mixed two different dimensions. CPCS should separate them.

### Acquisition class

```text
authored
observed
detected
measured
estimated
inferred
derived
```

### Epistemic state

```text
known
uncertain
unknown
unobservable
contradictory
```

`acquisition` answers **how the value entered the system**. `epistemic_state` answers **how strongly the system can claim the value is established**.

Examples:

- physical force plate reading → `acquisition=measured`;
- pose tracker keypoints → `acquisition=detected`;
- wrist velocity computed from detected keypoints → `acquisition=derived`, with `source_acquisition=detected`;
- force estimated from video plus a declared physical model → `acquisition=estimated`;
- a director's desired "heavy" movement → `acquisition=authored`;
- a semantic conclusion that an actor recoiled after contact → `acquisition=inferred`.

Any acquisition class may carry an epistemic state such as `known` or `uncertain`.

```json
{
  "evidence": {
    "acquisition": "derived",
    "source_acquisition": "detected",
    "epistemic_state": "uncertain",
    "confidence": 0.84
  }
}
```

### Measured

Requires an actual physical measurement source, e.g. force plate, inertial sensor, calibrated motion-capture system.

### Estimated

Algorithmically inferred from observations under a declared model.

### Inferred

Semantic conclusion supported by evidence but not directly measured.

### Unknown

Use `epistemic_state=unknown` when no sufficiently supported value exists.

### Unobservable

Use `epistemic_state=unobservable` when the available media cannot establish the value with acceptable uncertainty.

### Contradictory

Use `epistemic_state=contradictory` when accepted evidence sources materially disagree and the conflict has not been resolved.

## 8.2 Safe force representation

```json
{
  "force": {
    "status": "estimated",
    "vector": {
      "value": [0.0, 0.0, 0.0],
      "unit": "N",
      "frame": "world"
    },
    "method": "physics_informed_video_estimator",
    "confidence": 0.61,
    "assumptions": [
      "known_or_estimated_mass",
      "known_contact",
      "camera_geometry_estimated"
    ]
  }
}
```

If these assumptions are absent:

```json
{
  "force": {
    "status": "unobservable",
    "reason": "monocular_video_without_force_or_mass_constraints"
  }
}
```

## 8.3 Do not infer force from speed alone

A fast movement is not equivalent to a high measured force.

Likewise:

- `effort=strong` is not `force=500N`;
- `impact=dramatic` is not `impulse=...`;
- `heavy_style` is not `mass=...kg`.

This distinction is central to keeping the VOG evidence-safe.

## 8.4 Jerk

Jerk can be derived mathematically, but numerical differentiation amplifies noise. It should therefore be:

```json
{
  "jerk": {
    "status": "derived",
    "method": "smoothed_finite_difference",
    "confidence": 0.54
  }
}
```

rather than treated as a high-confidence primitive.

The 2026 video inverse-dynamics literature reinforces this caution: pose noise can be strongly amplified when differentiating toward physical quantities.

---

# 9. Interaction lifecycle

## 9.1 Recommended canonical lifecycle

```text
approach
→ proximity
→ alignment
→ contact_candidate
→ contact_established
→ grasp/support/collision
→ displacement/transfer
→ release
→ separation
→ reaction/recoil
```

Not every interaction has every state.

## 9.2 Canonical interaction object

```json
{
  "interaction_id": "int_004",
  "actor_a": "actor_01",
  "actor_b": "object_07",
  "type": "impact",
  "lifecycle": [
    {
      "state": "approach",
      "start": 1.10,
      "end": 1.24
    },
    {
      "state": "contact_established",
      "start": 1.24,
      "end": 1.30,
      "evidence_class": "detected",
      "confidence": 0.89
    },
    {
      "state": "recoil",
      "start": 1.30,
      "end": 1.62,
      "evidence_class": "inferred",
      "confidence": 0.74
    }
  ],
  "contact": {
    "site_a": "right_fist",
    "site_b": "torso",
    "visibility": "partially_occluded"
  }
}
```

## 9.3 Occluded contact

Do not encode:

```json
{"contact": true}
```

when the contact point is visually hidden and merely plausible.

Use:

```json
{
  "contact": {
    "status": "estimated",
    "visibility": "occluded",
    "confidence": 0.63
  }
}
```

or:

```json
{
  "contact": {
    "status": "unknown"
  }
}
```

depending on the evidence.

---

# 10. Continuity, persistence, occlusion, and causal event closure

The supplied critique identifies a failure class that is not fully represented by `MotionEvent`, `InteractionEvent`, or `phase_graph` alone: **state continuity through partial observability**.

This is a proposed CPCS semantic extension. It should be implemented as an extension of the universal kernel, not as a separate video ontology.

## 10.1 Why this is a separate semantic dimension

Motion answers **how** an entity moves.

Phase answers **when** an action is organized.

Interaction answers **with what / whom** an entity interacts.

Causality answers **why one event produces or depends on another**.

Continuity answers whether the same world state/entity persists across a partially or fully unobservable interval.

```text
STATE(t0)
   ↓
STATE TRANSITION
   ↓
PARTIALLY / UNOBSERVABLE INTERVAL
   ↓
STATE(t1)
```

A visibility change must not automatically become an existence change.

For example:

```text
visibility = partial/occluded
existence = continuous
identity = actor_B
trajectory = continuing
```

is semantically different from:

```text
existence = ended
identity = unknown
```

## 10.2 Proposed `ContinuityState`

```json
{
  "continuity_state": {
    "entity_id": "actor_B",
    "visibility": "partial",
    "existence": "continuous",
    "identity": "invariant",
    "actor_count": {
      "status": "known",
      "value": 1
    },
    "trajectory_continuity": "required",
    "pose_continuity": "required",
    "action_generation": "forbidden"
  }
}
```

### Semantics

`ContinuityState` describes invariants that must remain true across a temporal interval even when the complete visual state is not available.

It does **not** assert an unobserved exact pose or position. It constrains what may change and what must remain persistent.

## 10.3 Proposed `StateTransition`

```json
{
  "state_transition": {
    "entity_id": "actor_B",
    "type": "submersion",
    "onset": 1.20,
    "offset": 1.85,
    "path": {
      "direction": "vertical_down",
      "lateral_displacement": "minimal"
    },
    "pre_state_ref": "state_B_014",
    "post_state_ref": "state_B_015",
    "continuity_ref": "cont_B_007"
  }
}
```

The transition is a semantic bridge between accepted states. It must not invent exact hidden coordinates merely because a provider requires text.

## 10.4 Proposed `OcclusionInterval`

```json
{
  "occlusion_interval": {
    "entity_id": "actor_B",
    "start": 1.32,
    "end": 1.74,
    "cause": "water_splash",
    "visibility": "partial",
    "identity_preserved": true,
    "trajectory_preserved": true,
    "exact_pose": {
      "status": "unobservable"
    },
    "forbidden_generation": [
      "teleport",
      "clone",
      "pose_reset",
      "identity_swap",
      "new_unmotivated_action"
    ]
  }
}
```

`OcclusionInterval` is not merely an observation annotation. In the directing IR it becomes a **continuity constraint**: uncertainty about the hidden state is not permission to invent a new state.

## 10.5 Proposed `PersistenceConstraint`

```json
{
  "persistence_constraint": {
    "entity_id": "actor_B",
    "identity": "invariant",
    "count": "exactly_1",
    "wardrobe": "invariant",
    "topology": "invariant",
    "existence": "continuous",
    "visibility": "may_change",
    "position": "continuous_trajectory"
  }
}
```

This explicitly separates:

```text
existence changed
```

from:

```text
visibility changed
```

The same mechanism can apply to:

- actors;
- props;
- clothing;
- held objects;
- vehicles;
- environmental structures.

## 10.6 Proposed `CausalEvent`

`phase_graph` provides temporal organization but is not sufficient to express why a downstream event occurs.

```json
{
  "causal_event": {
    "event_id": "evt_water_impact_01",
    "cause": "A_kick_intersects_water",
    "produces": [
      "surface_displacement",
      "vertical_water_column",
      "splash"
    ],
    "depends_on": [
      "B_evasive_dive"
    ],
    "must_not_imply": [
      "A_contacts_B"
    ]
  }
}
```

CPCS should therefore distinguish:

```text
PhaseGraph    = WHEN
CausalEvent   = WHY / BECAUSE
SpatialState  = WHERE
MotionEvent   = HOW
Interaction   = WITH WHAT / WHOM
Continuity    = STILL THE SAME?
Visibility    = WHAT CAN BE OBSERVED?
```

The causal representation must distinguish:

- temporal succession;
- causal dependency;
- correlation;
- narrative motivation;
- observed co-occurrence.

They are not interchangeable.

## 10.7 Canonical family extension

The proposed universal family becomes:

```text
Scene
 ├── Actor
 ├── Object
 ├── Relation
 ├── ContinuityState
 ├── StateTransition
 │    └── OcclusionInterval
 ├── PersistenceConstraint
 ├── MotionEvent
 │    ├── trajectory
 │    ├── kinematics
 │    ├── phase_graph
 │    └── effort
 ├── CausalEvent
 ├── InteractionEvent
 │    ├── lifecycle
 │    ├── contact
 │    └── reaction
 ├── CameraState
 ├── StyleConstraint
 ├── EvidenceRecord
 └── ComplexityWindow
```

This remains one universal semantic kernel. These objects do not constitute a second ontology.

## 10.8 Compiler behavior

Continuity constraints are compiled before provider projection.

```text
accepted entity/state
    ↓
continuity + persistence constraints
    ↓
causal dependencies
    ↓
motion/phase/interaction controls
    ↓
provider capability negotiation
    ↓
provider projection
```

If the provider cannot reliably preserve a required continuity constraint, CPCS should not silently treat a descriptive prompt as successful control.

Possible compiler responses:

```text
native_continuity_control
semantic_prompt_constraint
shot_decomposition
visibility_bridge
reference_conditioning
explicit_compilation_loss
reject
```

`shot_decomposition` is a routing/compilation strategy, not a new semantic primitive.

## 10.9 Verification

Continuity must become a first-class verification dimension:

```text
identity_consistency
actor_count_consistency
existence_continuity
trajectory_continuity
wardrobe_continuity
prop_continuity
occlusion_transition_error
forbidden_event_rate
causal_edge_preservation
causal_false_positive_rate
```

For generated video, a continuity failure is not equivalent to a generic motion-adherence failure.

## 10.10 Complexity interaction

The vectorized complexity model should include:

```text
identity_burden
interaction_burden
occlusion_burden
camera_burden
temporal_density
actor_count
material_complexity
causal_dependency_density
continuity_burden
```

Do not collapse this vector into one authoritative score until calibrated against provider/model failure data.

# 10. Camera grammar

## 10.1 Separate semantic layers

### Layer 1 — camera motion

- locked/static;
- pan;
- tilt;
- roll;
- dolly;
- tracking;
- crane/elevate;
- orbit/arc;
- handheld/drift.

### Layer 2 — optical/image formation

- focal length;
- field of view;
- camera distance;
- camera height;
- focus plane;
- depth of field;
- aperture;
- rack focus;
- motion blur/shutter behavior.

### Layer 3 — exposure/color/device

- exposure;
- white balance;
- dynamic range;
- sensor/device character;
- color space;
- lens distortion;
- chromatic aberration;
- stabilization;
- compression/noise.

These must not all be represented as equivalent "camera motion."

## 10.2 Camera semantic object

```json
{
  "camera": {
    "pose": {
      "position": {
        "value": [0, 1.6, 4.0],
        "unit": "m",
        "frame": "world"
      },
      "orientation": {
        "representation": "quaternion",
        "value": [1, 0, 0, 0],
        "frame": "world"
      }
    },
    "optics": {
      "focal_length": {
        "value": 50,
        "unit": "mm",
        "status": "authored"
      },
      "field_of_view": {
        "horizontal": 39.6,
        "unit": "deg",
        "status": "derived"
      }
    },
    "motion": {
      "kind": "dolly",
      "direction": "forward",
      "profile": "ease_in_out",
      "target": "actor_01",
      "duration": 2.0
    },
    "focus": {
      "mode": "subject_tracking",
      "target": "actor_01"
    }
  }
}
```

## 10.3 Camera calibration

When the source is measured video, distinguish:

```text
intrinsics
  fx, fy
  cx, cy
  distortion

extrinsics
  camera position
  camera orientation
```

OpenCV's camera-calibration documentation explicitly models focal lengths, principal point and distortion coefficients as intrinsic parameters. This is appropriate as the measurement representation, not as a universal provider prompt representation.

## 10.4 Provider capability mapping

Runway's current guidance separates subject motion, scene motion, camera motion and style descriptors, and explicitly supports concepts such as locked, handheld and tracking camera movement. Google Veo's guide similarly recommends describing shot framing/motion and style. Kling exposes explicit camera movement controls including horizontal/vertical movement, zoom, pan, tilt and roll.

Therefore the adapter should map:

```text
canonical camera motion
→ provider capability
→ native control if available
→ semantic natural-language projection if not
→ unsupported/degraded if neither is reliable
```

---

# 11. Style grammar

## 11.1 Style object

```json
{
  "style": {
    "id": "documentary_observation",
    "domains": {
      "visual": {
        "invariants": [
          "naturalistic_materials",
          "non-stylized_skin_texture"
        ],
        "allowed_variation": [
          "natural_lighting_variation"
        ],
        "forbidden_drift": [
          "anime_face_geometry",
          "plastic_skin"
        ]
      },
      "motion": {
        "invariants": [
          "physically_plausible_timing"
        ],
        "allowed_variation": [
          "minor_handheld_micro_motion"
        ],
        "forbidden_drift": [
          "heroic_slow_motion_without_authorization"
        ]
      },
      "camera": {
        "invariants": [
          "motivated_camera_motion"
        ],
        "allowed_variation": [
          "subtle_handheld"
        ],
        "forbidden_drift": [
          "unmotivated_orbit"
        ]
      }
    },
    "priority": 0.9,
    "evidence_class": "authored"
  }
}
```

## 11.2 Why labels alone are insufficient

`anime`, `watercolor`, `documentary`, `UGC`, and `sakuga` are high-level descriptors. They are useful routing hints but are not executable constraints by themselves.

CPCS should compile style labels into observable/operational dimensions when evidence exists.

For example:

```text
UGC
→ performance: direct_to_camera
→ camera: handheld_or_phone_locked
→ framing: close/medium
→ editing: high_temporal_variability
→ visual: consumer_device_character
```

Only fields supported by the research or authored profile should be emitted. Do not invent a universal mapping for every style label.

---

# 12. Complexity and risk budgeting

## 12.1 Proposed representation

Treat complexity as a **heuristic risk estimate**, not an objective universal score.

```json
{
  "complexity": {
    "window": {
      "start": 0.0,
      "end": 8.0,
      "unit": "s"
    },
    "features": {
      "actor_count": 2,
      "simultaneous_actions": 3,
      "contact_count": 2,
      "camera_complexity": 0.7,
      "physics_complexity": 0.8,
      "style_vfx_complexity": 0.4,
      "dialogue_density": 0.1,
      "identity_burden": 0.8,
      "spatial_topology": 0.7,
      "temporal_density": 0.6
    },
    "score": null,
    "calibration_status": "uncalibrated_heuristic"
  }
}
```

## 12.2 Do not immediately collapse into one number

The individual feature vector is more useful than a single score because compiler behavior can be feature-specific.

For example:

- high actor count stresses identity;
- high contact count stresses interaction consistency;
- high temporal density stresses phase ordering;
- high camera complexity stresses camera adherence;
- high physics complexity stresses physical plausibility;
- high spatial topology stresses relative positions.

The scalar score should only be introduced after empirical calibration.

## 12.3 Candidate window aggregation

Use fixed windows, e.g. per shot:

```text
complexity(window)
=
weighted feature vector
+
constraint interactions
```

Then calibrate weights using observed generation failure rates.

Possible targets:

- identity error;
- action omission;
- contact error;
- camera error;
- temporal-order error;
- spatial-topology error;
- style drift.

---

# 13. Representation equivalence

## 13.1 One semantic meaning

Meaning:

> A person reaches with the right hand toward a cup over 0.8 seconds, accelerates into the reach, briefly decelerates near the cup, makes contact, and retracts.

### YAML authoring

```yaml
motion:
  actor: person_01
  limb: right_hand
  target: cup_01
  space: actor_local
  duration: 0.8s
  phases:
    - anticipation
    - initiation
    - acceleration
    - deceleration
    - contact
    - retraction
```

### Resolved JSON

```json
{
  "motion": {
    "actor_id": "person_01",
    "effector": "right_hand",
    "target_id": "cup_01",
    "reference_frame": "actor_local",
    "duration": {"value": 0.8, "unit": "s"},
    "phase_graph": [
      {"role": "anticipation"},
      {"role": "initiation"},
      {"role": "acceleration"},
      {"role": "deceleration"},
      {"role": "contact"},
      {"role": "retraction"}
    ]
  }
}
```

### XML projection

XML adds value if the execution envelope requires ordered event nodes:

```xml
<motion actor="person_01" effector="right_hand" target="cup_01">
  <phase role="anticipation"/>
  <phase role="initiation"/>
  <phase role="acceleration"/>
  <phase role="deceleration"/>
  <phase role="contact"/>
  <phase role="retraction"/>
</motion>
```

### Natural-language provider projection

> The person reaches toward the cup with the right hand. The hand accelerates into the reach, slows as it approaches the cup, makes contact, then retracts.

### What changes

- YAML is concise and author-friendly.
- JSON makes types, units, IDs and resolved defaults explicit.
- XML emphasizes ordered event structure and attributes.
- NL loses machine-enforced typing, provenance, exact units and guaranteed phase identity.

Therefore NL must never become canonical authority.

---

# 14. Compiler semantics

## 14.1 Required compiler pipeline

```text
research concept
→ retrieved evidence
→ director decision
→ canonical semantic field
→ control candidate
→ provider capability check
→ native / approximate / semantic / unsupported
→ provider representation
→ compilation-loss record
```

## 14.2 Capability classes

Use:

```text
native
approximate
semantic
unsupported
```

### Native

Provider exposes a direct control.

Example:

```text
canonical camera.pan
→ provider pan control
```

### Approximate

Provider has a related control but not the same semantic guarantee.

Example:

```text
canonical focal_length = 85mm
→ provider has no focal-length parameter
→ project to "compressed telephoto look"
→ mark approximate
```

### Semantic

Provider has no direct control but natural language can describe the desired effect.

Example:

```text
canonical motion_style = "subtle handheld micro-drift"
→ NL projection
```

### Unsupported

Required control cannot be safely expressed.

Example:

```text
canonical exact_world_trajectory
→ provider has no trajectory interface
→ UNSUPPORTED
```

Do not pretend the natural-language prompt provides exact trajectory control.

## 14.3 Compilation-loss record

```json
{
  "loss_id": "loss_009",
  "canonical_field": "camera.optics.focal_length",
  "requested": {
    "value": 85,
    "unit": "mm"
  },
  "provider": "provider_x",
  "capability": "unsupported",
  "projection": "semantic",
  "replacement": "telephoto_compressed_perspective",
  "loss": {
    "type": "numeric_control_loss",
    "severity": "medium"
  },
  "accepted": false
}
```

A required exact control should fail closed unless the caller explicitly permits degradation.

---

# 15. Provider-facing implications

## Runway

Runway's current Gen-4 guidance explicitly recommends focusing the video prompt on motion and separates subject motion, scene motion, camera motion and style. It also documents locked camera, handheld, tracking and focus-related concepts.

CPCS implication:

```text
subject_motion
scene_motion
camera_motion
style
```

should compile separately before being serialized into the provider prompt.

Runway also states that overly conceptual language can produce less predictable motion. This supports a compiler that turns abstract intent into observable action descriptions rather than passing abstract Laban/VAD labels directly to the provider.

## Google Veo

Google's current Veo prompting guide explicitly calls out shot framing/motion, style, lighting and character descriptions.

CPCS implication:

```text
canonical camera
→ framing + camera movement

canonical style
→ visual style projection

canonical lighting
→ lighting projection
```

Do not collapse these into a single `style` string.

## Kling

Kling's current camera-control documentation exposes explicit camera movement controls and displacement parameters for horizontal, vertical, zoom, pan, tilt and roll.

CPCS implication:

```text
camera.motion.kind
camera.motion.direction
camera.motion.amount
```

can sometimes map to native controls rather than NL.

The adapter should still record whether the provider's control is exact relative to the canonical semantics.

---

# 16. Model-conditioning and data-language effect

## 16.1 Evidence

Current structured-output research shows that structured output quality is measurable and that schema compliance and semantic correctness are separate dimensions. Provider-native structured output can enforce schema shape. Other recent benchmarks find substantial differences across structured formats and tasks.

There is insufficient evidence to claim:

```text
JSON is always better than YAML
XML is always better than JSON
NL is always better than structured input
```

The CPCS question is narrower and should be experimentally tested.

## 16.2 Required experiment

Create one canonical semantic dataset of at least:

- 100 motion intents;
- 50 interaction intents;
- 50 camera intents;
- 25 style intents;
- 25 mixed scenes.

Render each into:

1. JSON;
2. YAML;
3. XML;
4. Markdown table;
5. plain NL;
6. hybrid JSON + NL;
7. hybrid YAML + NL.

Hold constant:

- model;
- seed where supported;
- token budget;
- temperature;
- retrieved evidence;
- semantic meaning;
- provider;
- number of generation attempts.

Measure:

- schema validity;
- field preservation;
- action adherence;
- temporal-order preservation;
- actor identity consistency;
- left/right preservation;
- camera adherence;
- interaction/contact adherence;
- contradiction rate;
- omission rate;
- token count;
- latency;
- retry count.

The output should be a **CPCS empirical carrier profile**, not a universal claim.

---

# 17. Verification contract

## 17.1 Canonical validation

Every resolved JSON object must pass:

```text
schema_valid
units_valid
frame_valid
time_valid
identity_valid
evidence_class_valid
provenance_present
side_semantics_valid
```

## 17.2 Motion verification

For observed/generated video where measurement is available:

```text
trajectory_error
direction_error
speed_error
peak_timing_error
phase_boundary_error
contact_timing_error
left_right_error
identity_switch_rate
```

## 17.3 Camera verification

```text
camera_direction_accuracy
camera_motion_class_accuracy
framing_error
subject_tracking_error
focus_target_error
optical_control_adherence
```

## 17.4 Interaction verification

```text
contact_precision
contact_recall
contact_timing_error
near_miss_false_positive_rate
object_transfer_accuracy
reaction_order_accuracy
```

## 17.5 Style verification

Use measurable proxies where possible:

```text
style_invariant_violation_rate
forbidden_drift_rate
motion_style_adherence
camera_style_adherence
visual_style_adherence
```

Do not use one LLM-judge score as the sole verification mechanism.

---

# 18. Implementation placement

This section is intentionally expressed as a placement contract rather than invented repository filenames, because the actual CPCS tree was not supplied in the attached files.

| Addition | Existing owner to extend | New subsystem? | Authority | Runtime owner | Compiler owner | Validator | Fixture |
|---|---|---:|---|---|---|---|---|
| canonical motion state | universal semantic kernel | no | canonical JSON | director/runtime | provider compiler | schema validator | reach/punch |
| phase graph | motion/action schema | no | canonical JSON | director/runtime | provider compiler | temporal validator | punch/reach |
| bilateral semantics | actor/body schema | no | canonical JSON | observation/director | provider compiler | side validator | asymmetric reach |
| interaction lifecycle | interaction schema | no | canonical JSON | VOG/director | provider compiler | interaction validator | punch/contact/grasp |
| camera semantic object | camera schema | no | canonical JSON | director | camera adapter | camera validator | dolly/orbit |
| force evidence state | observation/evidence schema | no | VOG/evidence | observation layer | not normally compiled | evidence validator | unknown force |
| style invariants | style/profile schema | no | authored/profile | director | style compiler | invariant validator | UGC/documentary |
| complexity vector | scoring layer | no | derived score | director | routing policy | metric validator | multi-actor shot |
| compilation loss | compiler audit | no | execution record | compiler | compiler | loss validator | unsupported focal length |

**Do not create separate motion, camera, style and interaction ontologies if existing universal semantic objects can own these fields.**

---

# 19. Recommended canonical object family

The smallest useful universal family after the continuity/causality closure is:

```text
Scene
 ├── Actor
 ├── Object
 ├── Relation
 ├── ContinuityState
 ├── StateTransition
 │    └── OcclusionInterval
 ├── PersistenceConstraint
 ├── MotionEvent
 │    ├── trajectory
 │    ├── kinematics
 │    ├── phase_graph
 │    └── effort
 ├── CausalEvent
 ├── InteractionEvent
 │    ├── lifecycle
 │    ├── contact
 │    └── reaction
 ├── CameraState
 │    ├── pose
 │    ├── motion
 │    ├── optics
 │    └── image_formation
 ├── StyleConstraint
 │    ├── invariants
 │    ├── allowed_variation
 │    └── forbidden_drift
 ├── EvidenceRecord
 └── ComplexityWindow
```

This is still one universal semantic kernel. The additions explicitly cover the missing dimensions of persistence, partial observability and causality rather than creating separate ontologies for motion, interaction or video generation.

---

# 20. Critical design corrections

## 20.1 Do not make Laban the canonical kinematic representation

Laban/BESS is useful for expressive movement semantics. It is not a substitute for:

- position;
- orientation;
- velocity;
- acceleration;
- phase timing;
- contact state.

Recommended layering:

```text
kinematics
+
phase
+
Laban/BESS
```

rather than:

```text
Laban/BESS → everything
```

## 20.2 Do not make FACS an emotion ontology

FACS describes visible facial movement. Emotion interpretation belongs in a different semantic layer.

```text
FACS AU
→ facial movement evidence
→ optional interpretation
```

not:

```text
AU12 = happiness
```

## 20.3 Do not turn force into a style adjective

```text
heavy
powerful
violent
soft
explosive
```

are expressive/directorial qualities unless tied to a physical measurement or explicit physical model.

Use:

```json
{
  "effort_quality": {
    "weight": "strong",
    "time": "sudden",
    "space": "direct",
    "flow": "bound"
  }
}
```

separately from:

```json
{
  "force": {
    "status": "unknown"
  }
}
```

## 20.4 Do not pretend provider prompts are deterministic controls

Provider prompts are a projection surface. Even when documentation describes a control, actual generated video must be verified if the control is critical.

---

# 21. Minimal schema sketch

```yaml
MotionEvent:
  required:
    - motion_id
    - actor_id
    - temporal
    - reference_frame
    - semantics
  fields:
    motion_id: string
    actor_id: string
    temporal:
      start: number
      end: number
      unit: seconds
    reference_frame:
      position: world | camera | actor_local | object_local
      orientation: world | camera | actor_local | object_local
    semantics:
      action: string
      direction: optional
      amplitude: optional
      speed: optional
      acceleration_profile: optional
      effort: optional
    trajectory:
      type: optional
      points: optional
    joints:
      side_indexed: boolean
      values: optional
    phases:
      items: Phase
    evidence:
      class: authored | observed | measured | detected | inferred | interpreted | derived | unknown | unobservable
      confidence: number
      provenance: optional
```

---

# 22. JSONL observation/audit record

```json
{
  "record_type": "motion_observation",
  "observation_id": "obs_00091",
  "asset_id": "video_001",
  "actor_id": "actor_01",
  "quantity": "right_wrist_speed",
  "timestamp": 2.133,
  "timebase": "pts",
  "value": 1.42,
  "unit": "m/s",
  "coordinate_frame": "camera",
  "camera_motion_compensated": false,
  "method": "pose_tracker_v3",
  "confidence": 0.84,
  "occlusion": "none",
  "evidence": {
    "acquisition": "derived",
    "source_acquisition": "detected",
    "epistemic_state": "uncertain",
    "confidence": 0.84
  },
  "provenance": {
    "source_ref": "video_001",
    "locator": "frame:64"
  }
}
```

The pose tracker output is detected and the velocity is deterministically derived from it; therefore this record must not claim a physical `measured` status.

---

# 23. Research-to-runtime example

## Intent

> A boxer throws a fast right cross at an opponent, misses narrowly, recoils and resets. The camera makes a short handheld push toward the action.

## Director representation

```json
{
  "shot": {
    "actors": ["boxer", "opponent"],
    "actions": [
      {
        "type": "punch",
        "actor": "boxer",
        "effector": "right_hand",
        "target": "opponent",
        "contact": {
          "required": false,
          "desired": "near_miss"
        },
        "phases": [
          "anticipation",
          "initiation",
          "acceleration",
          "apex",
          "near_miss",
          "follow_through",
          "recovery"
        ],
        "speed": "fast"
      }
    ],
    "camera": {
      "motion": "handheld_push_in",
      "target": "action_center",
      "duration": 1.4
    }
  }
}
```

## Compiler behavior

```text
"fast"
→ provider motion-speed language
```

```text
"near_miss"
→ explicitly describe fist passing close to target
→ do not emit contact=true
```

```text
"handheld_push_in"
→ native camera control if provider supports it
→ otherwise semantic NL projection
```

## Verification

Measure/inspect:

```text
right-hand action occurs
near-miss rather than contact
recovery occurs
camera moves toward action
actor identities remain stable
left/right is preserved
temporal order is preserved
```

---

# 24. Priority order

## P0 — implement now

Additions from the continuity/causality closure are P0 because they define semantic invariants needed to verify generated-world continuity, not merely additional descriptive vocabulary.

1. explicit coordinate/reference frames;
2. typed time semantics;
3. side-indexed body/hand/foot semantics;
4. canonical motion event;
5. canonical phase graph;
6. interaction lifecycle;
7. evidence classes including `unknown` and `unobservable`;
8. camera semantic object;
9. compiler capability classes;
10. compilation-loss records;
11. round-trip semantic equivalence tests.

## P1 — implement after P0

1. FACS event timing;
2. continuous kinematic measurements;
3. style invariants/forbidden drift;
4. camera optics;
5. complexity feature vector;
6. VOG measurement adapters.

## P2 — experiment before making authoritative

1. universal complexity scalar;
2. jerk as a high-value control;
3. force/torque inference from ordinary video;
4. provider-specific numeric camera semantics;
5. JSON vs YAML vs XML conditioning superiority;
6. direct Laban-to-provider compilation;
7. automatic style-label decomposition.

---

# 25. CPCS_CLOSURE_MATRIX

| Gap | Existing CPCS support | New knowledge required | New representation | Measurement | Compiler effect | Experiment needed | Priority |
|---|---|---|---|---|---|---|---|
| Motion state precision | kinematics/topic coverage stated | frames, units, rotation conventions | `MotionEvent` | pose/trajectory | native/semantic | limited | P0 |
| Rotation convention | pose concepts stated | explicit convention | rotation object | pose orientation | adapter normalization | no | P0 |
| Bilateral semantics | FACS/body concepts stated | side preservation rule | side-indexed values | keypoint/AU detection | provider NL/native | no | P0 |
| Phase grammar | motion phase grammar stated | evidence vs engineering phase | `phase_graph` | boundary timing | ordered action projection | benchmark | P0 |
| Force certainty | force/dynamics stated | measurement vs estimate boundary | evidence-qualified dynamics | sensors/estimator | fail closed | yes | P1 |
| Interaction lifecycle | interactions stated | contact lifecycle and occlusion states | `InteractionEvent` | contact timing/site | semantic/native | benchmark | P0 |
| Camera image formation | camera grammar stated | intrinsic/extrinsic distinction | `CameraState` | calibration | native/approximate | provider test | P1 |
| Style decomposition | style transfer stated | invariant/variation/drift model | `StyleConstraint` | style adherence | compiler projection | yes | P1 |
| Continuity under occlusion | interaction/occlusion coverage | persistence, state-transition and visibility semantics | `ContinuityState`, `StateTransition`, `OcclusionInterval`, `PersistenceConstraint` | identity/count/trajectory continuity | continuity constraints, shot decomposition, explicit loss | mandatory provider evaluation | P0 |
| Causal event structure | phase/interaction coverage | causal dependency separate from temporal order | `CausalEvent` | causal-edge preservation / false positives | dependency ordering and semantic projection | mandatory | P0 |
| Evidence taxonomy | evidence classes | acquisition vs epistemic axes | `EvidenceRecord` | provenance/class consistency | fail-closed on unsupported certainty | no | P0 |
| Complexity | metrics stated | feature definitions/calibration | `ComplexityWindow` | failure-rate labels | routing/budget | mandatory | P2 |
| Carrier choice | YAML/XML/JSON/NL concepts stated | empirical conditioning effects | carrier experiment profile | adherence/token/latency | carrier selection | mandatory | P2 |
| Provider capability | adapters stated | exact capability matrix | capability contract | provider eval | native/approx/semantic/unsupported | continuous | P0 |
| Verification | metrics stated | operational metric definitions | verification contract | video comparison | acceptance gate | mandatory | P0 |

---

# 26. PROPOSED_AGENT_BUILD_PACKET

## Concepts

```text
MotionEvent
Phase
Trajectory
KinematicMeasurement
ContinuityState
StateTransition
OcclusionInterval
PersistenceConstraint
CausalEvent
InteractionEvent
ContactEvent
CameraState
StyleConstraint
ComplexityWindow
EvidenceRecord
CapabilityMatch
CompilationLoss
```

## Required fields

```text
MotionEvent
  actor_id
  effector
  reference_frame
  temporal
  action
  trajectory
  kinematics
  phases
  evidence
  provenance

Phase
  role
  start
  end
  boundary_basis
  confidence
  preconditions
  postconditions

InteractionEvent
  actor_a
  actor_b
  type
  lifecycle
  contact
  visibility
  evidence

CameraState
  pose
  motion
  optics
  focus
  image_formation

StyleConstraint
  domain
  invariants
  allowed_variation
  forbidden_drift
  priority
  evidence

Measurement
  quantity
  value
  unit
  frame
  timebase
  sampling_rate
  method
  confidence
  uncertainty
  missing_data
  occlusion
```

### ContinuityState

```text
entity_id
visibility
existence
identity
actor_count
trajectory_continuity
pose_continuity
action_generation
evidence
provenance
```

### StateTransition

```text
entity_id
type
onset
offset
path
pre_state_ref
post_state_ref
continuity_ref
evidence
```

### OcclusionInterval

```text
entity_id
start
end
cause
visibility
identity_preserved
trajectory_preserved
hidden_state_status
forbidden_generation
evidence
```

### PersistenceConstraint

```text
entity_id
identity
count
wardrobe
topology
existence
visibility
position
priority
```

### CausalEvent

```text
event_id
cause
produces
depends_on
must_not_imply
temporal_relation
evidence
provenance
```

## Mappings

```text
Laban/BESS
→ expressive movement attributes

FACS
→ facial movement events

Kinematics
→ measurable/derived motion quantities

Phase grammar
→ temporal action graph

Interaction grammar
→ contact/reaction graph

Camera grammar
→ camera semantic object

Style labels
→ style constraints

Provider adapters
→ capability matches
```

## Compiler operations

```text
resolve_defaults
normalize_units
normalize_frames
normalize_rotation
expand_side_semantics
resolve_phase_dependencies
resolve_continuity_constraints
resolve_persistence_constraints
resolve_causal_dependencies
validate_evidence
negotiate_capability
compile_native
compile_approximate
compile_semantic
reject_unsupported
emit_compilation_loss
```

## Metrics

```text
schema_validity
round_trip_semantic_equivalence
field_preservation
left_right_preservation
temporal_order_accuracy
phase_boundary_error
contact_timing_error
contact_precision
contact_recall
camera_motion_accuracy
framing_error
identity_consistency
actor_count_consistency
existence_continuity
trajectory_continuity
wardrobe_continuity
prop_continuity
occlusion_transition_error
causal_edge_preservation
causal_false_positive_rate
forbidden_event_rate
style_invariant_violation
forbidden_drift_rate
provider_adherence
measured_vs_target_error
compilation_loss_rate
```

## Fixtures

Minimum fixtures:

```text
1. right-hand reach
2. left-hand reach
3. asymmetric bilateral movement
4. bilateral symmetric movement
5. punch with contact
6. punch near-miss
7. kick
8. grab/hold/release
9. throw
10. jump/land
11. turn
12. recoil
13. camera locked
14. pan
15. tilt
16. dolly
17. orbit
18. handheld tracking
19. rack focus
20. unsupported exact focal-length request
21. unknown force
22. estimated force
23. occluded contact
24. multi-actor identity burden
25. style invariants with forbidden drift
26. actor disappears behind water splash and reappears
27. object remains continuous through occlusion
28. causal miss produces water displacement without actor contact
29. identity-preserving partial occlusion
30. contradictory identity evidence
```

## Tests

```text
test_rotation_convention_required
test_frame_required
test_units_required
test_left_right_not_collapsed
test_bilateral_not_averaged
test_phase_order_preserved
test_contact_not_inferred_from_proximity
test_visibility_change_not_existence_change
test_identity_persists_through_occlusion
test_actor_count_persists_through_occlusion
test_trajectory_continuity_required
test_occlusion_hidden_pose_can_be_unobservable
test_causal_dependency_separate_from_temporal_order
test_causal_edge_preserved_or_loss_recorded
test_force_unknown_when_unobservable
test_estimated_force_requires_method
test_camera_motion_separate_from_subject_motion
test_intrinsics_separate_from_camera_pose
test_style_invariants_survive_compile
test_unsupported_required_control_fails_closed
test_approximate_control_creates_loss_record
test_native_control_has_no_false_loss
test_yaml_json_semantic_equivalence
test_xml_order_preserved
test_nl_projection_is_non_authoritative
```

## Open research questions

1. What phase boundaries are sufficiently reproducible across annotators to become canonical?
2. Which motion quantities improve provider adherence enough to justify their schema complexity?
3. Which kinematic controls survive provider compilation reliably?
4. Which camera controls are actually native versus merely prompt-sensitive for each provider/model/version?
5. Can complexity features predict generation failures sufficiently well to become routing policy?
6. Does structured carrier choice materially change motion adherence when semantic content is held constant?
7. What is the minimum useful style invariant vocabulary?
8. Which force/dynamics estimates are reliable enough for VOG evidence rather than research-only annotations?
9. What calibration is required before a scalar complexity score can be used for production decisions?
10. How should CPCS represent uncertainty when multiple 3D pose hypotheses are equally plausible?
11. Which continuity constraints measurably reduce identity/teleport/pose-reset failures across providers?
12. Which occlusion types require explicit visibility bridges versus ordinary persistence constraints?
13. Can causal-event constraints improve generation outcomes without over-constraining creative variation?
14. Which continuity failures are best addressed by compiler decomposition rather than stronger prompting?

---

# 27. Final architectural conclusion

The main closure is **not** to add more movement terminology.

The missing layer is a typed bridge:

```text
expressive vocabulary
        +
physical/kinematic vocabulary
        +
temporal phase vocabulary
        +
interaction vocabulary
        +
camera vocabulary
        +
style constraints
        ↓
universal canonical semantic kernel
        ↓
capability-aware compiler
        ↓
provider projection
        ↓
observable verification
```

The most important implementation rule is:

> **Never allow a descriptive concept to masquerade as a measured physical quantity, and never allow a provider prompt phrase to masquerade as canonical control.**

For CPCS, the highest-value additions are explicit frames/units, bilateral semantics, phase graphs, interaction lifecycle, evidence-qualified dynamics, camera semantic separation, capability negotiation, compilation-loss auditing, and—after this revision—explicit continuity/persistence/occlusion and causal-event semantics.

The continuity additions are deliberately small:

```text
ContinuityState
StateTransition
OcclusionInterval
PersistenceConstraint
CausalEvent
```

They close a different failure class from ordinary motion adherence. They encode what must remain true when visibility is incomplete and what downstream events are causally permitted. They should therefore be treated as kernel semantics and compiler constraints, not as provider-specific prompt tricks.

Complexity scoring, carrier superiority, and precise physical-force recovery should remain experiments until measured.

---

# 28. Revision note

This v1.1 revision incorporates the supplied critique's five proposed additions:

1. `ContinuityState`
2. `StateTransition`
3. `OcclusionInterval`
4. `PersistenceConstraint`
5. `CausalEvent`

It also separates evidence acquisition from epistemic state and corrects the JSONL wrist-speed example so pose-derived velocity is represented as derived from detected evidence rather than as a physical measurement.

These are **CPCS engineering representations proposed by the closure process**. They are not claimed to be universal external standards. Their production authority should be established by CPCS fixtures, provider evaluations, and verification metrics.

---

# 29. Primary/authoritative sources used for verification

1. Loper et al., **SMPL: A Skinned Multi-Person Linear Model**, SIGGRAPH Asia 2015.
2. Ionescu et al., **Human3.6M: Large Scale Datasets and Predictive Methods for 3D Human Sensing in Natural Environments**, IEEE TPAMI 2014.
3. Pavllo et al., **3D Human Pose Estimation in Video With Temporal Convolutions and Semi-Supervised Training**, CVPR 2019.
4. Zhou et al., **On the Continuity of Rotation Representations in Neural Networks**, CVPR 2019.
5. Paul Ekman Group, **Facial Action Coding System**.
6. McNeill Lab, University of Chicago, **Gesture Annotation / Coding Manual**.
7. Kroemer et al., **Towards Learning Hierarchical Skills for Multi-Phase Manipulation Tasks**, ICRA 2015.
8. Hakala & Häkkinen, **A Method for Measuring Contact Points in Human–Object Interaction Utilizing Infrared Cameras**, Frontiers in Robotics and AI.
9. Li et al., **Estimating 3D Motion and Forces of Person-Object Interactions from Monocular Video**, 2019.
10. OpenCV, **Camera Calibration** documentation.
11. OpenStax, mechanics sections covering force, friction and angular momentum.
12. Runway, **Gen-4 Video Prompting Guide** and current Image-to-Video prompting guidance.
13. Google DeepMind, **How to create effective prompts with Veo 3**.
14. Kling AI, **AI Camera Control Guide**.
15. Singh et al., **The Structured Output Benchmark**, 2026.
16. Yang et al., **StructEval**, TMLR 2026.

