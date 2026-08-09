---
id: cpcs.canonical.control_scope
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§23]
primary_route: cpcs/runtime/06_canonical/field_policies/
secondary_routes:
  - cpcs/runtime/05_strategy/constraints/
interfaces: []
---

# Control Scope (Mandatory)

A control without scope is ambiguous — the same `bound` value could mean the
whole performance, one actor, an upper body, a single gesture, or an
anticipation phase.

## Canonical scope object

```json
{
  "scope": {
    "scene": "scene_07",
    "shot": "shot_03",
    "actor": "actor_A",
    "interaction": "interaction_02",
    "action": "counter",
    "body_region": "right_arm",
    "phase": "preparation"
  }
}
```

All unspecified dimensions inherit from the enclosing execution context rather
than becoming implicit global controls.

## Inheritance precedence (CPCS policy)

```text
explicit local scope > event scope > shot scope > scene scope > project default
```

If two controls conflict at the same scope and priority, the director must
resolve explicitly or mark it unresolved.

## Verification

`test_scope_does_not_leak` — a local control must not globalize.
