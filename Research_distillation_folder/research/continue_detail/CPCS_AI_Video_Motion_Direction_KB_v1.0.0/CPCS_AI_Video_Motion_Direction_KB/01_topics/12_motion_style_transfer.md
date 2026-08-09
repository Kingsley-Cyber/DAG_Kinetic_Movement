# 12 — Style Transfer in Motion

## Executive finding

CPCS should define style as a transform over a protected choreography record. Identity, action predicates, root path, contact topology, phase order, target/object state, and safety constraints are invariants by default. Style may time-warp phases, exaggerate poses, alter squash/stretch, add secondary motion, change frame cadence/camera/rendering, and selectively relax geometry—without silently changing what happened.

Learned motion-style-transfer research demonstrates partial content/style separation and body-part-local transfer, but no method guarantees perfect disentanglement. [S050; S051; S052]

## Invariants and transforms

The compiler order is:

1. lock invariants;
2. apply monotonic timing warp;
3. apply spatial/pose exaggeration;
4. re-solve contacts and inverse kinematics;
5. add secondary motion;
6. transform camera;
7. apply rendering style;
8. revalidate action predicates and contacts.

This order matters. Applying a large anime smear before contact re-solving can make a hand appear through a face; applying camera style before action validation can hide a failed interaction.

## Style profiles

| Profile | Cadence | Exaggeration | Devices | Contact policy |
|---|---|---|---|---|
| anime | variable/held | [0.6, 1.0] | smears, impact frames, speed lines, holds, dramatic zooms | preserve semantic contact; permit graphic abstraction |
| family_feature_cg | smooth theatrical | [0.35, 0.75] | clear silhouettes, appeal, overlap, readable anticipation | physical readability with controlled stylization |
| documentary | natural capture | [0, 0.2] | handheld restraint, natural blur, imperfect timing | strict plausible contact |
| martial_arts_film | clear action cadence | [0.15, 0.55] | wide readability masters, impact inserts, wirework optional, rhythmic exchanges | clear causal exchange |
| fashion | sustained holds/glides | [0.15, 0.5] | elongated line, controlled turns, product/garment secondary motion | preserve garment/body relation |
| commercial | crisp beat-aligned | [0.2, 0.65] | product legibility holds, clean transitions, repeatable hero motion | product interaction exact |
| hyperreal | high temporal fidelity | [0, 0.15] | physical blur, soft-tissue response, microbalance corrections | strict geometry/dynamics |

The internal canonical term `family_feature_cg` is descriptive. A user-facing prompt may preserve a user-provided brand/style reference, but the ontology should avoid making a commercial studio name the only semantic representation.

## Anime-specific motion

Anime can use held key poses, variable frame cadence, smears, impact frames, speed lines, dramatic zooms, and environmental secondary motion. “Limited animation” does not mean low quality: a held drawing with moving camera, particles, hair, or lighting can concentrate attention. AnimeInterp illustrates why interpolation is difficult when motion includes occlusion, sparse drawings, and non-photoreal deformation. [S044]

## Style–mood interaction

- High-arousal anime may compress acceleration into a few frames and use an impact frame; low-arousal anime may hold a pose while only hair/environment moves.
- Documentary style minimizes deformation and lets camera observation, imperfect balance, and natural timing carry emotion.
- Commercial style prioritizes product identity, legibility, beat alignment, and repeatability.
- Hyperreal style relies on microbalance, soft-tissue response, contact compliance, and physically coherent aftermath.

## Body-part-local style

Motion Puzzle supports the idea that style can be localized by body part. CPCS exposes separate transforms for root, spine, head, arms, hands, legs, and secondary systems. A fashion profile might elongate arm trajectories and sustain torso rise while keeping foot contacts physically strict.

## Example

Canonical choreography:

```json
{
  "predicate_chain": ["block","redirect","counter_strike"],
  "contact_topology_locked": true,
  "root_path_locked": true,
  "phase_order_locked": true
}
```

Anime transform:

```json
{
  "style": "anime",
  "timing_warp": {"preparation": 1.25, "acceleration": 0.55, "stroke": 0.70},
  "spatial_exaggeration": {"arms": 1.30, "spine": 1.12, "root": 1.00},
  "smear_frames": 1,
  "impact_frames": 2,
  "held_reaction_frames": 5,
  "contact_tolerance_m": 0.015
}
```

Documentary transform of the same choreography would keep timing near 1.0, disable squash/stretch and impact frames, use natural blur, and allow small balance corrections.

## Failure modes

- content leakage: style changes action identity;
- root/target drift;
- contact loss;
- phase inversion;
- identity drift;
- over-exaggeration beyond joint limits;
- visual style prompt overriding motion reference.

Each generated output should be scored on invariant preservation and style success separately. A stylish output that changed “block” into “being hit” is a failed transfer.

## References and locators

- **[S016]** Frank Thomas; Ollie Johnston (1981), *The Illusion of Life: Disney Animation*. **Locator:** Chapters on anticipation, follow-through, timing, arcs, exaggeration  
- **[S031]** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000), *The EMOTE Model for Effort and Shape*. **Locator:** SIGGRAPH 2000, pp.173–182  
- **[S038]** CG-HOI authors (2024), *Contact-Guided Human-Object Interaction Synthesis*. **Locator:** Contact representation and synthesis sections  
- **[S044]** Li Siyao et al. (2021), *AnimeInterp: Open-Domain Interpolation for 2D Animation*. **Locator:** CVPR 2021; formulation and occlusion-aware interpolation  
- **[S045]** Ruilong Li et al. (2021), *AIST++ Dance Motion Dataset*. **Locator:** ICCV 2021; dataset, beat alignment, evaluation  
- **[S050]** Kfir Aberman et al. (2020), *Unpaired Motion Style Transfer from Video to Animation*. **Locator:** ACM TOG/SIGGRAPH 2020; architecture/evaluation  
- **[S051]** Kfir Aberman et al. (2022), *Motion Puzzle: Arbitrary Motion Style Transfer by Body Part*. **Locator:** ACM TOG 41(4); body-part transfer and evaluation  
- **[S052]** Daniel Holden; Jun Saito; Taku Komura (2016), *A Deep Learning Framework for Character Motion Synthesis and Editing*. **Locator:** ACM TOG 35(4), article 138  
- **[S065]** Naureen Mahmood et al. (2019), *AMASS: Archive of Motion Capture as Surface Shapes*. **Locator:** ICCV 2019; dataset documentation  
- **[S067]** Ali-Akbar Samadani; Rob Gorbet; Dana Kulić (2020), *Affective Movement Generation Using Laban Effort and Shape and Hidden Markov Models*. **Locator:** Generation method, evaluation, limitations  
- **[S068]** Alexandros Paraschos et al. (2013), *ProMPs: Probabilistic Movement Primitives*. **Locator:** Representation, conditioning, blending  
- **[S069]** MagicFace authors (2025), *MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control*. **Locator:** §II-A historical AU convention; §III relative AU variation  
- **[S072]** Heechang Kim; Gwanghyun Kim; Se Young Chun (2025), *LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation*. **Locator:** §§1–4; Laban features; experiments
