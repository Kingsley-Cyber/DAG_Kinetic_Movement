# 14 — AI Video Model Capabilities and Control Surfaces

## Scope and date

The supplied query stopped after Topic 14’s intent line, so this file reconstructs the required control-surface analysis. It is a **dated snapshot verified 2026-07-30**, not a permanent ranking. Model names, endpoints, input limits, duration, resolution, and UI/API parity change frequently. Every adapter must revalidate official documentation and, where possible, a live endpoint schema before release.

## Capability status vocabulary

- `native`: an official surface exposes a structured control;
- `reference_conditioned`: an image/video/performance/keyframe conditions behavior;
- `prompt_only`: expressed through natural-language prompting;
- `postprocess`: achieved after generation;
- `unsupported`: explicitly unavailable;
- `unknown`: not verified;
- `legacy`: scheduled for retirement or no longer suitable for new integration.

CPCS never upgrades a prompt phrase to “native control” simply because the prompt sometimes works.

## Model matrix

| Provider | Model/surface | Status | Documented native controls/limits | Sources |
|---|---|---|---|---|
| Google | Veo 3.1 | current_preview/GA depends endpoint | {'duration_seconds': [4, 6, 8], 'aspect_ratio': ['16:9', '9:16'], 'resolution': ['720p', '1080p', '4k model-dependent'], 'seed': True, 'native_audio': True} | S053 |
| Kling AI | VIDEO 3.0 | current | {'duration_seconds': '3–15', 'multi_shot': True, 'custom_shot_duration': True, 'native_audio': True, 'resolution': ['720p', '1080p documented through current surfaces'], 'aspect_ratio': ['16:9', '9:16 and surface-dependent']} | S054 |
| Kling AI | VIDEO 3.0 Omni | current | {'duration_seconds': '3–15', 'multi_shot': True, 'shot_level_duration': True, 'native_audio': True, 'element_voice': True, 'resolution': ['720p', '1080p']} | S076 |
| Runway | Gen-4.5 | current | {'duration_seconds': '2–10 on documented web surface', 'fps': [24, 25], 'aspect_ratio': 'multiple; crop behavior applies', 'resolution': 'documented surface around 720p; verify endpoint'} | S055 |
| Runway | Act-Two | current | {'duration_seconds': '3–30', 'fps': 24, 'gesture_control': 'character image mode', 'resolution': ['1280x720', '720x1280', '960x960', '1104x832', '832x1104', '1584x672']} | S056 |
| Luma AI | Ray 3.2 Modify Video | current | {'motion': 'Off or 1–9', 'structure': 'Off or 1–9', 'faces': 'binary/selection behavior by surface', 'bodies_poses': 'Poses or Blocking and associated controls'} | S057, S058 |
| Adobe | Firefly Video | current | {'camera_motion_reference': '5–10s, under 200MB; first 5s used', 'camera_angles/motion': 'documented UI controls', 'style_presets': True, 'seed': 'surface-dependent', 'transparent_background': 'supported workflow'} | S059, S060 |
| OpenAI | Sora 2 | legacy_deprecating | {'status_only': 'Do not build new primary adapter without migration plan.'} | S061, S062 |

## Key findings by provider

### Google Veo 3.1

The Gemini API documentation exposes prompt, start image, last frame, up to three reference images on relevant variants, video extension, duration, aspect ratio, resolution, seed, and native audio. Some combinations require an 8-second duration or differ by model variant. CPCS should make invalid combinations a schema error before submitting a request. [S053, API parameters/specifications]

### Kling VIDEO 3.0 / Omni

Official Kling guidance documents multi-shot generation, durations from 3–15 seconds, image/start-end/element references, and native audio. Omni adds multimodal/video character references and custom multi-shot workflows. UI capabilities and API capabilities must be probed separately; CPCS stores `surface=web|api|partner_wrapper` and never assumes parity. [S054; S076]

### Runway Gen-4.5 and Act-Two

Gen-4.5’s documented web surface provides text/image-to-video, 2–10 second duration, aspect-ratio choices, and 24/25 fps. Act-Two is a different control surface: a driving performance plus character input can transfer face, speech, and movement for up to 30 seconds. Character-image mode supports body/hand gesture control; character-video mode prioritizes the original environment/camera and facial control. [S055; S056]

### Luma Ray 3.2

Modify Video exposes strong preservation/guidance controls such as Motion and Structure, with Poses versus Blocking controlling skeletal adherence. CPCS should favor these native/reference controls over verbose motion prose when the task is to preserve a source performance. [S057; S058]

### Adobe Firefly Video

Adobe documents first/last frames, camera controls, style/composition references, and a camera-motion reference workflow. The reference-video workflow has duration/file limits and may make other controls unavailable. CPCS must validate the selected model and workflow rather than treating all Firefly controls as simultaneously compatible. [S059; S060]

### OpenAI Sora 2

Sora 2 is a legacy adapter. OpenAI states that the web/app ended April 26, 2026 and the API is scheduled to end September 24, 2026. CPCS should not create new production dependency on it without a migration plan. [S061; S062]

## Canonical downcasting

| Canonical control | Preferred surface | Fallback | Loss risk |
|---|---|---|---|
| actor_identity | element/reference image/video, character asset | descriptive prompt + seed | high without reference |
| motion_trajectory | source/performance video, motion control, keyframes | prompt prose | high |
| camera_track | camera motion reference, shot-level camera controls | camera prompt phrases | medium-high |
| phase_timing | shot duration/keyframes/performance video | ordered prompt with time markers | high |
| FACS | driving performance/reference face | visible feature prose, not AU codes alone | high |
| BESS | performance/motion reference | natural-language descriptors | medium-high |
| audio/dialogue | native audio + speaker/voice controls | postproduction | model dependent |

The preferred order is structured native control, reference conditioning, prompt approximation, then postprocess. FACS, BESS, phase timing, and force cues are usually richer than any current public text-to-video schema. Performance/video references therefore remain the highest-fidelity bridge when available.

## Adapter contract

```json
{
  "provider": "google",
  "model_id": "veo-3.1-generate-preview",
  "surface": "gemini_api",
  "verified_at": "2026-07-30",
  "documentation_snapshot": "S053",
  "native_capabilities": ["duration","aspect_ratio","resolution","seed","start_image","last_frame","reference_images","audio"],
  "prompt_only": ["laban_bess","facs_track","phase_microtiming"],
  "validation_rules": ["reference_images=>duration=8", "resolution=4k=>duration=8"],
  "ttl_days": 30
}
```

## Capability probe

Every release should save provider, exact model/endpoint, surface, account region/tier, request/response schema hashes, observed limits, official documentation source, and verification date. If documentation and live schema conflict, the adapter stays blocked until the discrepancy is resolved and documented.

## Loss report

A compiled request returns:

- canonical fields preserved natively;
- fields represented by reference;
- fields translated to prose;
- fields deferred to postprocess;
- unsupported/unknown fields;
- expected failure risks;
- experiment IDs supporting model-specific prompt choices.

This makes CPCS auditable. A model output can succeed artistically while the adapter truthfully reports that phase timing and FACS were prompt approximations rather than native controls.

## References and locators

- **[S053]** Google AI for Developers (2026), *Generate Videos with Veo 3.1 in the Gemini API*. **Locator:** API parameters/specifications; model features; prompt guide  
- **[S054]** Kling AI (2026), *Kling VIDEO 3.0 Model User Guide*. **Locator:** Multi-shot, 3–15 second duration, camera/storyboard guidance  
- **[S055]** Runway (2026), *Creating with Gen-4.5*. **Locator:** Settings: 2–10 sec, aspect ratio, 24/25 fps  
- **[S056]** Runway (2026), *Performance Capture with Act-Two*. **Locator:** Inputs, gesture control, duration, resolution, fps  
- **[S057]** Luma AI (2026), *Ray 3.2 Controls & Workflows In Depth*. **Locator:** Motion, Structure, Characters, quick reference  
- **[S058]** Luma AI (2026), *Ray 3.2 Prompting, Outputs & Controls*. **Locator:** Poses vs Blocking; output/control behavior  
- **[S059]** Adobe Firefly (2026), *Match Camera Motion to Reference Video*. **Locator:** Reference requirements; first/last frames; advanced settings  
- **[S060]** Adobe Firefly (2026), *Generate Videos Using Text Prompts and Images*. **Locator:** Camera, composition, motion, first/last frame, output settings  
- **[S061]** OpenAI (2026), *What to Know About the Sora Discontinuation*. **Locator:** Discontinuation dates  
- **[S062]** OpenAI (2025), *Sora 2 Model Reference (Legacy)*. **Locator:** Input/output, duration, resolution, audio, pricing  
- **[S076]** Kling AI (2026), *Kling VIDEO 3.0 Omni Model User Guide*. **Locator:** Capabilities table; multimodal references; custom multi-shot; duration; pricing
