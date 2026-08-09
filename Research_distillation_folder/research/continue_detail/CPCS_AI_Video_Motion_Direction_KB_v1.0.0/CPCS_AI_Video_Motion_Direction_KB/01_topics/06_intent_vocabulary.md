# 06 — Intent Layer: Abstract Motion Intent Vocabulary

## Executive finding

Intent must sit above motion. One intent can compile into many actions, and the same action can serve different intents. A pointing gesture may invite, warn, accuse, direct, or dismiss depending on timing, gaze, relationship, and context. CPCS therefore represents `P(motion | intent, culture, relationship, context, actor, style, camera)` rather than a one-to-one table.

BML is useful downstream because it separates planning from behavior realization, while EMOTE, BEAT, BoME, and movement-emotion research supply examples of parameterized or annotated expressive behavior. None establishes a universal intent-to-pose dictionary. [S013; S030; S031; S032; S071]

## Canonical intent priors

The following ranges are **CPCS priors**, not universal psychological facts. In the Effort shorthand, high W means Strong, high T Sudden, high S Direct, and high F Bound.

| Intent | Goal | Effort prior ranges | Body priors | Face priors | Confidence |
|---|---|---|---|---|---|
| threaten | increase expected cost of noncompliance | W[0.65, 1] T[0.45, 1] S[0.65, 1] F[0.45, 0.9] | upper_lower grounding, advancing core-distal, direct gaze | anger prototype, AU4+AU7 | 0.55 |
| comfort | reduce distress and signal safety | W[0.15, 0.45] T[0.05, 0.35] S[0.35, 0.7] F[0.2, 0.55] | breath, core-distal reach, soft head-tail orientation | low AU1, low AU6+12 optional | 0.55 |
| seduce | invite intimacy while preserving optionality | W[0.2, 0.55] T[0.1, 0.45] S[0.25, 0.65] F[0.1, 0.45] | curved pathways, delayed distal gesture, gaze approach/withdraw | low AU12, AU6 optional, head tilt | 0.35 |
| hesitate | delay commitment while evaluating alternatives | W[0.15, 0.45] T[0.25, 0.65] S[0.1, 0.45] F[0.55, 0.95] | false starts, initiation without stroke, withdrawal | low AU1+4, gaze shifts, AU24 | 0.65 |
| celebrate | display positive outcome and recruit shared attention | W[0.35, 0.75] T[0.65, 1] S[0.35, 0.85] F[0.05, 0.45] | core-distal expansion, upper-lower jump/reach, repetition | Duchenne-pattern smile, AU25/26 | 0.7 |
| hide | reduce detectability of self/object/information/emotion | W[0.1, 0.45] T[0.1, 0.65] S[0.15, 0.55] F[0.6, 1] | enclosing, retreating, near kinesphere | gaze aversion, AU24, masking | 0.55 |
| challenge | test status, competence, or boundary | W[0.55, 0.9] T[0.35, 0.8] S[0.65, 1] F[0.5, 0.9] | stable base, direct frontal orientation | AU4, AU7, unilateral AU14 optional | 0.55 |
| submit | yield status/control | W[0.05, 0.35] T[0.05, 0.45] S[0.1, 0.5] F[0.45, 0.9] | sinking, enclosing, head/eyes lower | AU1, AU15 optional, gaze down | 0.45 |
| invite | open a path for participation/approach | W[0.1, 0.4] T[0.1, 0.45] S[0.55, 0.9] F[0.15, 0.5] | open palm, spreading, spoke/arc toward available space | low AU6+12 optional, gaze target then receiver | 0.6 |
| dismiss | terminate relevance or interaction | W[0.25, 0.7] T[0.35, 0.85] S[0.45, 0.9] F[0.35, 0.8] | distal flick, head turn away, withdraw attention | unilateral AU14, AU23 optional | 0.55 |
| assert | state/enact boundary or claim confidently | W[0.5, 0.85] T[0.3, 0.75] S[0.7, 1] F[0.55, 0.9] | stable base, direct gesture, clear stroke hold | low AU4/7, low AU23/24 | 0.6 |
| deceive | cause receiver to adopt a false belief | W[0.1, 0.9] T[0.1, 0.9] S[0.1, 0.9] F[0.1, 0.9] | no universal motor signature | no deterministic AU signature | 0.1 |
| protect | shield self/other/object from threat | W[0.55, 0.95] T[0.45, 1] S[0.65, 1] F[0.65, 1] | interpose body/limb, expand barrier, ground support | AU4, contextual AU5/7 | 0.65 |
| protest | publicly oppose action/rule/claim | W[0.45, 0.9] T[0.45, 0.9] S[0.55, 0.95] F[0.45, 0.85] | repeated emphatic strokes, collective synchrony | anger or concern motifs, speech | 0.45 |
| surrender | make nonresistance legible and transfer control | W[0.05, 0.35] T[0.25, 0.75] S[0.65, 0.95] F[0.55, 0.95] | hands visible/open, object release, slowed compliance | gaze monitoring, fear/concern contextual | 0.65 |
| dominate | control hierarchy, space, tempo, or options | W[0.55, 1] T[0.2, 0.85] S[0.65, 1] F[0.55, 1] | occupy space, control pace, stable gaze | low-medium AU4/7, unilateral AU14 optional | 0.5 |
| read_room | sample social state before action | W[0.1, 0.45] T[0.05, 0.4] S[0.05, 0.35] F[0.35, 0.75] | gaze scan, small head turns, minimal commitment | low AU1/2, low AU4 optional | 0.6 |
| uncertain_aggression | pressure while preserving retreat/deniability | W[0.45, 0.85] T[0.45, 0.9] S[0.35, 0.8] F[0.65, 1] | advance-retreat oscillation, guarded shoulders, false starts | AU4+7, AU20/23 optional | 0.5 |
| reassure | increase confidence in safety/competence/predictability | W[0.15, 0.45] T[0.05, 0.35] S[0.55, 0.85] F[0.25, 0.6] | stable posture, slow nod, open hand | low AU6+12, low AU1 | 0.55 |
| warn | draw attention to risk and induce protective action | W[0.35, 0.8] T[0.6, 1] S[0.75, 1] F[0.55, 0.9] | direct point/stop, gaze hazard then receiver | AU1+2+5 or AU4 contextual | 0.65 |

`deceive` deliberately has near-zero mapping confidence. There is no universal motor or facial signature for deception. CPCS can direct an actor to portray a deceptive beat, but it must not use visible motion to decide whether a real person is lying.

## Multi-scale compilation

- **Face only:** select AU/gaze/head motifs and suppress unsupported body claims.
- **Gesture:** add handshape, target, pathway, stroke, and hold.
- **Full body:** add BESS, support, connectivity, locomotion, and kinesphere.
- **Posture:** use sustained shape/body organization with low event density.
- **Group:** add formation, synchrony, turn-taking, leader/follower, and shared target.

An intent plan should return multiple realizations with exclusions. `comfort` might compile to a gentle touch, a held open palm without contact, respectful distance with a slow nod, or verbal reassurance. The appropriate version depends on culture, relationship, consent, and scene blocking.

## Cultural variation

Cross-cultural gesture research supports a culture-conditioned approach rather than a “universal gesture” database. CPCS culture profiles should contain community/region, formality, relationship, gesture variant, meaning distribution, taboo/restriction, evidence, and confidence. Production culture and intended audience culture may differ and must both be recorded. [S033]

Rules:

- never infer universality from one corpus;
- allow a no-gesture realization;
- preserve local variants rather than normalizing them away;
- use consultants/validated corpora for high-stakes representation;
- keep culture separate from ethnicity or appearance inference.

## Ambiguous intents

**Reading the room** is encoded as low commitment, indirect attention, small head/gaze scans, poststroke holds, and delayed selection—not as one gesture.

**Uncertain aggression** combines advancing pressure with retreat options: bound flow, incomplete preparations, forward/back weight oscillation, guarded shoulders, and inconsistent gaze. The ambiguity is intentional and should survive compilation.

**Assert vs dominate:** both can be direct and stable. Assert preserves the receiver’s options and uses a bounded claim; dominate controls space, tempo, and available choices. The interaction graph and camera framing help distinguish them.

## Example intent plan

```yaml
intent: protect
beneficiary: child_01
threat: falling_object_01
confidence: 0.88
realization_candidates:
  - predicate_chain: [approach, shield, support]
    body: [upper_lower_grounding, spreading_barrier]
    effort: {weight: 0.78, time: 0.92, space_effort: 0.94, flow: 0.86}
  - predicate_chain: [grasp, pull, retreat]
    constraint: no_collision_with_child
exclusions:
  - strike_threat
culture_profile: scene_specific
```

## Learning strategy

Curated intent records should initialize a conditional graph. Immutable experiments store prompt, model, seed, output, annotations, and success measures. Derived weights learn which realization works for each model/genre without changing the original definition of `protect`, `comfort`, or `challenge`.

Recommended training targets are distributions over candidate realization features, not a single “correct” pose. Retrieval from annotated examples followed by constraint-aware reranking is preferable to unconstrained generation of a mapping from scratch.

## References and locators

- **[S013]** SAIBA community (2011), *Behavior Markup Language 1.0 Specification*. **Locator:** Behavior phases, sync points, and synchronization  
- **[S015]** Adam Kendon (2004), *Gesture: Visible Action as Utterance*. **Locator:** Chapters on gesture units, phrases, and movement phases  
- **[S030]** Haiyang Liu et al. (2022), *BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis*. **Locator:** ECCV 2022; dataset statistics and §§3–5  
- **[S031]** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000), *The EMOTE Model for Effort and Shape*. **Locator:** SIGGRAPH 2000, pp.173–182  
- **[S032]** Andreas Aristidou et al. (2015), *Emotion Analysis and Classification Using LMA Entities*. **Locator:** Computer Graphics Forum 34(6), pp.262–276  
- **[S033]** Sotaro Kita (2009), *Cross-Cultural Variation of Speech-Accompanying Gesture: A Review*. **Locator:** Gesture 9(2), review sections  
- **[S067]** Ali-Akbar Samadani; Rob Gorbet; Dana Kulić (2020), *Affective Movement Generation Using Laban Effort and Shape and Hidden Markov Models*. **Locator:** Generation method, evaluation, limitations  
- **[S071]** Chenyan Wu et al. (2023), *Bodily Expressed Emotion Understanding Through Integrating Laban Movement Analysis*. **Locator:** BoME dataset and experiment sections
