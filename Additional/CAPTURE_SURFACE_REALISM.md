---
id: cpcs.reference.capture_surface_realism
kind: feature_spec
epistemic_status: PROJECT_DERIVED
acquisition: authored
primary_route: (buildable, dynamic spec for the 2nd brain)
companions: [cpcs.reference.living_performance_realism, cpcs.reference.natural_dialogue_mode, cpcs.reference.format_craft]
maps_to: [profile://capture/authentic_ugc_v2, LPR-007, LPR-008]
version: 1.0
status: ready_to_build
---

# Capture & Surface Realism — a *dynamic* elite spec

Make skin and camera read **captured, not generated** — on purpose, and **adaptively**. This is not a
fixed "iPhone preset." It's a **resolver**: given the scene (light, motion, device intent, distance,
subject, T2V/I2V, provider, realism target) it *computes* the right capture + surface parameters, so
one control travels across every future prompt and self-adjusts.

> **Core theorem:** an image reads real when it carries **two physical signatures the AI default
> omits** — a **device** (a real sensor+lens with imperfect behavior) and a **surface** (skin/coat
> with real microtexture), both revealed by **light that shows texture**. AI-clean fails by being
> *too perfect*: denoised, uniformly sharp, evenly lit, smooth-skinned, stabilized. The fix is
> **controlled degradation + named microtexture + revealing light** — bounded, never random.

---

## 0. The verified failure this closes

From live comparison of four real prompts: the ones that read real *described the camera and skin as
physical things* (phone sensor with AF/exposure behavior; real skin with pores under flat light). The
ones that flagged AI specified **structure + performance** precisely but left **capture, surface, and
light quality blank** — and set `camera: locked`. Two empty channels + a stabilized camera = the AI
look. **Format was not the cause; the missing capture/surface *content* was.**

---

## 1. The "low-and-high-res enough" paradox (the real secret)

Real footage is a **quality paradox**: high-res *enough* to resolve pores, low-fi *enough* to carry
sensor imperfection. The AI default is **too clean** — that cleanliness *is* the tell. So the lever is
**not resolution**; it's a **controlled-degradation stack** that reintroduces what a real pipeline
adds:

```
sensor noise/grain  ·  mild compression (blocking on motion)  ·  slight oversharpen halos
·  phone-HDR tone flatness (crushed highs / lifted shadows)   ·  auto-white-balance wobble
·  motion blur on movement  ·  faint rolling-shutter on fast pans  ·  mild chromatic aberration
·  subtle vignette  ·  NO denoise-clean  ·  NO uniform sharpness  ·  NO color grade
```

Each is a **dial**, and each is **bounded** — enough to read *captured*, never so much it reads
*filtered / vintage / glitch* (that's the over-correction failure, §9).

---

## 2. The realism triad (why skin only looks real sometimes)

Skin realism is not one setting — it's a **product of three**:

```
apparent_skin_realism  =  SURFACE spec  ×  CAPTURE that resolves it  ×  LIGHT that reveals it
```

- **Surface** — pores/tone/sheen must be *named* (or locked in a reference still).
- **Capture** — deep focus + enough resolution + no denoise, or the texture is smeared away.
- **Light** — **flat/hard/available** light *reveals* microtexture; **soft/even/studio** light *hides*
  it → smooth "render" look.

Miss any factor and skin goes waxy even if the other two are perfect. Elite work sets all three.

---

## 3. The eight axes (each a *dynamic* parameter, not a constant)

Every axis has: what it controls · values · default · **what it adapts to**.

| Axis | Controls | Values | Adapts to |
|---|---|---|---|
| **A. Device** | the sensor/pipeline identity | profile library (§4) | realism_target + distance |
| **B. Optics** | FOV, distortion, DOF | focal ~13/24/50/90mm; barrel by width; **deep focus/no bokeh** default | distance (selfie→wide) + realism_target |
| **C. Hold** | stabilization signature | locked→OIS-floaty→handheld→walking-bounce | motion_energy (**never `locked` for UGC**) |
| **D. Sensor behavior** | AF + AE + WB | AF hunt→snap; exposure drift/settle; AWB wobble | events (rack-focus points, light changes) |
| **E. Image register** | the degradation stack (§1) | noise/compression/sharpen/HDR/CA/vignette intensities | **inverse to light** (dim→more noise) + device |
| **F. Light quality** | texture revelation | flat / hard / soft; available / motivated | scene + mood (revealing vs flattering) |
| **G. Surface** | skin/coat microtexture | pores/tone/sheen/redness/asymmetry; species set | subject + exertion/temperature + i2v-lock |
| **H. Motion artifacts** | capture-of-motion | motion blur; rolling-shutter; step-jolt | motion_energy + pan speed |

**Forbid (steer away from AI):** `locked_tripod_look, gimbal_glide, bokeh, color_grade, studio_3point,
skin_smoothing, denoise_clean, poreless, waxy, plastic, uniform_sharpness, glamour_framing,
beauty_filter`.

---

## 4. Device-profile library (the reusable, expandable presets)

A device profile is a coherent bundle of A–H. Pick one, blend two, or let the resolver choose. Friends
extend this table — that's how it scales.

| Profile | Look | Optics | Hold | Image register | Best for |
|---|---|---|---|---|---|
| `iphone_recent` | clean-but-real HDR | ~24mm, mild barrel | OIS floaty micro-jitter | light noise, slight oversharpen, HDR-flat, cool WB | modern UGC selfie |
| `iphone_older` | softer, noisier | ~28mm | more shake | more noise, more compression, warmer | "a few years ago" UGC |
| `android_mid` | oversharpened, punchy | ~26mm | jittery | heavy oversharpen halos, saturated | budget-phone UGC |
| `webcam_laptop` | soft, low-light noise | ~50mm fixed | static-but-alive | low detail, noise, compression, flat | talking-head/call vibe |
| `gopro_action` | ultrawide, deep | ~16mm strong barrel | body-mounted bounce | high sharpen, high DOF, slight fisheye | POV/active |
| `dslr_real` | crisp yet human | 35/50mm, shallow-if-wanted | handheld breath | fine grain, minimal sharpen, gentle contrast | "nice but not ad" |
| `camcorder_2000s` | interlace-ish, soft | ~40mm | zoom-wobble | heavy compression, low res, date-stamp optional | nostalgia/found-footage |
| `security_cam` | wide, low fps, grain | ~2.8mm | fixed | heavy noise, low fps, timestamp | context/ambience |
| `film_16mm` | organic grain | prime | handheld | film grain, halation, gate weave | stylized-real |

Default when unspecified: `iphone_recent` for UGC, `dslr_real` for "premium but real."

---

## 5. The dynamic resolver (this is what makes it *dynamic*)

A workflow calls one function; it computes the capture+surface block. Pseudo-logic:

```python
def resolve_capture_surface(inputs) -> block:
    dev   = inputs.device_intent or infer_device(inputs.realism_target, inputs.distance)
    optics = device_optics(dev, inputs.distance)          # selfie→wider+more barrel; deep focus default
    hold  = stabilization_for(inputs.motion_energy)       # still→micro-sway; walking→bounce+step-jolt; NEVER locked for ugc
    afae  = sensor_behavior(inputs.events)                # AF hunt at rack points; exposure drift on light change; AWB wobble
    # E is the paradox engine: degradation scales INVERSELY with light
    noise = clamp(base_noise(dev) * (1/inputs.scene_light.level), lo, hi)
    hdr   = highlight_clip if inputs.scene_light.level=="bright" else lifted_shadows
    image = degradation_stack(dev, noise, hdr)            # + oversharpen, compression, CA, vignette (bounded)
    light = choose_light(inputs.scene_light, reveal=True) # prefer flat/hard to reveal texture, capped by mood
    surf  = surface_for(inputs.subject)                   # human pores/tone/sheen OR species set
    if inputs.mode == "i2v": surf = LOCK_IN_REFERENCE_STILL(surf)   # still carries G; prompt only maintains
    motion = motion_artifacts(inputs.motion_energy, inputs.pan_speed)
    block = assemble(dev, optics, hold, afae, image, light, surf, motion)
    for axis in block:                                    # provider routing
        if not provider_supports(inputs.provider, axis): block.route_to_post(axis)
    return clamp_all_bounded(block)                       # anti-over-correction (§9)
```

**The adaptation rules that matter (memorize these):**
1. **Grain/noise ∝ 1 / light.** Dim garage → more noise; bright store → cleaner but **highlight
   clipping + HDR flatness** instead. (Both are "captured"; the *type* of imperfection changes.)
2. **Motion blur & rolling-shutter ∝ motion.** Still talking-head → almost none; walking/fast pan →
   visible blur + jelly.
3. **Distortion ∝ closeness/width.** Arm-length selfie → wide + mild barrel + face bulge; medium →
   normal.
4. **AF/AE behavior is event-driven,** not constant: AF hunts *at* a rack-focus point; exposure
   drifts *when* light changes (garage→store). Motivated, not decorative.
5. **Light choice reveals or hides texture** — pick the revealing option consistent with the mood.
6. **I2V locks the surface in the still;** T2V must spell it out (no anchor).

---

## 6. T2V vs I2V (weight shifts hard here)

- **I2V:** skin + device grain are **baked into the reference still** — fix them *there* (a real,
  textured, phone-shot-looking frame). The video prompt then only **maintains** the surface and adds
  **motion artifacts** (blur, AF/AE behavior, hold). Lightest path to real skin.
- **T2V:** no anchor → you **must** write the full A–H block, and hold it stable across the clip.
  This is exactly what the AI-flagging prompts omitted.
- **Cross-shot consistency:** reuse the same reference still (I2V) or the same locked capture block
  (T2V) so grain/skin/optics don't shift shot-to-shot (a drift tell).

---

## 7. Provider matrix (honor vs post-inject)

| Provider | Honors natively | Route to post |
|---|---|---|
| **Veo 3.x / Sora 2** | device look, deep focus, light quality, handheld, skin texture (decent) | fine grain, precise rolling-shutter |
| **Kling / Runway** | motion, some optics | grain, compression, HDR-flatten, WB wobble → **add in edit** |
| **Any** | — | If a model over-smooths skin, **add grain + micro-contrast + slight sharpen in post** to restore texture |

**Post-pipeline (provider-agnostic realism):** grain plugin + light compression + subtle sharpen +
HDR-flatten LUT + optional rolling-shutter + vignette. The resolver flags which axes a given model
can't do so the edit fills them. This makes the block **portable across any generator.**

---

## 8. Verification / QC (measurable — ties to LPR-007/008 lane)
Check the render, don't trust the prompt:
- `sensor_noise_present == true` (FFT high-freq energy > floor)
- `uniform_sharpness == false` (sharpness varies across frame/focus)
- `bokeh_absent == true` (deep focus) *unless intentionally shallow*
- `color_grade_absent == true` (no filmic S-curve / teal-orange)
- `skin_texture_energy >= real_floor` (not smoothed) — LPR-007 proxy
- `camera_locked == false` for UGC (global-motion PSD shows handheld)
- `light_reveals_texture == true` (shadow micro-contrast present)
- `degradation_within_bounds == true` (not over-grained/vintage) — §9

**Repo gate:** concepts = registered kinds (`technique`); layers `appearance` (skin) / `camera` /
`lighting` / `effects` (image register) — all registered; namespaces `appearance.*`, `camera.*`,
`lens.*`, `lighting.*`, `effects.*` — registered; narrow gates → `validate_repo.py` green.

---

## 9. The over-correction guard (the *other* failure)
Realism is bounded on **both** sides. Too clean = AI; too degraded = fake-vintage / glitch /
Instagram-filter. Guards:
- noise/grain intensity ≤ "visible in shadows, invisible in midtones"
- one dominant imperfection per axis, not all maxed
- degradation must be **coherent with the device** (don't put film halation on an iPhone)
- keep it **temporally stable** (grain that swims or WB that pumps every frame reads processed)
- never let degradation destroy the **invariants** (label legibility, identity, anatomy)

---

## 10. Integration with the 2nd brain (buildable)

- **Mode profile** `mode/capture_surface_realism.yaml` — composes with `capture/authentic_ugc_v2`;
  `activation_labels: [realistic, phone footage, ugc, "looks real", "not ai"]`; forces coverage of
  `skin` (appearance), `camera`, `lighting`, and an `effects`/image-register slot.
- **Concept cluster** (promote via the bridge; kinds `technique`; layers `appearance`/`camera`/
  `lighting`/`effects`): `c_device_capture_signature`, `c_controlled_degradation`, `c_texture_revealing_light`,
  `c_skin_microtexture_positive`, `c_handheld_not_locked`, `c_motivated_af_ae`, `c_motion_capture_artifacts`,
  `c_overcorrection_guard`. Each gated on capture/skin tokens; sourced from LPR-007/008.
- **Control block** — the resolver output, stored as the `capture_surface` object, mapped into
  `appearance.*` / `camera.*` / `lighting.*` / `effects.*` controls with prose projections.
- **Reasoning policy** `rp_capture_surface`: run the resolver → set A–H from scene → apply the
  degradation stack inverse to light → verify against §8 → clamp per §9 → compile to prose (+ a post
  recipe for providers that can't honor an axis).

**Build order:** promote cluster → add mode profile (forces skin/camera/light/effects coverage) → add
`rp_capture_surface` + the resolver → mappings → `validate_repo.py` green → before/after emit proof.

---

## 11. Worked examples

### A. The fix (your P4, same brevity, now real)
```yaml
capture:                                   # add this block; flip camera off "locked"
  device: iphone_recent                    # 1080p/30, smart-HDR flat, cool WB
  optics: ~24mm, mild barrel; deep focus, NO bokeh
  hold: handheld arm-length; OIS micro-jitter; imperfect centering; one reframe
  sensor: AF hunts→snaps once; exposure drifts/settles; AWB wobble
  image: light sensor noise; slight oversharpen; mild compression; NO denoise-clean; NO grade
  light: available flat store fluorescents; unflattering, reveals texture
  skin: real pores, uneven tone, T-zone sheen, faint redness; asymmetry; never smooth/waxy/plastic
forbid: [locked_tripod_look, gimbal, bokeh, color_grade, studio_light, skin_smoothing, denoise_clean, uniform_sharpness]
```

### B. Same subject, three scenes — the resolver adapts (dynamic in action)
| Scene | Light | Resolver output (deltas) |
|---|---|---|
| Dim parking garage | low | **noise↑**, shadows lifted+noisy, AF hunts more, exposure searches, cool cast |
| Bright fluorescent store | high | noise↓ but **highlight clipping + HDR-flat**, faster AF, flat unflattering texture-reveal |
| Golden-hour window | warm directional | mild noise, **hard side-light reveals pores**, warm WB, gentle bloom, one exposure drift toward window |

Same person, same device — three different *captured* looks, none of them "render-clean."

### C. Non-phone / non-human (profile library + species surface)
- `dslr_real` premium interview: fine grain, 50mm, handheld breath, soft-but-directional key → "nice
  but clearly filmed."
- Animal (`gopro_action` or `dslr_real`): surface = fur direction/clumping + wet-nose specular; light
  reveals coat; motion blur on the run; **no skin-smoothing analog** (forbid fur-plastic).

---

## 12. The dynamic control object (what workflows pass downstream)
```json
{"capture_surface":{
  "device":"iphone_recent","optics":{"focal_mm":24,"distortion":"mild_barrel","dof":"deep","bokeh":false},
  "hold":{"mode":"handheld","jitter":"floaty_micro","reframe":1,"locked":false},
  "sensor":{"af":"hunt_snap_on_event","ae":"drift_settle","awb":"wobble"},
  "image":{"noise":0.3,"compression":0.2,"oversharpen":0.25,"hdr":"flat","ca":0.1,"vignette":0.1,"grade":false,"denoise_clean":false},
  "light":{"quality":"flat_available","reveals_texture":true,"source":"fluorescent"},
  "surface":{"subject":"human","named":["pores","uneven_tone","tzone_sheen","faint_redness","asymmetry"],"forbid":["smooth","waxy","plastic","poreless"]},
  "motion_artifacts":{"blur":"by_motion","rolling_shutter":"faint_on_fast_pan"},
  "bounds":"clamped","post_pipeline":[],"mode":"t2v"}}
```
Compile this to prose for the model; keep the JSON as the verifiable twin; carry it across every shot.

---

**Net:** capture+surface stops being a lucky phrase you remember and becomes a **dynamic control** the
workflow resolves from the scene — reusable, adaptive, provider-portable, and verifiable. It's the
sibling of Natural Dialogue Mode: that one makes the *voice* read human; this one makes the *image*
read captured.
