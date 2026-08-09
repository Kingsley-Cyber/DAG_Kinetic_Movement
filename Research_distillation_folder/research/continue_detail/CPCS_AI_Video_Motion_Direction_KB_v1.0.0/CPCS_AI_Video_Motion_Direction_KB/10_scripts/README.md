# Utility Scripts

These scripts are offline and deterministic. They do not call any model vendor.

## Validate the package

```bash
python 10_scripts/validate_package.py --root . --as-of 2026-07-31
```

Observable success: exit code `0`, `validation_report.json` has `summary.passed: true`, and `error_count: 0`.

## Compile an example against a capability snapshot

```bash
python 10_scripts/compile_example.py \
  05_examples/01_cross_punch \
  12_adapters/veo_3_1.json \
  --output /tmp/cpcs_compile.json
```

Observable success: output contains a canonical-scene SHA-256, a prompt, a conceptual request draft, lossy fields, and `not_executed: true`.

## Export the graph seed to Neo4j Cypher

```bash
python 10_scripts/export_graph.py --root . --output /tmp/cpcs_graph.cypher
```

Observable success: the command reports the entity/relation counts and creates idempotent `MERGE` statements.
