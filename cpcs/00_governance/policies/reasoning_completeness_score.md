---
id: cpcs.gov.reasoning_completeness_score
kind: metric_contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§50, §57]
primary_route: cpcs/00_governance/policies/
secondary_routes:
  - cpcs/research/coverage/
interfaces: []
---

# Reasoning Completeness Score (RCS)

A concept-level closure score for internal auditing:

```text
RCS = semantic + applicability + contraindication + scope + temporal
    + interaction + realization + compiler + verification
```

Each dimension scored: `0 = absent · 1 = proposed · 2 = evidence-supported/experimentally validated`.

## Example

```yaml
reasoning_completeness:
  semantic: 2
  applicability: 2
  contraindication: 2
  scope: 1
  temporal: 2
  interaction: 1
  realization: 1
  compiler: 2
  verification: 1
  status: partial
```

## Rules

- Do **not** interpret RCS as a scientific score — it is a CPCS engineering completeness index.
- A concept must not be marked `reasoning_complete` merely because its semantic definition scores 2.

## Closure criteria (SRC-002 L2.§57)

Six closure groups: semantic · application · composition · realization ·
compiler · verification. Each has a checklist that must be satisfied before
the FACS/Laban/Bartenieff package is declared fully closed (frozen-package
reconciliation still pending).
