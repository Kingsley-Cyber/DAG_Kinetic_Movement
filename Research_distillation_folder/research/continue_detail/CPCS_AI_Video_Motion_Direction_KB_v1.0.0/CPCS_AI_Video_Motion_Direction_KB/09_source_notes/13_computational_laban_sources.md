# Source Notes — Topic 13: Computational Laban

**Sources linked:** 29

## Reading order

### 1. [S064] MediaPipe Pose Landmarker

- **Authors/year:** Google AI Edge (2026)
- **Authority:** `official_current` / `official_technical_documentation`
- **Locator:** Outputs, landmarks, world coordinates, video/live modes
- **Use:** World coordinates are model-relative, not calibrated biomechanics.
- **URL:** https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
- **Verified:** `2026-07-30`

### 2. [S031] The EMOTE Model for Effort and Shape

- **Authors/year:** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** SIGGRAPH 2000, pp.173–182
- **Use:** Parameterized expressive-motion generation using Effort and Shape.
- **URL:** https://doi.org/10.1145/344779.352172
- **DOI:** `10.1145/344779.352172`

### 3. [S009] An XML Representation of Labanotation, LabanXML, and Its Implementation on the Notation Editor LabanEditor2

- **Authors/year:** Minako Nakamura; Kozaburo Hachimura (2006)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Review of the National Center for Digitization 9, pp.47–51
- **Use:** XML interchange for notation; not automatic qualitative LMA inference.
- **URL:** https://elib.mi.sanu.ac.rs/files/journals/ncd/9/ncd09047.pdf

### 4. [S073] Semantic Segmentation of Motion Capture Using Laban Movement Analysis

- **Authors/year:** Durell Bouchard; Norman I. Badler (2007)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** IVA 2007, LNCS 4722, pp.37–44
- **Use:** LMA-derived qualities for mocap segmentation; not full BESS from monocular video.
- **URL:** https://doi.org/10.1007/978-3-540-74997-4_4
- **DOI:** `10.1007/978-3-540-74997-4_4`

### 5. [S074] Laban Movement Analysis Using a Bayesian Model and Perspective Projections

- **Authors/year:** Joerg Rett; Jorge Dias; Juan-Manuel Ahuactzin (2008)
- **Authority:** `peer_reviewed` / `peer_reviewed_chapter`
- **Locator:** Feature construction, Bayesian classifier, perspective projection
- **Use:** Early LMA-inspired gesture classification under controlled conditions.
- **URL:** https://doi.org/10.5772/6037
- **DOI:** `10.5772/6037`

### 6. [S011] A Labanotation Based Ontology for Representing Dance Movement

- **Authors/year:** Katerina El Raheb; Yannis Ioannidis (2012)
- **Authority:** `peer_reviewed` / `peer_reviewed_chapter`
- **Locator:** LNCS 7206, Ch.10
- **Use:** Ontology-oriented representation of dance movement.
- **URL:** https://doi.org/10.1007/978-3-642-34182-3_10
- **DOI:** `10.1007/978-3-642-34182-3_10`

### 7. [S007] Laban Effort and Shape Analysis of Affective Hand and Arm Movements

- **Authors/year:** Ali-Akbar Samadani; SarahJane Burton; Rob Gorbet; Dana Kulić (2013)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** pp.343–348; §§II–V; Tables I–IV
- **Use:** Continuous physical correlates on a small, constrained hand/arm dataset.
- **URL:** https://doi.org/10.1109/ACII.2013.63
- **DOI:** `10.1109/ACII.2013.63`

### 8. [S032] Emotion Analysis and Classification Using LMA Entities

- **Authors/year:** Andreas Aristidou et al. (2015)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Computer Graphics Forum 34(6), pp.262–276
- **Use:** LMA-inspired features for movement emotion recognition.
- **URL:** https://doi.org/10.1111/cgf.12598
- **DOI:** `10.1111/cgf.12598`

### 9. [S075] Dynamic Gesture Recognition with Laban Movement Analysis and Hidden Markov Models

- **Authors/year:** Anh-Tuan Truong; Titus Zaharia (2017)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** §3 descriptors/HMM; experiments and limitations
- **Use:** LMA-inspired local descriptors; not expert-level full BESS coding.
- **URL:** https://doi.org/10.1186/s13640-017-0202-5
- **DOI:** `10.1186/s13640-017-0202-5`

### 10. [S008] Assessing the Reliability of the Laban Movement Analysis System

- **Authors/year:** Bernardet et al. (2019)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Methods; Results; Discussion on inter-rater reliability
- **Use:** Supports explicit coder reliability and uncertainty rather than treating expert labels as infallible.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6564005/

### 11. [S063] OpenPose: Realtime Multi-Person 2D Pose Estimation Using Part Affinity Fields

- **Authors/year:** Zhe Cao et al. (2019)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_article`
- **Locator:** IEEE TPAMI 43(1), pp.172–186
- **Use:** 2D pose front end; depth/camera ambiguity remains.
- **URL:** https://doi.org/10.1109/TPAMI.2019.2929257
- **DOI:** `10.1109/TPAMI.2019.2929257`

### 12. [S065] AMASS: Archive of Motion Capture as Surface Shapes

- **Authors/year:** Naureen Mahmood et al. (2019)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_dataset`
- **Locator:** ICCV 2019; dataset documentation
- **Use:** Large corpus; not natively Laban annotated.
- **URL:** https://amass.is.tue.mpg.de/

### 13. [S066] HumanAct12

- **Authors/year:** Guo et al. (2020)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_dataset`
- **Locator:** Dataset categories and action-to-motion paper
- **Use:** Action labels, not Laban labels.
- **URL:** https://ericguo5513.github.io/action-to-motion/

### 14. [S035] BABEL: Bodies, Action and Behavior with English Labels

- **Authors/year:** Abhinanda Punnakkal et al. (2021)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** CVPR 2021; dataset and annotation sections
- **Use:** Semantic labels over AMASS; not natively Laban annotated.
- **URL:** https://babel.is.tue.mpg.de/

### 15. [S045] AIST++ Dance Motion Dataset

- **Authors/year:** Ruilong Li et al. (2021)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_dataset`
- **Locator:** ICCV 2021; dataset, beat alignment, evaluation
- **Use:** 5.2 hours, 1,408 sequences, 10 dance genres; verify license.
- **URL:** https://google.github.io/aistplusplus_dataset/

### 16. [S006] AI-driven Human Motion Classification and Analysis using Laban Movement System

- **Authors/year:** Wenbin Guo et al. (2022)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** Abstract; §§3–5; manuscript pp.1–12
- **Use:** Supervised classification work over BESS-related labels; task and dataset constrained.
- **URL:** https://research.dwi.ufl.edu/file.php?f=guo_hcii2022.pdf

### 17. [S030] BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis

- **Authors/year:** Haiyang Liu et al. (2022)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** ECCV 2022; dataset statistics and §§3–5
- **Use:** 76 hours, 30 speakers, four languages, eight emotion categories; dataset terms govern use.
- **URL:** https://arxiv.org/abs/2203.05297

### 18. [S024] OpenCap: Human Movement Dynamics from Smartphone Videos

- **Authors/year:** Scott D. Uhlrich et al. (2023)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Methods pipeline; validation; limitations
- **Use:** Markerless video-to-biomechanics; forces remain model- and assumption-dependent.
- **URL:** https://doi.org/10.1371/journal.pcbi.1011462
- **DOI:** `10.1371/journal.pcbi.1011462`

### 19. [S036] Inter-X: Towards Versatile Human-Human Interaction Analysis

- **Authors/year:** Han Liang et al. (2023)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** CVPR 2023; dataset statistics and interaction annotations
- **Use:** Large two-person interaction dataset with part-level descriptions.
- **URL:** https://liangxuy.github.io/inter-x/

### 20. [S037] InterGen: Diffusion-Based Multi-Human Motion Generation Under Complex Interactions

- **Authors/year:** Han Liang et al. (2023)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_article`
- **Locator:** Paper §§3–5 and repository documentation
- **Use:** Generation does not guarantee physical contact validity.
- **URL:** https://github.com/tr3e/InterGen

### 21. [S071] Bodily Expressed Emotion Understanding Through Integrating Laban Movement Analysis

- **Authors/year:** Chenyan Wu et al. (2023)
- **Authority:** `peer_reviewed_open_dataset` / `peer_reviewed_article_and_open_dataset`
- **Locator:** BoME dataset and experiment sections
- **Use:** 1,600 clips with expert annotations for eleven selected LMA motor elements; not a complete BESS corpus.
- **URL:** https://arxiv.org/abs/2304.02187
- **DOI:** `10.1016/j.patter.2023.100816`

### 22. [S012] MoRTELaban: A Neurosymbolic Framework for Motion Representation Through Laban Movement Analysis

- **Authors/year:** Perez-Martinez et al. (2025)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** Abstract; framework and evaluation sections
- **Use:** Recent neurosymbolic work; reproduce before production reliance.
- **URL:** https://doi.org/10.1145/3708319.3734180
- **DOI:** `10.1145/3708319.3734180`

### 23. [S025] Pose2Sim: An Open-Source Python Package for Multiview Markerless Kinematics

- **Authors/year:** David Pagnon; Mathieu Domalain; Lionel Reveret (2022)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_software_article`
- **Locator:** JOSS 7(77), article 4362, pp.1–4
- **Use:** 2D pose, calibration, triangulation, filtering, inverse kinematics.
- **URL:** https://doi.org/10.21105/joss.04362
- **DOI:** `10.21105/joss.04362`

### 24. [S001] Movement Analysis Overview

- **Authors/year:** Laban/Bartenieff and Somatic Studies International (LSSI/LIMS) (2026)
- **Authority:** `primary_professional_body` / `official_framework_overview`
- **Locator:** § What is Laban/Bartenieff Movement Analysis?
- **Use:** Defines LMA as a detailed system for qualitative movement and relations among movement components.
- **URL:** https://labaninternational.org/scope-of-practice/movement-analysis/movement-analysis-overview/

### 25. [S005] LabanWriter

- **Authors/year:** Ohio State University Department of Dance (2026)
- **Authority:** `official_software` / `official_software_page`
- **Locator:** § LabanWriter; description of 700+ symbols and notation editor
- **Use:** Notation editor, not an automatic LMA detector.
- **URL:** https://dance.osu.edu/research/dnb/laban-writer

### 26. [S019] OpenFace Action Units Documentation

- **Authors/year:** OpenFace project; Tadas Baltrušaitis et al. (2026)
- **Authority:** `official_open_source` / `official_open_source_documentation`
- **Locator:** Supported AUs; presence and 0–5 intensity outputs
- **Use:** Automatic detector covers only a subset of FACS; presence and intensity models are distinct.
- **URL:** https://github.com/TadasBaltrusaitis/OpenFace/wiki/Action-Units

### 27. [S010] MovementXML: A Representation of Semantics of Human Movement Based on Labanotation

- **Authors/year:** Metadata varies across indexes; verify against thesis repository record (2006)
- **Authority:** `academic_thesis` / `academic_thesis`
- **Locator:** Chs.3–5 and Movement XML schema appendix
- **Use:** Useful representation work; authorship/year metadata should be rechecked before formal publication.
- **URL:** https://summit.sfu.ca/item/2741
- **Metadata confidence:** `0.55`

### 28. [S067] Affective Movement Generation Using Laban Effort and Shape and Hidden Markov Models

- **Authors/year:** Ali-Akbar Samadani; Rob Gorbet; Dana Kulić (2020)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** Generation method, evaluation, limitations
- **Use:** Useful generation evidence; not universal intent-to-motion mapping.
- **URL:** https://arxiv.org/abs/2006.06071

### 29. [S072] LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation

- **Authors/year:** Heechang Kim; Gwanghyun Kim; Se Young Chun (2025)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** §§1–4; Laban features; experiments
- **Use:** Inference-time Laban guidance for motion generation; not a full video detector.
- **URL:** https://arxiv.org/abs/2509.24469

## Topic-specific caution

No full-BESS OpenFace-equivalent system was verified; retain uncertainty and expert calibration.
