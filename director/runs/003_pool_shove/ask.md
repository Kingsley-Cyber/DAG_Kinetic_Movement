# Run 003 — thrown into the pool

## Ask

> At a backyard party, one friend shoves another into the swimming pool; he goes in fully clothed
> and comes up laughing, 8 seconds.

Target model: seedance (route unconfirmed; 2,000-character budget from third-party API docs, see
`profiles/seedance.yaml`).

## Intent brief

Locked by the user: a backyard party; two friends; one shoves the other into a swimming pool; the
one shoved goes in fully clothed and comes up laughing; 8 seconds. Open: who they are, what they
wear (beyond "fully clothed"), the pool and yard, the camera, the aspect ratio, the look.
Implied: the shove is a prank between friends, not an attack; the fall ends in a splash and the
clothes are visibly soaked afterwards.

Forced decisions. (1) Two contacts, each with its own cause and reaction: a light nudge (the
intensity anchor) and then the real shove, written "much more intense than the first nudge"; the
water entry is a third causal event on a separate beat. (2) The reaction of the world to the
body (splash crown, spray over the edge, bubbles, ripples) is owned by the water-entry event and
the new world treatment; wet clothes and hair and the moving pool surface are persistent changes
owned by continuity. (3) Screen direction is fixed: the man in red screen-left, his friend and the
pool screen-right, everything runs left to right. (4) The camera is the catalog handheld move,
side-on, so the shove, the fall and the splash are all in frame; no contact is hidden.

## Pass plan summary

Active: intent, entity, world, interaction, physics, staging, continuity, time, performance,
camera, synthesis. Inactive with reason: action (covered by interaction pathways and the two
physics events), attention (nothing withheld), light_color (not asked), style (no look or device
asked), audio (not asked; the laugh is stated as visible behaviour).
