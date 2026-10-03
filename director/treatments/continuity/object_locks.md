---
id: continuity.object_locks
pass: continuity
triggers: ["product", "bottle", "object stays the same", "label", "keeps its shape", "does not morph"]
not_when: ["no object persists across beats"]
backs: [cpcs.mx.continuity_state, cpcs.continuity.visibility_not_existence]
from: "Additional/HANDS_CONTACT_MANIPULATION.md §2.1 (invariants: forbid, not hope), §2.2 (object rigid, label readable); cpcs/knowledge/18_sequence_continuity/continuity_state.md"
origin: PROJECT_DERIVED
importance: 0.8
---
# Object locks

State what must stay identical as an outcome, before and after the action. Objects are rigid;
labels stay readable; a part that comes off stays visible where it went.

## Wording
```prompt core
Throughout, {items}.
```
```prompt core short
Throughout, {items_short}.
```

## Failure signs
- Bottle changes size, colour or label between beats.
- The cap vanishes, re-attaches, or hovers.
- Water level changes without a drink.

## Effects
- claim: outcome-stated locks hold object identity across beats · evidence_status: unverified · model: seedance · runs: —
