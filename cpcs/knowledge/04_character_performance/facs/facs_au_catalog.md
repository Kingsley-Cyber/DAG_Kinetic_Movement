---
id: cpcs.facs.au_catalog
kind: vocabulary
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §4, SRC-002-U01, SRC-002-U02]
primary_route: cpcs/knowledge/04_character_performance/facs/
interfaces: []
---

# FACS AU Catalog (Public Vocabulary Layer)

A **version-aware public vocabulary layer**, not a reproduction of the
proprietary manual. Per-AU operational region, side model, intensity, and
typical machine-detection status. Representative subset; full table in
SRC-002 §4.

| AU | Public descriptor | Region | Side model | Machine status |
|----|-------------------|--------|------------|----------------|
| AU1 | Inner Brow Raiser | upper face | bilateral/side-aware | detectable candidate |
| AU2 | Outer Brow Raiser | upper face | bilateral/side-aware | detectable candidate |
| AU4 | Brow Lowerer | upper face | bilateral/side-aware | detectable candidate |
| AU6 | Cheek Raiser | eye/cheek | bilateral/side-aware | detectable candidate |
| AU7 | Lid Tightener | eye | side-aware | difficult/confusable |
| AU12 | Lip Corner Puller | mouth | side-aware | common automation target |
| AU14 | Dimpler | cheek | side-aware | common automation target |
| AU15 | Lip Corner Depressor | mouth | side-aware | common automation target |
| AU17 | Chin Raiser | chin | bilateral/side-aware | common automation target |
| AU23 | Lip Tightener | mouth | bilateral/side-aware | confusable with AU24 |
| AU24 | Lip Pressor | mouth | bilateral/side-aware | common candidate |
| AU25 | Lips Part | mouth | bilateral | common automation target |
| AU26 | Jaw Drop | jaw | bilateral | common automation target |
| AU43 | Eyes Closed | eye | side-aware | common candidate |
| AU45 | Blink | eye | side-aware | common automation target |
| AU41/42/44 | legacy/reassigned | eye/brow | reject unless version-qualified | reject unless version-qualified |

(Full 30+ row table in source §4.)

## Machine-status legend

`detectable_candidate` · `common_automation_target` · `candidate` ·
`limited_automation` · `difficult/confusable` · `version/source controlled`.
Open question Q1 (SRC-002 §31): which AU subset should CPCS support natively
versus through semantic projection?

## UGC and combat usage patterns (SRC-010 EXTEND)

The lab's references add field-tested usage guidance on top of this
vocabulary (see `cpcs.ugc.realism_reference`, `cpcs.combat.math_metrics_layer`):

- **UGC talking-head:** 17 UGC-relevant AUs with plain-language translations;
  intensity stays **B–C** (D only for emphasis peaks; E = mug).
- **Genuine vs fake combos:** AU6+AU12 (Duchenne) reads real; AU4+AU12 mixed;
  AU1+AU12 polite; AU4+AU5+AU7 = negative flash.
- **Combat:** intensity runs **C–E** (E only at impact); 8 AU combos for
  fight faces; 3 rules — AU4+AU7 before contact, AU12 suppressed during
  threat, asymmetric AU43/AU45 blinks at impact.
- v004's plastic-skin collapse (skin realism 5→1) is a lab-original failure
  tied to the absence of microtexture — never "smooth" (p001,
  isolated_confirmed).

These are single-observer, render-derived usage patterns — not new AU
definitions; the vocabulary table above remains authoritative.
