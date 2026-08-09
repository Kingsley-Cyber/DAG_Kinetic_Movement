---
id: cpcs.adrg.verification_metrics
kind: metric_contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §16]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/runtime/07_compiler/
interfaces: [cpcs.verification.verification_contract, cpcs.verification.verification_layers, cpcs.adrg.decision_record]
---

# Verification Metrics: Planner and Video

## Planner metrics (§16.1)

| Metric | Definition |
| --- | --- |
| evidence_selection_precision | Relevant selected evidence / selected evidence |
| evidence_resolution | Cited evidence IDs that resolve |
| decision_trace_faithfulness | Decision record matches actual selected candidate and compiler result |
| constraint_preservation | Hard invariants retained after compilation |
| alternative_diversity | Meaningful typed semantic delta between candidates |
| unnecessary_branching | Branches that produce no meaningful semantic delta |
| strategy_stability | Same fixed inputs produce same decision under deterministic policy |
| token_cost | Input + output inference cost |
| decision_latency | Planner wall-clock latency |
| repair_efficiency | Successful repairs / repair attempts |
| regression_rate | Previously passing fixtures that fail after change |
| compile_loss_severity | Weighted loss introduced by target adapter |

## Video metrics (§16.2)

Use existing CPCS metrics plus:

```text
action_order
action_count
beat_timing_error
contact_timing_error
identity_consistency
camera_adherence
facial/gaze_event_visibility
product_visibility
continuity
variant_diversity
audience-meaning_judgment
```

## Relationship to existing verification

The existing `verification_contract` and `verification_layers` cards define
verification dimensions (geometric/temporal/interaction/continuity/perceptual/
semantic). The planner metrics above measure the *reasoning layer's* quality;
the video metrics measure the *render output*. Both feed the same verification
plane but at different levels.

## Verification

`test_evidence_selection_precision_measured`,
`test_constraint_preservation_after_compilation`,
`test_compile_loss_severity_recorded`,
`test_regression_rate_tracked`.
