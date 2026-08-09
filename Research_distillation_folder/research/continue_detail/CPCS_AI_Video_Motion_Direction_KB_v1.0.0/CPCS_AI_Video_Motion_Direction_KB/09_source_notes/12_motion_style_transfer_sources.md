# Source Notes — Topic 12: Motion Style Transfer

**Sources linked:** 14

## Reading order

### 1. [S031] The EMOTE Model for Effort and Shape

- **Authors/year:** Diane Chi; Monica Costa; Liwei Zhao; Norman Badler (2000)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** SIGGRAPH 2000, pp.173–182
- **Use:** Parameterized expressive-motion generation using Effort and Shape.
- **URL:** https://doi.org/10.1145/344779.352172
- **DOI:** `10.1145/344779.352172`

### 2. [S068] ProMPs: Probabilistic Movement Primitives

- **Authors/year:** Alexandros Paraschos et al. (2013)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Representation, conditioning, blending
- **Use:** Computational primitive model, not specific to Bartenieff.
- **URL:** https://doi.org/10.1162/NECO_a_00589
- **DOI:** `10.1162/NECO_a_00589`

### 3. [S052] A Deep Learning Framework for Character Motion Synthesis and Editing

- **Authors/year:** Daniel Holden; Jun Saito; Taku Komura (2016)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** ACM TOG 35(4), article 138
- **Use:** Learned motion representation and editing.
- **URL:** https://doi.org/10.1145/2897824.2925975
- **DOI:** `10.1145/2897824.2925975`

### 4. [S065] AMASS: Archive of Motion Capture as Surface Shapes

- **Authors/year:** Naureen Mahmood et al. (2019)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_dataset`
- **Locator:** ICCV 2019; dataset documentation
- **Use:** Large corpus; not natively Laban annotated.
- **URL:** https://amass.is.tue.mpg.de/

### 5. [S050] Unpaired Motion Style Transfer from Video to Animation

- **Authors/year:** Kfir Aberman et al. (2020)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** ACM TOG/SIGGRAPH 2020; architecture/evaluation
- **Use:** Content/style disentanglement is learned, not guaranteed.
- **URL:** https://arxiv.org/abs/2005.05751

### 6. [S044] AnimeInterp: Open-Domain Interpolation for 2D Animation

- **Authors/year:** Li Siyao et al. (2021)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** CVPR 2021; formulation and occlusion-aware interpolation
- **Use:** Relevant to sparse/held 2D animation timing.
- **URL:** https://arxiv.org/abs/2104.02495

### 7. [S045] AIST++ Dance Motion Dataset

- **Authors/year:** Ruilong Li et al. (2021)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_dataset`
- **Locator:** ICCV 2021; dataset, beat alignment, evaluation
- **Use:** 5.2 hours, 1,408 sequences, 10 dance genres; verify license.
- **URL:** https://google.github.io/aistplusplus_dataset/

### 8. [S051] Motion Puzzle: Arbitrary Motion Style Transfer by Body Part

- **Authors/year:** Kfir Aberman et al. (2022)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** ACM TOG 41(4); body-part transfer and evaluation
- **Use:** Supports part-local style controls.
- **URL:** https://doi.org/10.1145/3528223.3530116
- **DOI:** `10.1145/3528223.3530116`

### 9. [S037] InterGen: Diffusion-Based Multi-Human Motion Generation Under Complex Interactions

- **Authors/year:** Han Liang et al. (2023)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_article`
- **Locator:** Paper §§3–5 and repository documentation
- **Use:** Generation does not guarantee physical contact validity.
- **URL:** https://github.com/tr3e/InterGen

### 10. [S038] Contact-Guided Human-Object Interaction Synthesis

- **Authors/year:** CG-HOI authors (2024)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** Contact representation and synthesis sections
- **Use:** Supports contact-conditioned HOI synthesis.
- **URL:** https://arxiv.org/abs/2311.16097

### 11. [S016] The Illusion of Life: Disney Animation

- **Authors/year:** Frank Thomas; Ollie Johnston (1981)
- **Authority:** `foundational_practice_text` / `book`
- **Locator:** Chapters on anticipation, follow-through, timing, arcs, exaggeration
- **Use:** Animation craft source, not a biomechanical standard.
- **URL:** https://archive.org/details/illusionoflifedi0000thom

### 12. [S067] Affective Movement Generation Using Laban Effort and Shape and Hidden Markov Models

- **Authors/year:** Ali-Akbar Samadani; Rob Gorbet; Dana Kulić (2020)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** Generation method, evaluation, limitations
- **Use:** Useful generation evidence; not universal intent-to-motion mapping.
- **URL:** https://arxiv.org/abs/2006.06071

### 13. [S069] MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control

- **Authors/year:** MagicFace authors (2025)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** §II-A historical AU convention; §III relative AU variation
- **Use:** Relative continuous AU-conditioned generation; not a FACS manual replacement.
- **URL:** https://arxiv.org/abs/2501.02260

### 14. [S072] LaMoGen: Laban Movement-Guided Diffusion for Text-to-Motion Generation

- **Authors/year:** Heechang Kim; Gwanghyun Kim; Se Young Chun (2025)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** §§1–4; Laban features; experiments
- **Use:** Inference-time Laban guidance for motion generation; not a full video detector.
- **URL:** https://arxiv.org/abs/2509.24469

## Topic-specific caution

Score action/contact preservation separately from style similarity.
