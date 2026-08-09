# 03 — Motion Grammar: Phase State Machines

## Executive finding

The requested seven-phase sequence is a good **CPCS production grammar**, not an established universal motion model. Gesture studies commonly distinguish preparation, optional holds, a meaning-bearing stroke, and retraction; BML exposes behavior-specific synchronization points such as `start`, `ready`, `stroke_start`, `stroke`, `stroke_end`, `relax`, and `end`; animation contributes anticipation, follow-through, overlap, and timing. CPCS synthesizes these with action biomechanics into `Initiation → Preparation → Acceleration → Stroke → Overshoot → Recovery → Settle`. [S013; S014; S015; S016]

The compiler must permit omission and merging. A blink may have no useful preparation; continuous walking usually has no settle between steps; a held conversational gesture can add prestroke/poststroke holds; a collision can interrupt recovery.

## Canonical phases

| # | Phase | Purpose | Optional | Carries | Basis |
|---|---|---|---|---|---|
| 1 | initiation | first observable or inferred commitment | True | intent, attention shift, deception setup | CPCS synthesis |
| 2 | preparation | organize support, alignment, backswing, guard, anticipation | True | readability, feint information, pre-tension | gesture preparation + animation anticipation + biomechanics |
| 3 | acceleration | increase linear/angular velocity toward focal event | False | force development, urgency, commitment | biomechanical action phase |
| 4 | stroke | meaning-bearing apex, target acquisition, or contact | False | semantic payload, contact, emotion accent | Kendon/McNeill gesture stroke + action apex |
| 5 | overshoot | post-apex continuation due to momentum/follow-through/exaggeration | True | perceived force, style exaggeration | animation + biomechanics |
| 6 | recovery | retract, recoil, redirect, or return toward stable organization | True | defensive readiness, recoil, aftereffect | gesture retraction/BML relax-to-end |
| 7 | settle | dissipate residual motion and establish next stable state | True | weight resolution, secondary motion, reaction beat | CPCS production phase |

The word **Stroke** is role-based. In a gesture it is the semantically meaningful excursion; in a punch it can be contact or maximum extension; in a reach it can be grasp onset; in locomotion, “stroke” may be renamed `contact` to avoid implying a communicative gesture.

## State-machine rules

Default transitions follow phase order, but the schema permits `initiation→acceleration`, `preparation→stroke`, `stroke→recovery`, `stroke→settle`, and `recovery→next initiation`. Interruptions are first-class events. A block/collision may branch to a new interaction chain; a feint may abort before stroke; a moving target may cause retargeting; balance loss may invoke protective recovery.

Every phase should expose start/end time, progress curve, primary joints, contacts, force role, semantic role, emotional role, and confidence. This lets the same physical interval carry several functions without conflating them. For example, a punch’s Preparation may carry deception, force preloading, and visible anger at once.

## Timing presets

| Preset | Normalized phase ratios | Status |
|---|---|---|
| explosive | initiation:0.03 / preparation:0.09 / acceleration:0.19 / stroke:0.22 / overshoot:0.14 / recovery:0.22 / settle:0.11 | CPCS_CONVENTION |
| ballistic | initiation:0.03 / preparation:0.07 / acceleration:0.21 / stroke:0.22 / overshoot:0.20 / recovery:0.18 / settle:0.09 | CPCS_CONVENTION |
| controlled | initiation:0.07 / preparation:0.17 / acceleration:0.17 / stroke:0.22 / overshoot:0.07 / recovery:0.19 / settle:0.11 | CPCS_CONVENTION |
| sustained | initiation:0.07 / preparation:0.14 / acceleration:0.17 / stroke:0.27 / overshoot:0.06 / recovery:0.18 / settle:0.11 | CPCS_CONVENTION |
| microgesture | initiation:0.08 / preparation:0.10 / acceleration:0.16 / stroke:0.30 / overshoot:0.04 / recovery:0.18 / settle:0.14 | CPCS_CONVENTION |

These ratios sum to one and are **initialization presets only**. They should be learned per action, actor, genre, and model through immutable experiments. A generated clip that looks “floaty” may need shorter acceleration and more localized jerk, but blindly applying an explosive preset can remove intended hesitation or weight.

## Action decompositions

| Action | CPCS phase interpretation |
|---|---|
| jab | gaze/guard intent → minimal hidden preparation → lead-side acceleration → contact/max extension → small overshoot → rapid guard return → stance restabilizes |
| cross_punch | ground/hip commitment → rear-side load → leg–pelvis–trunk–arm acceleration → contact → rotational continuation → recoil/deceleration → guard reset |
| roundhouse_kick | weight shift → chamber/pivot → pelvis–thigh–shank acceleration → foot/shin contact → rotational continuation → re-chamber/step-through → stance reset |
| block | threat orientation → interception preparation → blocking surface acceleration → contact/deflection → redirect → return/counter → new guard |
| evade | attention/weight release → base organization → COM leaves line → maximum clearance → optional angle continuation → reorient → counter-ready position |
| reach | gaze to object → postural organization → hand approach → grasp/contact → optional miss overshoot → transport/retract → new contact state |
| turn | eyes/head orient → base preload → pelvis/trunk rotate → new orientation → secondary lag → braking → stable posture |
| walk_step | weight transfer → swing limb unload → swing advances → foot contact → COM progresses → opposite transition → normally no settle in continuous gait |

Combat technique is not identical across styles or performers. Walilko et al. provide protocol-specific boxing measurements, while the axe-kick review summarizes technique phases and study variation. CPCS therefore stores decomposition templates as editable priors, not fixed coaching doctrine. [S028, pp.710–719; S029, pp.3–13]

## Phase-level expressive roles

- **Force:** preparation and acceleration establish support/velocity; stroke carries contact; overshoot/follow-through externalizes commitment; recovery shows recoil or control.
- **Deception:** initiation/preparation can be hidden, redirected, repeated, or aborted; a false preparation can create a branch.
- **Emotion:** facial/postural onset may lead the physical action, peak at stroke, or lag as aftermath. Do not force all channels to peak simultaneously.
- **Readability:** anticipation and settle give the viewer causal boundaries. A realistic action can still be unreadable when the camera or edit erases these phases.

## XML beat ordering example

```xml
<action id="cross_01" actor="fighter_a" duration="1.10">
  <phase id="initiation" start="0.00" end="0.06" semantic="commit"/>
  <phase id="preparation" start="0.06" end="0.20" force="preload" deception="0.25"/>
  <phase id="acceleration" start="0.20" end="0.43" force="propulsive"/>
  <phase id="stroke" start="0.43" end="0.50" contact="fist_to_guard"/>
  <phase id="overshoot" start="0.50" end="0.61"/>
  <phase id="recovery" start="0.61" end="0.91" target="guard"/>
  <phase id="settle" start="0.91" end="1.10"/>
</action>
```

## Compiler requirements

- Pin contact events before time warping and preserve event order.
- Do not synthesize overshoot when the interaction constraint forbids it.
- Keep semantic apex and physical contact as separately addressable events.
- Expose skipped phases rather than inserting zero-duration ghosts.
- Validate that all phase durations are non-negative and exactly cover the action interval when coverage is required.
- Permit overlapping actions and nested phase hierarchies for two-person exchanges.

## References and locators

- **[S013]** SAIBA community (2011), *Behavior Markup Language 1.0 Specification*. **Locator:** Behavior phases, sync points, and synchronization  
- **[S014]** McNeill Lab, University of Chicago (2026), *Gesture Phases*. **Locator:** Preparation, prestroke hold, stroke, poststroke hold, retraction  
- **[S015]** Adam Kendon (2004), *Gesture: Visible Action as Utterance*. **Locator:** Chapters on gesture units, phrases, and movement phases  
- **[S016]** Frank Thomas; Ollie Johnston (1981), *The Illusion of Life: Disney Animation*. **Locator:** Chapters on anticipation, follow-through, timing, arcs, exaggeration  
- **[S027]** David A. Winter (2009), *Biomechanics and Motor Control of Human Movement, 4th ed.*. **Locator:** Chs.2–4 kinematics; Chs.5–7 kinetics, anthropometry, signal processing  
- **[S028]** Timothy J. Walilko; David C. Viano; Cynthia A. Bir (2005), *Biomechanics of the Head for Olympic Boxer Punches to the Face*. **Locator:** Br J Sports Med 39(10), pp.710–719  
- **[S029]** D. R. Mailapalli et al. (2015), *Biomechanics of the Taekwondo Axe Kick: A Review*. **Locator:** Archives of Budo SAMAES 11, pp.3–13  
- **[S039]** Selected peer-reviewed sports-biomechanics sources (2020), *Kinetic-Chain Evidence for Overarm Striking*. **Locator:** Segment sequencing, proximal-to-distal transfer, effective mass  
- **[S073]** Durell Bouchard; Norman I. Badler (2007), *Semantic Segmentation of Motion Capture Using Laban Movement Analysis*. **Locator:** IVA 2007, LNCS 4722, pp.37–44  
- **[S075]** Anh-Tuan Truong; Titus Zaharia (2017), *Dynamic Gesture Recognition with Laban Movement Analysis and Hidden Markov Models*. **Locator:** §3 descriptors/HMM; experiments and limitations
