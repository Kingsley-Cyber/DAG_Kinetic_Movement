---
id: cpcs.knowledge.pegasus_fight_analysis
kind: method
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 Pegasus paper Part III §21-29]
primary_route: cpcs/knowledge/05_action/combat/
interfaces:
  - cpcs.knowledge.combat_coding
  - cpcs.knowledge.anime_sakuga
  - cpcs.evaluation.video_observation_graph
---

# Pegasus Fight Analysis Framework

> Distilled from Pegasus paper Part III (fight layers, passes, measurement pipeline,
> canonical score, transfer YAML, compilation tiers, validation). This card captures
> the 8-layer fight decomposition and 5-pass analysis methodology.

## 8 fight layers

| Layer | Content |
| --- | --- |
| 1. Action causality | Graph of approach, attack, defense, counter, recoil, fall, recovery. Initiator, target, narrative function. |
| 2. Body-action | 9 landmarks: root/pelvis, shoulders, elbows, wrists, head, hips, knees, ankles, weapon endpoints. Proximal-to-distal sequencing. |
| 3. Phase | Approach, standoff, attack, defense, counterattack, recoil, fall, recovery, reaction. |
| 4. Interaction | Actor-to-actor distance, contact candidates, near-contact, staged impact, occlusion. |
| 5. Laban | Weight (light/strong), Time (sustained/sudden), Space (indirect/direct), Flow (free/bound). Describes quality, not action identity. |
| 6. Face/affect | Gaze target, blink suppression, jaw/brow activity, displayed valence/arousal/control, stylized anime face deformation. |
| 7. Camera/edit | Screen direction, shot scale, angle, push/pan/orbit/crop/shake, cut-on-action, impact cut, reaction cut, held frame, time warp. |
| 8. Anime VFX | Smear drawing, impact flash, speed lines, motion echo, energy trail, dust burst, debris, frame repetition, background abstraction, color/exposure pulse, screen deformation. |

## 5 Pegasus fight passes

| Pass | Function |
| --- | --- |
| F1 — Exchange segmentation | Segment source into tactical passages (approach, standoff, attack, defense, counter, recoil, fall, recovery, reaction). Fields: participants, initiator, target, visible_actions, tactical_function, camera_presentation, vfx_summary, contact_visibility, uncertainty. |
| F2 — Ordered visible actions | For each passage, request ordered list of visible physical events. Do not invent hidden motion. Require explicit language when cuts, flashes, blur, or occlusion hide the action. |
| F3 — Tactical/emotional interpretation | Apparent objective, commitment vs hesitation, dominance change, reaction/recovery, displayed affect, gaze relationship, narrative reversal. |
| F4 — Camera/editorial causality | What action the camera makes readable vs hides. Whether edit creates impact. Whether background motion implies camera movement. Time held/repeated/slowed. Screen direction continuity. |
| F5 — Anime effects | Effect onset, type, relationship to body movement, relationship to sound, whether it replaces a physically readable frame, whether to recreate as generation-time style or post-composite VFX. |

## 6-step measurement pipeline

1. **Track all participants** — stable actor IDs and masks through occlusion and cuts
2. **Extract reviewed 2D pose** — root, shoulders, elbows, wrists, head, hips, knees, ankles, heel/toe, weapon endpoints, contour anchors
3. **Derive motion primitives** — ankle velocity → foot plant; pelvis leads shoulder → proximal-to-distal; wrist-target minimum + flash + recoil → staged impact
4. **Separate camera and body motion** — estimate background transform after masking actors/effects
5. **Preserve screen-space truth** — for stylized anime, screen-space reconstruction may be more faithful than forced 3D. Preserve silhouette, image-space joint path, timing, perceived force.
6. **Optional physics refinement** — DeepMimic-style physics controllers for changed terrain/proportions. Should not erase deliberate anime timing.

## Fight transfer YAML

```yaml
transfer_policy:
  retain:
    - shot_order, screen_direction, action_causality
    - support_foot_schedule, major_joint_trajectory_shape
    - target_relationships, impact_frame, reaction_delay
    - laban_quality, camera_grammar, vfx_timing
  parameterize:
    action_speed_scale: 0.92
    displacement_scale: 1.05
    camera_shake_scale: 0.75
    energy_effect_density: 0.65
  replace:
    - character_identity, costume, setting
    - exact_energy_design, dialogue, source_music
```

## 5 fight compilation tiers

| Tier | Description |
| --- | --- |
| 1 — Text only | Action graph into precise ordered language. Cannot guarantee frame-level recreation. |
| 2 — Key poses | Anticipation, extension, target, recoil, recovery frames. Model interpolates. |
| 3 — Pose-conditioned video | Full pose sequence from reviewed tracking. Model follows pose. |
| 4 — Multi-asset | + camera path, masks, VFX timing, audio sync. |
| 5 — Closed-loop | + re-extraction, comparison, patch-based revision. |

## Fight validation (4 metric families)

1. **Temporal** — event timing error, action order agreement, reaction delay
2. **Physical** — contact/near-contact classification, support foot schedule, momentum direction
3. **Cinematic** — shot scale agreement, screen direction, camera-motion type, cut-on-action
4. **Stylistic** — Laban quality agreement, VFX timing, arousal/displayed control
