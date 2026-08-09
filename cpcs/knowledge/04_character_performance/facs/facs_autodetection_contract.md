---
id: cpcs.facs.autodetection_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §6, §47, SRC-002-U05, SRC-002-U06, SRC-002-U07]
primary_route: cpcs/knowledge/04_character_performance/facs/
secondary_routes:
  - cpcs/observation/pose/
  - cpcs/knowledge/00_foundations/uncertainty/
interfaces: []
---

# FACS Automatic-Detection Contract

Automatic AU detection is **evidence-producing, not authority-producing**.
OpenFace (U05) documents AU presence/intensity frame-by-frame but supports
only a subset, warns that presence and intensity models are **separately
trained and may disagree**, and that multi-face calibration differs from
single-face conditions.

## Detector observation object

```json
{
  "type": "facs_detection",
  "au_id": "AU12",
  "presence": 1,
  "intensity_proxy": 3.42,
  "model": "example_model",
  "model_version": "x.y",
  "confidence": 0.91,
  "frame_index": 42,
  "timestamp_s": 1.40,
  "evidence_class": "detected"
}
```

## Promotion rule

The observation must **not** be silently promoted to `evidence_class: measured`
unless the detector has been validated against the target measurement protocol.
Recommended machine states:

```text
detected   = algorithm produced a signal
measured   = signal has a defined measurement contract + calibration/validation
unknown    = system lacks sufficient evidence
unobservable = phenomenon cannot be recovered from available media
```

## Coder-equivalence boundary

```yaml
facs_observation:
  au_id: AU12
  presence: { value: true, basis: detected }
  intensity: { value: 3.2, basis: model_score }
  coder_equivalence: { status: not_established }
  calibration: { status: unknown }
```

Detector output may be useful for verification **without** being promoted to
ground-truth FACS annotation.

## Verification

`test_detector_output_not_promoted_to_measured`.
