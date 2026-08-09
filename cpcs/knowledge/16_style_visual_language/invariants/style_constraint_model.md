---
id: cpcs.style.constraint_model
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §1.2, §11, §24-P2.7]
primary_route: cpcs/knowledge/16_style_visual_language/invariants/
secondary_routes:
  - cpcs/knowledge/16_style_visual_language/allowed_variation/
  - cpcs/knowledge/16_style_visual_language/forbidden_drift/
interfaces: [style_x_motion, style_x_camera, style_x_editing]
---

# Style Constraint Model

## Principle

A style label is not a sufficient executable specification. CPCS separates
seven style domains — visual · motion · camera · editing · performance ·
audio · narrative — and each carries:

```text
invariants · allowed_variation · forbidden_drift · priority · evidence/provenance
```

(This is a CPCS representation proposal, not an externally standardized
ontology.)

Canonical shape (condensed):

```json
{
  "style": {
    "id": "documentary_observation",
    "domains": {
      "visual": {
        "invariants": ["naturalistic_materials"],
        "allowed_variation": ["natural_lighting_variation"],
        "forbidden_drift": ["anime_face_geometry", "plastic_skin"]
      }
    },
    "priority": 0.9,
    "evidence_class": "authored"
  }
}
```

## Labels are routing hints, not constraints

`anime`, `watercolor`, `documentary`, `UGC`, `sakuga` are high-level
descriptors — useful routing hints, not executable constraints. Compile
labels into observable/operational dimensions only when evidence exists.

Example decomposition (source §11.2):

```text
UGC → performance: direct_to_camera · camera: handheld_or_phone_locked
    · framing: close/medium · editing: high_temporal_variability
    · visual: consumer_device_character
```

Only fields supported by research or an authored profile may be emitted.
**Do not invent a universal mapping for every style label** — automatic
style-label decomposition is a P2 experiment.

## Failure modes

- Single-label style strings collapse domains (style drift untraceable).
- Invented label→field mappings overclaim beyond evidence.

## Verification

`style_invariant_violation_rate`, `forbidden_drift_rate`, per-domain
adherence metrics (see `verification/semantic/verification_contract.md`).
