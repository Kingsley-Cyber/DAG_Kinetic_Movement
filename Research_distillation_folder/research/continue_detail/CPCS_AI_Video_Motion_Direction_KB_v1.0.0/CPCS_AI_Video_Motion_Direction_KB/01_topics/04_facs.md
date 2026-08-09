# 04 — FACS: Action Units, Intensity, and Temporal Curves

## Executive finding

FACS is an observational coding system for visible facial movement. It is not an emotion detector and not a lie detector. The requested “44 AUs” must be handled carefully: public tables and datasets count facial AUs, action descriptors, head/eye codes, visibility codes, and gross behavior differently. CPCS stores original identifiers by group rather than inventing a universal flat cardinality. [S017; S018]

The full FACS manual is proprietary. This repository includes public names, broad anatomical bases, and engineering fields, but intentionally does not reproduce the manual’s detailed scoring criteria.

## Public facial/action-descriptor registry

| Code | Name | Broad anatomical basis | Visible action |
|---|---|---|---|
| 1 | Inner Brow Raiser | frontalis medial | raises medial brow |
| 2 | Outer Brow Raiser | frontalis lateral | raises lateral brow |
| 4 | Brow Lowerer | corrugator/depressor supercilii | draws brows down/medial |
| 5 | Upper Lid Raiser | levator palpebrae superioris | elevates upper lid |
| 6 | Cheek Raiser | orbicularis oculi orbital | raises cheek/narrows aperture |
| 7 | Lid Tightener | orbicularis oculi palpebral | tightens lids |
| 9 | Nose Wrinkler | levator labii superioris alaeque nasi | wrinkles nose |
| 10 | Upper Lip Raiser | levator labii superioris | raises upper lip |
| 11 | Nasolabial Deepener | zygomaticus minor | deepens nasolabial furrow |
| 12 | Lip Corner Puller | zygomaticus major | pulls corners up/lateral |
| 13 | Sharp Lip Puller | levator anguli oris; label varies | sharp lip-corner pull |
| 14 | Dimpler | buccinator | tightens corner/dimple |
| 15 | Lip Corner Depressor | depressor anguli oris | pulls corners down |
| 16 | Lower Lip Depressor | depressor labii inferioris | pulls lower lip down |
| 17 | Chin Raiser | mentalis | raises/protrudes lower lip |
| 18 | Lip Pucker | orbicularis/incisivii contribution | puckers lips |
| 20 | Lip Stretcher | risorius/platysma contribution | stretches corners lateral |
| 22 | Lip Funneler | orbicularis oris | funnels lips |
| 23 | Lip Tightener | orbicularis oris | tightens lips |
| 24 | Lip Pressor | orbicularis oris | presses lips |
| 25 | Lips Part | action descriptor | separates lips |
| 26 | Jaw Drop | jaw-opening action | drops jaw |
| 27 | Mouth Stretch | jaw/lip action | stretches mouth open |
| 28 | Lip Suck | orbicularis oris | rolls lips inward |
| 29 | Jaw Thrust | action descriptor | jaw forward |
| 30 | Jaw Sideways | action descriptor | jaw lateral |
| 31 | Jaw Clencher | masseter/jaw closers | clenches jaw |
| 32 | Lip Bite | action descriptor | bites lip |
| 33 | Cheek Blow | action descriptor | blows |
| 34 | Cheek Puff | oral pressure/buccinator | puffs cheeks |
| 35 | Cheek Suck | buccinator/oral pressure | draws cheeks inward |
| 36 | Tongue Bulge | tongue musculature | tongue presses cheek/lip |
| 37 | Lip Wipe | action descriptor | wipes lips |
| 38 | Nostril Dilator | nasalis alar | widens nostrils |
| 39 | Nostril Compressor | nasalis transverse | narrows nostrils |
| 41 | Lid Droop | reduced levator activity | upper lid droops |
| 42 | Slit | orbicularis oculi | slit-like eyes |
| 43 | Eyes Closed | closure action | eyes close |
| 44 | Squint | orbicularis/brow contribution | squints |
| 45 | Blink | orbicularis palpebral | brief bilateral closure |
| 46 | Wink | orbicularis oculi | unilateral closure |

Some listed items are action descriptors rather than single-muscle AUs. Anatomy should therefore be represented as a broad basis, not a claim that every code maps one-to-one to one muscle.

## Head and eye controls

| Code | Group | Meaning |
|---|---|---|
| 51 | head position or modifier | Head Turn Left |
| 52 | head position or modifier | Head Turn Right |
| 53 | head position or modifier | Head Up |
| 54 | head position or modifier | Head Down |
| 55 | head position or modifier | Head Tilt Left |
| 56 | head position or modifier | Head Tilt Right |
| 57 | head position or modifier | Head Forward |
| 58 | head position or modifier | Head Back |
| M57 | head position or modifier | Head Thrust Forward |
| M59 | head position or modifier | Head Nod |
| M60 | head position or modifier | Head Shake |
| M83 | head position or modifier | Head Up and to Side |
| 61 | eye position or modifier | Eyes Turn Left |
| 62 | eye position or modifier | Eyes Turn Right |
| 63 | eye position or modifier | Eyes Up |
| 64 | eye position or modifier | Eyes Down |
| 65 | eye position or modifier | Walleye |
| 66 | eye position or modifier | Cross-eye |
| M68 | eye position or modifier | Eyes Roll Up |
| 69 | eye position or modifier | Eyes Positioned at Other Person |
| M69 | eye position or modifier | Head or Eyes Move to Look at Other Person |

`M69` is treated as a relational gaze/head movement modifier, not a normal facial muscle AU. CPCS links gaze to an entity or spatial target and stores head pose continuously in degrees/quaternions; the FACS code remains a categorical annotation layer.

## Intensity

FACS uses ordinal intensity letters A–E for many AUs, with `0` for absence. CPCS maps `A..E` to `0.2..1.0` only to create a convenient unit interval. The mapping preserves order but does not claim that B is exactly twice A perceptually. OpenFace supplies 0–5 continuous intensity for a subset of AUs and separate presence models; these outputs must retain detector version, camera conditions, and confidence. [S019]

```json
{
  "au": "12",
  "side": "bilateral",
  "source_intensity": "C",
  "cpcs_unit_intensity": 0.6,
  "mapping_provenance": "CPCS_CONVENTION",
  "detector": null
}
```

## Expression motifs

| Motif | Required/formula | Optional | Status | Caution |
|---|---|---|---|---|
| duchenne_pattern_smile | ['AU6', 'AU12'] | ['AU25'] | EMPIRICAL/established prototype | Visible pattern, not proof of genuine happiness |
| happiness_prototype | ['AU6', 'AU12'] | ['AU25', 'AU26'] | EMPIRICAL/established prototype | Context dependent |
| surprise_prototype | ['AU1', 'AU2', 'AU5', 'AU25', 'AU26'] | ['AU27'] | EMPIRICAL/established prototype | Context dependent |
| fear_prototype | ['AU1', 'AU2', 'AU4', 'AU5', 'AU7', 'AU20', 'AU26'] | ['AU25'] | EMPIRICAL/established prototype | Context dependent |
| anger_prototype | ['AU4', 'AU5', 'AU7', 'AU23'] | ['AU24', 'AU17', 'AU38'] | EMPIRICAL/established prototype | Context dependent |
| sadness_prototype | ['AU1', 'AU4', 'AU15'] | ['AU17'] | EMPIRICAL/established prototype | Context dependent |
| disgust_prototype | ['AU9', 'AU15', 'AU16'] | ['AU10', 'AU17'] | EMPIRICAL/established prototype | Context dependent |
| contempt_prototype | ['unilateral_AU14'] | ['unilateral_AU12'] | EMPIRICAL/established prototype | Context dependent |
| pain_pspi | AU4 + max(AU6,AU7) + max(AU9,AU10) + AU43 | — | EMPIRICAL/established prototype | Context dependent |
| concerned | ['low_AU1', 'low_AU4'] | ['AU15', 'AU17', 'AU24'] | CPCS_CONVENTION | Context dependent |
| skeptical | ['unilateral_AU2', 'unilateral_AU14'] | ['AU4', 'AU23'] | CPCS_CONVENTION | Context dependent |
| amused_but_restrained | ['AU6', 'low_AU12'] | ['AU14', 'AU24'] | CPCS_CONVENTION | Context dependent |
| dupers_delight_hypothesis | ['possible_low_unilateral_AU12'] | ['AU14', 'AU24'] | UNVERIFIED_HYPOTHESIS | Do not use as deception detector |
| micro_expression_profile | — | — | EMPIRICAL/established prototype | No universal duration cutoff |

Du, Tao, and Martinez provide basic and compound expression prototypes. These are useful generation priors, not deterministic labels of inner emotion. The Prkachin–Solomon Pain Intensity formulation is specific to pain-expression research and cannot diagnose pain from an arbitrary video. [S021, E1454–E1462; S022, pp.82–97; S023, Eq.1]

A Duchenne-pattern smile uses AU6 + AU12, but even that visible pattern is not proof of genuine happiness. “Duper’s delight” is retained only as an unverified fictional-performance motif with extremely low confidence; it must never be used to judge deception.

## Timing: onset, apex, offset

Every AU event should have:

- onset start;
- apex start and end;
- offset end;
- easing/curve;
- peak intensity;
- laterality;
- masking/competing AUs;
- confidence and detector/annotator provenance.

Spontaneous and posed expressions can differ statistically in timing, smoothness, co-peaking, asymmetry, and duration, but no single cue is definitive. Micro-expression datasets also use different duration thresholds. CPCS therefore stores actual times and dataset/profile identifiers instead of a hard global “micro-expression < X ms” law. [S020, pp.22–35; S070, pp.5826–5846]

## Nuanced expression examples

**Concerned:** low AU1 + low AU4, optional AU15/17, slight head tilt, sustained gaze. This is a CPCS motif with medium-low confidence.

**Skeptical:** unilateral AU2 and/or AU14, possible AU4/23, head tilt, side glance. Laterality is essential; mirroring it into a bilateral expression changes the read.

**Amused but restrained:** AU6 with AU12 capped below full smile, optional AU14, and AU24 suppressing lip separation.

**Ambiguous fear/anger:** AU4+5+7 can be contextualized with advancing posture/high dominance for anger-like threat or retreating/enclosing posture/low dominance for fear-like response. Face-only coding should not resolve the intent.

## AI-video prompt compilation

Models rarely interpret raw strings such as `AU4=0.6` reliably. CPCS should preserve AU tracks internally and compile them into visible descriptions or, where supported, a reference/performance video:

> “Inner brows rise slightly while drawing together; upper eyelids open modestly, lower lids tighten, and the mouth remains pressed. The expression peaks for three frames, then softens asymmetrically on the right.”

A performance-reference adapter is preferred because it carries timing and co-articulation more directly than prose.

## Quality checks

- no AU event outside the actor’s visibility interval;
- no impossible side label for a bilateral-only event profile;
- apex intensity reached by the specified time;
- head/eye target consistency;
- no “emotion truth” assertion derived solely from AUs;
- detector output never overwrites expert/canonical values without provenance.

## References and locators

- **[S017]** Paul Ekman; Wallace V. Friesen; Joseph C. Hager (2002), *Facial Action Coding System, 2nd ed.*. **Locator:** AU chapters; intensity scoring; head/eye sections; proprietary pagination  
- **[S018]** Ying-li Tian; Takeo Kanade; Jeffrey F. Cohn (2001), *Recognizing Action Units for Facial Expression Analysis*. **Locator:** Public AU table and discussion of 44 FACS action units/intensity  
- **[S019]** OpenFace project; Tadas Baltrušaitis et al. (2026), *OpenFace Action Units Documentation*. **Locator:** Supported AUs; presence and 0–5 intensity outputs  
- **[S020]** Marian Stewart Bartlett et al. (2006), *Automatic Recognition of Facial Actions in Spontaneous Expressions*. **Locator:** pp.22–35; p.23 spontaneous-versus-posed dynamics  
- **[S021]** Shichuan Du; Yong Tao; Aleix M. Martinez (2014), *Compound Facial Expressions of Emotion*. **Locator:** PNAS 111(15), E1454–E1462; tables and supplementary AU prototypes  
- **[S022]** Kenneth M. Prkachin; Patricia E. Solomon (2008), *The Face of Pain: Evidence for a Core Configuration*. **Locator:** Pain 134(1–2), pp.82–97; PSPI formulation  
- **[S023]** Steffen Kaltwang; Ognjen Rudovic; Maja Pantic (2012), *Pain Recognition Based on Joint Feature Selection and Nonlinear Modeling of Facial Expressions*. **Locator:** p.370, Eq.1: AU4 + max(AU6,AU7) + max(AU9,AU10) + AU43  
- **[S069]** MagicFace authors (2025), *MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control*. **Locator:** §II-A historical AU convention; §III relative AU variation  
- **[S070]** Xianye Ben et al. (2022), *Video-Based Facial Micro-Expression Analysis: A Survey of Datasets, Features and Algorithms*. **Locator:** IEEE TPAMI 44(9), pp.5826–5846
