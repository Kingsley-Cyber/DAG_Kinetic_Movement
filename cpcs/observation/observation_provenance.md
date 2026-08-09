---
id: cpcs.mx.observation_provenance
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §95]
primary_route: cpcs/observation/
secondary_routes:
  - cpcs/knowledge/00_foundations/measurement_principles/
interfaces: [cpcs.found.uncertainty.evidence_two_axis_model]
---

# Observation Provenance

A pose pipeline may perform detection, tracking, smoothing, interpolation, and
derivative computation. These are not one acquisition event.

## Pipeline stages

```text
raw_observation → tracked_observation → filtered_observation → derived_measurement
```

Store the derivation chain explicitly. This makes velocity/acceleration
provenance much stronger.

If velocity is produced by differentiating detected position, then velocity is
not independently "measured":

```json
{
  "velocity": {
    "acquisition": "derived",
    "source_acquisition": "detected",
    "derivation": "central_difference"
  }
}
```

The same applies to: velocity → acceleration → force estimate. Uncertainty
should propagate rather than disappear.

## Uncertainty propagation

```json
{
  "uncertainty": {
    "basis": "propagated",
    "source_refs": ["position_uncertainty_01", "timebase_uncertainty_01"]
  }
}
```

Do not allow a high-confidence position detector to produce a falsely precise
acceleration merely because differentiation returns a number.

## Verification

`test_observation_provenance_chain_present`,
`test_derived_measurement_marked_derived`,
`test_uncertainty_propagated_not_swallowed`.
