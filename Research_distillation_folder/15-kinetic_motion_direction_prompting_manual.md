---
title: "Kinetic Motion Direction Prompting: Agent-Friendly Manual for AI Video Motion, Fight Choreography, and Realistic Movement"
version: "1.0"
created: "2026-07-06"
author_context: "Built as a companion to Ontology-Driven Multimodal Direction Prompting"
primary_concept: "Motion Core"
related_concepts:
  - "Performance Core = how one shot feels and acts"
  - "Control Modules = how a shot is styled for ads, UGC, anime, fights, drama, cinematic"
  - "Director System = how multiple shots connect into one coherent video"
  - "Motion Core = how bodies, objects, cameras, forces, and transitions move through time"
intended_use:
  - "AI video prompting"
  - "image-to-video direction"
  - "text-to-video direction"
  - "first-frame / last-frame workflow design"
  - "reference-to-video continuity"
  - "fight choreography prompting"
  - "UGC product motion prompting"
  - "cinematic camera movement prompting"
  - "RAG ingestion"
  - "agent workflow planning"
document_type: "manual"
rag_profile:
  chunking_strategy: "heading-based atomic chunks"
  recommended_chunk_size_tokens: "300-700"
  parent_summary: true
  extract_entities: true
  extract_relations: true
  extract_prompt_templates: true
  extract_validation_rules: true
  preserve_json_blocks: true
tags:
  - ai-video
  - motion-direction
  - fight-choreography
  - laban
  - biomechanics
  - animation-principles
  - kinetic-prompting
  - image-to-video
  - first-last-frame
  - continuity
  - rag-source
  - agent-schema
source_categories:
  - "Laban Movement Analysis"
  - "animation principles"
  - "cinematography"
  - "fight choreography"
  - "acting and performance"
  - "motion continuity"
  - "AI video workflow control"
---

# Kinetic Motion Direction Prompting

## 0. Executive Summary

**Kinetic Motion Direction Prompting** is the motion equivalent of **FACS + Valence/Arousal performance prompting**.

Where FACS and V/A describe *emotion and facial performance*, Kinetic Motion Direction describes:

- how the body initiates movement,
- how force travels through the body,
- how contact happens,
- how objects move,
- how weight and momentum are perceived,
- how camera motion supports action,
- how one motion beat connects to the next,
- how a shot starts and where it must land,
- how to keep motion consistent across multiple AI-video workflows.

The core formula:

```text
Motion intent
+ movement quality
+ biomechanics
+ motion path
+ timing
+ contact / interaction
+ reaction / recovery
+ camera readability
+ continuity constraints
+ end-frame goal
```

In short:

```text
Performance Core = what the character feels and performs.
Motion Core = how the character, object, camera, and environment move.
Control Modules = how the shot is styled for a use case.
Director System = how all shots connect into one coherent sequence.
```

---

# 1. Why Motion Needs Its Own Prompting System

## 1.1 The Problem

Most AI video prompts describe motion too vaguely:

```text
A cool fight scene.
A realistic punch.
A woman dances.
A person opens a box.
A camera moves cinematically.
```

These prompts leave the model guessing:

- Who initiates movement?
- What changes between the first frame and final frame?
- Where is the center of gravity?
- What body part leads the action?
- What body part follows?
- Is the movement sharp, fluid, heavy, light, sudden, sustained?
- Is there contact?
- What is the reaction?
- Does the camera need to reveal or hide the action?
- What must remain consistent?
- What is the final pose for the next shot?

A model may produce the right *theme*, but the motion will often become:

- floaty,
- rubbery,
- random,
- over-animated,
- unclear,
- disconnected from physics,
- inconsistent across shots,
- visually impressive but directionally useless.

## 1.2 The Solution

Use an atomic motion schema.

Instead of saying:

```text
He throws a punch.
```

Say:

```text
The fighter plants his rear foot, shifts weight forward, rotates hips and shoulders together, drives a compact straight punch along a direct path, makes clear contact at the opponent's jawline, then recoils the hand back to guard while the opponent's head and shoulders snap backward with delayed recoil.
```

The second version gives the model:

- stance,
- weight transfer,
- chain of motion,
- path,
- contact,
- reaction,
- recovery,
- continuity.

That is the essence of **Kinetic Motion Direction Prompting**.

---

# 2. Relationship to the Three Existing Concepts

## 2.1 Performance Core

**Performance Core** answers:

```text
How does one shot feel and act?
```

It includes:

- emotion state,
- valence/arousal,
- FACS,
- anatomy,
- actor behavior,
- breath,
- gaze,
- subtext,
- dialogue,
- lip sync.

Example:

```text
V/A: valence -0.82, arousal 0.79
Emotion family: anger, humiliation, threat response
FACS: AU4 + AU5 + AU7 + AU10 + AU23 + AU25
Anatomy: brows sharply pulled down, eyes wide and tense, upper lip raised into a snarl
Performance: shoulders forward, breath heavy, hands clenched
Subtext: he feels disrespected and is trying to regain dominance
Dialogue: "Oh yeah? You think you're so special?"
```

## 2.2 Motion Core

**Motion Core** answers:

```text
How does movement physically happen through time?
```

It includes:

- movement intent,
- movement quality,
- body mechanics,
- center of mass,
- weight transfer,
- contact,
- force,
- path,
- timing,
- anticipation,
- impact,
- reaction,
- recovery,
- camera readability,
- first-frame and last-frame motion contract.

Example:

```text
Movement Intent: survive pressure and counter without overcommitting
Movement Quality: direct, strong, sudden, bound
Body Mechanics: weight shifts from rear foot to lead foot; hips and shoulders rotate together
Motion Path: compact diagonal slip left, then straight counter forward
Impact: clear contact, slight compression, delayed recoil
Recovery: hands return to guard, stance resets
```

## 2.3 Control Modules

**Control Modules** answer:

```text
What genre or use case is this shot designed for?
```

Motion changes depending on the module:

- UGC: imperfect, handheld, casual, believable hand motion.
- Ads: product motion must demonstrate benefit clearly.
- Fights: setup-contact-reaction-readability.
- Anime: anticipation pose, smear frames, impact frames, sakuga burst.
- Drama: restrained motion, silence, micro-movement.
- Cinematic: lens, blocking, dolly, rhythm, edit design.
- Product demo: object handling, grip, rotation, scale, texture.
- Dance: beat matching, flow, body isolation.
- Sports: athletic mechanics, footwork, acceleration, recovery.
- Vehicles: mass, inertia, suspension, speed, turning radius.

## 2.4 Director System

**Director System** answers:

```text
How do multiple shots connect into one coherent video?
```

Motion Core plugs into the Director System through:

- first-frame lock,
- motion delta,
- end-frame goal,
- transition readiness,
- continuity anchors,
- screen direction,
- shot-to-shot movement logic.

Example:

```text
Previous shot ends with the character looking down at the product.
Next shot begins from that frame, only changing hand motion as the product is lifted into view.
Final frame holds product centered in palm for 0.5 seconds, ready for macro insert shot.
```

---

# 3. The Motion Core Ontology

## 3.1 Top-Level Motion Entities

```yaml
motion_entities:
  - MotionIntent
  - Mover
  - BodyPart
  - Object
  - Force
  - ContactPoint
  - MotionPath
  - TimingBeat
  - MovementQuality
  - KinematicChain
  - EnvironmentConstraint
  - CameraMotion
  - Reaction
  - Recovery
  - ContinuityAnchor
  - EndFrameGoal
```

## 3.2 Motion Relations

```yaml
motion_relations:
  - INITIATES
  - LEADS_WITH
  - FOLLOWS_THROUGH
  - TRANSFERS_WEIGHT_TO
  - CONTACTS
  - REACTS_TO
  - RECOVERS_INTO
  - MOVES_ALONG_PATH
  - ACCELERATES_DURING
  - DECELERATES_DURING
  - HOLDS_POSITION
  - MAINTAINS_SCREEN_DIRECTION
  - PREPARES_NEXT_SHOT
  - CONTRAINS_CHANGE_TO
```

## 3.3 Atomic Motion Unit

An **Atomic Motion Unit** is the smallest useful motion instruction that can be validated.

```json
{
  "motion_unit_id": "MU_001",
  "mover": "hero_fighter",
  "motion_intent": "avoid incoming strike and counter",
  "start_state": "guarded stance, weight slightly on rear foot",
  "lead_action": "head slips outside opponent's punch line",
  "body_mechanics": "rear foot pushes, hips rotate, shoulders follow",
  "motion_path": "diagonal left slip followed by straight forward counter",
  "timing": "anticipation 0.4s, execution 0.5s, reaction 0.6s, recovery 0.5s",
  "contact": "right fist contacts opponent jawline",
  "reaction": "opponent head and shoulders snap backward with delayed recoil",
  "end_state": "hero returns to guard, opponent staggered one step back",
  "continuity_constraints": [
    "same fighters",
    "same wardrobe",
    "same lighting",
    "no screen direction reversal"
  ],
  "negative_constraints": [
    "no teleporting",
    "no floaty impact",
    "no unclear contact"
  ]
}
```

---

# 4. The Four Pillars of Motion Prompting

## 4.1 Pillar 1: Movement Intent

Motion must have a reason.

Bad:

```text
The man runs.
```

Better:

```text
The man runs because he is trying to escape before the door closes.
```

Best:

```text
The man runs with urgent, survival-driven intent; his motion is forward-leaning, breathless, slightly off-balance, and focused entirely on reaching the closing door before it shuts.
```

### Movement Intent Types

```yaml
movement_intent_types:
  - escape
  - pursue
  - attack
  - defend
  - intimidate
  - seduce
  - demonstrate
  - reveal
  - hide
  - reach
  - lift
  - inspect
  - hesitate
  - collapse
  - transform
  - celebrate
  - recover
  - reset
```

### Prompt Field

```text
Movement Intent:
[Who is moving? Why are they moving? What are they trying to accomplish physically?]
```

---

## 4.2 Pillar 2: Movement Quality

Movement quality describes the *texture* of motion.

This is where Laban-style language becomes useful.

### Core Effort Dimensions

```yaml
movement_quality:
  space:
    direct: "focused path, precise target"
    indirect: "wandering, searching, diffuse path"
  weight:
    strong: "heavy, forceful, grounded"
    light: "delicate, soft, floating"
  time:
    sudden: "quick, urgent, explosive"
    sustained: "slow, controlled, extended"
  flow:
    bound: "controlled, restrained, contained"
    free: "loose, released, continuous"
```

### Common Combinations

```yaml
motion_feels:
  explosive_counter:
    space: direct
    weight: strong
    time: sudden
    flow: bound
  graceful_dance:
    space: indirect
    weight: light
    time: sustained
    flow: free
  nervous_fidget:
    space: indirect
    weight: light
    time: sudden
    flow: bound
  exhausted_walk:
    space: direct
    weight: strong
    time: sustained
    flow: bound
  chaotic_panic:
    space: indirect
    weight: light
    time: sudden
    flow: free
  controlled_threat:
    space: direct
    weight: strong
    time: sustained
    flow: bound
```

### Prompt Field

```text
Movement Quality:
Space: direct
Weight: strong
Time: sudden
Flow: bound
Overall feel: compact, sharp, grounded, controlled
```

---

## 4.3 Pillar 3: Biomechanics

Biomechanics makes movement feel physically believable.

Key questions:

- Where is the weight?
- What body part initiates?
- What body part follows?
- What joint chain is used?
- Is the motion grounded or floating?
- Is there balance or imbalance?
- Is there recoil or follow-through?

### Biomechanics Fields

```yaml
biomechanics:
  center_of_mass: "low, high, forward, backward, unstable, grounded"
  base_of_support: "wide stance, narrow stance, one-foot balance, seated"
  weight_transfer: "rear foot to front foot, left to right, heel to toe"
  kinetic_chain: "feet -> hips -> torso -> shoulder -> arm -> hand"
  lead_body_part: "eyes, head, shoulder, hips, hands, feet"
  follow_through: "short, long, restricted, loose"
  recovery: "return to guard, settle stance, regain balance, collapse"
```

### Prompt Field

```text
Body Mechanics:
Low center of gravity, weight shifts from rear foot to front foot, hips initiate the rotation, shoulders follow, arm extends last, then recoils back to guard.
```

---

## 4.4 Pillar 4: Motion Continuity

Motion must connect across time and shots.

The model needs to know:

- start state,
- allowed motion delta,
- final state,
- hold duration,
- next-shot readiness.

### Prompt Field

```text
Motion Continuity:
Start exactly from the input image. Change only the hand and head position. End with the product centered in frame and held still for 0.5 seconds so the frame can be reused as the first frame of the next shot.
```

---

# 5. The Motion Delta System

## 5.1 Definition

**Motion Delta** is the controlled change between the first frame and final frame.

It answers:

```text
What exactly changes during this shot?
```

For image-to-video, this is critical because the input image provides the start frame. The prompt must specify what is allowed to move and what must remain locked.

## 5.2 Motion Delta Schema

```json
{
  "motion_delta": {
    "start_frame_source": "previous_shot_final_frame",
    "locked_elements": [
      "identity",
      "wardrobe",
      "lighting direction",
      "background layout",
      "product shape",
      "camera angle"
    ],
    "allowed_changes": [
      "right hand lifts product",
      "eyes shift from desk to camera",
      "camera slowly pushes in"
    ],
    "forbidden_changes": [
      "face morph",
      "outfit change",
      "room layout change",
      "new object appears",
      "product changes size"
    ],
    "end_frame_goal": {
      "pose": "product centered in palm",
      "emotion": "calm focus",
      "composition": "hand and product fill lower third of frame",
      "hold_duration_seconds": 0.5
    }
  }
}
```

## 5.3 Motion Delta Prompt Template

```text
Use the provided image as the exact first frame.

FIRST FRAME LOCK:
Preserve identity, wardrobe, lighting, camera angle, background layout, object positions, and product shape.

MOTION DELTA:
Only change the following: [specific body/object/camera changes].

MOTION PATH:
Describe the path each moving element follows.

TIMING:
Describe when the motion begins, peaks, slows, and settles.

END FRAME GOAL:
By the final frame, [specific pose/action/composition], held stable for 0.5 seconds.

NEGATIVE CONSTRAINTS:
No identity drift, no extra objects, no camera cut, no product deformation, no style shift.
```

---

# 6. Choreography Grammar

## 6.1 Universal Motion Beat Structure

Most useful motion can be described as:

```text
Set-up -> Anticipation -> Initiation -> Action -> Contact / Peak -> Reaction -> Recovery -> Reset
```

### Beat Definitions

| Beat | Meaning | Prompt Use |
|---|---|---|
| Set-up | The state before motion | Establishes tension, position, intent |
| Anticipation | The pre-motion cue | Makes motion readable |
| Initiation | First actual movement | Defines what body part leads |
| Action | Main movement | Defines path, force, style |
| Contact / Peak | Moment of impact or maximum change | Critical for fights/product demos/transitions |
| Reaction | Consequence of action | Creates cause-effect |
| Recovery | Body/object settles | Prevents floatiness |
| Reset | Final stable state | Prepares next shot |

## 6.2 Beat Prompt Template

```text
Motion Beats:
0.0-0.5s: Set-up — character holds guarded stance, opponent advances.
0.5-0.8s: Anticipation — character shifts weight to rear foot and lowers chin.
0.8-1.3s: Initiation — character slips left, head leaves centerline.
1.3-1.7s: Action — compact counter travels straight forward.
1.7-1.9s: Contact — fist connects clearly with opponent jawline.
1.9-2.5s: Reaction — opponent head and shoulders recoil backward.
2.5-3.2s: Recovery — hero returns hand to guard.
3.2-4.0s: Reset — both fighters hold readable positions for next shot.
```

---

# 7. Contact and Impact System

## 7.1 Why Contact Matters

Bad AI fight/product motion often fails because contact is unclear.

The model shows:

- punch near face but no contact,
- hand passes through object,
- object floats,
- body does not react,
- motion continues without consequence.

You need a **contact contract**.

## 7.2 Contact Contract

```json
{
  "contact_contract": {
    "contact_type": "strike",
    "initiator": "hero_right_fist",
    "receiver": "opponent_jawline",
    "contact_visibility": "clear",
    "contact_duration": "brief",
    "compression": "slight at impact",
    "reaction_delay": "0.1s",
    "reaction_path": "opponent head snaps back, shoulders follow, feet adjust",
    "aftermath": "opponent staggers one step backward"
  }
}
```

## 7.3 Contact Types

```yaml
contact_types:
  strike: "quick impact from limb/object to target"
  grip: "hand closes around object/body part"
  push: "sustained force away from source"
  pull: "sustained force toward source"
  lift: "object/body moves upward against gravity"
  drag: "object moves with friction across surface"
  catch: "moving object is stopped by hand/body"
  release: "object/body is let go"
  collision: "two bodies or objects meet with visible consequence"
  brush: "light contact with small surface reaction"
  press: "sustained compression"
  rotate: "object turns around an axis"
```

## 7.4 Impact Prompt Template

```text
Impact Design:
The contact must be visible and causal. Show the strike landing, slight compression at contact, then delayed recoil through the receiver's head, shoulders, torso, and feet. The attacker recovers back to guard after impact. Avoid passing through, floaty motion, or unclear contact.
```

---

# 8. Camera Readability for Motion

## 8.1 Camera Must Serve the Motion

For motion-heavy scenes, camera is not decoration. It controls whether the audience can understand the action.

Bad:

```text
Intense shaky camera fight.
```

Better:

```text
Medium-wide three-quarter angle, full bodies visible, stable camera during the exchange, slight handheld tension only after the impact.
```

## 8.2 Readability Rules

```yaml
motion_readability_rules:
  - Keep full body visible for complex movement.
  - Use close-ups for emotional reaction, not complex choreography.
  - Avoid cutting during the main contact moment.
  - Preserve screen direction.
  - Keep spatial geography readable.
  - Use camera movement to reveal, not obscure.
  - Use silhouette and pose clarity for anime/action.
  - Use inserts for product interaction and hand motion.
```

## 8.3 Camera Motion Types

```yaml
camera_motion_types:
  locked_off: "static camera; best for clear movement validation"
  handheld_subtle: "human realism; good for UGC and tension"
  push_in: "increases emotional pressure"
  pull_back: "reveals context or isolation"
  pan: "follows horizontal motion"
  tilt: "follows vertical motion"
  tracking: "moves with subject through space"
  orbit: "stylized reveal; risky for continuity"
  whip_pan: "fast transition; risky for AI consistency"
  dutch_angle: "instability; use sparingly"
  macro_follow: "tracks small object/hand movement"
```

## 8.4 Motion-Camera Contract

```json
{
  "camera_motion_contract": {
    "shot_size": "medium-wide",
    "angle": "three-quarter side angle",
    "subject_visibility": "full bodies visible",
    "camera_motion": "slight lateral tracking",
    "stability": "stable during contact, subtle handheld after impact",
    "cutting": "no cuts during the main exchange",
    "screen_direction": "hero moves left-to-right throughout"
  }
}
```

---

# 9. Motion Core for Fight Scenes

## 9.1 Fight Prompting Goal

A good AI fight scene needs:

- combat intent,
- tactical objective,
- distance,
- stance,
- movement quality,
- body mechanics,
- contact,
- reaction,
- recovery,
- camera readability,
- continuity.

## 9.2 Fight Scene Schema

```json
{
  "fight_motion_core": {
    "combat_intent": "survive and counter",
    "power_dynamic": "smaller fighter under pressure",
    "range": "close range",
    "stance": "guarded, low center of gravity",
    "movement_quality": {
      "space": "direct",
      "weight": "strong",
      "time": "sudden",
      "flow": "bound"
    },
    "choreography_beats": [
      "opponent pressures forward",
      "hero retreats half step",
      "hero slips outside punch line",
      "hero counters compactly",
      "opponent recoils",
      "hero resets"
    ],
    "impact_design": {
      "setup": "opponent overcommits",
      "contact": "counter lands clearly",
      "reaction": "opponent recoils and staggers",
      "recovery": "hero returns to guard"
    },
    "camera": {
      "shot_size": "medium-wide",
      "readability": "full bodies visible",
      "cuts": "none during exchange"
    }
  }
}
```

## 9.3 Realistic Fight Prompt

```text
Scene Function:
A grounded realistic fight exchange where the smaller fighter survives pressure through timing and control.

Combat Intent:
The opponent tries to intimidate and overwhelm. The hero tries to stay calm, create a narrow opening, and counter without overcommitting.

Movement Quality:
Space: direct
Weight: strong
Time: sudden
Flow: bound
Motion feels compact, sharp, grounded, and controlled.

Body Mechanics:
Hero keeps low center of gravity, chin tucked, shoulders tense, hands near guard.
Weight shifts backward during pressure, then forward during counter.
Hips and shoulders rotate together.
Head moves slightly off centerline.
After contact, the striking hand recoils back to guard.

Choreography Beats:
0.0-0.8s: Opponent steps forward aggressively, crowding space.
0.8-1.3s: Hero retreats half step and lowers chin.
1.3-1.7s: Opponent commits forward.
1.7-2.1s: Hero slips outside the attack line.
2.1-2.4s: Compact counter lands with clear contact.
2.4-3.2s: Opponent torso snaps back with delayed recoil and foot adjustment.
3.2-4.0s: Hero resets stance, breathing hard, ready for the next move.

Camera:
Medium-wide three-quarter angle with full bodies visible.
Stable enough to read cause and effect.
No random cuts during the exchange.
Slight handheld tension only after the impact.

Avoid:
Floaty hits, teleporting, rubber limbs, excessive spinning, unclear contact, shaky camera hiding action, broken anatomy, inconsistent screen direction.
```

## 9.4 Elite Choreography Additions

For more advanced fight scenes, add:

```yaml
elite_fight_controls:
  tactical_problem: "What is each fighter trying to solve?"
  distance_management: "closing, retreating, circling, trapped, cornered"
  rhythm_change: "slow pressure -> sudden burst -> pause"
  feint: "false initiation that forces reaction"
  counter_timing: "attack during opponent's recovery"
  line_of_attack: "straight, diagonal, circular, rising, descending"
  defensive_action: "slip, parry, block, retreat, duck, pivot"
  aftermath: "fatigue, pain, breath, reset, fear, anger"
```

Example:

```text
Tactical Problem:
The hero cannot trade power directly. He must survive the opponent's forward pressure, draw an overcommitment, slip outside the line of attack, and counter during the opponent's recovery window.
```

---

# 10. Motion Core for Anime and Stylized Action

## 10.1 Anime Motion Is Not Just Realistic Motion

Anime action often uses:

- extreme anticipation poses,
- held frames,
- speed lines,
- smear frames,
- impact frames,
- exaggerated silhouette,
- limited animation followed by sakuga burst,
- camera shock,
- dramatic freeze after impact.

## 10.2 Anime Motion Schema

```json
{
  "anime_motion_layer": {
    "style_epoch": "late-90s OVA",
    "motion_style": "limited animation into sudden sakuga burst",
    "anticipation": "strong held pose before attack",
    "smear_frames": "visible arm smear during strike",
    "impact_frame": "one-frame white flash and black speed-line burst",
    "pose_design": "strong silhouette, readable line of action",
    "camera": "dynamic low angle, brief push-in before impact",
    "hold_after_impact": "0.3s dramatic freeze"
  }
}
```

## 10.3 Anime Fight Prompt

```text
Anime Motion Layer:
Late-90s OVA action style with sharp ink lines and dramatic cel shading.
The motion begins with a held anticipation pose, then erupts into a sudden sakuga burst.
Use a strong silhouette, exaggerated line of action, speed lines during the lunge, and a one-frame impact flash at contact.
After impact, hold the opponent's recoil pose briefly for dramatic readability.

Motion Quality:
Space: direct
Weight: strong
Time: sudden
Flow: free during burst, bound during reset

Avoid:
Generic 3D anime look, mushy motion, unclear contact, random camera spin, inconsistent face design.
```

---

# 11. Motion Core for UGC and Product Ads

## 11.1 UGC Motion Goal

UGC motion must feel:

- casual,
- imperfect,
- human,
- believable,
- handheld,
- not over-produced.

The model should not make motion too clean.

## 11.2 UGC Motion Schema

```json
{
  "ugc_motion_core": {
    "movement_intent": "demonstrate product naturally while speaking",
    "hand_motion": "small imperfect adjustments, realistic grip changes",
    "camera_motion": "subtle handheld sway",
    "body_motion": "natural posture shifts",
    "timing": "slight pauses, not perfectly choreographed",
    "product_continuity": "product shape, scale, and color must remain locked",
    "avoid": [
      "studio-perfect motion",
      "robotic hand movement",
      "product morphing",
      "overly polished influencer performance"
    ]
  }
}
```

## 11.3 Product Demo Motion Fields

```yaml
product_demo_motion:
  grip: "pinch, palm hold, two-hand hold, fingertip rotation"
  reveal: "lift into frame, slide across desk, open box, rotate toward camera"
  proof_action: "press button, pour, squeeze, wipe, compare, unfold, plug in"
  camera: "macro insert, over-the-shoulder, handheld close-up"
  object_physics: "rigid, flexible, soft, liquid, cloth, reflective"
  final_display: "hold product still and centered for recognition"
```

## 11.4 Product Demo Prompt

```text
Product Motion:
The creator lifts the product from the desk into frame with a casual one-hand grip.
The hand makes small natural adjustments as the product rotates 30 degrees toward the camera.
The product stays the same size, shape, color, and texture.
By the final frame, the product is held still in the center of the frame for clear recognition.

Camera:
Handheld phone camera, slight natural sway, close-up framing, realistic room lighting.

Avoid:
Product morphing, floating object, impossible grip, extra fingers, sudden cut, overly polished commercial movement.
```

---

# 12. Motion Core for Dance, Music, and Performance Videos

## 12.1 Dance Motion Goal

Dance requires:

- rhythm,
- body isolation,
- flow,
- timing,
- weight shifts,
- pose clarity,
- beat alignment.

## 12.2 Dance Motion Schema

```json
{
  "dance_motion_core": {
    "music_feel": "syncopated, relaxed, confident",
    "movement_quality": {
      "space": "indirect",
      "weight": "light",
      "time": "sustained with sudden accents",
      "flow": "free"
    },
    "body_isolation": [
      "shoulders",
      "hips",
      "hands"
    ],
    "beat_map": [
      "step on beat 1",
      "shoulder roll on beat 2",
      "hip shift on beat 3",
      "hand accent on beat 4"
    ],
    "camera": "medium shot with full upper body and hips visible",
    "avoid": [
      "off-beat movement",
      "rubber limbs",
      "random foot sliding",
      "identity drift"
    ]
  }
}
```

## 12.3 Dance Prompt

```text
Dance Motion:
Relaxed confident groove, upper body and hips visible.
Movement quality is light, free, and rhythmic, with sudden accents on the beat.
Shoulders roll first, hips follow, hands accent the rhythm.
Footwork is small and grounded, no sliding.
Camera stays medium-wide enough to read the body rhythm.
```

---

# 13. Motion Core for Drama and Emotional Body Language

## 13.1 Drama Motion Goal

Drama often depends on restraint.

Motion should be:

- small,
- specific,
- emotionally motivated,
- timed with silence,
- tied to subtext.

## 13.2 Drama Motion Schema

```json
{
  "drama_motion_core": {
    "subtext": "he wants an apology but refuses to ask",
    "movement_intent": "suppress emotion while staying composed",
    "motion_scale": "micro-movement",
    "body_cues": [
      "jaw tightens",
      "shoulders slowly lower",
      "hand loosens from fist",
      "eyes break contact briefly"
    ],
    "timing": "slow, sustained, restrained",
    "camera": "slow push-in, no cuts during emotional turn",
    "avoid": [
      "melodramatic gestures",
      "random pacing",
      "overacting"
    ]
  }
}
```

## 13.3 Drama Prompt

```text
Motion:
Very restrained. He does not explode.
His jaw tightens first, then his breath catches, then his shoulders slowly lower.
His hand opens from a fist only after the silence.
Eye contact breaks for half a second, then returns.
The movement should feel suppressed, not theatrical.
```

---

# 14. Motion Core for Cinematic Camera Movement

## 14.1 Camera Motion Is Also Motion

Motion Core applies to the camera too.

Camera motion needs:

- motivation,
- speed,
- path,
- stabilization,
- start and end composition,
- relationship to subject movement.

## 14.2 Camera Motion Schema

```json
{
  "camera_motion_core": {
    "camera_intent": "increase pressure as character realizes the truth",
    "start_composition": "medium close-up, character left of frame",
    "movement": "slow dolly push-in",
    "speed": "sustained, barely noticeable",
    "end_composition": "tight close-up, eyes centered",
    "relationship_to_subject": "camera moves only as the character stops moving",
    "avoid": [
      "random zoom",
      "unmotivated orbit",
      "sudden cut",
      "shaky camera"
    ]
  }
}
```

## 14.3 Camera Prompt

```text
Camera Motion:
Begin in a medium close-up with the character slightly left of frame.
As the realization lands, the camera performs a slow sustained push-in.
The subject stays physically still while the camera closes distance.
End in a tight close-up on the eyes and hold for 0.5 seconds.
No random zooms, cuts, or orbiting.
```

---

# 15. Motion Core for Vehicles, Machines, and Objects

## 15.1 Object and Vehicle Motion Goal

Objects and vehicles need physics.

You must define:

- mass,
- inertia,
- acceleration,
- deceleration,
- friction,
- suspension,
- contact with environment,
- object rigidity or flexibility.

## 15.2 Vehicle Motion Schema

```json
{
  "vehicle_motion_core": {
    "vehicle_type": "heavy armored truck",
    "mass_feel": "very heavy",
    "acceleration": "slow and forceful",
    "turning": "wide turn radius",
    "suspension": "body rolls slightly during turn",
    "surface_interaction": "tires compress gravel and kick dust",
    "camera": "low tracking shot",
    "avoid": [
      "floaty vehicle",
      "instant acceleration",
      "unrealistic sharp turn",
      "wheels not matching motion"
    ]
  }
}
```

## 15.3 Object Motion Schema

```json
{
  "object_motion_core": {
    "object": "small glossy product",
    "material": "smooth rigid plastic",
    "interaction": "hand rotates object slowly",
    "motion_path": "30-degree clockwise rotation toward camera",
    "surface_contact": "rests in palm, no floating",
    "lighting_interaction": "highlight moves across glossy surface as it turns",
    "avoid": [
      "object morphing",
      "scale change",
      "floating",
      "texture shift"
    ]
  }
}
```

---

# 16. Motion Core for Animals and Creatures

## 16.1 Animal Motion Goal

Animal motion must respect:

- gait,
- body structure,
- balance,
- species-specific movement,
- tail/ear/eye behavior,
- foot contact.

## 16.2 Animal Motion Schema

```json
{
  "animal_motion_core": {
    "species": "domestic cat",
    "gait": "slow cautious walk",
    "center_of_mass": "low and fluid",
    "lead_action": "head and ears orient first",
    "body_follow": "shoulders and hips follow in smooth sequence",
    "tail": "slow balancing movement",
    "foot_contact": "quiet precise steps",
    "avoid": [
      "human-like motion",
      "floating paws",
      "rubber spine",
      "incorrect gait"
    ]
  }
}
```

---

# 17. Motion Core for Transformations and VFX

## 17.1 Transformation Motion Goal

Transformation shots need:

- source state,
- target state,
- transformation mechanism,
- order of change,
- material behavior,
- camera relationship,
- continuity lock.

## 17.2 Transformation Schema

```json
{
  "transformation_motion_core": {
    "source_state": "ordinary sneaker",
    "target_state": "glowing futuristic sneaker",
    "transformation_mechanism": "light travels through seams first",
    "change_order": [
      "sole glows",
      "fabric texture tightens",
      "logo illuminates",
      "color shifts subtly"
    ],
    "motion_quality": "sustained and controlled",
    "locked_elements": [
      "same object silhouette",
      "same camera angle",
      "same table position"
    ],
    "avoid": [
      "object changes shape completely",
      "random extra parts",
      "camera cut",
      "scale change"
    ]
  }
}
```

---

# 18. Workflow-Specific Motion Controls

## 18.1 Text-to-Video

Text-to-video has the least visual anchoring.

Therefore, include:

- character description,
- motion intent,
- movement quality,
- body mechanics,
- environment,
- camera,
- continuity constraints,
- negative constraints.

### T2V Motion Template

```text
Workflow: Text-to-Video

Scene Function:
[What the shot must accomplish.]

Subject:
[Identity, body type, wardrobe, key visual anchors.]

Motion Intent:
[Why movement happens.]

Movement Quality:
[Space / Weight / Time / Flow.]

Body Mechanics:
[Weight, posture, lead body part, follow-through.]

Motion Beats:
[Timed sequence.]

Camera:
[Shot size, angle, motion, readability.]

End Frame Goal:
[Where the shot must land.]

Avoid:
[Motion failures to prevent.]
```

## 18.2 Image-to-Video

Image-to-video needs:

- first-frame lock,
- allowed motion delta,
- forbidden changes,
- end-frame goal.

### I2V Motion Template

```text
Workflow: Image-to-Video

Use the provided image as the exact first frame.

First Frame Lock:
Preserve identity, wardrobe, lighting, background, camera angle, product/object shape, and spatial layout.

Allowed Motion Delta:
Only [specific body/object/camera movements] may change.

Motion Path:
[Path of each moving element.]

Timing:
[Start, peak, settle.]

End Frame Goal:
[Exact final pose/composition/action.]

Continuity:
Final frame must be reusable as the first frame of the next shot.

Avoid:
No identity drift, no object morph, no new objects, no camera cut, no style shift.
```

## 18.3 Reference-to-Video

Reference-to-video needs:

- reference priority,
- which traits are locked,
- which traits can adapt,
- motion translation.

### Reference Motion Template

```text
Workflow: Reference-to-Video

Reference Priority:
Use the reference for [identity/product/style/pose/location].

Locked Traits:
[Face, outfit, product shape, color palette, style, room layout.]

Adaptable Traits:
[Expression, hand position, body pose, camera distance.]

Motion Translation:
Animate the locked subject performing [specific motion] while preserving reference identity and proportions.

Avoid:
Do not reinterpret the reference into a new character/object/style.
```

## 18.4 First/Last Frame Workflow

First/last-frame workflows are ideal for controlled transitions.

### First/Last Frame Contract

```json
{
  "first_last_frame_contract": {
    "first_frame": {
      "source": "provided_start_image",
      "must_match": true
    },
    "last_frame": {
      "target": "provided_end_image",
      "must_land_on": true
    },
    "allowed_transition": "smooth body turn and camera push-in",
    "forbidden_transition": "random cut or identity morph",
    "motion_path": "head turns first, shoulders follow, camera pushes in last",
    "timing": "start slow, accelerate in middle, settle before final frame"
  }
}
```

### Prompt Template

```text
Workflow: First/Last Frame Video

Start exactly on the provided first frame.
End exactly on the provided last frame.

Transition Motion:
[Describe how subject/object/camera moves between the two frames.]

Motion Order:
[What moves first, second, third.]

Timing:
[Slow-in, acceleration, settle.]

Continuity:
No identity drift, no outfit change, no background change, no style shift.

End:
Final frame must match the provided target frame cleanly and hold stable.
```

## 18.5 Pose/Skeleton-Controlled Workflow

Pose or skeleton control is useful for:

- dance,
- fights,
- sports,
- full-body acting,
- repeatable character motion.

### Pose-Control Template

```text
Workflow: Pose-Controlled Video

Use pose sequence as primary body-motion authority.
Preserve character identity and wardrobe from reference image.
Motion should follow the skeleton precisely while adding natural weight, balance, follow-through, and facial performance.
Hands, feet, and head orientation must remain anatomically plausible.
Avoid broken joints, foot sliding, rubber limbs, or motion that ignores the pose guide.
```

## 18.6 Depth / Canny / Edge-Controlled Workflow

Useful for:

- preserving composition,
- product shape,
- architecture,
- vehicle structure,
- scene layout.

### Structure-Control Template

```text
Workflow: Structure-Controlled Video

Use depth/edge map as structure authority.
Preserve silhouette, spatial layout, object boundaries, and camera geometry.
Only animate the specified motion delta.
Avoid changing object proportions, background layout, or camera perspective.
```

## 18.7 Video-to-Video / Enhancement Workflow

Useful for:

- improving realism,
- upscaling,
- style transfer,
- motion cleanup,
- texture improvement.

### V2V Motion Preservation Template

```text
Workflow: Video-to-Video Enhancement

Preserve original motion timing, choreography, camera path, identity, object positions, and scene layout.
Improve only texture, lighting realism, detail, sharpness, and temporal consistency.
Do not change choreography, add new motion, alter body mechanics, or reinterpret the scene.
```

---

# 19. Motion by Video Type

## 19.1 Ads

Motion priority:

```yaml
ads_motion_priority:
  - stop-scroll hook
  - visible problem
  - product reveal
  - proof action
  - before/after motion
  - final display
```

Prompt field:

```text
Motion must make the benefit understandable without explanation.
```

## 19.2 UGC

Motion priority:

```yaml
ugc_motion_priority:
  - believable hand motion
  - casual camera sway
  - natural posture shifts
  - imperfect timing
  - product continuity
```

Prompt field:

```text
Motion should feel like a real person filming casually, not a commercial actor.
```

## 19.3 Fights

Motion priority:

```yaml
fight_motion_priority:
  - tactical intent
  - distance
  - stance
  - setup
  - contact
  - reaction
  - recovery
  - camera readability
```

Prompt field:

```text
Every strike must have setup, contact, reaction, and recovery.
```

## 19.4 Anime

Motion priority:

```yaml
anime_motion_priority:
  - silhouette
  - anticipation pose
  - smear
  - impact frame
  - speed lines
  - held reaction
```

Prompt field:

```text
Use limited animation before the burst and a readable impact frame at contact.
```

## 19.5 Drama

Motion priority:

```yaml
drama_motion_priority:
  - restraint
  - micro-movement
  - breath
  - gaze
  - silence
  - delayed reaction
```

Prompt field:

```text
The emotional change should appear through small controlled motion, not big gestures.
```

## 19.6 Cinematic

Motion priority:

```yaml
cinematic_motion_priority:
  - motivated camera
  - blocking
  - screen direction
  - lens feel
  - composition shift
  - edit rhythm
```

Prompt field:

```text
Camera movement must reveal emotional or story information.
```

## 19.7 Product Demo

Motion priority:

```yaml
product_demo_priority:
  - clear grip
  - object scale
  - motion path
  - proof interaction
  - final hold
```

Prompt field:

```text
Object motion must clearly demonstrate the product benefit and end with product recognition.
```

## 19.8 Sports

Motion priority:

```yaml
sports_motion_priority:
  - stance
  - acceleration
  - footwork
  - balance
  - follow-through
  - fatigue
```

Prompt field:

```text
Athletic movement must show weight transfer, foot contact, and recovery.
```

## 19.9 Vehicles

Motion priority:

```yaml
vehicle_motion_priority:
  - mass
  - acceleration
  - turn radius
  - suspension
  - tire/surface contact
  - inertia
```

Prompt field:

```text
Vehicle movement must show mass, traction, suspension response, and realistic acceleration.
```

## 19.10 Animals

Motion priority:

```yaml
animal_motion_priority:
  - species gait
  - spine behavior
  - paw/hoof contact
  - tail balance
  - head/ear orientation
```

Prompt field:

```text
Animal movement must follow species-specific gait and balance.
```

## 19.11 VFX / Transformation

Motion priority:

```yaml
vfx_motion_priority:
  - source state
  - target state
  - transformation order
  - material behavior
  - silhouette lock
```

Prompt field:

```text
The transformation must preserve silhouette and follow a clear order of change.
```

---

# 20. Motion Validation Checklist

## 20.1 Universal Motion Validation

Ask after each generation:

```yaml
motion_validation:
  - Did the motion start from the intended first state?
  - Did only the allowed elements move?
  - Did the motion follow the stated path?
  - Was weight/momentum believable?
  - Was contact clear, if contact was required?
  - Did the reaction match the action?
  - Did the subject recover or settle naturally?
  - Did the camera help readability?
  - Did the final frame match the end-frame goal?
  - Can the final frame be reused as the next first frame?
```

## 20.2 Fight Validation

```yaml
fight_validation:
  - Was distance readable?
  - Did each fighter have a clear objective?
  - Was there setup before impact?
  - Was contact visible?
  - Did the receiver react causally?
  - Did the attacker recover?
  - Did screen direction remain consistent?
  - Did the camera avoid hiding the action?
```

## 20.3 Product Motion Validation

```yaml
product_validation:
  - Did the product keep its shape?
  - Did the hand grip look physically possible?
  - Did the proof action happen clearly?
  - Did the object avoid floating?
  - Did the final frame display the product clearly?
```

## 20.4 Repair Prompt Template

```text
Repair the previous generation by preserving the same character, scene, camera angle, and lighting.

Fix only the motion:
- Start from the same first frame.
- Keep [locked elements] unchanged.
- Make [specific action] follow this path: [path].
- Show clear [contact/reaction/recovery].
- End with [end-frame goal].
Avoid the previous errors: [list errors].
```

---

# 21. Agent-Friendly Motion Routing

## 21.1 Routing Decision Tree

```yaml
motion_router:
  if_input_is_text_only:
    route: "text_to_video_motion_prompt"
    required_fields:
      - subject
      - motion_intent
      - movement_quality
      - body_mechanics
      - camera
      - end_frame_goal

  if_input_is_image:
    route: "image_to_video_motion_delta"
    required_fields:
      - first_frame_lock
      - allowed_motion_delta
      - forbidden_changes
      - end_frame_goal

  if_input_has_start_and_end_frames:
    route: "first_last_frame_contract"
    required_fields:
      - transition_motion
      - motion_order
      - timing
      - continuity_locks

  if_input_is_reference_identity_or_product:
    route: "reference_to_video_motion_translation"
    required_fields:
      - locked_reference_traits
      - adaptable_traits
      - motion_translation

  if_input_is_existing_video:
    route: "video_to_video_motion_preservation"
    required_fields:
      - preserve_motion
      - enhance_only
      - forbidden_changes
```

## 21.2 Agent Extraction Targets

For RAG extraction, identify these fields:

```yaml
extract_motion_fields:
  - scene_function
  - mover
  - object
  - motion_intent
  - movement_quality
  - body_mechanics
  - motion_path
  - timing_beats
  - contact_contract
  - impact_design
  - camera_motion
  - continuity_anchors
  - end_frame_goal
  - negative_constraints
  - workflow_type
  - validation_rules
```

## 21.3 Agent Output Contract

An agent should not output a motion prompt until it can answer:

```yaml
agent_motion_requirements:
  - What is moving?
  - Why is it moving?
  - What starts the motion?
  - What path does it follow?
  - How fast is it?
  - What force/weight does it imply?
  - What contact occurs?
  - What reaction occurs?
  - What must not change?
  - Where must the shot end?
```

---

# 22. Master Motion Prompt Template

```text
MOTION CORE

Scene Function:
[What this motion must accomplish for the viewer/story/ad.]

Workflow Type:
[text-to-video / image-to-video / reference-to-video / first-last-frame / video-to-video / pose-control]

Mover:
[Character/object/animal/vehicle/camera.]

Motion Intent:
[Why the mover is moving.]

Start State:
[Exact starting pose, object position, camera composition.]

Movement Quality:
Space: [direct/indirect]
Weight: [strong/light]
Time: [sudden/sustained]
Flow: [bound/free]
Overall feel: [compact, fluid, nervous, explosive, restrained, etc.]

Body/Object Mechanics:
[Center of mass, weight transfer, lead body part, joint chain, grip, contact, mass, material behavior.]

Motion Path:
[Direction and trajectory.]

Timing Beats:
[Set-up -> anticipation -> action -> contact/peak -> reaction -> recovery -> reset.]

Contact / Interaction:
[If applicable: what touches what, when, with what consequence.]

Camera Motion:
[Shot size, angle, movement, stability, screen direction.]

End Frame Goal:
[Specific final pose/composition/action and hold duration.]

Continuity Locks:
[Identity, wardrobe, product, lighting, background, camera angle, screen direction.]

Negative Constraints:
[What to avoid.]
```

---

# 23. Master JSON Schema

```json
{
  "motion_core": {
    "scene_function": "",
    "workflow_type": "",
    "mover": {
      "type": "",
      "identity": "",
      "locked_traits": []
    },
    "motion_intent": "",
    "start_state": {
      "pose": "",
      "position": "",
      "composition": ""
    },
    "movement_quality": {
      "space": "",
      "weight": "",
      "time": "",
      "flow": "",
      "overall_feel": ""
    },
    "mechanics": {
      "center_of_mass": "",
      "base_of_support": "",
      "weight_transfer": "",
      "lead_body_part": "",
      "kinetic_chain": "",
      "follow_through": "",
      "recovery": ""
    },
    "motion_path": {
      "direction": "",
      "trajectory": "",
      "range_of_motion": ""
    },
    "timing_beats": [
      {
        "time_range": "",
        "beat_name": "",
        "action": "",
        "validation": ""
      }
    ],
    "contact_contract": {
      "required": false,
      "contact_type": "",
      "initiator": "",
      "receiver": "",
      "visibility": "",
      "reaction": "",
      "aftermath": ""
    },
    "camera_motion": {
      "shot_size": "",
      "angle": "",
      "movement": "",
      "stability": "",
      "screen_direction": "",
      "readability": ""
    },
    "end_frame_goal": {
      "pose": "",
      "composition": "",
      "hold_seconds": 0.5,
      "next_shot_ready": true
    },
    "continuity_locks": [],
    "negative_constraints": [],
    "validation_checklist": []
  }
}
```

---

# 24. Complete Example: Multi-Shot Fight Exchange

```json
{
  "sequence_id": "FIGHT_EXCHANGE_001",
  "director_goal": "Show that the hero survives because of timing and control, not superior strength.",
  "global_continuity": {
    "fighters": "same two fighters throughout",
    "location": "same warehouse hallway",
    "lighting": "same overhead fluorescent lighting",
    "screen_direction": "opponent pressures right-to-left, hero retreats left-to-right"
  },
  "shots": [
    {
      "shot_id": "SH01",
      "workflow_type": "text_to_video",
      "shot_function": "establish pressure and distance",
      "motion_core": {
        "motion_intent": "opponent crowds the hero backward",
        "movement_quality": {
          "space": "direct",
          "weight": "strong",
          "time": "sustained",
          "flow": "bound"
        },
        "mechanics": "opponent steps forward with heavy grounded pressure; hero retreats half step without turning away",
        "camera": "medium-wide side angle, full bodies visible",
        "end_frame_goal": "hero backed near wall, hands high, opponent within striking distance"
      }
    },
    {
      "shot_id": "SH02",
      "workflow_type": "image_to_video",
      "first_frame_source": "SH01_final_frame",
      "shot_function": "evasion and counter",
      "motion_delta": "hero slips left and counters; opponent overcommits",
      "motion_core": {
        "movement_quality": {
          "space": "direct",
          "weight": "strong",
          "time": "sudden",
          "flow": "bound"
        },
        "mechanics": "hero shifts weight off centerline, hips rotate, shoulder follows, compact counter extends",
        "contact_contract": "counter lands clearly at jawline; opponent head snaps back; feet adjust",
        "camera": "same angle, no cut during contact",
        "end_frame_goal": "opponent recoiling, hero hand returning to guard"
      }
    },
    {
      "shot_id": "SH03",
      "workflow_type": "image_to_video",
      "first_frame_source": "SH02_final_frame",
      "shot_function": "aftermath and reset",
      "motion_delta": "opponent staggers one step, hero breathes hard and resets stance",
      "motion_core": {
        "movement_quality": {
          "space": "direct",
          "weight": "strong",
          "time": "sustained",
          "flow": "bound"
        },
        "mechanics": "opponent regains balance slowly; hero does not chase, returns to guard",
        "camera": "subtle push-in on hero's controlled breathing",
        "end_frame_goal": "hero and opponent separated, ready for next beat"
      }
    }
  ]
}
```

---

# 25. Complete Example: UGC Product Motion

```text
Scene Function:
Show the tactile benefit of the product through believable hand motion.

Workflow:
Image-to-video from product-in-hand reference.

First Frame Lock:
Preserve the same hand, product, desk, lighting, camera angle, and background.

Motion Intent:
The creator casually demonstrates the product's texture and feel.

Movement Quality:
Space: direct but small
Weight: light
Time: sustained
Flow: free
Overall feel: natural, relaxed, tactile

Hand/Object Mechanics:
The thumb rolls the product slowly against the index finger.
The palm adjusts slightly to keep the product visible.
The product rotates about 30 degrees toward the camera.
The hand remains anatomically plausible and the product never floats.

Timing:
0.0-1.0s: product held still for recognition
1.0-3.0s: slow thumb roll and small rotation
3.0-4.5s: hand brings product slightly closer to camera
4.5-5.0s: final stable hold

Camera:
Handheld phone close-up with slight natural sway.

End Frame Goal:
Product centered, clearly visible, held still for 0.5 seconds.

Avoid:
Product morphing, extra fingers, impossible grip, floating object, sudden camera cut, over-polished commercial motion.
```

---

# 26. Complete Example: Cinematic Drama Motion

```text
Scene Function:
Reveal emotional defeat through restrained body movement.

Workflow:
Text-to-video or image-to-video.

Motion Intent:
The character tries to stay composed after hearing bad news.

Movement Quality:
Space: direct
Weight: strong
Time: sustained
Flow: bound
Overall feel: restrained, heavy, controlled

Body Mechanics:
The character stands still at first.
The jaw tightens before the body moves.
Shoulders slowly lower as breath leaves the chest.
One hand relaxes from a fist.
Eye contact breaks downward for half a second, then returns.

Camera:
Slow dolly push-in from medium close-up to tight close-up.
No cuts.
The camera moves only after the character becomes still.

End Frame Goal:
Tight close-up, eyes controlled but hurt, shoulders lowered, no dramatic gesture.

Avoid:
Crying exaggeration, melodramatic arm movement, random pacing, fast camera movement.
```

---

# 27. Complete Example: Anime Motion Burst

```text
Scene Function:
Show a sudden overwhelming attack in stylized anime language.

Workflow:
First/last-frame or image-to-video.

Motion Intent:
The hero compresses energy, then releases it in one decisive strike.

Movement Quality:
Space: direct
Weight: strong
Time: sudden
Flow: free during attack, bound at landing

Anime Motion:
Hold anticipation pose for 0.4 seconds.
Use strong silhouette and exaggerated line of action.
During the strike, add smear-frame arm motion and speed-line background.
At contact, use one-frame impact flash.
After impact, hold the opponent's recoil pose for 0.3 seconds.

Camera:
Low-angle three-quarter view, brief push-in before the strike, no confusing orbit.

End Frame Goal:
Hero lands in a grounded final pose, opponent recoiling, clear silhouette.

Avoid:
Mushy 3D anime motion, teleporting without anticipation, unclear hit, random camera spin, identity drift.
```

---

# 28. Source Reading Map

These sources support the concepts used in this manual.

## 28.1 Laban and Expressive Movement

- **Rudolf Laban / Laban Movement Analysis**  
  Use for Space, Weight, Time, Flow, effort, shape, and expressive motion vocabulary.  
  URL: https://en.wikipedia.org/wiki/Laban_movement_analysis

- **Laban for Actors and Dancers** by Jean Newlove  
  Use for actor-friendly movement qualities and physical characterization.

- **Affective Movement Generation using Laban Effort and Shape and Hidden Markov Models**  
  Use for the connection between Laban abstractions and computational affective motion.  
  URL: https://arxiv.org/abs/2006.06071

## 28.2 Animation Motion Principles

- **The Illusion of Life** by Frank Thomas and Ollie Johnston  
  Use for the 12 principles of animation: anticipation, staging, follow-through, arcs, timing, exaggeration, appeal.  
  URL: https://books.disney.com/book/the-illusion-of-life/

- **The Animator's Survival Kit** by Richard Williams  
  Use for timing, spacing, walks, runs, action, dialogue, and movement readability.  
  URL: https://www.faber.co.uk/product/9780571238347-the-animators-survival-kit/

## 28.3 Facial and Performance Complement

- **Facial Action Coding System** by Paul Ekman Group  
  Use for facial Action Units that complement Motion Core.  
  URL: https://www.paulekman.com/facial-action-coding-system/

- **Acting for Animators** by Ed Hooks  
  Use for turning motivation and objective into physical action.  
  URL: https://edhooks.com/

## 28.4 Cinematography and Shot Readability

- **The Five C's of Cinematography** by Joseph V. Mascelli  
  Use for camera angles, continuity, cutting, close-ups, and composition.

- **Film Directing: Shot by Shot** by Steven D. Katz  
  Use for blocking, storyboarding, shot design, and action continuity.

- **Cinematography: Theory and Practice** by Blain Brown  
  Use for lens, lighting, camera movement, and visual storytelling.

## 28.5 Fight Choreography

- **Fight Choreography: The Art of Non-Verbal Dialogue** by John Kreng  
  Use for fight beats, cause-effect, readable contact, and combat as storytelling.

- **Stage Combat / stunt choreography training material**  
  Use for safety-oriented structure: distance, target, reaction, selling impact, camera angle.

## 28.6 Editing and Continuity

- **In the Blink of an Eye** by Walter Murch  
  Use for timing, emotional cuts, and why the right cut matters.

- **The Technique of Film and Video Editing** by Ken Dancyger  
  Use for continuity editing, montage, action cutting, and dramatic rhythm.

---

# 29. RAG Ingestion Recommendations

## 29.1 Recommended Document Metadata

```json
{
  "doc_type": "motion_prompting_manual",
  "concept_family": "Motion Core",
  "parent_concepts": [
    "Ontology-Driven Multimodal Direction Prompting",
    "Performance Core",
    "Control Modules",
    "Director System"
  ],
  "domains": [
    "AI video",
    "choreography",
    "animation",
    "cinematography",
    "prompt engineering",
    "workflow design"
  ],
  "use_cases": [
    "fight scenes",
    "product ads",
    "UGC",
    "anime",
    "drama",
    "cinematic",
    "sports",
    "vehicles",
    "animals",
    "VFX transformations"
  ],
  "retrieval_priority": "high",
  "should_extract_templates": true,
  "should_extract_schemas": true
}
```

## 29.2 Recommended Entity Types

```yaml
entity_types:
  - MotionConcept
  - MotionField
  - WorkflowType
  - VideoGenre
  - ValidationRule
  - NegativeConstraint
  - PromptTemplate
  - JSONSchema
  - SourceBook
  - MotionFailureMode
```

## 29.3 Recommended Relations

```yaml
relations:
  - MotionCore HAS_FIELD MovementQuality
  - MovementQuality HAS_DIMENSION Space
  - MovementQuality HAS_DIMENSION Weight
  - MovementQuality HAS_DIMENSION Time
  - MovementQuality HAS_DIMENSION Flow
  - FightScene REQUIRES ContactContract
  - ImageToVideo REQUIRES MotionDelta
  - FirstLastFrameWorkflow REQUIRES EndFrameGoal
  - ProductDemo REQUIRES ObjectContinuity
  - AnimeFight USES ImpactFrame
  - RealisticMotion AVOIDS FloatyMovement
```

## 29.4 Query Examples

```text
How do I prompt a realistic fight scene with clear contact and reaction?
```

```text
What fields are required for image-to-video motion continuity?
```

```text
How do I preserve product shape while adding hand motion in UGC?
```

```text
What is the difference between Performance Core and Motion Core?
```

```text
How should an agent route a first-frame/last-frame video request?
```

---

# 30. Final Mental Model

The complete AI video direction stack is:

```text
Performance Core:
Emotion, face, subtext, acting, dialogue, lip sync.

Motion Core:
Movement intent, quality, biomechanics, path, force, contact, reaction, recovery.

Control Modules:
Ads, UGC, anime, fights, drama, cinematic, product, sports, vehicles, animals, VFX.

Director System:
Project bible, asset registry, scene graph, shot manifest, first/last-frame contracts, continuity ledger, validation loop.
```

For motion, always ask:

```text
What moves?
Why does it move?
How does it start?
What path does it follow?
What force does it imply?
What does it touch?
What reacts?
How does it recover?
Where must it end?
What must not change?
```

That is the core of **Kinetic Motion Direction Prompting**.
