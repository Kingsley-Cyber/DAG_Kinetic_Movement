---
id: style.capture_iphone_rear_handheld
pass: style
triggers: ["shot on a phone", "held by a friend", "phone video", "UGC", "looks real", "not AI", "filmed on a phone", "too polished"]
not_when: ["selfie or propped phone (use style.capture_iphone_selfie)", "cinematic or film look is wanted", "image-to-video with a reference still that already carries the surface"]
backs: [cpcs.ugc.realism_reference, cpcs.lab.pattern_registry]
from: "Additional/CAPTURE_SURFACE_REALISM.md §4 iphone_recent (~24 mm, OIS micro-jitter hold), §5 rules 1–4 (noise per light, distortion per closeness, event-driven AF/AE), §9 over-correction guard; adapted from treatment style.capture_iphone_selfie (its sources: prompt-system lab/blocks.yaml blk_device_iphone12, pattern p001; not re-read)"
origin: PROJECT_DERIVED
importance: 0.8
---
# Capture texture: recent iPhone, held by someone else

Same device signature as the selfie treatment, with the front-camera and bottle wording removed:
the camera is the main camera, held by a friend, so the hold is a small human sway rather than a
propped lock. Texture is applied to how the image is captured, never to the order of events.

## Wording
```prompt core
Shot on a recent iPhone main camera held by a friend: ordinary and real, not an ad. 1080p at 30fps, Smart-HDR flat tone, cool white balance, faint sensor noise visible only in shadows, slight oversharpening, mild compression, deep focus with no bokeh, no colour grade. Autofocus settles once as the case opens; exposure drifts slightly and settles. Real skin with fine pores, uneven tone and a little T-zone sheen; not smooth, not waxy. Available indoor light, flat and unflattering.
```
```prompt core short
Shot on a recent iPhone main camera held by a friend, real not cinematic: 30fps, flat HDR tone, deep focus, no bokeh, faint sensor noise, no grade; real skin with visible pores, not smooth or waxy.
```

## Failure signs
- Waxy, poreless skin (the word "smooth" anywhere near skin causes it).
- Bokeh, cinematic grade, studio light, tripod-locked steadiness.
- Grain that swims, white balance that pumps, filter-like degradation.

## Effects
- claim: device signature + positive skin microtexture read as real phone footage · evidence_status: supported (isolated for skin, front-camera selfie wording) · model: veo-3.1 · runs: prompt-system r001, r004
- claim: same with a friend-held main camera on Seedance · evidence_status: unverified · model: seedance · runs: —
