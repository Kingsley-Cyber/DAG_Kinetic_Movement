# 08 — Force Dynamics: Physical and Perceived Force

## Executive finding

Force must be factored into four truth levels: measured force, inverse-dynamics estimate, visual proxy, and creative prompt prior. LMA Weight and cinematic “power” belong to the perceptual/qualitative layers and cannot be substituted for newtons. OpenSim and standard biomechanics provide the physical machinery; animation, editing, sound, and target response determine how much force an audience perceives. [S026; S027]

## Canonical force profile

The profile stores anticipated force, actual peak/mean force, impulse, effective mass, resistance, compliance, recoil, follow-through, weight commitment, kinetic-chain coherence, support commitment, contact duration, measurement status, and uncertainty.

`weight_commitment` is an engineering control: how much recoverable support, body mass, and momentum the action appears to commit. It is not a laboratory variable unless a specific operational definition and measurement pipeline are attached.

## Same path, different force read

Two motions can share nearly the same end-effector path but read differently.

**Light execution** uses less support and effective-mass participation, less visible pre-tension, lower target deformation, and faster reversible recovery. **Strong execution** recruits a clearer base-to-distal chain, stronger preparation, more target reaction or displacement, and greater follow-through when constraints permit. The difference can be perceptual even when no physical contact is present.

## Impact decomposition

1. **Pre-impact:** support loading, alignment, pre-tension proxies, slack removal, visual/audio anticipation.
2. **Contact:** relative-velocity change, deformation, impulse, impact sound, graphic impact cue.
3. **Post-impact:** target motion, recoil, follow-through, secondary vibration, debris/cloth response.
4. **Resolution:** balance recovery, guard return, object rest state, reaction beat.

The contact instant should remain the causal anchor. A model that moves the target before contact may look energetic but fails physical causality.

## Kinetic chain

CPCS represents the chain as a directed temporal graph. Segment nodes carry angular velocity, energy, power, onset, and peak time; edges carry transfer lag and a confidence-weighted efficiency proxy. Proximal-to-distal sequencing is common in high-speed strikes and throws, but the optimal pattern depends on task, style, target, and athlete. [S027; S028; S039]

## Perceived-force controls

### Visual

- anticipation contrast;
- sharp spacing change localized near contact;
- target deformation/displacement;
- whole-body and environmental reaction;
- restrained, damped camera impulse;
- impact hold/freeze for stylization;
- secondary motion in clothing, hair, props, dust, and surfaces.

### Audio

- pre-impact silence/drop;
- sharp high-frequency transient;
- low-frequency body for mass;
- delayed debris, room response, or reverb.

### Editing

- cut on or just before impact;
- reaction shot showing consequence;
- time ramp or replay that reframes, rather than physically changes, the action.

## Combat-style production priors

| Profile | Preparation | Peak speed | Recoil | Follow-through | Commitment | Status |
|---|---|---|---|---|---|---|
| boxing_snap | 0.25 | 0.85 | 0.8 | 0.35 | 0.65 | CPCS production prior |
| muay_thai_commitment | 0.45 | 0.8 | 0.45 | 0.8 | 0.9 | CPCS production prior |
| tai_chi_redirection | 0.25 | 0.35 | 0.25 | 0.55 | 0.55 | CPCS production prior |
| mma_mixed | — | — | — | — | — | not one force style; compile by technique/range/context |

These are cinematic starting points, not claims that every boxer, Muay Thai fighter, Tai Chi practitioner, or MMA athlete moves this way. A jab and a committed cross already differ within boxing; MMA contains striking, grappling, wall work, and many force regimes.

## Example

```json
{
  "force_profile": {
    "anticipated_force": 0.68,
    "actual_peak_force_N": null,
    "impulse_Ns": null,
    "effective_mass_kg": null,
    "weight_commitment": 0.82,
    "kinetic_chain_coherence": 0.78,
    "recoil": 0.62,
    "follow_through": 0.71,
    "measurement_status": "prompt_prior"
  },
  "perceptual_cues": ["target_jacket_snap", "two_frame_impact_hold", "six_frame_camera_decay"]
}
```

Compiled prose: “The strike commits through the rear foot and torso, lands with a compact contact beat, drives the target’s shoulder back before the rest of the body follows, and leaves a short rotational follow-through; camera response is brief and damped, not continuous shake.”

## Validation

- physical values require units and measurement status;
- no inferred force without mass/contact assumptions;
- target response begins at or after contact;
- body and target momentum changes are mutually plausible;
- perceptual-force effects cannot conceal broken contact topology;
- style priors never overwrite measured dynamics.

## References and locators

- **[S002]** Irmgard Bartenieff; Dori Lewis (1980), *Body Movement: Coping with the Environment*. **Locator:** Ch.3 pp.23–48; Ch.4 pp.49–68; Ch.5 pp.69–82; Ch.6 pp.83–100; Appendix B from p.229  
- **[S004]** Rudolf Laban; F. C. Lawrence (1947), *Effort: Economy of Human Movement*. **Locator:** Parts on motion factors and basic effort actions; edition-specific pagination  
- **[S026]** Scott L. Delp et al. (2007), *OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement*. **Locator:** IEEE TBME 54(11), pp.1940–1950  
- **[S027]** David A. Winter (2009), *Biomechanics and Motor Control of Human Movement, 4th ed.*. **Locator:** Chs.2–4 kinematics; Chs.5–7 kinetics, anthropometry, signal processing  
- **[S028]** Timothy J. Walilko; David C. Viano; Cynthia A. Bir (2005), *Biomechanics of the Head for Olympic Boxer Punches to the Face*. **Locator:** Br J Sports Med 39(10), pp.710–719  
- **[S029]** D. R. Mailapalli et al. (2015), *Biomechanics of the Taekwondo Axe Kick: A Review*. **Locator:** Archives of Budo SAMAES 11, pp.3–13  
- **[S038]** CG-HOI authors (2024), *Contact-Guided Human-Object Interaction Synthesis*. **Locator:** Contact representation and synthesis sections  
- **[S039]** Selected peer-reviewed sports-biomechanics sources (2020), *Kinetic-Chain Evidence for Overarm Striking*. **Locator:** Segment sequencing, proximal-to-distal transfer, effective mass
