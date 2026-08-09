---
id: cpcs.runtime.bounded_local_search
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.5]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/research/sources/experiments/
interfaces:
  - cpcs.runtime.reasoning_budget_router
  - cpcs.runtime.failure_repair_contract
  - cpcs.runtime.selective_tree_search
  - cpcs.adrg.decision_aware_routing
---

# Bounded Local Search

> **Source:** SRC-006 §4.5 — "Bounded local search and AoT"

## Terminology correction

`aot_prompting` is an experiment in which an algorithmic exploration pattern
is supplied in context. `bounded_local_search` is CPCS runtime
infrastructure. They may be compared or combined, but they are **not the
same mechanism**. Do not use `AoT` as a synonym for local search in
experiment tables.

## Contract

```text
input              accepted immutable reasoning state
focus              unsatisfied obligations + localized uncertainty
operators          finite versioned operation registry
proposal           one semantic delta per operation
verification       deterministic checks first, calibrated model checks second
selection          feasible/Pareto/champion-preserving
rollback           parent state remains immutable
stopping           success, convergence, repetition, unsolvability, or
                   budget exhaustion
output             accepted child state or explicit no-change/failure
```

## Candidate operations

- split one compound event into phases;
- reorder two non-causal events;
- change shot size while preserving screen direction;
- add an explicit continuity invariant;
- replace an unsupported native control with a semantic approximation;
- increase emphasis on a failed provider clause without changing canonical
  intent;
- select another provider adapter;
- request targeted evidence or verification.

Each operation declares applicable atom types, touched paths, preconditions,
expected postconditions, verification requirements, and worst-case cost.

## Stopping conditions (any one)

- every required verification condition passes;
- no frontier candidate makes a material improvement;
- the next state repeats a decision-equivalence key;
- every remaining candidate is infeasible or dominated;
- a required value is `unknown`/`unobservable` and no authorized observation
  can resolve it;
- provider capability makes the task unsatisfiable;
- any resource budget is exhausted;
- iteration or wall-time deadline is reached.
