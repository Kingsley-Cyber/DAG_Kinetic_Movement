# 05 — Kinematics: Physics Parameters for Motion Control

## Executive finding

CPCS needs a separate physics layer because qualitative words such as “powerful,” “snappy,” or “heavy” are not measurements. Kinematics describe motion; dynamics describe forces and torques. A video can support position and derivative estimates after calibration/filtering, but force estimation needs anthropometry, contacts, boundary conditions, and a dynamical model. OpenCap, Pose2Sim, and OpenSim demonstrate viable pipelines while also documenting assumptions and validation limits. [S024; S025; S026]

## Canonical variables

| Variable | Symbol | Unit | Definition/formula |
|---|---|---|---|
| position | x(t) | m | — |
| velocity | v(t) | m/s | dx/dt |
| acceleration | a(t) | m/s² | d²x/dt² |
| jerk | j(t) | m/s³ | d³x/dt³ |
| orientation | R(t) or q(t) | — | — |
| angular_velocity | ω(t) | rad/s | — |
| angular_acceleration | α(t) | rad/s² | — |
| curvature | κ | 1/m | ||v×a||/||v||³ |
| linear_momentum | p | kg·m/s | m v |
| angular_momentum | L | kg·m²/s | — |
| impulse | J | N·s | ∫Fdt=Δp |
| segment_kinetic_energy | E | J | 0.5m||v||²+0.5ωᵀIω |
| center_of_mass | COM | m | Σm_i x_i/Σm_i |
| support_polygon | P_support | m² polygon | — |
| margin_of_stability | MoS | m | — |

All vector values require an explicit coordinate frame, handedness, scale, and sample rate. CPCS stores world, camera, actor-root, and local-joint frames separately. Quaternion or rotation-matrix conventions must be versioned; Euler angles may be exported for readability but should not be the canonical rotation representation.

## Contacts and ground reaction

A contact is an interval or event linking a body part to a surface/object with position/patch, normal, relative velocity, force if known, friction, compliance, and confidence. Foot strike should not be inferred from height alone; combine proximity, low relative velocity, support behavior, and visual evidence. Contact quality is one of the strongest determinants of whether generated motion looks physically grounded.

Ground-reaction force values vary with speed, gait, surface, footwear, technique, and measurement protocol. CPCS should store body-weight-normalized values when comparing actors, but must retain original newtons and body mass when available.

## Illustrative motion ranges

| Activity | Metric | Illustrative band | Status/caution |
|---|---|---|---|
| preferred young-adult walking | forward speed | 1.2–1.5 m/s | illustrative population band |
| moderate running example | forward speed | 2.5–4.0 m/s | task example, not human limit |
| trained boxing straight punch | fist speed near impact | 7.0–12.0 m/s | study-dependent illustrative band |
| trained high-speed kick | distal striking-point speed | 10.0–18.0 m/s | technique/study dependent; not universal |
| vertical jump | COM take-off vertical speed | 2.43–3.43 m/s | derived for 0.30–0.60m ballistic rise |

These are not hard generation limits. Walilko et al. report Olympic-boxer results under a specific protocol; kick studies vary by technique and striking point. A 0.30–0.60 m vertical COM rise corresponds to about 2.43–3.43 m/s take-off speed through `v=sqrt(2gh)`, but that is a simple ballistic derivation, not a normative athlete table. [S028; S029]

## Biomechanical constraints

Generic joint ranges are soft plausibility bounds. A production actor profile should carry comfortable, maximum, and prohibited ranges, plus context such as load and joint angle. Torque capacity is not one global lookup: it varies with body size, training, sex, age, contraction type, angle, and speed. CPCS therefore uses a normalized `capacity_fraction` and stores N·m only when an actor-specific or population model is named.

Reach is best represented as an actor-centered 3D reachable-volume mesh or signed-distance field conditioned on whether torso movement, stepping, and balance changes are allowed.

## Video-to-physics pipeline

| Step | Stage | Representative tools/methods | Verification checkpoint |
|---|---|---|---|
| 1 | calibrate | — | reprojection error distribution |
| 2 | 2d_pose | OpenPose, MediaPipe, DWPose-compatible frontend | confidence + manual spot checks |
| 3 | 3d_reconstruction | — | reprojection + bone-length consistency |
| 4 | filter | zero-phase Butterworth, Savitzky–Golay, smoothing spline | frequency/residual analysis |
| 5 | differentiate | velocity, acceleration, jerk | stability under filter perturbation |
| 6 | inverse_kinematics | — | tracking error/range checks |
| 7 | contact_inference | — | low contact drift, no foot skate, visual review |
| 8 | inverse_dynamics | — | dynamic residuals/sensitivity |
| 9 | uncertainty | intervals, distributions | coverage on measured held-out trials |

Derivative calculation must occur **after** smoothing. Differentiating noisy keypoints creates acceleration and jerk artifacts that can dominate downstream Laban or quality classifiers. A deterministic pipeline should save filter settings, cutoff, residuals, and a sensitivity test showing how outputs change when filter parameters vary.

## Which parameters most affect perceived quality?

1. **Contact integrity:** foot skate, penetrations, and drifting grasps are immediately visible.
2. **COM/support consistency:** unsupported poses without compensatory acceleration look weightless.
3. **Momentum continuity:** unexplained velocity discontinuities look synthetic unless stylized deliberately.
4. **Timing and spacing:** the same path can feel crisp or floaty through its derivative profile.
5. **Joint-limit margin:** hyperextension or axial twist breaks plausibility.
6. **Secondary motion:** cloth, hair, soft tissue, and props reveal acceleration and impact.
7. **Camera separation:** camera motion must be removed before actor velocity is interpreted.

## Prompt/control example

```json
{
  "right_fist": {
    "path": [[0.31,1.34,0.12],[0.48,1.36,0.20],[0.71,1.37,0.32]],
    "peak_velocity_mps": 8.5,
    "time_to_peak_s": 0.18,
    "peak_jerk_mps3": 240,
    "contact_event": "contact_17"
  },
  "center_of_mass": {"forward_displacement_m": 0.14},
  "measurement_status": "prompt_prior",
  "warning": "not measured force"
}
```

For a text-only model, compile to: “The fist accelerates sharply over the last fifth of the path; the hips and torso contribute before the arm; both feet stay planted until contact; the hand recoils immediately without sliding through the target.”

## Acceptance checks

- unit and coordinate-frame completeness;
- finite derivatives with no filter-edge spikes;
- bone-length consistency;
- contact drift below tolerance;
- joint-angle margins;
- inverse-dynamics residuals where dynamics are estimated;
- uncertainty intervals carried into downstream force/LMA labels.

## References and locators

- **[S007]** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013), *Laban Effort and Shape Analysis of Affective Hand and Arm Movements*. **Locator:** pp.343–348; §§II–V; Tables I–IV  
- **[S024]** Scott D. Uhlrich et al. (2023), *OpenCap: Human Movement Dynamics from Smartphone Videos*. **Locator:** Methods pipeline; validation; limitations  
- **[S025]** David Pagnon; Mathieu Domalain; Lionel Reveret (2022), *Pose2Sim: An Open-Source Python Package for Multiview Markerless Kinematics*. **Locator:** JOSS 7(77), article 4362, pp.1–4  
- **[S026]** Scott L. Delp et al. (2007), *OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement*. **Locator:** IEEE TBME 54(11), pp.1940–1950  
- **[S027]** David A. Winter (2009), *Biomechanics and Motor Control of Human Movement, 4th ed.*. **Locator:** Chs.2–4 kinematics; Chs.5–7 kinetics, anthropometry, signal processing  
- **[S028]** Timothy J. Walilko; David C. Viano; Cynthia A. Bir (2005), *Biomechanics of the Head for Olympic Boxer Punches to the Face*. **Locator:** Br J Sports Med 39(10), pp.710–719  
- **[S029]** D. R. Mailapalli et al. (2015), *Biomechanics of the Taekwondo Axe Kick: A Review*. **Locator:** Archives of Budo SAMAES 11, pp.3–13  
- **[S063]** Zhe Cao et al. (2019), *OpenPose: Realtime Multi-Person 2D Pose Estimation Using Part Affinity Fields*. **Locator:** IEEE TPAMI 43(1), pp.172–186  
- **[S064]** Google AI Edge (2026), *MediaPipe Pose Landmarker*. **Locator:** Outputs, landmarks, world coordinates, video/live modes
