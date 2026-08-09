# 11 — Emotional Dynamics: VAD Trajectories

## Executive finding

Valence, Arousal, and Dominance are useful because they permit continuous trajectories instead of static emotion labels. Russell’s circumplex grounds valence/arousal; Warriner et al. and Mohammad provide lexical VAD norms. Lexical ratings are not direct measurements of a performer’s body state, and the NRC VAD data have licensing/redistribution conditions. CPCS references the lexicon but does not copy it. [S046, pp.1161–1178; S047, pp.1191–1207; S048, pp.174–184; S049]

## Coordinate model

All dimensions use `[0,1]`:

- Valence: unpleasant to pleasant;
- Arousal: deactivated to activated;
- Dominance: low agency/controlled to agentic/in-control.

CPCS adds **confidence**, **certainty**, and **engagement** because dominance alone cannot distinguish “I control the situation” from “I am certain,” and arousal cannot distinguish activation from attention.

## Engineering seed anchors

| Label | Valence | Arousal | Dominance | Status |
|---|---|---|---|---|
| joy | 0.85 | 0.72 | 0.72 | CPCS seed, not lexicon value |
| calm | 0.76 | 0.2 | 0.62 | CPCS seed, not lexicon value |
| anger | 0.15 | 0.82 | 0.7 | CPCS seed, not lexicon value |
| fear | 0.1 | 0.84 | 0.25 | CPCS seed, not lexicon value |
| sadness | 0.12 | 0.25 | 0.28 | CPCS seed, not lexicon value |
| surprise | 0.55 | 0.78 | 0.5 | CPCS seed, not lexicon value |
| disgust | 0.12 | 0.63 | 0.55 | CPCS seed, not lexicon value |
| contempt | 0.22 | 0.48 | 0.68 | CPCS seed, not lexicon value |
| relief | 0.8 | 0.3 | 0.58 | CPCS seed, not lexicon value |
| shame | 0.18 | 0.38 | 0.18 | CPCS seed, not lexicon value |

These values are deliberately labeled `CPCS_CONVENTION`. They initialize motion planning and should be replaced or recalibrated by licensed norms, project annotations, and model experiments where appropriate.

## Trajectory representation

A trajectory consists of keyframes with time, VAD, extension dimensions, label hint, cause event, and uncertainty. Interpolation may be linear, cubic Hermite, monotone cubic, ease, or step. A sudden appraisal change can still produce lagged body and face responses; CPCS therefore permits separate latent/intent, face, body, voice, and camera channels.

```json
{
  "affect_track": [
    {"t": 0.0, "vad": [0.62,0.35,0.55], "label_hint": "calm approach"},
    {"t": 2.0, "vad": [0.40,0.62,0.52], "cause_event": "challenge"},
    {"t": 4.0, "vad": [0.18,0.88,0.65], "label_hint": "angry conflict"},
    {"t": 8.0, "vad": [0.72,0.28,0.62], "label_hint": "relief"}
  ],
  "interpolation": "cubic_hermite"
}
```

## VAD-to-motion mapping

**Arousal** has the most direct motion priors: event density, speed, acceleration, amplitude, and hold length. **Dominance** often affects rising/spreading/advancing Shape, kinesphere, base stability, and whether the actor yields. **Valence** is more context-sensitive: positive affiliation may open/spread, but positive pride can be still and high-dominance; negative anger advances while negative fear may retreat.

Confidence and certainty influence directness, false starts, checking gaze, and phase cleanliness. Engagement influences gaze/torso orientation and response latency.

These are conditional priors, not universal equations. BoME and LMA-emotion work support the usefulness of bodily motor elements, but annotation scope and culture remain limitations. [S032; S071]

## VAD-to-face mapping

| VAD region | Candidate motifs | Confidence |
|---|---|---|
| positive_high_arousal | AU6+12, AU25/26 optional | medium |
| negative_high_arousal_high_dominance | AU4+7, AU23/24 optional | medium |
| negative_high_arousal_low_dominance | AU1+2+4+5+20/26 fear prototype | medium |
| negative_low_arousal_low_dominance | AU1+4+15 sadness prototype | medium |
| ambiguous | blend or channel conflict; no deterministic AU set | high for caution |

A face is a channel, not a direct VAD sensor. The same AU combination can occur in different contexts, and masking can produce channel conflict—for example, a low-valence body with a socially maintained smile.

## Transition types

- **Gradual:** smooth movement through the space over a phrase.
- **Sudden:** steep appraisal change, with physically plausible channel lag.
- **Masked:** internal/intent track changes while observable channels delay or oppose it.
- **Mixed:** channels express different components at once.

## Culture and context

Display rules, relationship, status, genre, camera visibility, and actor baseline condition expression. Cross-cultural gesture variation requires project-specific profiles. CPCS must not infer culture from appearance; it uses explicit production metadata. [S033]

## Prompt example

> “Begin calm and moderately confident. At the interruption, arousal rises sharply over six frames while valence falls; the body advances slightly but dominance remains uncertain, creating a half-step and bound shoulders. After the other person yields, arousal decays over one second, the torso spreads, and the gaze steadies before the smile appears.”

This directs a trajectory and channel ordering rather than asking the model for one static “angry-to-happy” label.

## References and locators

- **[S007]** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013), *Laban Effort and Shape Analysis of Affective Hand and Arm Movements*. **Locator:** pp.343–348; §§II–V; Tables I–IV  
- **[S021]** Shichuan Du; Yong Tao; Aleix M. Martinez (2014), *Compound Facial Expressions of Emotion*. **Locator:** PNAS 111(15), E1454–E1462; tables and supplementary AU prototypes  
- **[S030]** Haiyang Liu et al. (2022), *BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis*. **Locator:** ECCV 2022; dataset statistics and §§3–5  
- **[S032]** Andreas Aristidou et al. (2015), *Emotion Analysis and Classification Using LMA Entities*. **Locator:** Computer Graphics Forum 34(6), pp.262–276  
- **[S033]** Sotaro Kita (2009), *Cross-Cultural Variation of Speech-Accompanying Gesture: A Review*. **Locator:** Gesture 9(2), review sections  
- **[S046]** James A. Russell (1980), *A Circumplex Model of Affect*. **Locator:** JPSP 39(6), pp.1161–1178  
- **[S047]** Amy Beth Warriner; Victor Kuperman; Marc Brysbaert (2013), *Norms of Valence, Arousal, and Dominance for 13,915 English Lemmas*. **Locator:** Behavior Research Methods 45, pp.1191–1207  
- **[S048]** Saif M. Mohammad (2018), *Obtaining Reliable Human Ratings of Valence, Arousal, and Dominance for 20,000 English Words*. **Locator:** ACL 2018, pp.174–184; §§2–5  
- **[S049]** Saif M. Mohammad (2025), *NRC VAD Lexicon v2*. **Locator:** Official v2.1 page; released March 2025; arXiv:2503.23547  
- **[S071]** Chenyan Wu et al. (2023), *Bodily Expressed Emotion Understanding Through Integrating Laban Movement Analysis*. **Locator:** BoME dataset and experiment sections
