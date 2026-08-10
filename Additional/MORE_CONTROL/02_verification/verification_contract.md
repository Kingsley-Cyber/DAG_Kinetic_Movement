---
id: cpcs.verification.semantic.verification_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §17, §26, SRC-002 §24]
primary_route: cpcs/verification/semantic/
secondary_routes:
  - cpcs/verification/
interfaces: [state_x_continuity, motion_x_physics]
---

# Verification Contract (SRC-001 §17)

Consolidated verification obligations. Every layer below is additive:
canonical validation is mandatory for every resolved object; domain metric
lists apply where measurement is available.

## 17.1 Canonical validation (mandatory, every resolved JSON object)

```text
schema_valid
units_valid
frame_valid
time_valid
identity_valid
evidence_class_valid
provenance_present
side_semantics_valid
```

## 17.2 Motion verification (observed/generated video, where measurable)

```text
trajectory_error
direction_error
speed_error
peak_timing_error
phase_boundary_error
contact_timing_error
left_right_error
identity_switch_rate
```

## 17.3 Camera verification

```text
camera_direction_accuracy
camera_motion_class_accuracy
framing_error
subject_tracking_error
focus_target_error
optical_control_adherence
```

## 17.4 Interaction verification

```text
contact_precision
contact_recall
contact_timing_error
near_miss_false_positive_rate
object_transfer_accuracy
reaction_order_accuracy
```

## 17.5 Style verification (measurable proxies)

```text
style_invariant_violation_rate
forbidden_drift_rate
motion_style_adherence
camera_style_adherence
visual_style_adherence
```

## FACS verification (SRC-002 §24)

```text
AU ID valid for declared version
intensity enum valid
left/right preserved
bilateral not silently averaged
temporal order valid
offset >= onset
apex inside onset/offset
unobservable state accepted
confidence range valid
```
AU-detection metrics: precision · recall · F1 · per-AU support · macro/micro
averages · calibration error. Intensity: ICC · MAE · rank correlation ·
per-AU error. Temporal: onset/apex/offset error · temporal IoU ·
tolerance-window agreement. Bilateral: left/right accuracy · bilateral
agreement · asymmetry preservation. Avoid a single F1-binary for highly
imbalanced AU detection.

## Laban / Bartenieff / Affect verification (SRC-002 §24)

Laban: effort-factor enums valid · `proxy != semantic field` · unvalidated
proxy cannot become canonical · coordinate frame declared for direction.
Bartenieff: pattern enum valid · side preserved · connectivity interval
valid · measurement basis explicit. Affect: `affect_target != observed_emotion`
· private mental state rejected unless explicitly authored/hypothesized ·
valence/arousal scale declared · trajectory timestamps monotonic.

## Hard rule

> Do not use one LLM-judge score as the sole verification mechanism.

## Extended metric list (SRC-001 §26 build packet)

Adds continuity/causality metrics beyond §17:
`actor_count_consistency · existence_continuity · trajectory_continuity ·
wardrobe_continuity · prop_continuity · occlusion_transition_error ·
causal_edge_preservation · causal_false_positive_rate ·
forbidden_event_rate · compilation_loss_rate · measured_vs_target_error`.

## Test inventory (SRC-001 §26)

25 named tests — see ledger
`research/distillation/ledger/01_ai_video_motion_direction_kb_gap_closure.md`
for the full list; three govern the compiler directly:
`test_unsupported_required_control_fails_closed`,
`test_approximate_control_creates_loss_record`,
`test_native_control_has_no_false_loss`.
