---
id: cpcs.adrg.director_invariant
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §9, §19.2]
primary_route: cpcs/runtime/05_strategy/constraints/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/runtime/06_canonical/
interfaces: [cpcs.adrg.decision_record, cpsc.runtime.05_strategy.constraints.constraint_feasibility]
---

# Director Invariant and Variant Axes

The decision-level constraint model has three tiers (SRC-004 §9):

```text
hard_invariant
soft_preference
controlled_degree_of_freedom
```

These are distinct from compiler-level constraints. They live at the reasoning
layer and govern candidate admission before compilation.

## Hard invariant

Must not change. Violation rejects the candidate.

```text
identity · subject · action_identity · duration · safety_class ·
required_product_visibility · contact_topology · continuity_lock
```

```json
{
  "invariant_id": "inv.action_identity",
  "kind": "hard_invariant",
  "path": "/actions/0/identity",
  "value": "single_near_contact_strike",
  "source": "authored",
  "enforcement": "reject_candidate"
}
```

## Soft preference

Optimization target, not prohibition. Violation incurs a score penalty, not
rejection.

```text
cinematic_intimacy · camera_participation · emotional_subtlety ·
visual_dynamism
```

## Controlled degree of freedom

An explicit axis with allowed values and preserved invariants:

```json
{
  "axis": "camera_treatment",
  "allowed_values": ["low_tracking_medium", "telephoto_observer"],
  "preserved_invariants": ["action_identity", "duration", "subject_visibility"]
}
```

A variant records only deltas:

```json
{
  "variant_id": "v2",
  "parent_id": "v1",
  "deltas": [
    {"axis": "camera_treatment", "from": "low_tracking_medium", "to": "telephoto_observer"}
  ]
}
```

This makes semantic diversity measurable and prevents lexical paraphrase from
being mistaken for creative variation.

## Relationship to existing constraint system

The existing compiler constraints (`applicability_contraindication_rules`,
`semantic_guardrails`) operate at the control-mapping level. Director invariants
operate one layer above: they govern which candidates are admissible before
the compiler sees them.

## Variant lattice (SRC-011 EXTEND)

> **Source:** SRC-011 §11 — "Variant lattice".

Invariants, axes, and deltas form a lattice with explicit structure:

- **invariants** — must hold across all variants (identity, action identity,
  duration, contact topology, continuity locks);
- **axes** — typed variation dimensions with allowed values;
- **deltas** — each variant records only its axis changes against a parent;
- **incompatibilities** — declared axis-pair conflicts (e.g. camera
  participation vs no-participation axes may be incompatible);
- **maximum_simultaneous_deltas** — default 2; a variant may not change more
  declared axes than this without explicit authorization.

### Diversity selection J(S)

Diversity is measured on **semantic deltas**, never on wording. For a
candidate set \(S\):

\[
J(S) = \frac{1}{|S|^2} \sum_{a \in S} \sum_{b \in S} \delta_{\text{sem}}(a, b)
\]

where \(\delta_{\text{sem}}\) is the typed delta distance between two
variants. This prevents lexical paraphrase from being mistaken for creative
variation (consistent with the delta-only variant record above).

### Prompt optimization vs shot optimization

Shot optimization (vary camera/performance/action controls on declared axes)
comes first; prompt optimization (vary wording while keeping semantics) is a
separate, later activity. They are not substitutes and must be measured
independently.

### Model-scaled variant counts

mini 1 + 1 baseline; standard 3 variants with up to 2 simultaneous deltas;
large 4–8 candidates narrowed to 2–4 by \(J(S)\). Defaults, not laws (see
`model_scaled_reasoning_policy`).

## Verification

`test_hard_invariant_blocks_candidate`,
`test_variant_changes_only_declared_axes`,
`test_no_duplicate_semantic_variant`.
