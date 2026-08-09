---
id: cpcs.motion.kinematics.measurement_contract
kind: method
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §7]
primary_route: cpcs/knowledge/06_body_motion/kinematics/
secondary_routes:
  - cpcs/knowledge/00_foundations/measurement_principles/
  - cpcs/knowledge/00_foundations/coordinate_systems/
interfaces: [motion_x_camera]
---

# Kinematic Measurement Contract

## Method

Every measured/derived kinematic quantity must carry:

```text
source · timestamp/timebase · sampling rate · coordinate frame · units ·
method · confidence · uncertainty/error (where available) ·
missing-data state · occlusion state · camera-motion compensation state
```

## Canonical measurement object

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
    "error": { "type": "estimated", "value": 0.12, "unit": "m/s" },
    "missing_data_behavior": "unknown"
  }
}
```

## Camera-motion contamination

For image-derived motion, `world`, `camera`, and `actor_local` must never be
conflated. A person can appear to move in image coordinates while stationary
in world coordinates because the camera moves. Therefore
`{position: camera, camera_motion_compensated: false}` is materially
different from `{position: world, camera_motion_compensated: true}` and the
difference must be explicit on every image-derived quantity.

## Applies when

Any observation-pipeline quantity enters the Video Observation Graph or is
used to validate generated video.

## Failure modes

- Apparent-motion false positives from uncompensated camera movement.
- Missing timebase/sampling metadata makes temporal error bounds uncomputable.

## Verification

Schema validation of the required field list; frame + compensation state
checked on every image-derived quantity.
