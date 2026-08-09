---
id: cpcs.complexity.feature_vector
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §12, §10.10, §24-P2.1]
primary_route: cpcs/knowledge/19_generation_complexity/
secondary_routes:
  - cpcs/knowledge/19_generation_complexity/partitioning/
interfaces: [state_x_continuity]
---

# Complexity as Feature Vector (Not a Scalar)

## Principle

Complexity is a **heuristic risk estimate**, not an objective universal
score. Keep it as a feature vector per window (e.g. per shot); compiler
behavior is feature-specific:

```json
{
  "complexity": {
    "window": { "start": 0.0, "end": 8.0, "unit": "s" },
    "features": {
      "actor_count": 2, "simultaneous_actions": 3, "contact_count": 2,
      "camera_complexity": 0.7, "physics_complexity": 0.8,
      "style_vfx_complexity": 0.4, "dialogue_density": 0.1,
      "identity_burden": 0.8, "spatial_topology": 0.7,
      "temporal_density": 0.6
    },
    "score": null,
    "calibration_status": "uncalibrated_heuristic"
  }
}
```

Extended by the continuity closure: `occlusion_burden`,
`causal_dependency_density`, `continuity_burden`.

## Feature → failure stress mapping

- high actor count → identity errors
- high contact count → interaction consistency
- high temporal density → phase ordering
- high camera complexity → camera adherence
- high physics complexity → physical plausibility
- high spatial topology → relative positions

## No premature scalar

Introduce a scalar score only after empirical calibration against observed
generation failure rates (targets: identity error, action omission, contact
error, camera error, temporal-order error, spatial-topology error, style
drift). The universal complexity scalar is a **P2 experiment**. Do not invent
calibrated probabilities.

## Failure mode

Routing decisions keyed to an uncalibrated scalar mis-budget generation and
hide which dimension actually failed.
