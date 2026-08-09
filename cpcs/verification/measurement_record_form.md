---
id: cpcs.verification.measurement_record_form
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §5, §11.1]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.found.evidence_two_axis_model
  - cpcs.runtime.failure_repair_contract
  - cpcs.found.exactness_taxonomy
  - cpcs.verification.verification_layers
---

# Universal Measurement Record

> **Source:** SRC-006 §5 — "Measurement form"

## Principle

Measurement records must not hide a semantic judgment behind a numeric
field. A VLM saying "the action looks correct" is `interpreted` or
`detected`, not a physical measurement.

## Record fields (19)

```text
metric_id and metric_version · target_ref / canonical_path
what_is_measured · measurement_source · sample_source and sampling_rate
video_timebase_id · presentation timestamp vs sample timestamp
coordinate_frame_id · normalization · laterality handling · units
confidence/calibration reference · error or tolerance
missing-data behavior · occlusion behavior
camera-motion compensation · aggregation rule · derived metrics
origin_class · provenance
```

## Video-target metrics

| Metric | Status | Key rule |
| --- | --- | --- |
| `required_element_recall` | measurable with detector calibration | unobservable elements excluded only with reason |
| `unexpected_element_rate` | partly detected/interpreted | unknown if detector lacks class coverage |
| `temporal_order_accuracy` | measurable after event detection | overlapping uncertain intervals yield `inconclusive` |
| `interval_iou` | measurable | requires same timebase |
| `contact_time_error` | measurable where contact visible | occluded contact is unobservable; no undeclared interpolation |
| `spatial_relation_accuracy` | measurable with uncertainty | camera compensation only with valid transform |
| `identity_switch_rate` | measurable but detector-dependent | occlusion handled by tracker confidence and re-ID policy |
| `attribute_binding_accuracy` | detected/interpreted | unknown when entity or attribute unobservable |
| `action_binding_accuracy` | detected/interpreted | actor occlusion yields unknown, not automatic fail |
| `camera_trajectory_error` | measurable only in suitable scenes | invalid without recoverable geometry/scale |
| `camera_semantic_adherence` | detected/interpreted | never reported as pose error |
| `audio_sync_offset` | measurable | unknown if onset cannot be localized |
| `physical_commonsense` | interpreted; human preferred | separate from caption adherence |
| `semantic_adherence` | interpreted/detected | preserve evaluator confidence and coverage |

## Reasoning-process metrics

schema validity · hard-constraint pass/fail · semantic field preservation ·
temporal/spatial/causal correctness · binding and identity correctness ·
compilation loss · branch materiality/deduplication · patch scope and
repair regression · verifier calibration/human agreement · full resource
cost.

## Boundary

`unknown` (value not known), `unobservable` (no observation path exists),
absent, and explicit `null` remain distinct states. Measurement records
live in the VOG/evaluation layer; they never overwrite canonical authored
intent.

## Target/observation join contract (SRC-007 G011–G013)

Evaluator inputs: target canonical record, observed VOG, measured tracks,
semantic observations, human review. Outputs: metric, score, confidence,
evidence locator, failure class.

The join contract defines how target actor, object, event, interval, side,
coordinate frame, and field IDs match VOG tracks and measurements. Four
confidence layers are kept separate: detector confidence, measurement
uncertainty, semantic interpretation confidence, and final metric
confidence.

Every metric specifies: target field paths, observed inputs, alignment,
camera/body disentanglement, formula, unit, tolerance provenance,
missing/occluded behavior, aggregation, decision threshold, failure class,
and repairable owner. Required exemplars: one valid 2D metric, one requiring
calibrated 3D, one semantic human-review metric, and one that must return
`unobservable`. The evaluator result causes acceptance or a minimal repair —
it never rewrites the target.

`test_join_contract_matches_target_to_observation`,
`test_four_confidence_layers_kept_separate`,
`test_metric_specification_complete`,
`test_unobservable_metric_returns_unobservable`.
