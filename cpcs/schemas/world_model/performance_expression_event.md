---
id: cpcs.schema.performance_expression_event
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
curation_status: proposal
sources: [SRC-002 §16, L2.§38, L2.§54]
primary_route: cpcs/schemas/world_model/
secondary_routes:
  - cpcs/knowledge/04_character_performance/
interfaces: []
---

# Performance Expression Event — Combined Canonical Form

The major architectural closure (SRC-002 §16/L2.§38): **do not create one
mega-label**. Use layered components. FACS/Laban/Bartenieff are typed values
inside a universal object, not competing ontologies.

## Layered form (SRC-002 §16)

A `performance_expression_event` combines facial[] (FACS AUs), gaze{},
head_orientation{}, laban{effort/shape/phrasing}, bartenieff[], and
affect_target{} — each in its own field, none flattened into "emotion".

## Executable directing package (SRC-002 L2.§38, §54)

```json
{
  "performance_expression_event": {
    "id": "evt_004",
    "actor": "actor_A",
    "intent": { "summary": "restrained defensive readiness", "evidence_class": "authored" },
    "context": { "action": "counter", "shot_scale": "medium", "interaction": "duet", "visibility": "full_upper_body" },
    "controls": [
      { "framework": "facs", "control": "AU04", "scope": { "actor": "actor_A", "phase": "anticipation" }, "priority": "medium" },
      { "framework": "laban", "control": "effort.flow.bound", "scope": { "actor": "actor_A", "action": "counter", "phase": "preparation" }, "priority": "high" },
      { "framework": "bartenieff", "control": "upper_lower", "scope": { "actor": "actor_A", "action": "counter" }, "priority": "high" }
    ],
    "temporal_coordination": [],
    "causal_dependencies": [],
    "realizations": [],
    "persistence": [],
    "continuity": [],
    "conflicts": [],
    "observability": [],
    "provider_budget": {},
    "verification": {}
  }
}
```

## Authoring flow (SRC-002 L2.§39)

`authored YAML → resolved canonical JSON (inheritance/aliases/defaults/scope/
evidence) → NL provider projection (lossy)`. XML only where ordered/
namespaced envelopes add real integration value. NL is a projection, not
canonical truth.

## Key semantic boundary (SRC-002 §32)

```text
FACS = visible facial action
Laban = qualitative movement organization
Bartenieff = connectivity organization
VAD/affect = higher-level authored/interpreted target
kinematics = measurement/proxy layer
provider prompt = projection
```

Qualitative frameworks must not be made artificially scientific by assigning
arbitrary numbers to their labels.
