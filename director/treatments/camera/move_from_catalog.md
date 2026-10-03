---
id: camera.move_from_catalog
pass: camera
triggers: ["camera", "shot", "dolly", "pan", "tilt", "zoom", "orbit", "tracking", "crane", "drone", "handheld", "static", "follow", "reveal"]
not_when: ["the camera is a propped phone or fixed selfie (use camera.selfie_framing)"]
backs: [cpcs.camera.three_layer_semantics, cpcs.camera.impact_sync]
from: "director/vocab/camera_moves.yaml (aicameramovements.com, read 2026-10-03); cpcs/knowledge/12_camera_image_formation/camera_three_layer_semantics.md"
origin: UNVERIFIED
importance: 0.9
---
# One camera move, stated in the four-part grammar

The camera pass picks one move id from `director/vocab/camera_moves.yaml` by its `function`
(what the move does for the viewer), copies its Movement / Speed / Framing / End fields into the
control's value, and adapts the framing line to the scene. A move not in the catalog is allowed
only as `move: custom` with a justification in the decision record. Optics-layer entries (zooms,
tilt-shift) are lens changes, not camera motion; never describe a zoom as the camera moving.

## Wording
```prompt core
Camera: {phrase}. Movement: {movement}. Speed: {speed}. Framing: {framing}. End: {end}.
```
```prompt core short
Camera: {phrase}; {speed}; {end}.
```

## Failure signs
- The camera moves when the catalog entry is a lens change, or zooms when a dolly was asked.
- Horizon drifts on a pan or truck that should stay level.
- The move never settles: no readable end composition.
- Two moves blended into one clip without a stated order.

## Effects
- claim: the four-part grammar (move, movement, speed, framing, end) yields the intended move more often than a bare move word · evidence_status: unverified (site's claim; no runs here) · model: seedance · runs: —
