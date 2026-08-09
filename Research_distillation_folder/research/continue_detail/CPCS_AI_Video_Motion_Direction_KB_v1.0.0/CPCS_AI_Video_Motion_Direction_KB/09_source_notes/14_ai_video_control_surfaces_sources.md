# Source Notes — Topic 14: AI Video Control Surfaces

**Sources linked:** 11

## Reading order

### 1. [S053] Generate Videos with Veo 3.1 in the Gemini API

- **Authors/year:** Google AI for Developers (2026)
- **Authority:** `official_current` / `official_api_documentation`
- **Locator:** API parameters/specifications; model features; prompt guide
- **Use:** Prompt, start image, last frame, up to three reference images, extension, duration, resolution, aspect ratio, seed, native audio; version dependent.
- **URL:** https://ai.google.dev/gemini-api/docs/veo
- **Verified:** `2026-07-30`

### 2. [S054] Kling VIDEO 3.0 Model User Guide

- **Authors/year:** Kling AI (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Multi-shot, 3–15 second duration, camera/storyboard guidance
- **Use:** UI capabilities do not automatically imply identical API parameters.
- **URL:** https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide
- **Verified:** `2026-07-30`

### 3. [S055] Creating with Gen-4.5

- **Authors/year:** Runway (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Settings: 2–10 sec, aspect ratio, 24/25 fps
- **Use:** Documented web surface; API may differ.
- **URL:** https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5
- **Verified:** `2026-07-30`

### 4. [S056] Performance Capture with Act-Two

- **Authors/year:** Runway (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Inputs, gesture control, duration, resolution, fps
- **Use:** Character image vs video retains different channels; up to 30 seconds documented.
- **URL:** https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two
- **Verified:** `2026-07-30`

### 5. [S057] Ray 3.2 Controls & Workflows In Depth

- **Authors/year:** Luma AI (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Motion, Structure, Characters, quick reference
- **Use:** Modify Video controls and ranges; version/UI dependent.
- **URL:** https://lumalabs.ai/learning-center/articles/ray-3-2-controls-and-workflows-in-depth
- **Verified:** `2026-07-30`

### 6. [S058] Ray 3.2 Prompting, Outputs & Controls

- **Authors/year:** Luma AI (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Poses vs Blocking; output/control behavior
- **Use:** Poses is stronger skeletal adherence; Blocking is sparser/flexible.
- **URL:** https://lumalabs.ai/learning-center/articles/ray-3-2-prompting-outputs-and-controls
- **Verified:** `2026-07-30`

### 7. [S059] Match Camera Motion to Reference Video

- **Authors/year:** Adobe Firefly (2026)
- **Authority:** `official_current` / `official_product_documentation`
- **Locator:** Reference requirements; first/last frames; advanced settings
- **Use:** Reference 5–10 sec, under 200 MB; first 5 sec used on documented surface.
- **URL:** https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/match-camera-motion-to-reference-video.html
- **Verified:** `2026-07-30`

### 8. [S060] Generate Videos Using Text Prompts and Images

- **Authors/year:** Adobe Firefly (2026)
- **Authority:** `official_current` / `official_product_documentation`
- **Locator:** Camera, composition, motion, first/last frame, output settings
- **Use:** Controls and incompatibilities depend on selected model.
- **URL:** https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-text-prompts.html
- **Verified:** `2026-07-30`

### 9. [S061] What to Know About the Sora Discontinuation

- **Authors/year:** OpenAI (2026)
- **Authority:** `official_current` / `official_product_notice`
- **Locator:** Discontinuation dates
- **Use:** Web/app ended 2026-04-26; API scheduled to end 2026-09-24.
- **URL:** https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
- **Verified:** `2026-07-30`

### 10. [S076] Kling VIDEO 3.0 Omni Model User Guide

- **Authors/year:** Kling AI (2026)
- **Authority:** `official_current` / `official_model_guide`
- **Locator:** Capabilities table; multimodal references; custom multi-shot; duration; pricing
- **Use:** Native audio, multi-shot, 3–15 sec, video-character references; exact API availability must be probed.
- **URL:** https://app.klingai.com/global/quickstart/klingai-video-3-omni-model-user-guide
- **Verified:** `2026-07-30`

### 11. [S062] Sora 2 Model Reference (Legacy)

- **Authors/year:** OpenAI (2025)
- **Authority:** `official_legacy` / `official_legacy_model_page`
- **Locator:** Input/output, duration, resolution, audio, pricing
- **Use:** Legacy/deprecating; not a recommended new CPCS primary adapter.
- **URL:** https://platform.openai.com/docs/models/sora-2
- **Verified:** `2026-07-30`

## Topic-specific caution

Revalidate official documentation and live schemas; UI/API/wrapper surfaces differ.
