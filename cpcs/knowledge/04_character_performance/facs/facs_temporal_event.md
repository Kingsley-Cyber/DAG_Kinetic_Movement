---
id: cpcs.facs.temporal_event
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §3.4, §7, SRC-002-U03]
primary_route: cpcs/knowledge/04_character_performance/facs/
secondary_routes:
  - cpcs/research/numerical/timing_relations/
interfaces: []
---

# FACS Temporal Event Semantics

A facial action is a **temporal interval**, not a static bag of AUs.

## Canonical temporal fields

```text
onset        : first accepted temporal point
apex_start   : beginning of sustained peak interval (when applicable)
apex_end     : end of peak interval (when applicable)
offset       : end of visible action
duration     : deterministic difference onset → offset
```

Always preserve the original timebase:

```json
"timebase": { "kind": "presentation_timestamp", "unit": "seconds", "source_fps": 30.0 }
```

## Missing data

If source timestamps are unavailable:

```json
{ "observability": "unobservable", "reason": "missing_source_timestamps" }
```

**Do not fabricate exact timing.** Sampling must use source-frame timestamps;
never assume 30 fps. Aggregation preserves event-level data first; phrase-level
summaries are derived second.

## Verification (SRC-002 §7)

onset/apex/offset error · temporal IoU · tolerance-window agreement. A
tolerance window improves temporal agreement (U03 psychometric finding).
