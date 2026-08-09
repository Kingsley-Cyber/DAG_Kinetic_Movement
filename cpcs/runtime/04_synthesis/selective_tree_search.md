---
id: cpcs.runtime.selective_tree_search
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.3, §11.4]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/research/sources/experiments/
interfaces:
  - cpcs.runtime.reasoning_budget_router
  - cpcs.runtime.state_equivalence_keys
  - cpcs.adrg.decision_aware_routing
  - cpcs.compiler.capability_classes_loss_records
---

# Selective Tree Search

> **Source:** SRC-006 §4.3 — "Selective tree search"

## Branch eligibility

A candidate deserves a distinct branch only if its normalized semantic delta
changes at least one of:

- hard-constraint satisfiability;
- event order, causal dependency, contact ownership, or actor binding;
- staging topology or shot structure;
- required verification obligations;
- provider realization class (`native`, `approximate`, `semantic`,
  `unsupported`);
- expected compilation-loss class or severity;
- a calibrated metric by more than its declared materiality tolerance;
- a genuine creative choice the user/director has elected to compare.

Differences in whitespace, key order, prose wording, aliases, comments,
audit IDs, or numerically equivalent units do **not** create branches.

## Branch axes

```text
staging · camera · performance · motion · editing · audio · VFX
narrative_reveal · provider_realization
```

Vary one axis at a time for controlled attribution. Permit joint-axis
branches only when a dependency makes independent variation invalid; record
the coupling reason.

## Candidate evaluation (ordered)

1. Reject schema-invalid or hard-constraint-invalid candidates.
2. Reject candidates with required unsupported controls unless an explicit
   degradation policy applies.
3. Deduplicate candidates by the applicable equivalence key.
4. Retain the Pareto frontier across required coverage, verified adherence,
   compilation loss, risk, and cost.
5. Use an authored or calibrated preference model only to break remaining
   ties.
6. Preserve uncertainty and individual metric provenance.

Do not collapse all evidence into an unexplained scalar.

## Rejection codes

```text
schema_invalid · hard_constraint_failed · unsupported_required_control
equivalent_duplicate · dominated · budget_exceeded · verifier_unavailable
verification_inconclusive · causal_incoherence · temporal_incoherence
identity_violation · provider_loss_exceeds_policy
```

## State rules

- parent/champion state remains immutable;
- equivalent candidates deduplicate, material differences survive;
- hard-invalid candidates never win on preference score;
- Pareto selection is reproducible (SRC-006 §11.4).
