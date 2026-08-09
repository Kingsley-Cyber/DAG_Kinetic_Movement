---
id: cpcs.adrg.state_contraction
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §8]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/03_retrieval/
  - cpcs/observation/
interfaces: [cpcs.synthesis.long_form_scheduler, cpcs.observation.observation_provenance]
---

# State Contraction

CPCS has atomic/dependency-style reasoning execution but does not yet expose a
durable contract separating active, compressed, and memory states (SRC-004 §8).
This matters because context can be contracted without losing the ability to
audit why a decision was made. The result is non-Markovian auditability without
keeping the entire context window alive.

## State model

```text
active_state
compressed_state
source_memory
decision_memory
failure_memory
```

### active_state

Only what the next operation needs:

```json
{
  "current_question": "...",
  "hard_invariants": [],
  "selected_evidence_refs": [],
  "candidate_ids": [],
  "relevant_capabilities": [],
  "unresolved": []
}
```

### compressed_state

A deterministic digest of completed work:

```json
{
  "intent_hash": "...",
  "decision_ids": [],
  "selected_candidate_ids": [],
  "invariant_status": {},
  "coverage": {},
  "loss_status": {},
  "state_digest": "sha256:..."
}
```

### source_memory

Never silently discard: source ID, locator, source digest, evidence class,
provenance, retrieval timestamp/version, capability profile version.

### decision_memory

Retain: selected candidate, rejected candidate IDs, rejection reason codes,
decision criteria, decision confidence, assumptions, unresolved items.

### failure_memory

Retain: validator ID, failure code, responsible layer, affected object/path,
repair ID, patch digest, result, recurrence count.

## What may be discarded

After a decision is resolved, active context may discard:

```text
raw retrieved prose · duplicate evidence text ·
rejected candidate payloads after disposition · scratch reasoning ·
intermediate formatting · tool chatter
```

It must NOT discard:

```text
stable IDs · evidence provenance · decision outcome · rejection reason ·
invariant status · compile loss · failure/repair history ·
hashes needed for reproducibility
```

## Relationship to long-form scheduler

The long-form scheduler (`long_form_scheduler`) manages temporal state evolution
across shots (STATE_t + ACTION_t + CONTROL_t → STATE_t+1). State contraction
manages context within a single reasoning session. They are complementary: the
scheduler produces the timeline; contraction keeps the audit trail compact.

## Verification

`test_state_contraction_preserves_audit_refs`,
`test_compressed_state_deterministic`,
`test_source_memory_not_discarded`.
