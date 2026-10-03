---
id: camera.selfie_framing
pass: camera
triggers: ["selfie", "films herself", "phone propped", "front camera", "talking to the phone"]
not_when: ["cinematic camera moves", "third-person camera"]
backs: [cpcs.camera.three_layer_semantics]
from: "cpcs/knowledge/12_camera_image_formation/camera_three_layer_semantics.md (motion layer, optics layer); Additional/CAPTURE_SURFACE_REALISM.md §4 iphone_recent (~24 mm, mild barrel), §5 rule 3 (distortion ∝ closeness)"
origin: PROJECT_DERIVED
importance: 0.9
---
# Explicit camera grammar for a phone selfie

Camera grammar is always stated: motion layer, optics layer, framing. For a propped phone the
motion layer is static with a faint settle; the optics layer is the wide front camera at arm's
length with deep focus; framing is a medium close-up with the action entering from below.

## Wording
```prompt core
Camera: {motion}. {optics}. {framing}.
```
```prompt core short
Camera: {motion_short}; {optics_short}; {framing_short}.
```

## Failure signs
- Camera drifts or orbits on its own.
- Shallow depth of field or a cinematic lens look.
- Optical choices rendered as camera movement (a zoom instead of a wide lens).

## Effects
- claim: explicit static-propped grammar prevents invented camera moves · evidence_status: unverified · model: seedance · runs: —
