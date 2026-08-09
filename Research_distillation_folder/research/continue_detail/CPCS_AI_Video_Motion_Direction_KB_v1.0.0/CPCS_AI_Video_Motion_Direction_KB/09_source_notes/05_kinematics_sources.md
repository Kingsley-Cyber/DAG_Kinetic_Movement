# Source Notes — Topic 05: Kinematics

**Sources linked:** 10

## Reading order

### 1. [S064] MediaPipe Pose Landmarker

- **Authors/year:** Google AI Edge (2026)
- **Authority:** `official_current` / `official_technical_documentation`
- **Locator:** Outputs, landmarks, world coordinates, video/live modes
- **Use:** World coordinates are model-relative, not calibrated biomechanics.
- **URL:** https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
- **Verified:** `2026-07-30`

### 2. [S027] Biomechanics and Motor Control of Human Movement, 4th ed.

- **Authors/year:** David A. Winter (2009)
- **Authority:** `foundational_biomechanics` / `book`
- **Locator:** Chs.2–4 kinematics; Chs.5–7 kinetics, anthropometry, signal processing
- **Use:** Core formulas and methodological cautions.
- **URL:** https://doi.org/10.1002/9780470549148
- **DOI:** `10.1002/9780470549148`

### 3. [S028] Biomechanics of the Head for Olympic Boxer Punches to the Face

- **Authors/year:** Timothy J. Walilko; David C. Viano; Cynthia A. Bir (2005)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Br J Sports Med 39(10), pp.710–719
- **Use:** Reported values are protocol- and population-specific; not universal punch limits.
- **URL:** https://doi.org/10.1136/bjsm.2004.014126
- **DOI:** `10.1136/bjsm.2004.014126`

### 4. [S026] OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement

- **Authors/year:** Scott L. Delp et al. (2007)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** IEEE TBME 54(11), pp.1940–1950
- **Use:** Musculoskeletal modeling and inverse-dynamics foundation.
- **URL:** https://doi.org/10.1109/TBME.2007.901024
- **DOI:** `10.1109/TBME.2007.901024`

### 5. [S007] Laban Effort and Shape Analysis of Affective Hand and Arm Movements

- **Authors/year:** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** pp.343–348; §§II–V; Tables I–IV
- **Use:** Continuous physical correlates on a small, constrained hand/arm dataset.
- **URL:** https://doi.org/10.1109/ACII.2013.63
- **DOI:** `10.1109/ACII.2013.63`

### 6. [S029] Biomechanics of the Taekwondo Axe Kick: A Review

- **Authors/year:** D. R. Mailapalli et al. (2015)
- **Authority:** `peer_reviewed` / `peer_reviewed_review`
- **Locator:** Archives of Budo SAMAES 11, pp.3–13
- **Use:** Review of technique phases and cited kinematics; do not generalize a single velocity range.
- **URL:** https://www.redalyc.org/pdf/3010/301042304013.pdf

### 7. [S063] OpenPose: Realtime Multi-Person 2D Pose Estimation Using Part Affinity Fields

- **Authors/year:** Zhe Cao et al. (2019)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_article`
- **Locator:** IEEE TPAMI 43(1), pp.172–186
- **Use:** 2D pose front end; depth/camera ambiguity remains.
- **URL:** https://doi.org/10.1109/TPAMI.2019.2929257
- **DOI:** `10.1109/TPAMI.2019.2929257`

### 8. [S024] OpenCap: Human Movement Dynamics from Smartphone Videos

- **Authors/year:** Scott D. Uhlrich et al. (2023)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Methods pipeline; validation; limitations
- **Use:** Markerless video-to-biomechanics; forces remain model- and assumption-dependent.
- **URL:** https://doi.org/10.1371/journal.pcbi.1011462
- **DOI:** `10.1371/journal.pcbi.1011462`

### 9. [S025] Pose2Sim: An Open-Source Python Package for Multiview Markerless Kinematics

- **Authors/year:** David Pagnon; Mathieu Domalain; Lionel Reveret (2022)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_software_article`
- **Locator:** JOSS 7(77), article 4362, pp.1–4
- **Use:** 2D pose, calibration, triangulation, filtering, inverse kinematics.
- **URL:** https://doi.org/10.21105/joss.04362
- **DOI:** `10.21105/joss.04362`

### 10. [S039] Kinetic-Chain Evidence for Overarm Striking

- **Authors/year:** Selected peer-reviewed sports-biomechanics sources (2020)
- **Authority:** `evidence_bundle` / `evidence_bundle`
- **Locator:** Segment sequencing, proximal-to-distal transfer, effective mass
- **Use:** Sport/style generalizations remain probabilistic priors.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/?term=kinetic+chain+striking+review

## Topic-specific caution

Force requires dynamics/contact assumptions; video derivatives require filtering and calibration.
