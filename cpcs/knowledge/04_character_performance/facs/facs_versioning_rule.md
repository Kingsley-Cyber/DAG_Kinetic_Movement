---
id: cpcs.facs.versioning_rule
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §4, SRC-002-U01, SRC-002-U02]
primary_route: cpcs/knowledge/04_character_performance/facs/
interfaces: []
---

# FACS Versioning Rule

The 2002 revision changed the handling/meaning of several earlier identifiers.
Published documentation warns that **AU41, AU42 and AU44 were eliminated as
separate actions** in the 2002 scoring system and those numbers were reused
for other strands.

## Required field

```json
{ "facs_version": "2002" }
```

CPCS must require `facs_version` before interpreting version-sensitive AU
numbers. `facs_version` is the scoring vocabulary version, **not** a provider
version.

## Prohibited

Do not build a universal catalog that silently merges 1978 and 2002 semantics.
AU41/AU42/AU44 must be **rejected unless version-qualified**.

## Authority boundary

The 2002 manual is proprietary. CPCS stores the **public vocabulary, version
metadata, provenance, and project-level abstractions**; licensed FACS
training/manual material remains the authority for exact coder rules and must
not be reconstructed from secondary lists.

## Verification

`test_facs_version_required`, `test_legacy_au_rejected_without_version`.
