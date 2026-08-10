---
id: cpcs.style.anime_sakuga
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §18]
primary_route: cpcs/knowledge/16_style_visual_language/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/knowledge/06_body_motion/action_primitives/
interfaces:
  - cpcs.body.superhuman_transform
  - cpcs.mx.style_mechanics
  - cpcs.found.exactness_taxonomy
  - cpcs.found.layer_architecture
---

# Anime, Sakuga, Limited Animation, and Cartoon Physics

> **Source:** SRC-005 §18 — "Anime, sakuga, limited animation, and cartoon physics"

## Problem

Anime and other stylized 2D animation often optimize for designed drawings and
perceptual motion rather than continuous anatomical reconstruction. The source
may contain held cels, exposure changes, extreme key poses, smear drawings,
multiplane background movement, perspective deformation, impact flashes, and
deliberate temporal discontinuities. Treating every frame as a sample of a
smooth 3D human skeleton can destroy the style.

## Dual representation

CPCS-MX stores two linked representations:

1. **choreographic skeleton:** action, root, joint, phase, and contact logic;
2. **graphic motion layer:** key drawings, silhouette, deformation, exposure,
   smear, effects, and camera-plane motion.

## Exposure and held drawings

An animation exposure track states which drawing or pose is displayed and for
how long:

```yaml
exposure_track:
  - frames: [0, 2]
    pose_ref: anticipation_key_A
    hold: true
  - frames: [3, 3]
    pose_ref: smear_01
    deformation_mode: graphic
  - frames: [4, 5]
    pose_ref: contact_key_B
    hold: true
```

The underlying skeleton may interpolate continuously for simulation or camera
integration, while the render selects held or deformed drawings.

## Smear frames

A smear is not simply motion blur. It is an authored shape that connects
positions, preserves direction, and improves readability. CPCS-MX represents:

```text
source and destination silhouette anchors
smear duration in exposures
body regions affected
maximum deformation
multiplicity or echo count
line-of-action
color and effect treatment
whether the rig or only the render deforms
```

## Keyframe economy

A stylized sequence can concentrate information in anticipation, apex,
contact, and recoil keys. In-between density becomes a style control. Fewer
in-betweens do not imply poor motion if timing, arcs, silhouettes, and action
causality are clear. The score stores `key_pose_priority` and
`inbetween_policy` rather than demanding constant frame-to-frame change.

## Perspective and anatomy

A fist may enlarge toward camera, limbs may stretch, or the torso may twist
beyond human anatomy for one drawing. These are graphic deformations. They
should compile through camera-relative scaling, blendshapes, cage deformation,
or 2D warps — not by silently changing the human joint-limit schema.

## Impact grammar

An anime impact may combine:

```text
contact key
+ one-frame monochrome or inverse-color flash
+ background speed-field discontinuity
+ screen shake
+ debris burst
+ held recoil silhouette
+ delayed sound or silence gap
```

Each element has independent timing. The impact can be superhuman in
presentation while the choreography retains a staged near-contact.

## Style transfer limits

A scalar `style_intensity` can be a user interface control, but the compiler
should expand it into multiple parameters: hold density, smear probability,
deformation scale, camera amplitude, effect density, time-warp strength, and
anatomical deviation. Otherwise one slider can produce incoherent combinations.

## Combat style notes (SRC-010 EXTEND)

The lab's combat reference and the naruto_sasuke_rooftop_clash variant add
render-tested style parameterization on top of this representation (see
`cpcs.combat.math_metrics_layer`):

- **Shonen:** anime scale 1.5–3× human strike velocities; held impact frames
  1–8; mixed frame rate 1s/2s/3s exposure with bpm_by_beat tempo (160 global,
  140→60 per beat); power_curve normalized 0.30→1.00 with monotonic
  escalation; style_overrides (2d_anime_cel) applied as a layer, not a
  rewrite. Worked example: 10 s / 24 fps / 240 frames, 12×8 m arena at 25 m
  elevation, characters with explicit body proportions (reach_m 0.58/0.61).
- **Wuxia:** loose engagement ranges (1.5–2.5 m), floaty weight, indirect
  space.
- **MMA:** tight ranges (0.3–0.5 m), real velocities, minimal stylization.
- **Superhero:** superhuman physics split — presentation scale is separate
  from the choreographic skeleton; staged near-contact stays honest.

The dual representation (choreographic skeleton + graphic motion layer) is
exactly what makes these style parameters swappable without disturbing the
skeleton.

## Boundary

This card defines anime/sakuga representation. It does not prescribe a
specific animation toolchain; it defines the semantic layer that any toolchain
must respect.
