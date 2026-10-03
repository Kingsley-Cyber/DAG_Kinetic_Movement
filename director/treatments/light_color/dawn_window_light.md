---
id: light_color.dawn_window_light
pass: light_color
triggers: ["dawn", "sunrise", "morning light", "light through a window", "light moves across", "golden hour", "window light", "empty room"]
not_when: ["studio or soft even light is wanted", "night or artificial light only", "the light must stay constant"]
backs: [cpcs.ugc.realism_reference]
from: "Additional/CAPTURE_SURFACE_REALISM.md §2 (light reveals or hides microtexture: flat, hard, available light reveals it; soft even light gives the smooth render look), §5 rule 1 (grain rises as light falls: faint noise in the shadows at dawn), rule 4 (exposure drifts when the light changes, motivated), rule 5 (choose the revealing light); §11B row golden-hour window"
origin: PROJECT_DERIVED
importance: 0.7
---
# Dawn window light: one low source that reveals surface

Pick the light that shows texture: one low, warm, hard-edged source, a window, with the rest of
the room left dim. Soft, even light would hide the grain of wood and plaster. Dim light brings
faint sensor noise in the shadows, and the exposure drifts a little as the lit area grows; both
are motivated by the light changing, not decoration. When the light is the subject of the clip,
state where it enters, how its edge moves, and what it lands on, in the beats, and keep this
control to the quality of the light.

## Wording
```prompt core
Light comes only from {source}: low, warm dawn light with a hard edge, the rest of the room dim, so the grain and texture of {surfaces} show where the light touches them. Faint sensor noise shows in the shadows, and the exposure drifts slightly as the lit area grows.
```
```prompt core short
Light comes only from {source}: low, warm, hard-edged dawn light, the rest of the room dim; faint noise in the shadows.
```

## Failure signs
- Flat, soft, even light with no visible edge: the surfaces go smooth and the light has nothing to move across.
- The light flickers, jumps, or reverses instead of travelling in one direction.
- The room brightens everywhere at once, so the moving edge is lost.
- Over-clipped highlights where the light lands, or a heavy colour grade.

## Effects
- claim: naming one low hard-edged source and its direction gives a readable moving light edge, and raw surface texture where it lands · evidence_status: unverified · model: seedance · runs: —
