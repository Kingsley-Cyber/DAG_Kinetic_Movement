---
id: cpcs.camera.impact_sync
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/knowledge/12_camera_image_formation/
secondary_routes:
  - cpcs/knowledge/10_time_rhythm/
  - cpcs/knowledge/07_interaction_contact/
interfaces:
  - cpcs.rhythm.metrics_contract
  - cpcs.contact.interaction_lifecycle
  - cpcs.camera.three_layer_semantics
---

# Camera Impact Synchronization

> **Source:** SRC-012 topic 9 — "Camera Grammar"

## Principle

Camera motion changes perceived speed, force, geography, and attention
without changing the actor's underlying motion. Camera state, subject state,
and **relative image-plane motion** are stored separately. In a pinhole
approximation \(x = fX/Z\), apparent image velocity depends on focal length,
depth, and camera–subject relative velocity.

## Impact binding chain

Camera and sound events are bound to:

```text
anticipation peak → contact → reaction onset → camera impulse peak →
audio transient → cut → settle
```

**The subject contact event remains authoritative.** Every other bound event
keeps a declared offset (authored `s`/frames or `measured` + timebase) and
can be edited independently without moving the contact. This mirrors the
causal bundle in `interaction_lifecycle.md` (attacker end-effector path,
defender target position, near-contact decision, defender reaction onset,
sound onset, VFX accent, camera shake, edit point).

## Impact response record

```json
{
  "impact_response": {
    "amplitude": 0.22,
    "peak_offset_frames": 0,
    "decay_frames": 6
  }
}
```

- **Zero-frame camera-impulse offset** is the CPCS preset (different
  amplitudes/decays allowed); presets are starting points, not laws.
- Expected check from the worked example: camera impulse decays within
  **six frames**.
- At 24 fps, a **two-frame impact hold ≈ 83 ms**; that can read as stylized
  emphasis rather than literal time.
- `handheld_impulse` primitive parameters: `amplitude, frequency_hz,
  impact_sync, decay_s` — a band-limited trajectory, not random frame jitter.

## Camera math (formulas)

\[
\text{exposure\_time} = \frac{\text{shutter\_angle}}{360 \times \text{fps}}
\]

(180° @ 24 fps → 1/48 s; lower shutter = crisper/staccato action, longer
exposure = more blur/perceived speed but may erase contacts.)

\[
x = fX/Z \quad\text{(pinhole projection; apparent velocity depends on
focal length, depth, and relative velocity)}
\]

Motion blur can be estimated from exposure time and image velocity.

## Perceived-motion controls

| Control | Effect | Caution |
|---|---|---|
| follow_subject | reduces subject screen velocity; parallax shows travel | can reduce perceived strike speed if over-locked |
| counter_move | increases relative screen velocity | may sacrifice geography |
| close_wide_lens | exaggerated near/far scale and parallax | edge distortion |
| long_lens_far_camera | lower parallax, compressed depth; lateral motion legible | does not change physical speed |
| lower_shutter_angle | crisper action | may feel harsh |
| longer_exposure | more blur, perceived speed/softness | may erase contacts |
| foreground_parallax | amplifies travel | avoid occluding impact |

## Action coverage

A robust action sequence normally needs: a **readability master** (full
bodies, distances, feet, axis); an **impact insert** only when causality
remains clear; a pursuit/follow shot; a power approach; a vulnerability
frame. Fast camera movement is not a substitute for coherent choreography.
Reference/native camera control outranks prose; unsupported controls emit a
lossy-compilation warning (compilation hierarchy: camera reference →
keyframes → native control → prompt phrase → post-generation edit; never
label a prompt phrase as a native trajectory).

## Anime/stylized devices

| Device | Frame/parameter guidance |
|---|---|
| impact_frame | [1, 3] frames at contact |
| smear_frame | [1, 2] frames |
| speed_lines | direction, density, length, opacity, vanishing point |
| held_pose | hold_frames, secondary_motion, camera_motion |
| dramatic_zoom | fov_start, fov_end, frames, easing |
| freeze_frame | frames, audio_continuation, graphic_treatment |

These are production conventions, not one uniform "anime law".

## DAG representation

```text
contact_event →(binds)→ camera_impulse   (offset_frames, decay_frames)
contact_event →(binds)→ audio_transient  (offset_s)
contact_event →(binds)→ cut              (cut candidate, offset)
contact_event →(binds)→ reaction_onset   (causality: onset >= contact)
camera_track →(has_primitive)→ truck|handheld_impulse|... (impact_sync flag)
```

All offsets are edge attributes; the contact node is the anchor. The rhythm
card's `peaks_with`/`synchronizes_with` edges attach the same binding chain
to beats and accents.

## Verification

`test_contact_event_authoritative_anchor`,
`test_camera_impulse_decay_within_six_frames`,
`test_handheld_impulse_band_limited`,
`test_prompt_phrase_not_labeled_native_trajectory`.
