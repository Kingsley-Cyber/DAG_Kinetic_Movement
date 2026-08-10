# Granular Motion Control for AI Video Generation: A Physics-, Biomechanics-, and Animation-Aware Knowledge Base

This synthesis reflects the state of controllable AI video generation on **August 8, 2026**. One important market change is worth stating up front: Sora’s web and app experiences were discontinued on April 26, 2026, and OpenAI says the Sora API will be discontinued on September 24, 2026. Sora 2 remains technically instructive because its prompting guidance is unusually explicit about motion timing, reference images, clip extension, and shot construction, but it should no longer be the foundation of a new long-term production pipeline. citeturn16search0turn17search0turn17search1

A second conclusion cuts across nearly every current system: **text is best used to describe the semantics, character, physical quality, and timing of motion; stronger spatial constraints should be delegated to stronger control signals**. Trajectories, pose/skeleton signals, first/last frames, source performances, reference video, motion sketches, depth, and structural controls are increasingly the mechanisms that determine *where* things go, while text describes *how the movement should feel and why it behaves that way*. Research on trajectory-conditioned generation reaches the same conclusion: ordinary language is poorly suited to specifying detailed spatiotemporal paths, while sparse and dense trajectories provide direct motion constraints. citeturn20search0turn20search3turn20search6

## Biomechanics of human and animal gait

**Objective 1.** The most reliable way to prompt locomotion is to stop thinking of “walking,” “running,” “trotting,” or “sprinting” as single actions. They are **cyclic contact-state machines**. The generator should be told, or externally conditioned on, a sequence of support, load transfer, propulsion, recovery, and re-contact.

Human gait is commonly decomposed into initial contact, loading response, mid-stance, terminal stance, pre-swing, initial swing, mid-swing, and terminal swing. At a coarser level these belong to stance and swing, with double-support periods during walking. Mechanically, walking repeatedly redirects the center of mass over the stance limb; heel and forefoot rocker behavior contributes respectively to early-stance load acceptance and late-stance propulsion. citeturn6search2turn6search4turn6search8turn6search10

### The gait cycle as promptable events

For generative video, anatomical terminology is less useful than **visible mechanical events**:

| Biomechanical phase | What physically matters | Better prompt vocabulary |
|---|---|---|
| Initial contact / heel strike | New support constraint begins | “left heel makes firm contact with the pavement” |
| Loading response | Body mass is accepted by the limb | “the knee flexes slightly as weight settles onto the planted left foot” |
| Mid-stance | Center of mass passes above support | “the pelvis travels forward over the fixed left foot” |
| Terminal stance | Body moves ahead of support | “the heel rises only after the torso has passed the planted foot” |
| Push-off / pre-swing | Ground reaction produces forward impulse | “the forefoot presses into the ground and pushes the body forward” |
| Initial swing | Foot leaves ground; knee flexes | “the toes leave the surface cleanly and the knee flexes for clearance” |
| Mid-swing | Limb advances | “the lower leg swings forward in a smooth pendular arc” |
| Terminal swing | Limb prepares for next contact | “the knee extends without locking as the heel reaches for the next contact” |

The distinction matters because “a man walks naturally” leaves contact mechanics unspecified, whereas “the heel contacts, the sole settles, weight passes over the planted foot, the heel rises, the forefoot pushes, and the toes release” provides a sequence of visible constraints.

OpenAI's Sora 2 guidance independently recommends breaking motion into **beats or counts** rather than giving a generic action label; its example replaces an underspecified walking instruction with a counted sequence of steps, pause, and final action. Runway likewise supports timestamp-oriented sequencing in its current text-to-video guidance, although it warns that timestamps guide rather than precisely dictate timing. citeturn17search0turn15search4

A compact natural-language gait prompt therefore looks like:

> Medium-wide side view. An adult walks at an unhurried, steady pace. Each step has a clear heel contact, brief weight acceptance, pelvis passing over the firmly planted foot, heel rise, forefoot push-off, and clean toe release. The stance foot stays fixed to the pavement until push-off. The pelvis rotates subtly opposite the shoulders; the arms counter-swing naturally. The torso remains vertically supported with a small rhythmic rise and fall of the center of mass. Knees and ankles remain anatomically firm, never rubbery. Three complete steps, constant cadence, then gradual deceleration into a balanced stop.

The structured equivalent should encode *state*, not literary prose:

```yaml
primary_motion:
  type: locomotion
  gait: human_walk
  speed:
    qualitative: unhurried
    target_m_s: 1.25        # metadata/control target; omit from prose if model ignores numbers
  cadence:
    qualitative: steady
  step_length:
    qualitative: moderate

  gait_cycle:
    - phase: initial_contact
      cue: "heel makes firm ground contact"
    - phase: loading_response
      cue: "knee yields slightly as body weight transfers onto the foot"
    - phase: mid_stance
      cue: "pelvis and center of mass pass over the fixed stance foot"
    - phase: terminal_stance
      cue: "heel rises after the body has moved ahead of the stance foot"
    - phase: push_off
      cue: "forefoot pushes against the ground"
    - phase: initial_swing
      cue: "toes release cleanly; knee flexes for clearance"
    - phase: mid_swing
      cue: "leg advances in a smooth forward arc"
    - phase: terminal_swing
      cue: "knee extends softly; heel prepares for next contact"

  coordination:
    pelvis_rotation: subtle
    shoulder_rotation: opposite_pelvis
    arm_counter_swing: natural
    torso_lean: slight_forward
    com_vertical_motion: subtle_periodic
    joint_behavior: "firm, anatomically constrained, mildly elastic"

constraints:
  support:
    stance_foot_world_locked: true
    weight_transfer_visible: true
    toe_release_after_push_off: true
```

The numeric velocity belongs primarily in your **motion specification and experiment record**. Proprietary video models do not guarantee that “1.25 m/s” will be realized metrically. When accuracy matters, convert that target into a point trajectory, skeleton animation, reference performance, or known travel distance/time.

### Variables that make gait look heavy, light, fast, or intentional

A locomotion description becomes substantially more controllable when it separates these variables:

**Speed and cadence** determine the rate of the cycle. **Step length** determines spatial displacement per step. **Trunk lean** signals acceleration and running effort. **Pelvic rotation** extends reach and contributes to whole-body coordination. **Arm counter-swing** helps visually communicate balance and angular-momentum management. **Center-of-mass motion** communicates whether mass is actually being supported by the legs. **Joint stiffness/compliance** determines whether motion reads as athletic, elderly, fatigued, robotic, loose, or rubbery.

Rather than writing:

> Powerful athletic walk with good biomechanics.

write:

> Fast purposeful walk, long but not exaggerated steps, slightly higher cadence, small forward trunk lean, firm knee tracking, compact vertical center-of-mass excursion, pelvis rotating subtly with each step, shoulders counter-rotating, arms swinging opposite the legs. Every stance foot remains anchored until heel rise and push-off.

“Joint tension,” in particular, is usually better translated into visible behavior:

```yaml
joint_behavior:
  knee:
    stiffness: medium_high
    flexion_on_loading: small
    hyperextension: forbidden_in_spec
  ankle:
    compliance: moderate
    behavior: "compresses under load, then plantarflexes during push-off"
  elbow:
    stiffness: moderate
    swing: "relaxed but structurally stable"
```

The compiler might turn that into:

> Knees and elbows remain structurally firm with controlled flexion; limb lengths stay constant; joints do not wobble under load.

### Animal gait requires support-pattern language

Quadrupeds need another layer: **which limbs contact the ground together, and in what phase relationship?** Slow mammalian walking tends toward four-beat sequences; trotting produces paired rhythm, typically organized around diagonal limb coordination; higher-speed galloping becomes asymmetric and may include aerial phases. Experimental dog measurements also show that increasing locomotion speed strongly shortens stance time while swing time changes much less, making duty factor an important cue for speed. citeturn14search8turn14search11

For example:

> A large dog moves in a steady working trot. Diagonal limb pairs coordinate rhythmically: left foreleg with right hindleg, then right foreleg with left hindleg. Ground contacts are crisp and load-bearing. The torso remains supported rather than floating. The shoulder and hip joints swing cyclically, elbows and knees flex more during limb recovery, and stance duration is shorter than during a walk. The head remains comparatively stabilized while the spine and tail provide restrained secondary balance motion.

```yaml
primary_motion:
  type: quadruped_locomotion
  species_profile: large_dog
  gait: trot

  support_pattern:
    symmetry: bilateral
    paired_contacts:
      - [left_fore, right_hind]
      - [right_fore, left_hind]

  phases:
    stance:
      duration: shorter_than_walk
      foot_contact: firm
      load_bearing: true
    swing:
      limb_flexion: increased
      purpose: ground_clearance

  body_coordination:
    spine_motion: restrained_elastic
    head_stabilization: moderate
    tail_balance: subtle
```

### Failure modes and exact corrective interventions

Current human-motion benchmarks still find temporal instability, anatomically implausible poses, and motion drift in generated humans; HumanScore was introduced in 2026 specifically to evaluate generated human motion through kinematic plausibility, temporal stability, and biomechanical consistency rather than visual quality alone. citeturn20search2

The highest-value corrections are:

| Failure | Underlying representation problem | Prompt intervention | Stronger non-text intervention |
|---|---|---|---|
| **Foot sliding** | Model changes foot position while treating it as support | “The stance foot remains fixed relative to the pavement from contact through heel rise; body weight travels over it before push-off.” | Track heel/ankle; pose sequence; reference performance |
| **Floating / weightless torso** | No visible load acceptance or reaction force | “On each landing the supporting knee compresses slightly, the pelvis settles, then rebounds as the leg pushes against the ground.” | Pose/ref video; stable ground plane |
| **Rubbery knees/elbows** | Articulation underconstrained | “Limb lengths remain constant; joints follow anatomical hinge-like arcs with firm tracking and no hyperextension.” | Skeleton/pose conditioning |
| **Abrupt start** | Missing anticipation and acceleration | “Brief weight shift forward; first step short; accelerate over the next two steps.” | Reference clip containing acceleration |
| **Abrupt stop** | Velocity disappears without braking | “Shorten the final two steps, reduce forward speed progressively, shift weight onto the lead foot, then settle.” | Last-frame/keyframe + timing |
| **Moonwalking** | Swing/support states confused | Explicitly distinguish “planted stance foot” from “airborne recovery foot” | Two ankle trajectories or skeleton |
| **Leg teleportation** | Too much distance per temporal interval | Reduce requested travel, cadence, camera motion, or duration complexity | Denser pose/motion trajectory |
| **Gait/camera interference** | Global optical flow mistaken for body translation | Temporarily freeze camera while debugging gait | Camera control separated from subject control |

The core rule is:

> **Treat every locomotion problem as a support-contact problem before treating it as a style problem.**

“Realistic walking” is a style request. “The left foot is world-locked while load passes over it” is a mechanical constraint.

## Rigid-body and soft-body physics for prompting

**Objective 2.** A useful physics prompt should describe a **causal chain**:

**initial state → applied force → acceleration/deformation → free evolution → contact/collision → reaction → damping/deceleration → settled state.**

Simply writing “realistic physics,” “natural weight,” or “physically accurate motion” leaves the causal sequence unspecified. This is especially important because current research shows that physical plausibility remains a weakness of video generators. WMReward, for example, treats physics improvement as an inference-time alignment problem and obtains better results by using a latent world model to select or steer physically plausible generations rather than relying on text alone. citeturn20search1turn20search4

Research on **Force Prompting** goes one step further by explicitly conditioning generative systems on localized or global forces, such as a point force applied to an object or a wind field applied to fabric. This reinforces an important design principle: when the control interface permits it, forces themselves can be more informative than prose about the expected outcome. citeturn20search9

### Rigid-body prompting

For a heavy crate:

**Weak**

> A heavy wooden crate is pushed realistically with natural weight and momentum.

**Stronger**

> The crate begins fully at rest. The worker leans into it and applies sustained horizontal force. For a brief moment the crate resists because of floor friction, then accelerates slowly. While the push continues it gains speed gradually. When the hands release, it keeps moving forward from inertia while floor friction steadily slows it. It stops without bouncing. The worker's upper body reacts backward slightly when contact ends.

```yaml
physics:
  body_type: rigid
  mass_impression: heavy
  initial_state:
    velocity: zero
    grounded: true

  force_events:
    - source: worker_hands
      target: crate
      direction: forward
      onset: gradual
      duration: sustained

  expected_response:
    acceleration: low
    inertia_after_release: visible
    friction_deceleration: gradual
    bounce: negligible

  contacts:
    floor:
      persistent: true
      friction: high
    hands:
      reaction_visible_on_worker: true

  settle:
    oscillation: none
    final_velocity: zero
```

The phrase **“natural weight and momentum throughout”** is useful as a summary, but it should come *after* observable mechanics, not substitute for them.

A useful rigid-body vocabulary map is:

| Physics variable | Prompt-visible language |
|---|---|
| Mass | “accelerates slowly under the push,” “requires sustained effort” |
| Momentum | “continues moving after the force ends” |
| Inertia | “does not instantly match the hand's motion” |
| Static friction | “resists briefly before beginning to slide” |
| Kinetic friction | “gradually loses speed across the floor” |
| Impulse | “a sharp impact produces an immediate change in velocity” |
| Reaction force | “the striker recoils as the object accelerates away” |
| Restitution | “small rebound,” “dead impact,” “springy bounce” |
| Damping | “oscillations become smaller with each cycle” |
| Gravity | “accelerates downward continuously once unsupported” |
| Contact constraint | “remains flush against the surface without penetration” |

### Do not prompt equations when you can prompt consequences

A generator is unlikely to honor literal equations such as:

```yaml
force_newtons: 180
mass_kg: 60
friction_coefficient: 0.42
```

unless a surrounding system converts those quantities into trajectories or simulator outputs.

Keep such values in your **source specification** because they are useful for simulation, procedural controls, and experiments, but compile them into visible consequences:

```yaml
compiler:
  verbalize_physics:
    mass_kg: "heavy, slow to accelerate"
    friction_coefficient: "noticeable resistance and gradual deceleration"
```

This distinction is supported by recent physics-generation research: specifying desired physical behavior in language creates a **specification bottleneck** because prose omits many variables required to determine dynamics. In other words, a physics-aware prompt representation can be much richer than the final text sent to a proprietary generator. citeturn13view1

### Contact is where physical plausibility is won or lost

For impact, landing, grabbing, pushing, kicking, or sitting, explicitly describe:

1. approach;
2. first contact;
3. load/impulse;
4. deformation or recoil;
5. resulting motion;
6. damping/settling.

For example:

> The basketball falls under gravity, compresses subtly at floor contact, reverses direction immediately, rises to a lower height, then repeats with progressively smaller bounces until it settles.

This encodes gravity, collision response, restitution, deformation, and energy loss without asking the model to solve a numerical mechanics problem.

### Soft-body prompting: separate primary response from secondary motion

Cloth, hair, water, smoke, sand, and viscoelastic materials should not all be described as “flowing.” Their useful abstractions differ substantially. Physics-based computer graphics likewise treats cloth as deformable sheets, hair as constrained elastic strands, water/smoke as fluids, and sand as granular matter rather than as interchangeable deformable effects. citeturn21search0turn21search1turn21search2turn21search3

| Material | Primary behavior to encode | Secondary behavior to encode |
|---|---|---|
| **Fabric** | attached points, drape, stretching resistance, collision | folds lag body motion, waves propagate, then damp |
| **Hair** | roots anchored; strands bend | tips lag, overshoot, swing back, settle |
| **Skin/soft tissue** | localized compression under force | small damped return/jiggle |
| **Water** | gravity-driven bulk flow, volume continuity, impacts | splashes, droplets, ripples, residual waves |
| **Sand** | granular displacement, pile formation, friction | grains scatter, avalanche locally, tracks persist |
| **Smoke** | advected buoyant volume | curling vortices, turbulent breakup, diffusion |
| **Dough** | slow plastic/viscoelastic deformation | delayed partial recovery |
| **Silicone** | elastic compression and shear | overshoot plus damped recovery |

Cloth simulation research emphasizes elastic/internal forces and contact/collision; mechanical hair models treat strands as elastic rods or constrained strand systems; established graphics simulation treats smoke and water as fluid dynamics; granular-simulation methods explicitly model sand as interacting particles or elastoplastic granular matter. citeturn21search31turn21search19turn21search24turn21search2turn21search7turn21search30

A fabric example:

> The runner's torso drives the motion. The jacket is attached at the shoulders and waist and does not move independently. During acceleration the loose fabric initially lags behind the torso, then catches up. Each stride sends a small fold wave through the hem. When the runner stops, the body stops first; the jacket hem continues forward briefly, swings back once with smaller amplitude, then settles.

```yaml
secondary_action:
  - element: jacket
    driver: torso_translation
    material: lightweight_fabric

    attachment:
      anchors: [shoulders, waist]

    response:
      onset: delayed
      direction: opposite_initial_acceleration
      amplitude: low_medium
      propagation: "small fold wave toward hem"

    follow_through:
      after_primary_stop: true
      overshoot: small
      damping: high
      settle_cycles: 1
```

For hair:

> The head turn is the primary action. Hair roots follow the skull immediately; the loose ends lag behind the turn, sweep through a curved arc, pass the final head orientation slightly, then return with one damped settling motion.

```yaml
secondary_action:
  - element: long_hair
    parent_motion: head_yaw
    root_lock: head
    phase_delay: small
    amplitude: moderate
    path: curved_arc
    overshoot: subtle
    damping: medium_high
```

### Secondary motion timing

There is no universally validated “correct” frame delay for generative video. Delay depends on mass, stiffness, damping, speed, model, frame rate, and the strength of external control.

For experimentation at 24 fps, a useful **starting heuristic**, not a law, is:

- tight clothing / short hair: roughly 1–3 frames of perceptual lag;
- loose jacket hem / long hair: roughly 2–6 frames;
- heavier pendulous accessory: roughly 4–8 frames;
- settling may extend several additional frames after the primary body stops.

Classical animation formalizes the broader concepts—follow-through and overlapping action—without prescribing a universal frame count. citeturn7search0

Represent this relatively whenever possible:

```yaml
secondary_action:
  phase_delay:
    relative_to_primary_period: 0.08
  amplitude_ratio:
    relative_to_primary: 0.25
  damping:
    settle_fraction_of_clip: 0.15
```

Relative timing scales more gracefully when clip length changes.

### Subtractive prompting is often more powerful than “negative prompting”

When a motion fails, the best first intervention is frequently to **remove degrees of freedom**:

> moving person + moving camera + moving background + wind + hair + cloth + interaction

becomes:

> static camera + simple floor + one person + one action.

This matches OpenAI's Sora guidance to strip a failing shot back, keep motion simple, and use one camera action plus one subject action. Runway similarly tells users not to underestimate prompt simplicity, while Gen-4 guidance specifically favors positive phrasing rather than negative prompts. citeturn17search0turn15search2

Therefore distinguish:

**Good subtractive strategy**

> Remove camera orbit. Remove crowd. Remove wind. Test only the walk.

from:

**Potentially counterproductive negative prompt**

> no sliding, no wobbling, no floating, no morphing, no glitches, no strange legs...

Many current systems respond more consistently to a positive target state:

> Feet remain firmly planted during stance; limb lengths remain constant; joints move through stable anatomical arcs.

For Luma's Ray3.2 video-to-video workflow, Luma similarly recommends describing the desired resulting state and avoiding temporal/imperative or negation-heavy instructions. citeturn9search5

## Classical animation principles applied to AI video

**Objective 3.** Traditional animation principles remain valuable because they convert vague “natural motion” into temporal relationships. John Lasseter's influential 1987 SIGGRAPH paper explicitly adapted traditional principles such as timing, anticipation, follow-through, slow-in/slow-out, arcs, and secondary action to computer animation. citeturn7search0

The important adaptation for generative video is to treat them as **constraints on temporal organization**, rather than stylistic buzzwords.

### Weight

Weight is perceived when movement has consequences: acceleration takes time, support limbs compress, contacts produce reactions, heavy objects continue moving, and braking takes distance.

**Weak**

> He lifts a heavy suitcase.

**Physics/animation-aware**

> He braces his feet first, bends at the hips and knees, grips the suitcase, shifts his center of mass backward, then drives upward through the legs. The suitcase leaves the floor slightly after his body begins exerting force. His shoulders rise under load and his arms remain visibly tensioned. At the top, his body makes a small corrective balance shift before settling.

```yaml
primary_motion:
  action: lift_heavy_suitcase
  anticipation:
    - brace_feet
    - lower_center_of_mass
    - establish_grip
  effort:
    acceleration: slow
    body_compensation: visible
  contact:
    suitcase_ground_release: delayed_until_force_builds
  settle:
    corrective_balance_shift: small
```

### Timing and spacing

Timing determines **how long** an event takes; spacing determines **how position changes within that time**. Constant spacing reads mechanically uniform. Increasing spacing corresponds perceptually to acceleration; decreasing spacing to deceleration.

For text-driven systems, convert that into beats:

> 0–1 s: shifts weight forward.  
> 1–3 s: accelerates through the first three running steps.  
> 3–6 s: maintains a constant stride.  
> 6–8 s: progressively shortens steps and decelerates to rest.

Runway's current text-to-video guidance explicitly supports timestamp prompts as a way to guide general sequencing, while warning they are not perfectly precise. Sora recommends action counts and beats for the same reason. citeturn15search4turn17search0

```yaml
temporal_structure:
  - range: [0.0, 0.12]
    beat: anticipation
  - range: [0.12, 0.38]
    beat: acceleration
  - range: [0.38, 0.75]
    beat: steady_state
  - range: [0.75, 0.95]
    beat: deceleration
  - range: [0.95, 1.0]
    beat: settle
```

Use normalized fractions in your master schema; compile them to seconds once duration is known.

### Anticipation

Anticipation prepares the body's mechanical state.

Before a jump:

> The athlete lowers the hips, flexes knees and ankles, swings the arms backward, pauses for a fraction of a beat, then explosively extends the legs and swings the arms forward into takeoff.

Do not merely write:

> anticipation before jumping.

Encode the visible counter-motion.

```yaml
anticipation:
  duration_fraction: 0.15
  actions:
    - lower_com
    - knee_flexion
    - ankle_dorsiflexion
    - arms_swing_backward
  transition_to_primary:
    continuous: true
```

### Follow-through

Primary motion ends first; attached or loosely coupled systems continue.

> The runner stops first. The ponytail swings forward past the head's resting orientation, reverses, and settles with decreasing amplitude.

```yaml
follow_through:
  element: ponytail
  primary_stop_time: 0.78
  continue_after_primary: true
  overshoot: moderate
  oscillations: 1_to_2
  amplitude_decay: strong
```

### Overlapping action

Not every body part starts and stops simultaneously.

A natural turn might be:

> Eyes shift first, head follows, shoulders begin rotating a moment later, pelvis follows after the shoulders, and the coat hem catches up last.

```yaml
overlapping_action:
  phase_order:
    - eyes
    - head
    - shoulders
    - pelvis
    - garment
  phase_offsets:
    eyes_to_head: small
    head_to_shoulders: small
    shoulders_to_pelvis: small
    pelvis_to_garment: medium
```

This often produces a better generative instruction than asking for “fluid full-body rotation.”

### Slow-in / slow-out

Use acceleration language explicitly:

> The hand begins moving almost imperceptibly, accelerates through the middle of the reach, then progressively slows as the fingertips approach the glass.

```yaml
motion_profile:
  easing: ease_in_out
  acceleration:
    start: low
    middle: peak
    end: negative
```

For physically ballistic actions, however, do not apply symmetrical ease-in/ease-out blindly. A thrown object may leave the hand with high velocity and then follow gravity, while impact introduces a discontinuous change in velocity. Animation principles should respect mechanics rather than override them.

### Arcs

Human limb endpoints rarely move as arbitrary straight sliders because most motion arises from rotating joints.

> The hand reaches toward the cup through a shallow curved arc driven by shoulder and elbow rotation.

```yaml
trajectory:
  end_effector: right_hand
  geometry: shallow_arc
  origin: current_hand_position
  target: cup_handle
```

A trajectory control is preferable when the exact arc matters. Motion Prompting and ATI both demonstrate trajectory-based representations capable of expressing object movement, camera movement, and localized deformation more directly than prose. citeturn20search0turn20search6

### Secondary action

Secondary action should reinforce the primary action rather than compete with it.

For a walk:

```yaml
primary_motion:
  action: forward_walk
  priority: 1.0

secondary_actions:
  - action: arm_counter_swing
    parent: gait_cycle
    priority: 0.35
    amplitude: subtle

  - action: ponytail_follow_through
    parent: head_and_torso
    priority: 0.18
    phase_delay: small
```

Avoid:

```yaml
primary_motion:
  - walking
  - waving
  - turning_around
  - jumping
  - looking_behind
  - removing_jacket
  - dodging_people
```

unless a model is specifically operating in a multishot/storyboard mode.

This “one dominant motion” principle is not merely classical-animation advice. Sora's official guide says that motion is one of the hardest aspects of generation and recommends **one clear camera move and one clear subject action per shot**. Runway likewise recommends beginning simply and layering complexity iteratively. citeturn17search0turn15search2

A useful complexity budget is:

```yaml
motion_budget:
  dominant_subject_action: 1
  major_camera_move: 1
  secondary_body_actions: 1_to_2
  passive_material_responses: 1_to_3
```

This is a production heuristic, not a universal architectural limit.

## Modular prompt architecture and markup languages

**Objective 4.** YAML, JSON, or XML should be treated primarily as a **motion intermediate representation**, not as magic syntax that proprietary video models intrinsically understand better.

That distinction is critical.

Most official proprietary-model documentation still teaches natural-language prompting. OpenAI recommends concrete prose organized around shot/action/camera/timing; Runway recommends natural-language motion descriptions; Google's Veo documentation breaks prompts into semantic components. There is not currently strong vendor-published evidence that simply wrapping the same prose in raw YAML improves Sora, Veo, Runway, Kling, or Luma video fidelity. citeturn17search0turn15search0turn15search3

Structured representations nevertheless offer enormous workflow advantages:

**human reproducibility → validation → reusable modules → parameter injection → model-specific compilation → experiment tracking.**

Research systems have begun using structured textual representations such as JSON, XML, or YAML to encode hierarchical spatial and temporal structure, and systems such as VISTA use YAML-like structured instructions as an intermediate layer for downstream video-generation prompting. This supports the architecture, but it should not be misread as proof that every proprietary generator natively performs better when fed raw YAML. citeturn13view4turn5search3

### The recommended architecture

Use:

**YAML source of truth → validation → control resolver → model dialect compiler → generation API/UI**

rather than:

**YAML pasted blindly into every video model.**

Conceptually:

```text
motion_scene.yaml
       │
       ├── semantic compiler ───────→ concise natural-language prompt
       │
       ├── timing compiler ─────────→ timestamp / beat instructions
       │
       ├── trajectory compiler ─────→ point tracks / splines
       │
       ├── pose compiler ───────────→ skeleton sequence
       │
       ├── reference resolver ──────→ image/video/element IDs
       │
       └── model adapter ───────────→ Sora / Runway / Veo / Kling /
                                       Luma / LTX / MiniMax / Seedance
```

### Recommended master YAML schema

The following schema deliberately keeps **physical intent**, **observed motion**, **hybrid controls**, and **model compilation** separate.

```yaml
schema:
  name: physics_aware_video_motion
  version: "1.0.0"

project:
  id: gait_test_014
  shot_id: shot_003
  module_versions:
    gait: human_walk_v1.4
    cloth: light_jacket_followthrough_v0.7
    camera: lateral_track_v1.1

target:
  model_family: runway
  model_version: gen-4.5
  mode: image_to_video
  duration_s: 8
  fps_target: 24
  aspect_ratio: "16:9"

intent:
  dominant_action: "adult walks steadily from left to right"
  realism_priority: high
  motion_priority: high
  identity_priority: high

subject:
  id: subject_a
  type: human

  appearance:
    source: reference_image
    lock_priority: high

  physical_properties:
    height_m: 1.78
    mass_impression: medium
    build: athletic
    limb_proportions: natural
    joint_stiffness: medium_high

  clothing:
    upper:
      type: lightweight_jacket
      material_behavior: flexible_damped
    lower:
      type: trousers

initial_state:
  subject_pose: upright
  support:
    left_foot: planted
    right_foot: unloaded
  linear_velocity:
    qualitative: slow_forward
  angular_velocity:
    qualitative: near_zero
  camera_state:
    motion: already_tracking

primary_motion:
  category: locomotion
  action: walk
  priority: 1.0

  path:
    geometry: straight
    screen_direction: left_to_right

  biomechanics:
    gait: normal_walk
    speed: moderate
    cadence: steady
    step_length: moderate
    trunk_lean: slight_forward

    coordination:
      pelvis_rotation: subtle
      shoulder_counter_rotation: subtle
      arm_counter_swing: natural

    center_of_mass:
      forward_progression: continuous
      vertical_excursion: subtle
      lateral_shift: small

    gait_cycle:
      - initial_contact
      - loading_response
      - mid_stance
      - terminal_stance
      - push_off
      - initial_swing
      - mid_swing
      - terminal_swing

  contact_mechanics:
    stance_foot_world_locked: true
    weight_acceptance_visible: true
    heel_rise_after_com_passes: true
    toe_off_after_push: true
    ground_penetration: false

  dynamics:
    acceleration_profile: steady
    momentum_continuity: high
    joint_compliance: controlled

secondary_actions:
  - id: arm_swing
    driver: gait_cycle
    relationship: counter_phase
    amplitude: moderate
    delay: minimal
    priority: 0.35

  - id: jacket_followthrough
    driver: torso
    relationship: passive
    material: lightweight_fabric
    delay:
      qualitative: slight
      frames_at_24fps_starting_guess: 3
    amplitude: low
    overshoot: subtle
    damping: high
    priority: 0.15

environment:
  surface:
    type: dry_asphalt
    planar: true
    traction: high

  interaction:
    foot_contact:
      shadow_consistency: required
      displacement: none
    wind:
      strength: calm

camera:
  framing: medium_wide
  perspective: side_view
  move:
    type: lateral_tracking
    direction: left_to_right
    speed_relationship: match_subject_average_speed
    acceleration: smooth

  stabilization: high
  focal_behavior: fixed_subject_distance

temporal_structure:
  units: normalized

  beats:
    - interval: [0.00, 0.10]
      state: establish_motion
    - interval: [0.10, 0.80]
      state: steady_gait
    - interval: [0.80, 0.96]
      state: gradual_deceleration
    - interval: [0.96, 1.00]
      state: balanced_settle

physics:
  gravity: earthlike
  inertia: visible
  momentum_continuity: required
  contact_reaction: visible
  damping: physically_plausible

constraints:
  positive:
    - "stance feet remain fixed relative to the ground"
    - "limb lengths remain constant"
    - "joints move through stable anatomical arcs"
    - "body mass is visibly supported by the stance leg"
    - "acceleration and deceleration are gradual"

  diagnostic_failures:
    - foot_sliding
    - floating_center_of_mass
    - limb_length_drift
    - joint_rubberiness
    - instantaneous_velocity_change

hybrid_controls:
  first_frame:
    enabled: true
    asset: subject_start.png
    owns:
      - identity
      - wardrobe
      - composition

  last_frame:
    enabled: false

  motion_tracks:
    enabled: true
    tracks:
      - id: pelvis_track
        target: pelvis
        role: global_subject_translation

  pose:
    enabled: false
    source: null

  reference_video:
    enabled: false
    source: null

control_ownership:
  identity: first_frame
  wardrobe: first_frame
  subject_path: motion_tracks
  biomechanics_quality: text_prompt
  contact_logic: text_prompt
  secondary_material_motion: text_prompt
  camera_path: camera_control
  final_pose: generative_model

compiler:
  prose_style: concise_visual
  use_positive_constraints: true
  include_raw_numbers: only_when_model_supports
  max_major_actions: 1

  dialect:
    runway:
      image_to_video:
        omit_static_visual_description: true
        emphasize_motion: true

    sora:
      use_action_counts: true
      max_primary_actions_per_shot: 1

    luma_ray32:
      describe_target_state_not_commands: true

evaluation:
  expected:
    stance_slip_score_max: 0.08
    limb_length_variation_max: 0.05
    trajectory_error_max: 0.08

  human_review:
    weight: 1_to_5
    contact: 1_to_5
    temporal_fluidity: 1_to_5
    secondary_motion: 1_to_5
```

The deliberately model-neutral fields are the valuable part. The `compiler.dialect` section prevents the same structured specification from being naively fed to incompatible interfaces.

### Variable injection

Define reusable modules:

```yaml
modules:
  human_walk:
    vars:
      speed: moderate
      cadence: steady
      step_length: moderate
      trunk_lean: slight

  cloth_followthrough:
    vars:
      material: lightweight
      lag: slight
      damping: high

scene:
  use:
    - module: human_walk
      with:
        speed: brisk
        cadence: moderately_high

    - module: cloth_followthrough
      with:
        material: heavy_wool
        lag: moderate
        damping: medium
```

Your compiler then creates:

> Brisk purposeful walk with moderately high cadence. Clear heel contact and weight transfer on every step; stance feet remain fixed until heel rise and forefoot push-off. Heavy wool coat follows the torso with moderate delayed motion, one restrained overshoot, then damped settling.

### Version your modules as code

Store:

```text
motion_modules/
  locomotion/
    human_walk_v1.0.yaml
    human_walk_v1.1.yaml
    sprint_acceleration_v0.8.yaml

  contacts/
    foot_plant_v1.3.yaml
    heavy_landing_v1.2.yaml

  materials/
    long_hair_v0.9.yaml
    light_cloth_v1.0.yaml

  camera/
    static_v1.0.yaml
    lateral_track_v1.2.yaml

experiments/
  gait_001/
    baseline.yaml
    condition_a.yaml
    condition_b.yaml
    scores.csv
```

Each version should record:

```yaml
module_metadata:
  version: "1.3.0"
  tested_on:
    - runway_gen_4_5
    - veo_3_1
    - ltx_2_3

  change_log:
    - "Added explicit stance-foot world lock."
    - "Moved arm swing from primary action to secondary layer."

  evidence:
    generations: 48
    improved_metric: stance_slip
    relative_result: "better than v1.2 in internal test"
```

Do **not** label a prompt module “proven” merely because one attractive generation succeeded. Generative systems are stochastic, and vendor models can change.

### Structured versus pure natural language

The most defensible current conclusion is:

| Use of structure | Evidence level |
|---|---|
| Better human organization and reproducibility | **High** |
| Easier variable isolation and A/B testing | **High** |
| Easier routing to pose/trajectory/reference controls | **High** |
| Better modular production pipelines | **High** |
| Raw YAML intrinsically improves Sora/Runway/Veo output | **Unverified** |
| A compiled structured representation can improve control | **Strong architectural rationale; supported by research systems** |

Structured-text research shows that temporal/spatial relationships can be represented hierarchically in JSON/XML/YAML-like forms, but official commercial prompting guides remain centered on natural language and multimodal controls. citeturn13view4turn17search0turn15search3

Therefore:

> **Use YAML as your control language. Use model-native prose and native controls as your execution language.**

## Motion prompting and hybrid controls

**Objective 5.** The emerging control stack can be understood as a hierarchy of signal authority.

The mistake is to give **every signal responsibility for everything**.

Instead, assign ownership.

| Property | Best signal |
|---|---|
| Identity / wardrobe / object design | reference image, element, ingredient |
| Initial composition | first frame |
| Final composition / pose | last frame / terminal keyframe |
| Exact path | point tracks / trajectories |
| Articulated pose | skeleton / pose control |
| Performance rhythm | reference video / performance capture |
| Camera trajectory | native camera control, camera track, or explicit camera prose |
| Motion style / effort / weight | text |
| Contact logic | text + pose/trajectory/ref video |
| Material response | text; stronger with source simulation/video |
| Environment geometry | depth/structure/edge controls |
| Shot timing | timestamps, beats, reference motion, storyboard |
| Audio rhythm | audio/reference signal where supported |

Trajectory-conditioned research makes the sparse/dense distinction explicit. Motion Prompting supports spatiotemporally **sparse or dense** trajectories for object and global scene motion and introduces “motion prompt expansion” to transform higher-level requests into denser trajectories. ATI similarly seeks to unify camera, object, and local deformation control under trajectory representations. citeturn20search0turn20search6

### Sparse versus dense tracks

Use **sparse tracks** when:

- only overall object direction matters;
- the model should retain freedom to synthesize articulation;
- you are directing a camera path;
- you want a person's pelvis to move through space without prescribing each joint.

Example:

```yaml
motion_tracks:
  - target: pelvis
    interpolation: spline
    points:
      - {t: 0.00, x: 0.20, y: 0.62}
      - {t: 0.50, x: 0.50, y: 0.61}
      - {t: 1.00, x: 0.82, y: 0.62}
```

Use **denser trajectories or skeleton controls** when:

- hand placement matters;
- feet must contact known locations;
- precise interaction is required;
- dance/choreography must match;
- limb sequencing cannot be safely inferred.

LTX-2.3 makes this paradigm directly usable: its Motion-Track-Control IC-LoRA accepts sparse spline-based trajectories visualized as trails of circles and supports one or several simultaneous motion paths. LTX also provides pose, depth, and Canny control workflows in its open model ecosystem. citeturn18search2turn18search5

### Complement trajectories with qualitative text

Do not merely send:

```yaml
track: A -> B -> C
```

Pair it with:

> The pelvis follows the supplied path at a steady walking cadence. Translation is produced by alternating planted steps rather than gliding. Each stance foot is fixed to the floor while the pelvis travels over it. The torso maintains balanced vertical support; arm swing remains secondary.

Trajectory owns **path**.

Text owns **locomotion mechanism and quality**.

### Region-direction and motion-sketch controls

The old “paint a region and draw its direction” idea remains conceptually useful, but terminology differs by platform.

Runway's legacy **Motion Brush** belonged to older Gen-2 workflows; Gen-3 has also been retired. Current Runway tooling instead includes newer mechanisms such as **Motion Sketch**, keyframe-oriented apps, and performance-transfer tooling alongside Gen-4.5. Treat tutorials telling you to use Gen-2 Motion Brush on current Runway as historical. citeturn2search2turn2search3turn8search0

A region-control text companion should explain mechanism:

> The highlighted sleeve follows the arm's movement passively; its shoulder seam stays attached while the cuff lags behind the hand and settles after the arm stops.

not:

> Move this area right.

### First-frame conditioning

First frames are excellent at assigning the generator a well-posed initial state.

OpenAI describes Sora image input as an anchor for the first frame that can lock character design, wardrobe, set dressing, and aesthetic while text tells the model what happens next. Runway's current image-to-video guide likewise recommends focusing the text primarily on motion because the image already establishes composition and appearance. citeturn17search0turn15search0

A strong I2V prompt therefore omits redundant appearance prose:

> The subject shifts weight onto the left leg, takes three measured steps forward, stops gradually, and settles into a balanced stance. Feet remain firmly planted through each load-bearing phase. Camera remains nearly static.

rather than redescribing every visual feature already present.

### First-and-last-frame control

Boundary-frame control is one of the highest-value tools for transformations, pose transitions, and known endpoints.

Veo 3.1 officially supports first-and-last-frame workflows, with Google advising users to describe the **transition** between the supplied endpoint images. citeturn15search1turn15search7

Kling VIDEO 3.0 likewise supports start/end-frame video generation, and LTX-2.3's API includes first-to-last-frame control. citeturn18search1turn18search11

Use:

```yaml
hybrid_controls:
  first_frame:
    owns: [initial_pose, identity, framing]

  last_frame:
    owns: [terminal_pose, endpoint_composition]

text_owns:
  - transition_quality
  - acceleration_profile
  - contact_mechanics
  - secondary_motion
```

Prompt:

> Begin from the supplied first pose and arrive naturally at the supplied final pose. The character does not interpolate as a floating morph: the transition is produced by two grounded steps, visible weight transfer, and a gradual torso rotation. The hair follows the head turn with delayed, damped motion.

### Pose and skeleton conditioning

Pose/skeleton control should own **articulation geometry**, especially when hands, knees, foot contacts, dance poses, or specific body mechanics matter.

LTX currently exposes pose control through IC-LoRA workflows, illustrating the direction in which open systems are moving. citeturn18search5

Text can then be simplified:

```yaml
pose_control:
  owns:
    - joint_locations
    - limb_phase
    - footfall_sequence

text_prompt:
  owns:
    - effort
    - mass
    - compliance
    - contact_quality
    - follow_through
```

A pose sequence that is mechanically bad will not necessarily be rescued by “realistic biomechanics.” Control signals must themselves encode plausible motion.

### Reference-video and performance-transfer conditioning

Reference performance is often the most powerful signal for complex human motion because it bundles:

- trajectory;
- articulation;
- timing;
- phase relationships;
- acceleration;
- expressive rhythm.

Kling's 2026 Motion Control workflow explicitly takes a **reference action video plus a character image**, with optional facial-element binding for identity consistency. Kling describes the reference performance as the motion source. citeturn18search0turn18search9

Runway's current Act-Two workflow similarly transfers performance from a driving video to a character representation, supporting facial expression and, in appropriate workflows, gestures/body performance. citeturn2search1

The best conceptual assignment is:

```yaml
reference_video:
  owns:
    - performance_timing
    - pose_sequence
    - gesture_rhythm
    - body_dynamics

character_reference:
  owns:
    - identity
    - clothing
    - morphology

text:
  owns:
    - environment
    - cinematic_quality
    - force_impression
    - material_secondary_motion
```

### Multimodal role assignment in current systems

This architecture has become increasingly explicit.

MiniMax H3, released July 31, 2026, accepts text, images, videos, and audio in a unified reference-generation workflow; its official API documentation specifically lists **character, motion, camera, style, voice, and editing rhythm** as reference roles. It supports first/last-frame generation and up to nine images, three videos, and three audio clips in reference mode. Hailuo 2.3 and Hailuo 02 are now listed as legacy models, so H3 should be treated as the current MiniMax reference point. citeturn19search0turn19search11turn19search12

MiniMax even exposes an H3 Context-IR system that interprets relationships among multimodal inputs and converts them into a richer structured representation before generation, which is particularly relevant to the structured-control architecture advocated here. citeturn19search6

Seedance has moved similarly. Seedance 2.0 introduced unified image/video/audio/text references; Seedance 2.5, announced July 31, 2026, raises the reference budget to as many as **30 images, 10 video clips, and 10 audio clips**, adds timestamp-level editing, and extends single-pass generation to 30 seconds. citeturn19search1turn19search2

The lesson is not “feed the model more references.” It is:

> **Give each reference a job.**

For example:

```json
{
  "references": [
    {
      "asset": "character_turnaround.png",
      "role": "identity"
    },
    {
      "asset": "walk_reference.mp4",
      "role": "motion_and_timing"
    },
    {
      "asset": "camera_orbit.mp4",
      "role": "camera_only"
    },
    {
      "asset": "coat_material.mp4",
      "role": "fabric_response"
    }
  ],
  "text_owns": [
    "scene semantics",
    "weight impression",
    "contact behavior",
    "cinematic intent"
  ]
}
```

Ambiguous reference ownership is a new form of prompt conflict.

## The art of chaining for fluid long-form motion

**Objective 6.** Long-form continuity is fundamentally a **state-transfer problem**.

A clip boundary does not only contain an image. It contains hidden motion state:

- body position;
- linear velocity;
- angular velocity;
- support foot;
- gait phase;
- joint velocities;
- center-of-mass direction;
- camera pose and velocity;
- cloth/hair oscillation phase;
- object contacts;
- environment deformation;
- audio rhythm.

When the next clip receives only the last RGB frame, much of this state is missing. The generator may therefore “restart” motion.

### Use the richest continuation mechanism available

Sora's extension API is an unusually clear illustration: an extension uses the **full source clip as context**, specifically to preserve motion, camera direction, and scene continuity. Each extension can add additional duration, although the API itself is now approaching its September 24, 2026 discontinuation. citeturn17search1turn16search0

Veo 3.1 gained video extension in Vertex AI, and Seedance 2.5 supports multi-round extension after its 30-second single-pass generation. citeturn15search9turn19search1

Where full-video continuation is available:

> **full source clip > last frame alone**

for preserving momentum.

Where it is not, construct a continuity packet.

### The continuity packet

```yaml
continuation_state:
  clip_boundary: clip_04_to_05

  identity:
    reference: protagonist_master

  pose:
    support_foot: right
    left_leg_phase: early_swing
    torso_orientation_deg: 18
    head_orientation: forward

  motion:
    state: already_moving
    direction: screen_right
    speed: steady_jog
    acceleration: zero_approximately

  center_of_mass:
    direction: forward
    vertical_phase: rising_slightly

  contact:
    right_foot: planted
    left_foot: airborne

  camera:
    type: tracking
    direction: screen_right
    speed_relationship: matched_to_subject
    angular_velocity: near_zero

  secondary:
    ponytail:
      phase: trailing_right
      velocity: returning_toward_center

  environment:
    dust:
      previous_footfall_cloud: dissipating
```

Compile:

> Continue from the existing jog without restarting or re-accelerating. The right foot is already supporting body weight as the clip begins; the left leg is in early swing. Maintain the same forward heading, cadence, stride scale, and camera tracking speed. The ponytail is already trailing and continues its existing return motion rather than beginning a new swing.

Where a model dislikes negative construction, rewrite positively:

> The first frame is already mid-jog at full steady cadence. Motion flows continuously from the previous stride.

### Preserve momentum explicitly

Bad continuation:

> He starts running forward.

Good continuation:

> He is already running at a steady pace as the shot begins and completes the stride that was underway at the preceding cut.

Bad:

> Camera follows him.

Better:

> The lateral tracking camera is already moving at matched speed in the opening frame and maintains that velocity continuously.

### Carry physical phase, not merely visual identity

For gait:

```yaml
carry_over:
  gait_phase: terminal_stance_left
  next_expected_event: left_toe_off
```

For hair:

```yaml
carry_over:
  hair:
    angular_displacement: backward
    phase: overshoot
    next_state: returning
```

For bouncing object:

```yaml
carry_over:
  ball:
    position: airborne
    velocity_direction: downward
    next_event: floor_contact
```

This is particularly important at high-motion cuts. A still frame of a falling ball does not reveal whether the ball is traveling up or down.

### Plan long actions as beats before generating shots

Example: running jump over an obstacle.

```yaml
sequence:
  - beat: approach
    duration_s: 2.0
    state_out:
      speed: high
      support: alternating_run

  - beat: takeoff_preparation
    duration_s: 0.8
    actions:
      - lower_com
      - shorten_penultimate_step
      - plant_takeoff_foot

  - beat: propulsion
    duration_s: 0.4
    actions:
      - leg_extension
      - arm_drive

  - beat: airborne
    duration_s: 1.0
    constraints:
      - ballistic_com_arc
      - no_ground_contact

  - beat: landing
    duration_s: 0.7
    actions:
      - forefoot_contact
      - knee_hip_compression
      - forward_momentum_absorption

  - beat: recovery
    duration_s: 1.1
    actions:
      - two_decelerating_steps
      - upright_settle
```

Generate one or more beats per clip depending on model competence.

### Choose chain boundaries strategically

The easiest boundaries are often moments with a relatively unambiguous state:

- firm foot plant;
- held pose;
- hand securely gripping an object;
- brief apex of motion;
- object momentarily at rest.

But do **not** always stop at rest. If the purpose of the shot is momentum, preserve motion explicitly with full video context, reference performance, or a state manifest.

### Identity state and physics state are different

Identity continuity answers:

> Is this the same person?

Physics continuity answers:

> Is this the same *ongoing event*?

A character reference can solve the first without solving the second.

This is why modern platforms increasingly combine identity elements with temporal controls. Kling 3.0's Elements are designed to preserve character/item/scene traits across camera and scene changes, while its start/end frame and Motion Control systems address other aspects of temporal behavior. citeturn18search1turn18search10

### Practical long-form production workflow

A robust workflow is:

```text
Storyboard
   ↓
Beat decomposition
   ↓
Biomechanics / physics state specification
   ↓
Reference asset assignment
   ↓
Generate simplest motion test
   ↓
Validate contacts + trajectory
   ↓
Add camera
   ↓
Add secondary motion
   ↓
Generate N candidates
   ↓
Select by motion/physics metrics
   ↓
Record terminal state
   ↓
Continue / extend
   ↓
Editorial assembly
```

This staged approach is more reliable than attempting the final fully art-directed shot from the first prompt, and it aligns with official Sora and Runway guidance favoring simple starting prompts followed by iterative refinement. citeturn17search0turn15search2

## Model-specific best practices, experimental methodology, and study roadmap

**Objective 7.** By August 2026, models differ less in whether they accept “good prose” and more in **which stronger control channels they expose**.

### Current model dialects

| System | Current control dialect | Highest-leverage motion practice |
|---|---|---|
| **Sora 2** | Concrete shot prose, action beats/counts, image first-frame reference, extensions | One camera move + one subject action; counted beats; full-clip extension for continuity |
| **Runway Gen-4.5** | Natural-language movement description; I2V motion-centric prompting; timestamps; apps/tools | In I2V, let image own appearance and prompt motion; use timestamps for sequence; Motion Sketch/performance tools when prose is insufficient |
| **Veo 3.1** | Detailed natural language, first/last frames, reference ingredients, extension, native audio | Assign references explicitly; use endpoint frames for transitions; describe camera/action/audio distinctly |
| **Kling VIDEO 3.0 / Omni** | Start/end frames, Elements, multi-shot/custom multi-shot, multimodal refs, Motion Control | Use reference video for performance and Elements for identity; isolate single-shot physics testing from multishot storytelling |
| **Luma Ray family** | Generation plus source-grounded transform workflows; keyframes and adherence controls | In source/video transformation, let source motion own dynamics; use keyframes for exact moments; prompt desired result rather than narrating every intermediate instruction |
| **MiniMax H3** | Unified text/image/video/audio references; first/last; explicit reference roles | Assign motion, camera, style, identity, voice, and rhythm to specific assets |
| **LTX-2.3** | Open node pipeline; first/last; trajectory, pose, depth, Canny IC-LoRAs | Best suited to explicit modular control stacks; route structured YAML fields into actual control nodes |
| **Seedance 2.5** | Long single-pass generation, multimodal references, extensions, timestamp editing | Use longer 30 s shot planning when it avoids unnecessary chains; allocate reference roles instead of relying on prose alone |

#### Sora

OpenAI's official Sora 2 prompting guide says movement is frequently the hardest component and recommends one clear camera move and one clear subject action, expressed in beats or counts. Image references anchor the first frame; extensions use the full preceding video context. These remain excellent general lessons, but the product is being sunset: web/app ended April 26, 2026 and API termination is scheduled for September 24, 2026. citeturn17search0turn17search1turn16search0

**Best reusable Sora lesson:**

> Specify the minimum achievable temporal unit.

Not:

> An elaborate acrobatic chase through the city.

But:

> The runner takes three accelerating steps, plants the right foot, jumps the low barrier, lands on the left foot, then takes two recovery steps.

#### Runway

Runway's newest prompting documentation is optimized for Gen-4.5. In text-to-video, Runway recommends a combination of visual and motion description; in image-to-video, it recommends focusing much more strongly on motion because the input frame already supplies appearance and composition. Timestamp prompting can guide temporal ordering but should not be expected to function as a frame-exact timeline. Runway's Gen-4 guidance also favors positive phrasing and simplicity. citeturn15search0turn15search2turn15search4

**Runway dialect:**

> The subject takes three steady steps forward. Each foot remains firmly planted during weight transfer. Her body decelerates through the final step and settles. The camera performs a gentle lateral track at matched speed.

Avoid feeding an I2V model several paragraphs redescribing what the image already shows.

Current Runway tooling also matters: older advice about Gen-2 Motion Brush or Gen-3 should be treated as legacy; newer workflows include Motion Sketch, keyframe-oriented tools, references, and performance-transfer mechanisms such as Act-Two. citeturn8search0turn2search1turn2search3

#### Veo

Google's production model line is Veo 3.1; the older Veo 3.0 model lifecycle has already moved toward 3.1, and Google's current documentation supports first/last frames, reference workflows, and video extension. Veo also includes prompt rewriting in some product/API contexts, which means the exact text you enter may not always be the literal text ultimately interpreted by the generator. citeturn15search7turn15search9turn15search12turn0search12

This reduces the value of hyper-fragile “magic keyword” prompting.

Prefer semantic clarity:

> Low side-tracking shot. The horse transitions smoothly from walk into trot over three gait cycles. Contact rhythm changes progressively rather than instantly. Hooves load the ground visibly; the torso remains supported and the mane trails with delayed, damped movement.

#### Kling

Kling VIDEO 3.0 supports text-to-video, image-to-video, start/end frames, native audio, multi-shot generation, element references, multiple characters, and 3–15 second generation. Custom Multi-Shot can specify individual shot content and durations. Elements are intended to maintain character/item/scene traits across changing shots and camera positions. citeturn18search1turn18search4

For biomechanics, Kling Motion Control is especially important: the user supplies an action video plus a character image, and facial references can be separately bound for identity. citeturn18search0

Thus:

> **Reference video owns choreography; character asset owns identity; text owns physical interpretation and environment.**

#### Luma

Luma's current workflows make a particularly clear distinction between unconstrained generation and source-grounded transformation. Ray3.2 video-to-video can use many keyframes at chosen positions and exposes separate Motion and Structure adherence controls. In that workflow, the source clip already determines temporal motion, so Luma advises prompting the desired resulting state rather than describing an elaborate temporal story. citeturn9search1turn9search3turn9search5

That implies a very different prompt from T2V:

**Wrong abstraction**

> First she raises the arm, then she rotates, then the camera moves...

**Better V2V abstraction**

> The same body performance and timing are preserved. The subject is now wearing a heavy leather coat; body pose and blocking remain faithful to the source.

#### MiniMax / Hailuo

For new workflows, **MiniMax H3** is the relevant current system, not Hailuo 02/2.3. MiniMax released H3 on July 31, 2026 and lists Hailuo 2.3 and Hailuo 02 under legacy video models. H3 accepts text, image, video, and audio, generates 4–15 second outputs at 768P or 2K, and supports reference generation where assets can represent character, motion, camera, style, voice, or edit rhythm. citeturn19search0turn19search11turn19search12

Older Hailuo camera-tag syntax can still be useful when working deliberately with those historical versions, but it should not be generalized as a universal H3 prompting language.

#### LTX

LTX-2.3 is one of the most interesting systems for researchers because its open tooling exposes the actual modular controls discussed throughout this report. LTX documents Motion-Track-Control using sparse spline trajectories and IC-LoRA controls for pose, depth, and Canny structure, while recommending ComfyUI as an accessible route to the open model's node-level capabilities. citeturn18search2turn18search5turn18search16

LTX's hosted/API product has also moved to 2.3, with previous LTX-2 API variants scheduled for removal on August 15, 2026. citeturn18search11

For a controllability research lab, this makes LTX particularly suitable for a real YAML → node-graph compiler:

```yaml
hybrid_controls:
  pose:
    adapter: IC-LoRA-Pose

  depth:
    adapter: IC-LoRA-Depth

  subject_motion:
    adapter: IC-LoRA-Motion-Track-Control

  appearance:
    adapter: reference_conditioning
```

The YAML fields can map to real inference controls rather than merely being converted into prose.

#### Seedance

Seedance 2.5 is exceptionally relevant to long-form planning because ByteDance says it supports up to **30 seconds in a single pass**, multiple rounds of extension, and up to 30 images, 10 videos, and 10 audio references, along with timestamp-level editing. It was announced July 31, 2026. citeturn19search1turn19search4

This changes the chaining tradeoff: a sequence that previously required three 10-second generations may now be representable as one 30-second planned generation. That does **not** guarantee better biomechanics over the longer duration, but it removes two artificial state-reset boundaries.

### Highest-leverage prompting interventions across models

Across the official guidance and current research, the interventions with the strongest practical rationale are:

**Explicit contact mechanics.**  
Replace “walk naturally” with planted-foot, load-transfer, heel-rise, push-off, and toe-release language.

**Beat-based timing.**  
Turn complex actions into a few observable sequential events; both Sora and Runway's guidance supports this pattern. citeturn17search0turn15search4

**One dominant action.**  
Do not make locomotion, waving, camera orbit, transformation, falling objects, hair, cloth, rain, and crowd movement all equal-priority instructions.

**Reference-driven choreography.**  
When timing matters more than novelty, use a motion reference, pose sequence, or trajectory. Kling Motion Control, Runway performance capture, LTX trajectory/pose controls, and current multimodal Seedance/MiniMax workflows all push in this direction. citeturn18search0turn2search1turn18search2turn19search0turn19search1

**First/last frames for boundary states.**  
Use them to determine endpoints; let the prose define the mechanically plausible transition. Veo, Kling, LTX, and MiniMax all expose variants of this paradigm. citeturn15search1turn18search1turn18search11turn19search0

**Subtractive debugging.**  
Freeze camera, simplify background, isolate the subject action, prove the mechanics, then add layers.

**Best-of-N selection.**  
Generating several candidates and selecting by physics-aware criteria is not merely an artist's workaround; WMReward provides direct research evidence that inference-time candidate search/steering can substantially improve physical plausibility. citeturn20search1turn20search4

### Research directions worth studying

**Motion Prompting** is foundational for understanding sparse/dense trajectory conditioning, motion prompt expansion, camera/object motion, and motion transfer. citeturn20search0turn20search3

**Any Trajectory Instruction** is useful for thinking about one unified trajectory language spanning camera motion, object translation, and localized deformation. citeturn20search6

**Force Prompting** is particularly relevant to physics-aware interfaces because it explores direct force signals instead of merely text descriptions of resulting motion. citeturn20search9

**WMReward** demonstrates that physics can be improved at inference time by steering/selecting candidates with a learned world-model reward. citeturn20search1

**HumanScore** is important because it evaluates human movement through interpretable dimensions including kinematic plausibility, temporal stability, and biomechanical consistency. citeturn20search2

The current research frontier therefore suggests a future architecture closer to:

```text
natural-language intent
        +
structured physical scene specification
        +
trajectory / pose / force controls
        +
reference assets
        ↓
video generator
        ↓
physics + biomechanics evaluator
        ↓
candidate selection / corrective regeneration
```

rather than a single increasingly elaborate English prompt.

### Research experiment template

Use controlled experiments rather than judging a prompt after one generation.

```yaml
experiment:
  id: footplant_007
  date: "2026-08-08"

  hypothesis:
    statement: >
      Explicit stance-foot anchoring and weight-transfer language
      will reduce visible foot sliding relative to a generic
      "walk naturally" prompt.

  model:
    family: runway
    version: gen-4.5
    mode: image_to_video

  fixed_conditions:
    input_image: walk_start_v3.png
    duration_s: 8
    aspect_ratio: "16:9"
    camera: static
    environment: simple_flat_floor
    character_reference: same
    generation_settings: identical_when_exposed

  independent_variable:
    name: contact_prompt
    conditions:

      baseline:
        prompt: >
          The subject walks naturally from left to right at a steady pace.

      treatment_a:
        prompt: >
          The subject walks left to right at a steady pace.
          Each stance foot stays firmly fixed relative to the floor
          while body weight passes over it. The heel rises only after
          the pelvis moves forward over the planted foot; the forefoot
          pushes and the toes then leave the ground.

      treatment_b:
        prompt: >
          Same as treatment_a, with a pelvis motion track and ankle
          pose control.

  sample_plan:
    generations_per_condition: 12
    reject_for_safety_filter: record_not_replace_silently
    cherry_picking: prohibited

  metrics:
    foot_slip:
      method: >
        Track heel/toe landmarks during predicted stance and measure
        their image-plane velocity relative to local ground.
      normalize_by: body_height_pixels
      lower_is_better: true

    limb_length_variance:
      method: >
        Estimate pose; measure normalized femur and tibia length
        variation over time.
      lower_is_better: true

    temporal_jerk:
      method: >
        Smooth tracked pelvis position and estimate change in
        acceleration over time.
      lower_is_better: true

    human_contact_score:
      scale: [1, 5]
      blind_review: true

    human_weight_score:
      scale: [1, 5]
      blind_review: true

    human_fluidity_score:
      scale: [1, 5]
      blind_review: true

  secondary_motion_metric:
    enabled: false

  decision_rule:
    promote_module_when:
      - median_foot_slip_improves
      - human_contact_score_improves
      - no_material_identity_regression

  outputs:
    save:
      - prompts
      - model_version
      - generation_ids
      - raw_videos
      - tracking_data
      - metric_results
      - reviewer_scores

  result:
    status: pending
    winning_condition: null

  module_update:
    promote_to_library: false
    new_version: null
```

HumanScore's emphasis on kinematic plausibility, temporal stability, and biomechanical consistency provides a good conceptual basis for this style of evaluation. citeturn20search2

### Practical metrics for motion research

For **foot sliding**, track the contacting heel/toe relative to the ground during stance. A physically fixed support foot should have low velocity in the ground frame.

For **trajectory adherence**, calculate normalized distance between requested point track and resulting tracked feature.

For **joint stability**, monitor inferred limb-length variation and anatomically suspicious joint-angle excursions. This is imperfect because pose estimators themselves introduce error, so always combine automated scores with blinded human review.

For **fluidity**, examine velocity continuity and jerk around transitions. Do not penalize legitimate impulses—for example, a collision can create a sharp velocity change.

For **secondary action**, compare the motion signal of the primary driver with hair/cloth/accessory motion. A cross-correlation peak at a small positive delay provides a quantitative proxy for follow-through.

For **weight**, a useful human rubric asks whether acceleration, stance compression, braking distance, contact reaction, and settling are mutually consistent.

For **identity**, evaluate separately from biomechanics. Otherwise a beautiful face can bias reviewers toward calling bad motion “good.”

### A high-value ablation ladder

Do not simultaneously test five prompt ideas.

Use this sequence:

```text
A  generic action
B  + explicit beats
C  + contact mechanics
D  + acceleration/deceleration
E  + center-of-mass language
F  + secondary action
G  + camera movement
H  + trajectory or pose control
I  + reference performance
```

At each stage ask:

> Did the new intervention improve its intended metric without damaging previously solved dimensions?

For example, a pose constraint might reduce foot slip but increase visual stiffness. That is not an unqualified improvement.

### Prioritized study roadmap

**First: master contact and weight before style.**  
Learn stance/swing structure, center-of-mass transfer, anticipation, push-off, landing compression, momentum, friction, deceleration, and settling. Build five canonical modules: walk, run acceleration, stop, jump/landing, push/lift. Human and animal gait mechanics give you the vocabulary for what the generator should visibly do. citeturn6search2turn14search8

**Second: master temporal animation grammar.**  
Build reusable modules for anticipation, slow-in/slow-out, follow-through, overlapping action, arcs, and secondary motion. The goal is to convert “fluid” from an adjective into explicit phase relationships. citeturn7search0

**Third: move spatial control out of prose.**  
Learn point trajectories, pose conditioning, first/last frames, keyframes, and performance references. Motion Prompting, ATI, and LTX's current trajectory controls are especially useful study material. citeturn20search0turn20search6turn18search2

**Fourth: build YAML as an intermediate representation.**  
Do not optimize for pretty YAML. Optimize for fields that can either compile into visible language or map directly onto a control signal.

```text
identity      → reference
position/path → trajectory
pose          → skeleton
timing        → reference/timestamps
weight        → prose + physics evaluator
material      → prose/reference/simulation
camera        → camera control
```

**Fifth: develop per-model compilers.**  
Runway I2V should receive motion-focused prose; Sora-style prompts should be beat-oriented; Luma V2V should emphasize the desired transformed state; LTX fields can map directly to adapters; multimodal MiniMax/Seedance references should receive explicit roles. citeturn15search0turn17search0turn9search5turn18search2turn19search0

**Sixth: learn stateful chaining.**  
Preserve support state, velocity, gait phase, camera velocity, and secondary-motion phase—not merely the final image. Prefer full-video continuation where supported. citeturn17search1turn15search9turn19search1

**Seventh: build an evaluation harness.**  
Measure contact slip, trajectory error, joint stability, center-of-mass smoothness, secondary-action lag, and blinded human perception. Treat attractive single generations as anecdotes, not evidence. HumanScore and physics-alignment research make a strong case for evaluation beyond generic “video quality.” citeturn20search2turn20search1

**Eighth: add physics-aware candidate selection.**  
Once generation is reliable enough, sample multiple candidates and rank them with pose/contact/trajectory metrics or learned world-model rewards. Research such as WMReward indicates that inference-time selection and steering can recover substantially more physically plausible samples from an existing generator. citeturn20search1turn20search4

### Highest-ROI techniques available now

The current highest-return control stack is:

**Use a visual identity anchor rather than repeatedly describing identity.** Reference images, Kling Elements, Veo ingredients, multimodal H3/Seedance references, and analogous mechanisms reduce the burden on text. citeturn17search0turn18search1turn15search1turn19search0

**Use a trajectory, pose sequence, or performance video whenever spatial precision matters.** Text should not carry exact geometry when the platform exposes a stronger signal. citeturn20search0turn18search2turn18search0

**Prompt contacts, not “realism.”**

```text
contact
→ load acceptance
→ center-of-mass transfer
→ propulsion/reaction
→ release
→ follow-through
→ settle
```

**Express motion as beats.** Three or four achievable temporal events outperform an unordered paragraph of simultaneous actions, a pattern directly reflected in Sora and Runway guidance. citeturn17search0turn15search4

**Give one signal ownership of each variable.**

```text
Reference image  = who / what
Trajectory       = where
Pose/video       = articulation + timing
Text             = how it feels
Camera control   = viewpoint movement
First/last frame = boundary states
Evaluator        = whether physics succeeded
```

**Make primary and secondary motion asymmetric in priority.** The body action drives the shot; hair, cloth, tail, jewelry, dust, and facial details respond to it.

**Describe acceleration and deceleration explicitly.** “Starts,” “moves,” and “stops” often produce temporal discontinuities; “shifts weight, accelerates over three steps, maintains speed, shortens two steps, settles” supplies the missing transition states.

**Debug subtractively.** Static camera, one subject, one action, simple ground plane. Only reintroduce camera and secondary dynamics after contact mechanics work. This is consistent with current official guidance emphasizing simplicity and focused iteration. citeturn17search0turn15search2

**Use structured YAML as the source of truth, not as a superstition.** Its main value is modularity, reproducibility, version control, validation, routing, and experiment design; there is currently insufficient evidence to claim that raw YAML itself universally improves proprietary model adherence.

**Carry physics state across clip boundaries.** The last frame alone does not encode velocity, gait phase, or cloth oscillation.

**Generate several candidates and score them.** Modern video generation remains probabilistic, and 2026 physics-alignment research provides evidence that inference-time search and reward-based selection can improve physical plausibility without retraining the base generator. citeturn20search1

The resulting end-to-end philosophy can be summarized as:

```yaml
control_philosophy:
  appearance:
    use: references

  spatial_motion:
    use: trajectories_or_pose

  temporal_performance:
    use: beats_or_reference_video

  physical_quality:
    use:
      - contact_specific_language
      - acceleration_and_deceleration
      - center_of_mass_logic
      - reaction_and_followthrough

  secondary_motion:
    use:
      - parent_child_relationship
      - phase_delay
      - amplitude
      - damping

  long_form:
    use:
      - explicit_state_transfer
      - full_context_extension_when_available

  reliability:
    use:
      - one_variable_at_a_time_testing
      - multiple_samples
      - quantitative_motion_metrics
      - blinded_human_review

  prompt_architecture:
    source_of_truth: versioned_yaml
    execution: model_native_compiler
```

The central technical lesson of the 2026 landscape is therefore not that a sufficiently elaborate prompt can control everything. It is almost the opposite: **high-end controllability comes from decomposing motion into variables and assigning each variable to the strongest available representation**. Text remains indispensable for semantics, force impression, biomechanical intent, timing language, and secondary-motion relationships; trajectories and poses constrain geometry; references constrain identity and performance; boundary frames constrain state; structured schemas keep the system composable; and physics-aware evaluation closes the loop. That layered architecture is far more scalable than searching for a single universal “perfect prompt.” citeturn20search0turn20search1turn18search2turn19search0