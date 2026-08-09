---
id: cpcs.strategy.observability_conditioned_selection
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§28]
primary_route: cpcs/runtime/05_strategy/constraints/
secondary_routes:
  - cpcs/runtime/07_compiler/salience_budgeting/
interfaces: []
---

# Observability-Conditioned Control Selection

A semantic control can remain canonical intent even when it is not worth
sending to a provider because the shot cannot meaningfully display it.
Distinguish:

```text
semantic relevance · visual observability · compilation value
```

## Shot-scale guidance (CPCS heuristic; needs provider experiments)

| Shot | High-value controls | Lower-value controls |
|---|---|---|
| ECU | FACS, gaze, eyelid/eye behavior | full-body connectivity |
| CU | FACS, gaze, head orientation | distal locomotor details |
| Medium | gaze, posture, Effort, Shape | tiny AU asymmetries |
| Full body | Laban, Bartenieff, support, trajectory | micro-FACS |
| Wide | spacing, trajectory, major Shape, rhythm | facial AU detail |
| Extreme wide | actor relationships, path, major action | most micro-expression |

The canonical intent is **not deleted** when a control is suppressed:

```yaml
projection_decision:
  control: facs.au12
  semantic_status: required
  observability: low
  provider_projection: suppressed
  loss_type: low_observability
  verification: not_applicable
```

## Verification

`test_low_observability_control_can_be_suppressed`.
