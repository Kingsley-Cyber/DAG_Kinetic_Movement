---
id: cpcs.gov.operational_knowledge_model
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§18, §60]
primary_route: cpcs/00_governance/policies/
secondary_routes:
  - cpcs/runtime/04_synthesis/
interfaces: []
---

# Operational / Application Knowledge Model

SRC-002 L2.§18 distinguishes six knowledge strata. The operational layer
must **not silently redefine** FACS/Laban/Bartenieff; it is a CPCS reasoning
layer around them.

```text
semantic representation   = what a concept means
operational knowledge     = when the concept should be considered
application knowledge     = when the concept should actually be selected
realization knowledge    = what visible behavior the selected concept produces
composition knowledge    = how selected concepts interact across frameworks/time
compiler knowledge        = how the canonical control survives provider translation
verification knowledge   = how the rendered result is judged against the target
```

## Epistemic bases (SRC-002 L2.§18)

Every operational statement must identify its basis:

```text
source_established · source_supported_interpretation · cpcs_policy ·
derived · experimental_hypothesis · unknown
```

A coding agent must never convert `cpcs_policy` or `experimental_hypothesis`
into an externally established fact.

## Reasoning-complete lifecycle (L2.§19.1)

`concept → meaning → applicability → contraindication → context conditioning
→ scope → temporal behavior → interaction → observable realization →
provider compilation → verification`. A concept is reasoning-complete only
when every applicable stage has evidence / a labeled CPCS policy / a labeled
experimental hypothesis / an explicit `unknown`.

## Final verdict (L2.§60)

DO NOT expand FACS/Laban/Bartenieff into larger parallel ontologies.
DO expand the universal CPCS operational layer around them.
