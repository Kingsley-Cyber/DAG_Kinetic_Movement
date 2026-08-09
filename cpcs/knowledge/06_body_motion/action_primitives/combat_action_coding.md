---
id: cpcs.body.combat_coding
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §17]
primary_route: cpcs/knowledge/06_body_motion/action_primitives/
secondary_routes:
  - cpcs/knowledge/07_interaction_contact/
  - cpcs/knowledge/06_body_motion/phase_grammar/
interfaces:
  - cpcs.contact.interaction_lifecycle
  - cpcs.found.causality.causal_event_semantics
  - cpcs.mx.relative_motion
  - cpcs.found.exactness_taxonomy
---

# Staged Combat and Multi-Actor Action Coding

> **Source:** SRC-005 §17 — "Staged combat and multi-actor action coding"

## Scope and safety

This card concerns **virtual character animation and professionally staged
screen action**. It does not provide instructions for injuring a person.
Professional stage-combat practice prioritizes safety, repeatability,
theatrical commitment, and storytelling. Apparent impacts can be created
through distance, angle, timing, reaction, sound, editing, and VFX rather
than actual force.

## Atomic action vocabulary

A fight scene is decomposed into functional actions rather than named
techniques alone:

```text
establish stance or guard
approach, retreat, circle, close distance
shift support
step-in or step-out
pivot or turn
load or anticipate
reach or strike-like extension
block, parry, evade, duck, redirect
staged near-contact or virtual impact
recoil, displacement, stumble, fall
catch, roll, brace, land
recovery, reorientation, return to guard
reaction or decision pause
```

Named martial-arts labels can be metadata, but the executable score uses root,
joint, phase, contact, and target relations.

## Coupled actor score

A combat beat is not two independent clips. It is a coupled system:

```json
{
  "beat_id": "exchange_03",
  "participants": ["attacker","defender"],
  "events": [
    {"id":"A_step","actor":"attacker","type":"step_in","start_s":1.20,"end_s":1.48},
    {"id":"A_extend","actor":"attacker","type":"strike_like_extension","start_s":1.36,"apex_s":1.67,"end_s":1.82},
    {"id":"near_contact","type":"staged_near_contact","source":"attacker.hand_r","target":"defender.head_region","time_s":1.67},
    {"id":"B_recoil","actor":"defender","type":"recoil","start_s":1.71,"apex_s":1.88,"end_s":2.20}
  ],
  "relations": [
    {"type":"causes","from":"near_contact","to":"B_recoil"},
    {"type":"targets","from":"A_extend","to":"defender.head_region"}
  ]
}
```

## Contact, impulse, and reaction

A contact event can include: visual minimum distance, collision decision,
contact normal, virtual impulse, defender reaction delay, local deformation,
root displacement, camera and audio accents, and recovery duration. For staged
near-contact, the attacker trajectory and defender reaction can be authored
independently, with camera placement making the event read as contact. This
permits repeatability and avoids requiring a physically accurate collision.

## Falls and recovery

Falls use support-state and landing-event notation:

```text
loss of balance
→ base of support failure
→ protective or stylized response
→ first contact
→ load distribution
→ secondary contacts
→ slide or roll
→ settle
→ recovery decision
```

## Readability and camera cheats

Fight choreography is designed for an audience. Screen direction, silhouette,
target visibility, reaction timing, and cut placement are perceptual
constraints. A camera-side cheat can preserve a visible gap while making
trajectories overlap in projection. The score stores both world-space and
screen-space contact conditions so the technique is explicit.

## Fine-tuning loop

For a generated fight:

1. compile pose, root, contact, and camera controls
2. generate the clip
3. re-extract actors and pose
4. measure contact frame, minimum distance, root path, phase, reaction delay,
   and screen direction
5. adjust only the failing modules
6. regenerate the smallest affected interval
7. verify continuity at splice boundaries

This modular loop is more deterministic than rewriting an entire paragraph
prompt.

## Combat math metrics layer (SRC-010 EXTEND)

The lab's combat choreography reference adds the quantitative layer to this
ontology — units, frame budgets, and tolerances — distilled to
`cpcs.combat.math_metrics_layer`:

- **Two-document architecture:** YAML authoring (intent, beats, style) + JSON
  kinematic canon (keyframes, vectors, contacts, tolerances). The kinematic
  doc is the executable truth (v005 proved it sufficient alone).
- **Frame budget identity:** `beat_frames = (end − start) × fps` — every beat
  satisfies it exactly (TOL_FRAME 0).
- **4-phase strike ratios:** anticipation 25–35% · contact 10–15% ·
  follow-through 25–35% · recovery 15–30%; held impact frames 1–8.
- **Per-beat kinematics:** closing_speed_ms, screen_velocity_pct_s,
  strike_velocity_ms, torso_rotation_per_strike_deg, recoil_distance_m,
  weight_transfer_time_ms. Jab reference 6–8 m/s typical / 10–14 elite;
  anime scale 1.5–3×.
- **Contact geometry:** separation ≤ combined reach + 0.35 m — v005's 1.60 m
  separation vs 1.42 m reach (0.18 m deficit) was caught by tooling, not by
  eye.
- **10 required constraints** with tolerances, all machine-checkable
  (v006: 0 failures on validate_kinematics).
- **Camera math:** 7 parameters (focal_length_mm, angle_deg,
  tracking_speed_match, shake_amplitude_px, shake_frequency_hz 8–15,
  shake_decay_frames, whip_pan_speed_deg_s 120–240), patterned by beat type.

Applies to the fine-tuning loop above: step 4 (measure) becomes deterministic
via the constraints; step 5 (adjust only failing modules) is guided by which
check family failed.

## Boundary

Real stunt planning belongs to qualified professionals, not an automated
animation schema. Combat examples describe virtual animation or professionally
staged screen action, not real-world injury optimization.
