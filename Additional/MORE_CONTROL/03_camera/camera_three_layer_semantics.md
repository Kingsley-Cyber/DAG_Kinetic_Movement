---
id: cpcs.camera.three_layer_semantics
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §10'.1–§10'.4 (camera grammar), §15, SRC-001-U10, SRC-001-U12, SRC-001-U13, SRC-001-U14]
primary_route: cpcs/knowledge/12_camera_image_formation/
secondary_routes:
  - cpcs/knowledge/12_camera_image_formation/lens/
  - cpcs/knowledge/12_camera_image_formation/movement/
interfaces: [motion_x_camera, blocking_x_camera]
---

# Camera: Three Semantic Layers + Calibration Split

## Principle

Camera knowledge must not all be represented as equivalent "camera motion".
Three separate semantic layers:

**Layer 1 — camera motion**: locked/static · pan · tilt · roll · dolly ·
tracking · crane/elevate · orbit/arc · handheld/drift.

**Layer 2 — optical / image formation**: focal length · field of view ·
camera distance · camera height · focus plane · depth of field · aperture ·
rack focus · motion blur/shutter behavior.

**Layer 3 — exposure / color / device**: exposure · white balance · dynamic
range · sensor/device character · color space · lens distortion · chromatic
aberration · stabilization · compression/noise.

The canonical `CameraState` carries `pose · motion · optics · focus ·
image_formation` (schema: `cpcs/schemas/world_model/universal_kernel_family.md`).

## Calibration split (measured video)

Camera calibration distinguishes (U10, authoritative implementation
reference):

- **intrinsics**: focal lengths fx/fy, principal point cx/cy, distortion
- **extrinsics**: camera position and orientation relative to a reference frame

This is the measurement representation — not a universal provider prompt
representation.

## Provider support for a universal camera layer

Provider documentation confirms semantic camera concepts with differing
capabilities — supporting a universal camera semantic layer with provider
adapters rather than provider-specific ontologies:

- Runway (U12): locked, handheld, tracking; subject/scene/camera/style
  separation.
- Veo (U13): shot framing/motion separated from style/lighting/character.
- Kling (U14): explicit camera movement controls + displacement parameters
  (horizontal/vertical, zoom, pan, tilt, roll).

Adapter mapping: `canonical camera motion → provider capability → native
control if available → semantic NL projection if not → unsupported/degraded
if neither is reliable`. Per-provider details in `providers/{runway,veo,kling}/`.

## Applies when

Any camera field is authored, observed, or compiled. Camera is never merely
"shot type".

## Failure modes

- Optical parameters emitted as camera motion.
- Intrinsics conflated with camera pose.
- Assuming documented provider controls are exact without verification.

## Fight camera math (SRC-010 EXTEND)

The lab's combat reference adds 7 numeric fight-camera parameters that map
onto the three layers (motion = Layer 1; optics = Layer 2):

`focal_length_mm` · `angle_deg` · `tracking_speed_match` (camera speed
matches subject speed) · `shake_amplitude_px` · `shake_frequency_hz` (8–15) ·
`shake_decay_frames` · `whip_pan_speed_deg_s` (120–240).

Patterns by beat type: wide establishing for anticipation, tight + shake on
impact, release on recovery. These were exercised in v005/v006 combat canons
and validated by `validate_kinematics.py` (0 failures, v006). They are
authoring controls (Layer 2/3 device character included), not measurement
calibration — the intrinsics/extrinsics split above stays the measurement
representation.
