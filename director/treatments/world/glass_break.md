---
id: world.glass_break
pass: world
triggers: ["drinking glass", "glass falls", "shatters", "breaks on the floor", "knocked off the table", "smashes", "dropped glass", "broken glass"]
not_when: ["the glass lands on something soft and survives", "the glass is held and only set down", "no glass or brittle object falls"]
backs: [cpcs.mx.material_response, cpcs.mx.affordance_constraints]
from: "cpcs/knowledge/17_vfx_secondary_motion/material_response.md (MaterialResponse: the same trigger-bound pattern applies to glass, debris and liquid; persistence mode); Additional/07 CPCS World Model _ Causal State _ Attention Gap Closure.md §1 (a delta persists after its cause); cpcs/knowledge/08_objects_affordances/affordance_constraints.md (a hard floor is a constraint surface)"
origin: PROJECT_DERIVED
importance: 0.7
---
# Glass answers a fall onto a hard floor

Glass is brittle: a fall onto a hard floor does not end in a bounce, it ends in a break at the
point of impact. The break is bound to the floor contact (nothing breaks in the air), the pieces
travel outward from that point and then stay where they stop. The physics event of the impact owns
the break itself; this treatment states what the floor is and what the pieces do afterwards.

## Wording
```prompt core
The floor is {floor}; glass that lands on it breaks at the point of impact into sharp pieces that skid outward and stay where they stop.
```
```prompt core short
The floor is {floor}; broken glass skids and stays where it stops.
```

## Failure signs
- The glass bounces or lands whole, or breaks in the air before it reaches the floor.
- Pieces vanish, re-form, or return to the table after the break.
- A break with no impact point, or pieces that never come to rest.
- The floor changes material or size between frames.

## Effects
- claim: binding the break to the floor contact gives a break that follows the fall and pieces that stay put, not a decorative shatter · evidence_status: unverified · model: seedance · runs: —
