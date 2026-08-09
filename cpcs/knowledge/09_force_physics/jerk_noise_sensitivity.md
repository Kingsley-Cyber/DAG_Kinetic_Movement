---
id: cpcs.physics.jerk.noise_sensitivity
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §8.4, §1.2, §24-P2.2]
primary_route: cpcs/knowledge/09_force_physics/
secondary_routes:
  - cpcs/knowledge/06_body_motion/kinematics/
interfaces: [motion_x_physics]
---

# Jerk Noise Sensitivity

## Principle

Jerk (third temporal derivative of position) is mathematically derivable, but
numerical differentiation amplifies pose noise dramatically. It must be
treated as a low-confidence derived quantity, not a high-confidence primitive:

```json
{
  "jerk": {
    "status": "derived",
    "method": "smoothed_finite_difference",
    "confidence": 0.54
  }
}
```

## Evidence status

- Mathematical/kinematic concept — well-defined.
- 2026 video inverse-dynamics literature (per SRC-001 §1.2/§8.4): pose noise
  is strongly amplified when differentiating toward physical quantities.
- Confidence in the source's own evidence ledger: medium.

## CPCS status

Experimental/optional. Using jerk as a high-value control is a **P2
experiment** — do not promote it to a canonical control before benchmarking.

## Applies when

Any third-derivative quantity is computed from detected/derived pose data.

## Failure mode

Raw finite-difference jerk from noisy trackers produces dominated-by-noise
values that look precise but carry no signal.
