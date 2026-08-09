---
id: cpcs.ugc.realism_reference
kind: catalog
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U22, SRC-010-U23, SRC-010-U24]
primary_route: cpcs/knowledge/04_character_performance/
secondary_routes:
  - cpcs/evaluation/reference_video/
interfaces:
  - cpcs.lab.architecture
  - cpcs.lab.pattern_registry
  - cpcs.facs.au_catalog
  - cpcs.laban.numeric_calibration_contract
  - cpcs.runtime.cross_format_compiler_reference
---

# UGC Realism Reference

> **Source:** SRC-010 `references/iphone_rawugc_realism.md`,
> `references/facs_laban_reference.md`, `references/method_details.md`.
> Field-tested rules for "looks like a real phone video" — champion v001 was
> built from these (5/5/4/5, user-validated).

## The two failure modes and their cures

1. **Anti-cinematic block** — output reads as a movie clip. Cure: raw_ugc
   render style, capture grammar, device signature (below), ordinary
   environment, phone-mic audio.
2. **AI-skin** — plastic skin, the #1 AI tell. Cure: **positive microtexture**
   recipe + **negative forbid list** (never "smooth", "flawless") + framing
   line. Empirically the only `isolated_confirmed` pattern in the lab (e002).

## iPhone-12 look signature (device-signature realism)

`30 fps NOT 24` (30 reads UGC, 24 reads cinema) · smart HDR · cool white
balance · noise-reduction smear · floaty stabilization · AF/AE breathing ·
23 mm f/2.2 field. One device's signature is worth more than generic
"realistic".

## Performance and face

- `performance.direction: loose_casual` (p004) — never scored beats for UGC.
- `face.motion: alive_face_motion` — micro head/eye drift (p005, low
  confidence: bundled).
- **Speech:** ~165–190 wpm with a 0.28 s pause before the proof moment.

## Format note (p006)

Format ≠ realism; **content** does. Two house formats both scored 5/5/4/5:
YAML-in-XML and YAML+JSON. Image-to-video rule: **skin is set by the reference
still**, not by the prompt.

## Looks-real lock list (capture grammar)

Reference-still pattern (Nano Banana): start-of-action pose, hands out,
9:16, 2–3 candidates. Multi-clip assembly: jump cuts, room-tone bridge,
captions added in the editor (~1.15 cards/s, ~4 words).

## 10-item verification checklist (deterministic pass/fail)

| # | Check | Threshold |
|---|---|---|
| 1 | Hook | ≤ 1.35 s ± 0.25 |
| 2 | Product shown | ≤ 3.0 s |
| 3 | Product runtime share | ≥ 35% |
| 4 | CTA | ≥ 2.5 s |
| 5 | Gaze | 0.6–0.8 toward camera |
| 6–10 | (capture grammar, speech, skin, assembly, audio per lock list) | pass/fail |

## FACS/Laban cheat sheet (UGC talking-head)

- **17 UGC-relevant AUs** with plain-language translations (AU12 = smile, …);
  full table in `cpcs.facs.au_catalog`.
- **Intensity A–E:** UGC stays **B–C**; D only for emphasis peaks; **E = mug**.
- **Genuine vs fake combos:** AU6+AU12 (Duchenne) real; AU4+AU12 mixed;
  AU1+AU12 polite; AU4+AU5+AU7 = negative flash.
- **UGC baseline Efforts:** light · sustained · direct · free.
- **Body catalog:** breath, weight shift, head, torso, shoulders, hands —
  micro-motion beats stillness.

## Reverse path

Pegasus slow-proxy: playback at 0.25×–0.5× to extract timing from a
reference UGC clip (see `cpcs.lab.runbooks` #1).

## Per-model notes

Veo 3.1: 8 s native audio · Sora 2 / Videos API: **deprecated** (shutdown
Sept 2026) · Kling 2.x: strong on movement, check skin · Runway Gen-4:
cinematic default, needs the anti-cinematic block. Model notes may become
outdated — always verify against current provider docs.

## Boundary

The lock list and checklist are authored, field-tested lab practice — the
checklist thresholds are deterministic, the style guidance is qualitative
(single-observer). Sora 2 notes are stale by design.
