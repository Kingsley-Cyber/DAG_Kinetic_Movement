---
id: cpcs.adrg.model_scaled_policy
kind: policy
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-011 §9, examples/reasoning_policy.yaml]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/05_strategy/
interfaces:
  - cpcs.adrg.decision_aware_routing
  - cpcs.runtime.reasoning_budget_router
  - cpcs.adrg.decision_record
---

# Model-Scaled Reasoning Policy

> **Source:** SRC-011 §9 — "Model-scaled policy" +
> `examples/reasoning_policy.yaml` (`adrg.default.model_scaled.v1`).

Reasoning effort must scale with model capability, not with task ambition.
The same request is planned differently by a mini model, a standard model, and
a large model — but all three share the same compiler and verifier contracts,
the same decision-ledger obligation, and the same escalation channel. A
reasoning profile is a default that requires local calibration
(`proposed_defaults_require_local_calibration` in the policy file).

## Profile table (exact defaults)

| Dimension | mini | standard | large |
| --- | --- | --- | --- |
| planner_profile | planner.mini.strict.v1 | planner.standard.modular.v1 | planner.large.adaptive_graph.v1 |
| decomposition | fixed_director_dag | fixed_graph_with_local_extension | adaptive_director_reasoning_graph |
| responsibilities_per_call | 1 | 2 | 4 |
| retrieval top_k | 4 | 6 | 10 |
| retrieval graph_depth | 1 | 2 | 2 |
| include_conflicts/failures | true | true | true |
| hierarchical summaries | false | false | true |
| branch width × depth | 2 × 1 | 3 × 2 | 5 × 3 |
| branch admission | high_impact_uncertainty_only | high_value_decisions | impact_uncertainty_coupling_budgeted |
| intrinsic critique passes | 0 | 1 | 1 |
| specialist critics | — | — | performance, motion, camera, compiler |
| external validator passes | 1 | 1 | 1 |
| maximum repairs | 1 | 2 | 2 |
| output format | JSON (schema-constrained) | JSON (schema-constrained) | JSON (schema-constrained) |
| decision record | compact | standard | detailed_but_concise |
| raw_chain_of_thought | false | false | false |
| self-consistency | — | — | on high_impact_ambiguous_decision |

Mini models get one responsibility per call, a fixed narrow DAG, a small
retrieval bundle, strict schemas, bounded repair, and escalation. Large models
may branch wider, aggregate more, and invoke specialist critics — but never
gain the right to skip the decision ledger or silently drop a hard control.

## Escalation record

Escalation is a first-class output, not a failure dump. Trigger conditions
(`on_*` flags in the policy file): hard conflict, missing capability, second
validation failure. The record carries:

```json
{
  "needs_escalation": true,
  "reason": "evidence conflict on hard invariant",
  "failed_validator": "validator.contact_timing",
  "unresolved": ["candidate set exhausted"],
  "recommended_action": "human review or provider switch"
}
```

When a mini model cannot resolve a decision it must escalate on the declared
conditions — it must never silently resolve cross-domain content it lacks
context for.

## Model-scaled variant counts

Variant generation is budgeted per model class (SRC-011 §11): mini produces
1 variant + 1 baseline (1+1); standard 3 variants with up to 2 simultaneous
deltas; large 4–8 candidates narrowed to 2–4 by diversity selection. These
are defaults, not laws.

## Teacher-to-mini decision distillation

A documented pattern for scaling throughput with small models: larger models
produce validated, concise decision examples offline (rationale supervision);
smaller specialists are then deployed with fixed schemas and external checks
rather than being asked to perform wide free-form search. The teacher's
output must pass the same validators before it becomes a training or
exemplar example.

## Boundary

Model-scaled policy selects **how much reasoning** to assign — it does not
change compiler authority, verifier obligations, or the boundary rule that
ADRG feeds the existing compiler rather than replacing it (SRC-004 §21).
Thresholds are proposed engineering defaults; replace them only with
held-out CPCS evidence (SRC-011 §22: small-model limits are a CAUTION claim
until experiments run).

## Verification

`test_profile_budgets_match_policy_file`,
`test_mini_one_responsibility_per_call`,
`test_escalation_trigger_recorded`,
`test_large_branch_uses_diversity_selection`,
`test_all_profiles_emit_decision_records`.
