---
id: cpcs.canonical.generative_realization_layer
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§21, §22]
primary_route: cpcs/runtime/06_canonical/control_registry/
secondary_routes:
  - cpcs/runtime/07_compiler/semantic_mapping/
interfaces: []
---

# Generative Realization Layer

Research concepts are not necessarily the language a video generator
understands. An intermediate representation sits between framework semantic
controls and provider syntax:

```text
framework semantic control → observable/generative realization → provider projection
```

This is a **compiler-facing operational representation**, not a replacement
ontology for FACS/Laban/Bartenieff.

## RealizationPrimitive (L2.§21.2)

```yaml
realization_primitive:
  id: realization.decisive_weight_commitment
  source_controls: [laban.effort.weight.strong]
  action_classes: [strike, push, pull]
  observable_targets: [visible_weight_commitment, decisive_acceleration, grounded_support]
  not_guaranteed: [exact_force_measurement, exact_laban_coder_score]
  evidence_class: cpcs_proposed
  verification: [support_stability, trajectory_commitment, action_adherence]
```

## Action-conditioned mapping (L2.§22)

A qualitative control does not have one universal visible manifestation:
`semantic control × action × body scope × temporal phase × scene context →
candidate realization`. Generic mappings are insufficient; maintain an
evidence-status matrix (`proposed/verify` vs `source-supported`) and a
minimal-pair requirement (one semantic variable changed, expected visible
difference) as a regression fixture.
