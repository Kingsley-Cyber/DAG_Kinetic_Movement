---
id: cpcs.canonical.director_control_ir
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§54]
primary_route: cpcs/runtime/06_canonical/control_registry/
secondary_routes:
  - cpcs/runtime/05_strategy/
interfaces: []
---

# Director Control IR

A compact implementation target — the recommended universal operational
envelope. It does **not** replace the semantic domain objects.

```yaml
director_control:
  intent:
  context:
  controls:
    - { framework:, concept:, value:, scope:, envelope:, priority:, evidence_class: }
  composition: { interactions:, conflicts:, dependencies: }
  realizations:
    - { primitive:, target:, confidence:, basis: }
  continuity:
  observability:
  provider_strategy:
  verification:
```

Every operational control should support, as applicable: `id · framework ·
concept · value · basis · evidence_class · confidence · scope · envelope ·
priority · applicability · contraindications · interactions · realizations ·
observability · persistence · continuity · provider_strategy · verification ·
source_ref`.
