---
id: cpcs.found.invariant.epistemic_firewall
kind: doctrine
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §27, §8.3, §20.1, §20.2, §20.3, §20.4, SRC-002 §8, L2.§44, SRC-004 §14]
primary_route: cpcs/knowledge/00_foundations/invariants/
secondary_routes:
  - cpcs/knowledge/00_foundations/epistemic_classes/
  - cpcs/knowledge/09_force_physics/
  - cpcs/knowledge/04_character_performance/facs/
interfaces: [state_x_continuity, motion_x_physics]
---

# Epistemic Firewall Doctrine

## Definition

The governing invariant of the CPCS kernel:

> **Never allow a descriptive concept to masquerade as a measured physical
> quantity, and never allow a provider prompt phrase to masquerade as
> canonical control.**

## Prohibited collapses (each is a firewall violation)

- `effort=strong` is not `force=500N`
- `impact=dramatic` is not a value for `impulse`
- `heavy_style` is not `mass=...kg`
- `AU12 = happiness` — FACS describes visible facial movement; emotion
  interpretation belongs to a different semantic layer
  (`FACS AU → facial movement evidence → optional interpretation`)
- Laban/BESS labels substituted for position, orientation, velocity,
  acceleration, phase timing, or contact state
- Operational qualitative-to-numeric collapses (SRC-002 L2.§44):
  `Time=Sudden ≠ entire_clip_is_fast`; `Weight=Strong ≠ maximum_force`;
  `Flow=Bound ≠ frozen`; `Bartenieff Cross-Lateral ≠ confidence`.
  Localize each quality to its action phase, never globalize it.
- A natural-language prompt treated as deterministic control — provider
  prompts are a projection surface; critical controls must be verified on
  generated output even when documented

## Expressive qualities stay expressive

`heavy`, `powerful`, `violent`, `soft`, `explosive` are expressive/directorial
qualities unless tied to a physical measurement or an explicit physical model.
Effort qualities (`weight/time/space/flow`) are carried separately from force,
whose status is declared (`unknown`/`estimated`/`measured`).

## Structured-output caution (SRC-004 §14)

Parse validity ≠ schema validity ≠ decision correctness ≠ render success.

```text
parse_validity
  ≠ schema_validity
  ≠ decision_correctness
  ≠ render_success
```

A model can produce perfectly valid JSON and still select a candidate that
violates a hard invariant. Each level must be reported separately. Do not let
output format validity masquerade as semantic correctness.

## Verification

Any object that promotes a qualitative label to a numeric physical quantity
without a declared measurement source, model, or labeled PROJECT_DERIVED
transform is a schema violation. Any object that conflates parse validity,
schema validity, decision correctness, or render success is also a violation.
