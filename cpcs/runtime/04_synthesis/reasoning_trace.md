---
id: cpcs.adrg.reasoning_trace
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §11, §13]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/knowledge/00_foundations/invariants/
interfaces: [cpcs.synthesis.director_decision_procedure, cpcs.adrg.decision_record]
---

# Reasoning Trace Without Chain-of-Thought

Raw chain-of-thought should not become a canonical artifact (SRC-004 §2.1, §11).
A generated explanation is not reliable evidence of the true causal basis of a
model output (Turpin et al., 2023). The trace should be a structured production
record, not a prose narrative.

## 14-element production trace

```text
problem_ref
question
retrieved_evidence_refs
applied_invariants
admitted_candidates
rejected_candidates
rejection_reasons
selected_candidate
selection_criteria
assumptions
unresolved_items
consequences
loss_records
verification_refs
```

Each element is a reference (ID or typed value), not free-form prose. The trace
is machine-checkable: evidence IDs must resolve, invariants must be preserved,
and the selected candidate must exist in the admitted set.

## Why not chain-of-thought

CoT is a useful operator for generating candidate reasoning, but:

- Self-generated explanation is not reliable evidence of causal basis.
- A trace that says "I chose X because Y" is not proof that Y was the actual
  decision basis.
- External validation is required for hard structural/semantic claims.

The DecisionRecord IS the trace. The reasoning operator (CoT, ToT, GoT, etc.)
produces it; the trace does not depend on any specific operator.

## Verification

`test_decision_trace_faithfulness` — decision record matches actual selected
candidate and compiler result.
`test_rejection_reason_required` — every rejected candidate has a reason code.
`test_decision_evidence_ids_resolve` — all evidence_refs resolve to real sources.
