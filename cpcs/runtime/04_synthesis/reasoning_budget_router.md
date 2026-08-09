---
id: cpcs.runtime.reasoning_budget_router
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.7, §11.6]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/knowledge/19_generation_complexity/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.mx.complexity_feature_vector
  - cpcs.adrg.decision_aware_routing
  - cpcs.runtime.selective_tree_search
  - cpcs.runtime.bounded_local_search
---

# Reasoning Budget and Deterministic Router

> **Source:** SRC-006 §4.7 — "Reasoning budget"

## Principle

Budgets are **vectors**, not token counts alone. Do not begin with a
universal weighted scalar; preserve raw typed complexity signals.

## Resource dimensions

```text
model_input_tokens · model_output_tokens · model_calls
parallel_candidates · sequential_revisions · graph_nodes · graph_edges
verifier_calls · detector_runs · video_renders · render_seconds
gpu_seconds · wall_time_ms · estimated_cost · repair_iterations
human_review_minutes
```

## Complexity signal vector

```text
causal_dependency_count · actor_count · interaction_count
open_event_count · temporal_constraint_count · events_per_second
hard_constraint_count · ambiguous_binding_count
unresolved_state_count · provider_gap_count
required_exactness_classes · continuity_horizon
cross_view_conflict_count · prior_failure_count · verifier_coverage
estimated_solvability
```

## Initial deterministic router

| Observable state | Initial mode | Reason |
| --- | --- | --- |
| No material choice, all hard controls expressible, no prior failure | `direct` | search has no identified value |
| One promising state with a localized, patchable weakness | `bounded_refine` | sequential exploitation |
| Two or more material alternatives on one/few axes | `selective_tree_search` | controlled exploration |
| Independently produced partial decisions with cross-dependencies/conflicts | `typed_graph_aggregation` | merge and conflict handling |
| Finite operators and executable verifiers exist | `bounded_local_search` | search is bounded and testable |
| A generated artifact has a localized failure | `failure_directed_repair` | minimal counterexample-driven correction |
| Verifier coverage insufficient or task appears unsatisfiable | stop/review/provider switch | more sampling is not justified |

Thresholds such as "two branches" are initial engineering rules, not
scientific truths. Log them and replace them only with held-out CPCS
evidence.

## Verification

`test_all_resource_dimensions_recorded`,
`test_mode_requires_minimum_feasible_budget`,
`test_budget_exhaustion_returns_explicit_state`,
`test_router_records_input_features_and_policy_version`,
`test_routing_thresholds_are_logged_configuration` (SRC-006 §11.6).
