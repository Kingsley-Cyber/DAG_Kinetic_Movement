---
id: style.capture_iphone_selfie
pass: style
triggers: ["phone video", "looks real", "not AI", "UGC", "selfie", "filmed on a phone", "too cinematic", "too polished"]
not_when: ["cinematic or film look is wanted", "image-to-video with a reference still that already carries the surface"]
backs: [cpcs.ugc.realism_reference, cpcs.lab.pattern_registry]
from: "Additional/CAPTURE_SURFACE_REALISM.md §4 iphone_recent, §5 rules 1–4, §9 over-correction guard, §11A; prompt-system lab/blocks.yaml blk_device_iphone12 (proven r001); pattern p001 skin microtexture (isolated, r001 vs r004)"
origin: PROVIDER_EXPERIMENT
importance: 0.8
---
# Capture texture: recent iPhone, propped selfie

Texture is applied to how the image is captured, never to the order of events. Realism is bounded
on both sides: one dominant imperfection per axis, coherent with the device, temporally stable,
and never at the cost of label legibility or identity.

## Wording
```prompt core
Shot on a recent iPhone front camera: ordinary and real, not an ad. 1080p at 30fps, Smart-HDR flat tone, cool white balance, faint sensor noise visible only in shadows, slight oversharpening, mild compression, deep focus with no bokeh, no colour grade. Autofocus settles once as the bottle lifts; exposure drifts slightly and settles. Real skin with fine pores, uneven tone and a little T-zone sheen; not smooth, not waxy. Available indoor light, flat and unflattering.
```

```prompt core short
Shot on a recent iPhone front camera, real not cinematic: 30fps, flat HDR tone, deep focus, no bokeh, faint sensor noise, no grade; real skin with visible pores, not smooth or waxy.
```

## Failure signs
- Waxy, poreless skin (the word "smooth" anywhere near skin causes it).
- Bokeh, cinematic grade, studio light, tripod-locked steadiness.
- Grain that swims, white balance that pumps, filter-like degradation.

## Effects
- claim: device signature + positive skin microtexture read as real phone footage · evidence_status: supported (isolated for skin) · model: veo-3.1 · runs: prompt-system r001, r004
- claim: same on Seedance · evidence_status: unverified · model: seedance · runs: —
