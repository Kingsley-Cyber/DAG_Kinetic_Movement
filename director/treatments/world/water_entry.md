---
id: world.water_entry
pass: world
triggers: ["pool", "swimming pool", "falls into the water", "pushed into the water", "thrown into", "splash", "jumps in", "lake", "fountain"]
not_when: ["shallow water, a puddle or a stream the body does not enter", "a dive or jump the actor controls (use the entry as a planned action)", "no body enters the water"]
backs: [cpcs.mx.material_response, cpcs.mx.affordance_constraints]
from: "cpcs/knowledge/17_vfx_secondary_motion/material_response.md (MaterialResponse for water: trigger bound to the contact site, immediate response local displacement and splash, secondary response ripples, persistence mode decay); cpcs/knowledge/08_objects_affordances/affordance_constraints.md (water is penetrable; environment as a constraint field with interaction surfaces and hazards)"
origin: PROJECT_DERIVED
importance: 0.7
---
# Water answers a body entering it

Water is penetrable: a falling body does not stop at the surface, it displaces water. The response
is bound to the point of contact (not decoration): water goes up and outward at the entry, some
of it leaves the pool over the edge, and the rest settles. The physics event of the entry owns the
splash itself; this treatment states what the pool is and where the displaced water goes.

## Wording
```prompt core
The pool water is {depth}; a body falling into it displaces water outward and upward, and some of it slops over the stone edge before the surface settles.
```
```prompt core short
The pool is {depth}; displaced water slops over the stone edge.
```

## Failure signs
- The body bounces on or skates over the surface, or stops at it.
- A splash with no entry point, or a splash before the body touches the water.
- The water stays flat after the entry, or the splash hangs in the air.
- The pool changes size or depth between frames.

## Effects
- claim: binding the water response to the entry point gives a splash that follows the body in, not a decorative burst · evidence_status: unverified · model: seedance · runs: —
