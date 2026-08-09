# 09 — Camera Grammar for Motion and Action Scenes

## Executive finding

Camera motion changes perceived speed, force, geography, and attention without changing the actor’s underlying motion. CPCS therefore stores camera state, subject state, and **relative image-plane motion** separately. In a pinhole approximation `x=fX/Z`, so apparent image velocity depends on focal length, depth, and camera–subject relative velocity. Perspective is determined by camera position; focal length changes field of view, and the familiar “wide versus telephoto perspective” difference appears when camera distance changes to maintain framing. [S040; S042]

## Camera state

Canonical state includes world position/orientation, focal length or field of view, sensor/equivalent format, focus distance, aperture if rendered, shutter angle/exposure, frame rate, stabilization mode, and target lock. Motion blur can be estimated from `exposure_time = shutter_angle/(360×fps)` and image velocity.

## Motion primitives

| Primitive | Axis/path | Parameters |
|---|---|---|
| pan | yaw | degrees, duration_s, easing, subject_lock |
| tilt | pitch | degrees, duration_s, easing, subject_lock |
| roll | optical | degrees, duration_s, easing |
| dolly | local_z | distance_m, duration_s, easing |
| truck | local_x | distance_m, duration_s, parallax_target |
| pedestal | world_y | distance_m, duration_s |
| orbit | around_subject | arc_deg, radius_m, elevation_deg, subject_lock |
| crane | compound | control_points, duration_s |
| push_in | physical_or_optical | screen_scale_ratio, duration_s, method |
| pull_out | physical_or_optical | screen_scale_ratio, duration_s, method |
| whip_pan | yaw/pitch | degrees, frames, settle_frames |
| handheld_impulse | 6dof | amplitude, frequency_hz, impact_sync, decay_s |

A `push_in` must record whether it is a physical dolly, optical zoom, digital crop, or a compound move; they produce different parallax and embodiment cues. “Handheld” should be a band-limited trajectory with amplitude, frequency, and decay—not random frame jitter.

## Perceived-motion controls

| Control | Effect | Caution |
|---|---|---|
| follow_subject | reduces subject screen velocity while background parallax shows travel | can reduce perceived strike speed if over-locked |
| counter_move | increases relative screen velocity | may sacrifice geography |
| close_wide_lens | exaggerated near/far scale and parallax | edge distortion |
| long_lens_far_camera | lower parallax/compressed depth; lateral motion legible | does not change physical speed |
| lower_shutter_angle | crisper/staccato action | may feel harsh |
| longer_exposure | more blur, perceived speed/softness | may erase contacts |
| foreground_parallax | amplifies travel | avoid occluding impact |

Following a runner can stabilize the actor while foreground/background parallax communicates speed. Moving against the runner increases screen velocity. A close wide lens amplifies approach and limb foreshortening but can distort anatomy; a distant telephoto view reduces parallax and can make lateral motion cleanly legible.

## Continuity

| Rule | Operational interpretation | Status |
|---|---|---|
| axis_180 | stay on one side of established action axis unless crossing is motivated/shown | PRACTICE |
| change_30 | change angle/size enough to avoid accidental jump cut | PRACTICE with perceptual evidence |
| match_on_action | preserve action phase/contact continuity across cut | PRACTICE |
| eyeline_match | preserve gaze target geometry | PRACTICE |
| screen_direction | retain left/right travel unless reversal is marked | PRACTICE |

The 180-degree and 30-degree rules are conventions with perceptual motivation, not laws. CPCS stores the action axis and desired screen direction, then permits a marked axis crossing when a shot reveals the crossing or disorientation is intentional. [S043]

## Action coverage

A robust action sequence normally needs:

- a **readability master** showing full bodies, distances, feet, and axis;
- an **impact insert** only when causality remains clear;
- a pursuit/follow shot for travel;
- a power approach using close wide geometry or controlled counter-move;
- a vulnerability frame using negative space, higher angle, or retreating camera.

The model should not substitute fast camera movement for coherent choreography. When a reference or native camera control exists, it outranks prose. When unsupported, CPCS emits a lossy-compilation warning.

## Impact synchronization

Camera and sound events are bound to anticipation peak, contact, reaction onset, camera impulse peak, audio transient, cut, and settle. The subject contact event remains authoritative. CPCS presets suggest zero-frame camera-impulse offset with different amplitudes/decays, but they are starting points. At 24 fps, a two-frame impact hold is about 83 ms; that can read as stylized emphasis rather than literal time.

## Anime/stylized devices

| Device | Definition | Frame/parameter guidance |
|---|---|---|
| impact_frame | high-contrast/abstracted frame at contact | [1, 3] |
| smear_frame | stretched or multi-position bridge between poses | [1, 2] |
| speed_lines | graphic technique | ['direction', 'density', 'length', 'opacity', 'vanishing_point'] |
| held_pose | graphic technique | ['hold_frames', 'secondary_motion', 'camera_motion'] |
| dramatic_zoom | graphic technique | ['fov_start', 'fov_end', 'frames', 'easing'] |
| freeze_frame | graphic technique | ['frames', 'audio_continuation', 'graphic_treatment'] |

AnimeInterp is relevant to the technical difficulty of interpolation in sparse, non-photoreal animation, but impact frames, smears, speed lines, and holds are production conventions rather than one uniform “anime law.” [S044]

## Canonical camera record

```json
{
  "shot_size": "medium_full",
  "focal_length_equiv_mm": 28,
  "fps": 24,
  "shutter_angle_deg": 180,
  "track": {"primitive": "truck", "distance_m": 1.4, "duration_s": 2.0},
  "subject_lock": ["fighter_a", "fighter_b"],
  "action_axis": "fighter_a_to_fighter_b",
  "impact_response": {"amplitude": 0.22, "peak_offset_frames": 0, "decay_frames": 6},
  "contact_visibility_required": true
}
```

## Model compilation hierarchy

1. camera reference/trajectory;
2. keyframes;
3. documented native camera control;
4. prompt phrase;
5. post-generation edit.

The compiler never labels a prompt phrase as a native camera trajectory. It records what was requested, what the model actually received, and the expected loss.

## References and locators

- **[S016]** Frank Thomas; Ollie Johnston (1981), *The Illusion of Life: Disney Animation*. **Locator:** Chapters on anticipation, follow-through, timing, arcs, exaggeration  
- **[S040]** David Bordwell; Kristin Thompson; Jeff Smith (2020), *Film Art: An Introduction*. **Locator:** Cinematography, editing, continuity, temporal relations  
- **[S041]** Karen Pearlman (2016), *Cutting Rhythms: Intuitive Film Editing, 2nd ed.*. **Locator:** Timing, pacing, trajectory phrasing, tension/release  
- **[S042]** Vittorio Gallese; Michele Guerra and related empirical work (2019), *Camera Movements and Viewer Motor Cognition*. **Locator:** Static, zoom, dolly, Steadicam, handheld comparisons  
- **[S043]** Empirical editing-perception researchers (2013), *The 30-Degree Rule and Perceptual Continuity*. **Locator:** Experimental methods and results  
- **[S044]** Li Siyao et al. (2021), *AnimeInterp: Open-Domain Interpolation for 2D Animation*. **Locator:** CVPR 2021; formulation and occlusion-aware interpolation  
- **[S053]** Google AI for Developers (2026), *Generate Videos with Veo 3.1 in the Gemini API*. **Locator:** API parameters/specifications; model features; prompt guide  
- **[S054]** Kling AI (2026), *Kling VIDEO 3.0 Model User Guide*. **Locator:** Multi-shot, 3–15 second duration, camera/storyboard guidance  
- **[S055]** Runway (2026), *Creating with Gen-4.5*. **Locator:** Settings: 2–10 sec, aspect ratio, 24/25 fps  
- **[S057]** Luma AI (2026), *Ray 3.2 Controls & Workflows In Depth*. **Locator:** Motion, Structure, Characters, quick reference  
- **[S059]** Adobe Firefly (2026), *Match Camera Motion to Reference Video*. **Locator:** Reference requirements; first/last frames; advanced settings  
- **[S060]** Adobe Firefly (2026), *Generate Videos Using Text Prompts and Images*. **Locator:** Camera, composition, motion, first/last frame, output settings
