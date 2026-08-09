---
id: cpcs.gaps.src007_dmr_runtime_gaps
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007]
primary_route: cpcs/research/gaps/
---

# SRC-007 — DMR Runtime Gap Register (Research Prompt)

SRC-007 is a deep-research prompt over the DMR gap register. It names
G001–G009, G011–G017, G019–G021 (19 gaps). **G010, G018, G022 are undefined
in this prompt and must be recovered from the attached DMR register — never
inferred from numbering.** Every register entry must end as `closed`,
`implementable_now`, `requires_experiment`, `unknown`, `deferred`, or
`rejected` with a reason. All statuses below are `requires_experiment` or
`unknown` pending the research pass — none is closed.

## Gap coverage table

| Gap | Domain | Status | Distilled to |
| --- | --- | --- | --- |
| G001 | Canonical ScenePlan reconciliation | requires_experiment | sceneplan_authority_projection |
| G002 | Temporal solver (Allen/STN/STNU) | requires_experiment | temporal_solver_semantics |
| G003/G004 | Action preconditions/effects, persistent state | implementable_now (catalog) | state_variable_catalog |
| G005 | Typed contact lifecycle | implementable_now | interaction_lifecycle EXTEND |
| G006 | Feasibility validator | implementable_now | constraint_feasibility EXTEND |
| G007/G008 | Provider contracts and adapters | unknown (needs docs) | provider_capability_snapshots |
| G009 | Exactly-once compilation-loss report | implementable_now | capability_classes_and_loss_records EXTEND |
| G010 | **undefined in prompt** | unknown | recover from register |
| G011/G012/G013 | Measurement stack and evaluator | requires_experiment | measurement_record_form EXTEND |
| G014/G015 | Failure taxonomy and minimal patch | implementable_now | failure_repair_contract EXTEND |
| G016/G017 | Benchmark and experiment harness | requires_experiment | benchmark_harness_contract |
| G018 | **undefined in prompt** | unknown | recover from register |
| G019 | Format doctrine | requires_experiment | carrier_effect_experiment_design EXTEND |
| G020 | FACS/Laban scale calibration | requires_experiment | numeric_scale_calibration |
| G021 | Provider lifecycle | implementable_now | provider_capability_snapshots |
| G022 | **undefined in prompt** | unknown | recover from register |

## Shared application fixture

One stable fixture throughout the packet (causal spine may not change):

```text
Actor A rotates toward a table and accidentally strikes a drinking glass with
the right forearm. The glass leaves the table, breaks on the floor, and the
shards persist. Actor B notices the impact after a constrained reaction
latency. The camera reframes to Actor B, then reveals the broken glass. At
least one requested control is unsupported natively by the selected provider.
```

The fixture must appear in canonical JSON, an authoring format, a provider
request, the compilation-loss report, and evaluator output. Every introduced
value is labeled by origin.

## Required packet sections (6)

1. `DMR_RUNTIME_DECISION_TABLE` — condition, consulted object, rule, output,
   failure path, owner.
2. `SCENEPLAN_AUTHORITY_MATRIX` — field ownership across Universal Score,
   CPCS-MX, VOG, DMR.
3. `END_TO_END_SCENE_TRACE` — shared fixture from intent through acceptance
   or repair.
4. `MINIMAL_DMR_VERTICAL_SLICE` — smallest build proving state + time +
   contact + capability negotiation + evaluation.
5. `DEFERRED_SCOPE` — excluded fields/subsystems and evidence needed to add
   them.
6. `ACCEPTANCE_AND_FALSIFICATION` — observable tests and rejection
   conditions.

## Execution rules

Use the attached frozen package as primary corpus, but verify claims with
primary sources; never silently "fix" the package. Distinguish
package-derived claims, external-source findings, proposed CPCS
representations, and experimental hypotheses. Do not redesign CPCS — DMR is
execution/runtime research behind the existing CPCS semantic authority.
