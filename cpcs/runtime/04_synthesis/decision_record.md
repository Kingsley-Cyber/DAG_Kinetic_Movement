---
id: cpcs.adrg.decision_record
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §5, §19.1, §19.3]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/control_registry/
  - cpcs/verification/
interfaces: [cpcs.synthesis.director_decision_procedure, cpcs.compiler.capability_classes_loss_records]
---

# DecisionRecord, Candidate, and Consequence

The missing abstraction is: **reasoning method ≠ reasoning decision.** CPCS
already has reasoning methods (six policies + executors). What it lacks is a
compact, first-class semantic representation of the director decisions those
methods resolve. DecisionRecord is that representation (SRC-004 §0, §5).

## DecisionRecord

```json
{
  "decision_id": "dec.camera.treatment",
  "question": "Which camera treatment best preserves action readability?",
  "problem_ref": "problem.action_readability",
  "candidate_ids": ["cand.low_tracking", "cand.telephoto", "cand.handheld"],
  "criteria": ["action_readability", "subject_visibility", "continuity",
               "generation_reliability"],
  "constraint_refs": ["inv.action_identity", "inv.subject_identity"],
  "evidence_refs": ["evidence.anticipation_readability", "profile.camera.capability.v3"],
  "scores": {
    "cand.low_tracking": {
      "action_readability": 0.90,
      "subject_visibility": 0.88,
      "continuity": 0.86,
      "generation_reliability": 0.81
    }
  },
  "selected": "cand.low_tracking",
  "rejected": [
    {"candidate_id": "cand.handheld", "reason_codes": ["continuity_risk"]}
  ],
  "assumptions": ["single_actor_visibility"],
  "confidence": 0.81,
  "unresolved": ["target_specific_camera_adherence"],
  "consequences": ["control.camera.low_tracking", "verification.camera.adherence"],
  "loss": []
}
```

### What confidence does NOT mean

`confidence` is not the probability that the director is objectively correct. It
is confidence in the decision under the declared evidence, rubric, and unresolved
assumptions. `selected` does not mean rendered success. `evidence_refs` establish
provenance, not truth.

## Candidate

A candidate treatment with typed deltas against its parent:

```json
{
  "candidate_id": "cand.camera.tracking",
  "parent_id": null,
  "type": "candidate_treatment",
  "decision_id": "dec.camera",
  "deltas": [],
  "preserves": ["inv.action_identity", "inv.duration"],
  "requires": ["cap.camera_tracking"],
  "expected_effects": ["higher_action_readability"],
  "risks": [],
  "evidence_refs": [],
  "status": "proposed"
}
```

A variant records only deltas, preventing lexical paraphrase from being mistaken
for creative variation.

## Consequence

```json
{
  "consequence_id": "cons.camera_tracking",
  "decision_id": "dec.camera",
  "target": "control.camera.treatment",
  "type": "derived",
  "expected_effect": "higher_action_readability",
  "verification_refs": ["metric.action_readability"]
}
```

## Canonical mapping

DecisionRecord.selected → selected concept/mapping IDs → existing
directing_strategy → existing score request → existing control translation
registry → existing universal score → existing provider adapter. ADRG should
**feed** the existing compiler, not replace it (§21).

## Implementation boundary

Do NOT create a second reasoning authority, second graph database, second
compiler, or generic `ADRGEngine` that duplicates the existing policy runtime
(§18, §29). DecisionRecord is a semantic bridge into the existing pipeline.

## Decision-ledger doctrine (SRC-011 EXTEND)

> **Source:** SRC-011 §4 — "Raw CoT not production artifact".

Raw chain-of-thought text is **not** the canonical artifact of a decision.
The primary design decision of the ADRG package: reasoning happens, but the
ledger — question, alternatives, criteria, scores, selection, evidence refs,
assumptions, confidence, unresolved, loss — is what is stored, retrieved, and
compiled. Three risks justify this (SRC-011 §4):

1. **False provenance** — CoT explanations are post-hoc rationalizations; they
   do not prove the actual causal basis of a choice (Turpin et al., S013).
2. **Retrieval contamination** — raw reasoning text injected into retrieval
   corpora mixes private rationale with canonical evidence and corrupts
   future retrievals.
3. **Token and privacy overhead** — verbose rationale costs tokens, latency,
   and exposes internal deliberation that is not needed by downstream
   consumers.

**What may be retained** (SRC-011 §4): a compact decision record; a local
reasoning trace for debugging when explicitly requested; teacher-model
rationales used offline for decision distillation (see
`model_scaled_reasoning_policy`); never raw private CoT as canonical
provenance. The planner prompts in the package enforce this at prompt level
("Do not output a private chain-of-thought transcript").

The compact ledger form (SRC-011 §4) is a subset of the full DecisionRecord
above — required fields `decision_id, question, alternatives, criteria,
selected, evidence_refs, confidence, unresolved, loss` — and is what mini
profiles emit (`decision_record: compact` in reasoning_policy.yaml).

## Verification

`test_decision_selected_candidate_exists`,
`test_rejection_reason_required`,
`test_decision_evidence_ids_resolve`,
`test_compiled_control_has_realization_status`,
`test_loss_record_required_for_non_exact_realization`.
