---
id: cpcs.laban.proxy_measurement_contract
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 §11, §12, §48, SRC-002-U09, SRC-002-U10]
primary_route: cpcs/knowledge/06_body_motion/laban_bess/
secondary_routes:
  - cpcs/observation/pose/
  - cpcs/research/numerical/calibration/
interfaces: [style_x_motion]
---

# Laban Proxy Measurement Contract

## Architecture

```text
LMA semantic control → optional measurable proxy → video/mocap measurement
    → calibration/validation
```

Never: `kinematic feature = Laban truth`.

## Candidate proxies (SRC-002 §11)

| Effort factor | Candidate kinematic proxies |
|---|---|
| Space (direct/indirect) | `path_straightness = straight_line_distance(start,end)/path_length` |
| Time (sustained/sudden) | acceleration/deceleration profile · duration · peak velocity · time-to-peak · velocity concentration |
| Weight (strong/light) | acceleration · estimated interaction force (if instrumented) · momentum change · amplitude×temporal profile |
| Flow (bound/free) | movement interruption · trajectory smoothness · endpoint constraints · jerk · repeated correction |
| Shape | normalized body-keypoint geometry: torso width/height · limb spread · center-to-distal distances · body envelope area |
| Phrasing | velocity/acceleration peaks · energy distribution across phrase thirds · onset-to-apex ratio · repetition intervals |

## Numeric policy (SRC-002 §12)

Optional numeric fields must be typed as proxies, never bare:

```json
{
  "proxy": {
    "name": "path_straightness",
    "value": 0.72,
    "unit": "ratio",
    "basis": "kinematic_proxy",
    "validation_status": "uncalibrated"
  }
}
```

`{ "directness": 0.72 }` is **forbidden** unless a project-specific
calibration has explicitly established that mapping. 2D/3D video alone cannot
directly recover physical effort.

## Three representations (SRC-002 §48)

```text
1. semantic LMA value   2. ordinal/project encoding   3. physical measurement proxy
```

These must never be silently substituted for one another.
