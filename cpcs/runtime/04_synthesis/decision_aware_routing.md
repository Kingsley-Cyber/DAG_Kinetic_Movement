---
id: cpcs.adrg.decision_aware_routing
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §7]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/07_compiler/salience_budgeting/
interfaces: [cpcs.compiler.salience.control_priority_attention_budget, cpcs.adrg.decision_record]
---

# Decision-Aware Routing

The existing policy layer routes by task complexity/type. ADRG requires routing
based on the properties of the **decision itself** (SRC-004 §7). These are
features of routing, not a replacement policy framework.

## Routing features

```json
{
  "impact": 0.0,
  "uncertainty": 0.0,
  "coupling": 0.0,
  "irreversibility": 0.0,
  "validator_strength": 0.0,
  "budget": {
    "context_tokens": 0,
    "generation_cost": 0,
    "latency_ms": 0
  }
}
```

- **impact** — effect on audience meaning or hard compliance.
- **uncertainty** — unresolved uncertainty after retrieval.
- **coupling** — cross-domain dependencies.
- **irreversibility** — cost of choosing incorrectly.
- **validator_strength** — availability of deterministic verification.

These are proposed operational variables, not universal scientific scales.

## Routing matrix

| Signal | Preferred operator | Reason |
| --- | --- | --- |
| low complexity + strong validator | Direct | No need for search |
| decomposable dependency chain | AoT / least-to-most | Sequential local resolution |
| high impact + independent alternatives | ToT | Compare bounded candidates |
| high coupling | GoT | Aggregate dependent decisions |
| external state/tool needed | ReAct-style tool action | Retrieve/measure/validate externally |
| deterministic computation | CoC/program-aided | Move arithmetic/validation to code |
| ambiguous high-impact decision | Self-consistency | Sample alternatives where rubric exists |
| validator failure | bounded repair | Patch the earliest responsible layer |
| deterministic compiler can decide | no extra reasoning | Avoid unnecessary model calls |

## Critical finding

Critique, self-consistency, and repair do not require new top-level reasoning
frameworks. They should be operators inside the existing policy runtime. The
existing six executors remain; routing selects which to invoke.

## Weighted router and budget ledger (SRC-011 EXTEND)

> **Source:** SRC-011 §10 — "Reasoning router" +
> `examples/reasoning_policy.yaml` (operator_router, 6 rules).

### Routing score

The package provides a weighted router default for operator selection:

\[
D = w_I \cdot I + w_U \cdot U + w_C \cdot C + w_R \cdot R - w_V \cdot V
\]

where \(I\) impact, \(U\) uncertainty, \(C\) coupling, \(R\) irreversibility,
\(V\) validator strength (each 0–1). Weights are defaults, not laws —
consistent with the budget-router doctrine that vectors, not a universal
scalar, are the raw signal; \(D\) ranks operator choice, the budget ledger
records the vector.

### Operator selection (6 rules)

| Condition | Operator |
| --- | --- |
| low_complexity and strong_validator | direct_compile_validate |
| moderate_complexity | least_to_most |
| high_impact and alternatives_independent | selective_tree_of_thoughts |
| high_impact and cross_domain_coupling | graph_of_thoughts_subgraph |
| external_state_required | react_tool_action |
| deterministic_computation_required | program_aided_runtime |

Use the cheapest operator that covers the decision. Branch only on declared
axes when impact and uncertainty justify it.

### Branch admission (5 conditions)

A branch/candidate is admitted only when all of: (1) it changes at least one
declared variation axis; (2) it preserves every hard invariant; (3) it is not
dominated by or a duplicate of an existing candidate; (4) the target model
can realize it; (5) its evaluation cost is justified within the current
budget.

### Early pruning (6 conditions)

Prune when: invariant violation; unsupported hard control; dominated
candidate; semantic duplicate; budget exhaustion for the branch; validator
already failed on the same axis without new evidence.

### Reasoning budget ledger (100 units)

Each request starts a reasoning budget ledger (default 100 units). Phases
consume units: retrieval, candidate generation, branching, critique,
validation, repair. The ledger is a vector record, not a token cap;
exhaustion returns an explicit state (degrade / escalate / fallback) — never
silent truncation.

### Escalation record

A decision with `needs_escalation: true` records reason, failed validator,
unresolved items, and recommended action. Escalation triggers: hard conflict,
missing capability, second validation failure (see
`model_scaled_reasoning_policy`).

## Relationship to existing attention budget

The existing control-priority/attention-budget system
(`control_priority_attention_budget`) operates at the compiler level (which
controls to prioritize). Decision-aware routing operates one layer above: it
selects which reasoning operator to invoke for a given decision. The budget
field connects the two — token/cost/latency constraints flow from routing into
the compiler's carrier/token budget.

## Verification

`test_router_is_deterministic`,
`test_existing_policies_remain_replay_stable`,
`test_unnecessary_branching_reduced`.
