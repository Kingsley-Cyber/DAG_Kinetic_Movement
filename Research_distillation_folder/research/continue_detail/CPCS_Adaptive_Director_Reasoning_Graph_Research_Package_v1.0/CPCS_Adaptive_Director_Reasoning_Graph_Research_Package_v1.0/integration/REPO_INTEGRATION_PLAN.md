# Repository Integration Plan

Target: `Kingsley-Cyber/ai-video-movement-prompt-system`

## Constraint observed from the repository

The existing research packages are governed as frozen upstream inputs. `lab/graph.json` is derived and must not be edited manually. A new research package requires source aliasing, concept cards, concept-index coverage, graph rebuild, and repository validation.

## Files to copy

Copy the entire package into:

```text
research/CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/
```

Then integrate these supplied files:

```text
integration/concept_cards.proposed.jsonl  → append reviewed lines to lab/concepts.jsonl
integration/CONCEPT_INDEX_ADDITION.md     → merge as a new part in lab/CONCEPT_INDEX.md
integration/BUILD_GRAPH_EXTENSION.md      → apply the alias and optional graph changes
```

## Recommended staged rollout

1. Add package, source alias, concept cards, and index only.
2. Rebuild RAG and graph; run all repository validators.
3. Add decision-ledger output beside one existing composition workflow.
4. Add mini/standard/large planner profiles.
5. Run E-ADRG-001 through E-ADRG-005 before promoting policies.
6. Add dedicated graph node kinds only after the source contracts are stable.

## Commands

```bash
python3 research/CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/scripts/validate_package.py
python3 lab/scripts/concepts.py validate
python3 lab/scripts/build_graph.py
python3 lab/scripts/validate_repo.py
python3 lab/scripts/sync_repo.py --fix
python3 lab/scripts/validate_repo.py
```

## Verification checkpoints

- every command exits 0;
- the package manifest and SHA256 file match;
- all source IDs resolve;
- concept IDs are unique;
- graph endpoints resolve;
- no frozen package changed;
- `lab/graph.json` changed only through rebuild;
- new policies remain `unexplored` until isolated experiments support them.
