---
id: cpcs.runtime.state_equivalence_keys
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.8, §11.1]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.execution_reasoning_state_schema
  - cpcs.runtime.selective_tree_search
  - cpcs.compiler.capability_classes_loss_records
  - cpcs.runtime.canonical_schema
---

# State Equivalence: Six Keys

> **Source:** SRC-006 §4.8 — "State equivalence"

## Principle

There is no single safe equivalence relation. Different consumers need
different preservation guarantees.

| Key | Preserves | May ignore | Use |
| --- | --- | --- | --- |
| `byte_key` | exact bytes | nothing | artifact identity/debug |
| `structural_key` | parsed structure after format canonicalization | whitespace, object-key order | round-trip/serialization checks |
| `semantic_key` | resolved canonical meaning | carrier, comments, aliases, audit timestamps, unordered-set order | branch dedup/experiment matching |
| `evidence_key` | meaning plus evidence/provenance state | presentation noise only | evidence-sensitive retrieval/audit |
| `decision_key` | enabled operations, hard constraints, unresolved obligations, current world projection | closed audit history | search cache/reuse |
| `compile_key` | semantic state plus provider capability/adapter/compiler versions | non-provider audit fields | provider compilation cache |

## Normalization algorithm (12 steps)

1. Validate against the declared schema version.
2. Resolve defaults and inheritance into canonical JSON.
3. Resolve aliases to stable IDs.
4. Convert units to declared base units.
5. Preserve ordered arrays; sort only arrays declared as sets.
6. Normalize interval convention and coordinate-frame identifiers.
7. Preserve `unknown`, `unobservable`, absent, and explicit `null` as
   distinct states.
8. Remove fields listed by the named equivalence profile only.
9. Apply tolerance quantization only where the profile defines a valid
   domain tolerance.
10. Canonicalize the semantic projection with RFC 8785/JCS.
11. Hash with a versioned algorithm such as SHA-256.
12. Include schema version, equivalence-profile version, and relevant
    capability/compiler versions in the hash preimage.

## JCS boundary

RFC 8785 sorts object properties recursively but preserves array order.
JCS alone is therefore insufficient for semantic equivalence: CPCS must
first normalize units, defaults, IDs, set-like arrays, and non-semantic
fields.

## Hash stability rules

Semantic hashes remain stable under whitespace, key-order, and allowed
set-order changes; they change when actor binding, laterality, event order,
causality, required exactness, or provider-relevant meaning changes
(SRC-006 §11.1).
