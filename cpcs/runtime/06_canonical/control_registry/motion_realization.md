---
id: cpcs.mx.motion_realization
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §19, §20, §21]
primary_route: cpcs/runtime/06_canonical/control_registry/
secondary_routes:
  - cpcs/knowledge/06_body_motion/
interfaces: [cpcs.canonical.generative_realization_layer, cpcs.mx.action_template]
---

# MotionRealization

A semantic request such as `heavy` is not itself executable motion.
MotionRealization converts semantic controls into observable targets.

## Canonical structure

```json
{
  "motion_realization": {
    "semantic_control": "heavy",
    "action_class": "strike",
    "observable_targets": [
      "grounded_preparation",
      "visible_weight_transfer",
      "proximal_to_distal_acceleration",
      "sharp_contact_accent",
      "recoil",
      "deliberate_recovery"
    ],
    "does_not_require": ["exact_force_value"],
    "evidence_status": "candidate_action_conditioned_mapping"
  }
}
```

The critical point: `heavy × strike` is not the same realization as
`heavy × landing` or `heavy × walk`.

## Action-conditioned realization

```text
semantic_control × action_class × body_scope × phase × environment → realization
```

Examples:

```text
heavy × strike     → grounded preparation + sharp transfer + recoil
heavy × landing     → increased pre-contact preparation + strong absorption + settling
heavy × walk        → greater support commitment + reduced lightness + deliberate transfer
light × gesture     → reduced amplitude + quick recovery + low visible effort
```

These should be research-backed mappings or explicitly marked hypotheses. Do
not encode them as universal biomechanical laws.

## Observable vs hidden mechanics

A provider generally cannot reproduce exact torque, COP trajectory, or joint
moment from prose. It can potentially reproduce visible weight transfer, clear
preparation, abrupt contact accent, visible recoil, deliberate settling.

Therefore realization should have:

```text
observable_targets
mechanical_targets
optional_internal_targets
```

and should never require an unobservable internal value when an observable
proxy is available.

## Verification

`test_observable_targets_present`,
`test_realization_action_conditioned`,
`test_no_unobservable_required`.
