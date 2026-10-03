# WO-05 — Run 003: thrown into the pool (T12; world reactions)

## The ask (verbatim)

> At a backyard party, one friend shoves another into the swimming pool; he goes in fully clothed
> and comes up laughing, 8 seconds.

Target model: `seedance`.

## Read first

WO-04 (same procedure) · `plan/ARCHITECTURE.md` §2.2 (the World example), §3.5.7 ·
`cpcs/knowledge/08_objects_affordances/` · the `material_response` card under
`cpcs/knowledge/17_vfx_secondary_motion/` · `Additional/07 CPCS World Model _ Causal State _
Attention Gap Closure.md` (skim for water, wetness, persistence) ·
`Additional/HANDS_CONTACT_MANIPULATION.md` §3 (person contact), §4.4 (geography and causality).

## Decisions already made

- Active passes must include world, physics, staging, continuity and camera.
- The causal chain is written as physics events on separate beats: shove (contact: palms on
  chest/shoulder) → loss of balance → water entry (contact: body on water surface) → surface.
  Secondary reactions carry the world response: displaced water, splash crown, ripples; settle:
  he stands or treads water, clothes soaked and clinging, hair wet, laughing.
- Persistent changes go to continuity locks: wet clothes and hair stay wet; the pool surface keeps
  moving after the splash.
- Screen direction is conserved across the shove and the fall (staging control).
- Force uses an anchor (a first playful nudge, then the real shove "much harder than the nudge")
  only if the 8 s fit allows the extra beat; otherwise anchor the shove to a visible fact.
- Write world treatments only for what this run needs (water entry response, wet-state
  persistence): `director/treatments/world/water_entry.md`, `director/treatments/continuity/wet_state.md`.
  Each with `from` pointing at the source read, origin PROJECT_DERIVED or INFERENCE as true.
- Camera: one catalog move; state where, movement and lens.
- "comes up laughing" is performance; write visible behaviour, no affect words.

## Steps and acceptance

Same as WO-04 steps 1–7, in `director/runs/003_pool_shove/`. Additional acceptance: the prompt
reads cause → contact → reaction → settle for both contacts in order; read-back lists the splash
after the entry and the wet state after surfacing.

## Stop if

The run cannot fit 8 s without dropping a contact's reaction. Do not drop it: return the
OVERLOADED options, pick "cut lowest-importance beat" or "lengthen", record the decision.
