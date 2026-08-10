---
id: cpcs.mx.camera_subject_parallax
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-003 §78]
primary_route: cpcs/knowledge/12_camera_image_formation/
secondary_routes:
  - cpcs/knowledge/06_body_motion/
interfaces: [cpcs.camera.three_layer_semantics, cpcs.mx.spatial_state]
---

# Camera-Subject Parallax

Camera and actor motion are correctly separated, but they also interact
perceptually. The same actor trajectory can look different under locked camera,
dolly, tracking, orbit, handheld, or zoom.

## Coupling model

```yaml
camera_subject_relation:
  subject: actor_A
  camera_mode: tracking
  framing:
    preserved: medium_shot
  relative_screen_motion:
    target: stable
```

Current human-video motion research explicitly treats camera trajectories and
human pose as joint spatio-temporal control variables rather than unrelated
signals.

## Verification

`test_camera_subject_relation_present`,
`test_framing_preservation_checked`.
