---
id: cpcs.compiler.control_priority_attention_budget
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§29, SRC-004 §7]
primary_route: cpcs/runtime/07_compiler/salience_budgeting/
secondary_routes:
  - cpcs/runtime/05_strategy/locks/
interfaces: []
---

# Control Priority and Attention Budget

Canonical richness vs provider bandwidth: the semantic model may contain many
constraints; the provider prompt should not necessarily contain all of them.

## Compiler flow

```text
canonical intent → salience ranking → provider capability filtering
    → attention budget → minimal sufficient projection
```

## Priority classes (engineering vocabulary, not FACS/Laban terms)

```text
locked · required · high · medium · low · optional
```

`locked` constraints (identity, actor_count, action_order, contact,
spatial_relationship) must survive the attention budget.

## Attention budget

```text
canonical controls: 31
provider-safe controls: 12
projected controls: 8
suppressed controls: 23
```

## Decision-aware routing features (SRC-004 §7)

The attention budget at the compiler level receives routing signals from the
decision layer above. Five features flow into the budget:

```text
impact          — effect on audience meaning or hard compliance
uncertainty     — unresolved uncertainty after retrieval
coupling        — cross-domain dependencies
irreversibility — cost of choosing incorrectly
validator_strength — availability of deterministic verification
```

These are proposed operational variables, not universal scientific scales. They
connect decision-aware routing (`cpcs.adrg.decision_aware_routing`) to the
existing attention budget. High-impact decisions get more attention budget;
low-impact decisions get less.

Suppression must produce a reason code: `low_observability ·
provider_unsupported · redundant · conflicting · lower_priority ·
already_encoded_by_stronger_control · token_budget`.

## Verification

`test_locked_constraint_survives_attention_budget`,
`test_routing_features_flow_into_budget`.
