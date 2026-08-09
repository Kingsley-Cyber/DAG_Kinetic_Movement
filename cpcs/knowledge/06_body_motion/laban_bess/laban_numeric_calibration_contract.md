---
id: cpcs.laban.numeric_calibration_contract
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 §12, SRC-002-U09, SRC-002-U10]
primary_route: cpcs/knowledge/06_body_motion/laban_bess/
secondary_routes:
  - cpcs/research/numerical/calibration/
interfaces: []
---

# Laban Numeric Calibration Contract

Laban semantics are **categorical/qualitative by default**. Numeric fields are
optional and must always be typed as proxies (see
`laban_proxy_measurement_contract.md`).

## Promotion ladder

```text
uncalibrated_proxy  →  validated_proxy
```

A proxy may be promoted to `validated_proxy` **only after**:

1. CMA-coded reference data exists
2. independent motion measurements are extracted
3. mapping is trained/fitted
4. held-out agreement is reported
5. cross-subject performance is measured
6. failure cases are documented

## No universal numeric conversion

No evidence supports a universal numeric conversion from Laban qualitative
elements to `[0,1]` (SRC-002 §1.6, §48). Quantitative analysis does not
automatically transform qualitative LMA categories into universal physical
measurements.

## Verification

`test_laban_proxy_not_semantic`,
`test_unvalidated_proxy_not_compiled_as_exact`.

## Combat float encoding as typed proxies (SRC-010 EXTEND)

The lab's combat reference uses Laban floats for authoring: weight / time /
space ∈ [0, 1], flow ∈ [−1, 1], with 9 named Effort float signatures (e.g.,
punch = strong/fast/direct + bound flow). This is consistent with the
"no universal numeric conversion" rule: these floats are **typed proxies for
authoring**, not universal measurements.

Empirical status: v005's `lab_control` effort vectors were rendered and
proved as a working control channel for combat (5/5/5, JSON alone). The
proxies therefore sit at the top of the promotion ladder's evidence scale
among proxies — render-validated as a control channel — but remain proxies:
they never become `validated_proxy` without the 6-step calibration (CMA-coded
reference data, independent measurements, fitted mapping, held-out agreement,
cross-subject performance, documented failures).
