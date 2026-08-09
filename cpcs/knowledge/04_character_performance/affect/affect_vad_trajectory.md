---
id: cpcs.affect.vad_trajectory
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §9, SRC-002-U08]
primary_route: cpcs/knowledge/04_character_performance/affect/
secondary_routes:
  - cpcs/knowledge/04_character_performance/facs/
interfaces: []
---

# Affect (VAD) Is a Separate Semantic Layer

Affect is modeled **separately from FACS**. Russell's circumplex model (U08)
supports valence/pleasure and arousal/activation as dimensions of affect;
continuous-affect research shows valence/arousal can be modeled over time.
This does **not** establish that FACS AUs uniquely determine an individual's
private affect.

## Canonical affect_target

```json
{
  "type": "affect_target",
  "dimensions": {
    "valence":  { "value": 0.35, "scale": "project_normalized", "basis": "authored" },
    "arousal":  { "value": 0.20, "scale": "project_normalized", "basis": "authored" }
  },
  "temporal": { "kind": "trajectory" }
}
```

## Trajectory

```json
{
  "trajectory": [
    { "t": 0.0, "valence": 0.10, "arousal": 0.15 },
    { "t": 1.0, "valence": 0.25, "arousal": 0.20 },
    { "t": 2.0, "valence": 0.40, "arousal": 0.35 }
  ]
}
```

The numeric scale is **project-defined** unless a source explicitly specifies
a scale. `affect_target != observed_emotion`; private mental state is rejected
unless explicitly authored/hypothesized.

## Verification

`test_affect_not_inferred_from_au`; trajectory timestamps must be monotonic.
