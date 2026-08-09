---
id: cpcs.mx.verification_layers
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §98, §99, SRC-004 §3.4, §16]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/verification/semantic/
interfaces: [cpcs.verification.verification_contract]
---

# Verification Layers: Perceptual vs Geometric and Invariant vs Preference

A trajectory can be geometrically accurate but visually wrong. Use at least:

## Verification dimensions

```text
geometric_verification · temporal_verification · interaction_verification ·
continuity_verification · perceptual_verification · semantic_verification
```

Example: hand reached mathematically correct point BUT motion looked hesitant.
This is not a geometry failure — it is a perceptual verification failure.

## Invariant vs preference

Some checks should be hard:

```text
identity preserved · no impossible penetration · required contact occurs · side preserved
```

Others are preferences:

```text
graceful · natural · dramatic · fluid · stylized
```

Do not let aesthetic preference failures invalidate a physically valid action
unless explicitly requested.

## Four-level verification separation (SRC-004 §3.4)

```text
structural → schema validity (JSON Schema)
semantic    → graph/domain rules
perceptual  → metrics/human review
empirical   → controlled render comparison
```

A schema-valid decision can still be semantically wrong. A semantically valid
decision can still render incorrectly. Report each level separately.

## ADRG planner metrics (SRC-004 §16.1)

The verification plane also measures the reasoning layer:
`evidence_selection_precision`, `evidence_resolution`,
`decision_trace_faithfulness`, `constraint_preservation`,
`alternative_diversity`, `unnecessary_branching`, `strategy_stability`,
`token_cost`, `decision_latency`, `repair_efficiency`, `regression_rate`,
`compile_loss_severity`.

See `cpcs.adrg.verification_metrics` for full definitions.

## Verification

`test_verification_layer_identified_on_failure`,
`test_invariant_checked_hard`,
`test_preference_checked_soft`,
`test_four_level_verification_reported_separately`.

## CPCS-MX verification metric vectors (SRC-005 §27)

SRC-005 defines metric vectors that never collapse all quality into one
unexplained score. Each vector measures a specific verification dimension:

| Vector | Metrics |
| --- | --- |
| Clock/event | event time error, interval start/end/duration, partial-order violation count |
| Root/joint | positional trajectory error, facing/yaw error, speed profile, path curvature, geodesic rotation distance |
| Contact/support | foot slip during planted contact, vertical penetration, orientation drift, support-polygon relation |
| Smoothness (phase-labeled) | jerk within preparation, execution, contact, recovery — impact discontinuity is not a failure |
| Dynamics | residual forces, GRF consistency, momentum change, COM behavior, energy balance |
| Laban/performance | proxy features (acceleration onset for Time, path straightness for Space, impulse for Weight) with declared `proxy_profile_id` |
| Face/gaze/breath | AU onset/apex/offset, gaze-target agreement, blink timing, breath-audio alignment |
| Perceptual/cinematic | silhouette separation, contact readability, screen-direction continuity, impact-frame detectability |

Error is localized to a layer: e.g., "semantic action correct; contact 3
frames late" or "body motion correct; camera reverses screen direction." This
diagnosis determines whether to revise text, a trajectory, an IK constraint, a
style transform, or presentation.
