---
id: cpcs.compiler.carrier_role_semantics
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §3.1, §13, §16.1, SRC-002 §22]
primary_route: cpcs/runtime/07_compiler/carrier_planner/
secondary_routes:
  - cpcs/research/representation/
interfaces: []
---

# Carrier Role Semantics

## Doctrine

CPCS represents **meaning**, not serialization format and not a provider's
prompt dialect. Conceptual layering:

```text
research/evidence → director interpretation → canonical scene/world state
→ canonical control intent → capability negotiation → provider projection
```

Carrier roles:

| Carrier | Role | Best suited to |
| --- | --- | --- |
| JSON | **resolved canonical machine truth** | typed state, exact numerics, validation-safe structures, API representation |
| YAML | authoring-oriented | human-authored intent, policy, profiles, configuration, inheritance |
| XML | explicit projection only | ordered temporal events, nested event relationships, namespaced triggers, mixed-content sequencing — only when it provides a real advantage |
| Natural language | **lossy provider projection** | creative intent, observable description, semantic fallback — never canonical authority |
| JSONL | append-only records | evidence, experiments, observations, verification, provenance, maintenance history |

## Equivalence example (source §13)

"A person reaches with the right hand toward a cup over 0.8 seconds…"
renders identically in meaning across YAML (author-friendly), JSON
(explicit types/units/IDs), XML (ordered phase nodes), NL (loses typing,
provenance, exact units, guaranteed phase identity).

## Hard rules

- Never store intended meaning as `{"prompt": "camera slowly moves in"}`
  when a typed camera-motion object can express it.
- Round-trip semantic tests operate against **resolved JSON**, not textual
  equality.
- Do not author the same resolved truth independently in every format.
- No universal carrier-superiority claims are evidence-supported
  (structured-output research separates schema compliance from semantic
  correctness); carrier effects must be measured by CPCS experiment
  (see `research/sources/experiments/carrier_effect_experiment_design.md`).

## Verification

`test_yaml_json_semantic_equivalence`, `test_xml_order_preserved`,
`test_nl_projection_is_non_authoritative` (SRC-001 §26).

## SRC-002 §22 confirmation

SRC-002 §22 confirms the carrier roles above: XML should only be emitted
where ordered/namespaced event envelopes provide a real integration
advantage (it adds ordering/namespacing, not new semantics); NL is the
provider projection expressing visible behavior and intended control, not
unsupported claims about private mental state.
