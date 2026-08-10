---
id: cpcs.adrg.measurement_form
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §17]
primary_route: cpcs/verification/
secondary_routes:
  - cpcs/observation/
  - cpcs/runtime/07_compiler/semantic_mapping/
interfaces: [cpcs.verification.verification_contract, cpcs.observation.observation_provenance]
---

# Measurement Form

For every measurable control, the following 14 fields must be declared
(SRC-004 §17). Do not turn semantic labels into fake measurements —
"controlled performance" is an interpretation/creative target, not a directly
measured physical quantity.

```text
what:          exact phenomenon
source:        measured / detected / observed / inferred
timebase:      seconds / frames / presentation timestamp / sample timestamp
sampling:      Hz or frame rate
coordinates:   declared frame/world/camera coordinates
normalization: raw / normalized / calibrated
side:          left / right / bilateral / side-indexed event
confidence:    [0,1] operational confidence
tolerance:     explicit error threshold
missing:       unknown / unobservable / unavailable
occlusion:     flag + confidence degradation
camera_contamination: flag if measurement is camera-motion dependent
aggregation:   min/max/mean/median/percentile/event rule
provenance:    source ID + digest
```

## Relationship to evidence model

The `source` field maps directly to the acquisition class in
`evidence_two_axis_model` (measured/detected/observed/inferred). The
`confidence` field maps to the epistemic state. The `provenance` field carries
source ID + digest for auditability.

## Boundary

Qualitative directorial terms (`controlled`, `dramatic`, `fluid`) are creative
targets, not physical measurements. They must not appear in the `what` field
as if they were directly measurable phenomena.

## Verification

`test_measurement_has_source_class`,
`test_qualitative_label_not_in_what_field`,
`test_provenance_present_for_all_measurements`.
