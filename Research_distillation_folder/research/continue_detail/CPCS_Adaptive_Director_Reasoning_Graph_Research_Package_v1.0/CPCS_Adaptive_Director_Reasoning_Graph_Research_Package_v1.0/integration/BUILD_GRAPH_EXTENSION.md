# Proposed `build_graph.py` Extension

Do not hand-edit `lab/graph.json`. Add the research package alias and concept cards, then rebuild.

## 1. Paper alias

Add an alias similar to:

```python
PAPER_ALIASES = {
    # existing aliases...
    "CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0": [
        "ADRG §",
        "CPCS-ADRG",
        "CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0",
    ],
}
```

Match the exact structure used by the current builder before applying this snippet.

## 2. Initial integration with no graph-schema migration

Append `integration/concept_cards.proposed.jsonl` to `lab/concepts.jsonl`. Existing `pairs_with`, `conflicts`, `evidence`, `source`, and `layer` fields will produce useful graph edges through the current builder.

## 3. Optional node-kind migration

After retrieval requirements are stable, add source files and node kinds for:

```text
reasoning_policy
model_profile
decision_template
compiler_rule
variant_axis
failure_card
```

Do not add a node kind until its source-of-truth file, required fields, and validation rules are defined.

## 4. Optional edge vocabulary

Recommended new edges:

```text
decomposes_to
depends_on
grounds
requires
mitigates
variant_of
selected_over
compiled_to
approximated_by
validated_by
repaired_by
preserves
```

Add edge-specific validation. `selected_over` requires a decision ID. `compiled_to` requires a target adapter and realization status. `depends_on` must be acyclic in the compilation subgraph.

## 5. Verification

```bash
python3 lab/scripts/concepts.py validate
python3 lab/scripts/build_graph.py
python3 lab/scripts/validate_repo.py
```

Inspect the graph diff before commit. Expected changes are new ADRG concept and paper nodes plus `pairs`, `conflicts`, `in_layer`, and `sourced_from` edges. No existing frozen research package should change.
