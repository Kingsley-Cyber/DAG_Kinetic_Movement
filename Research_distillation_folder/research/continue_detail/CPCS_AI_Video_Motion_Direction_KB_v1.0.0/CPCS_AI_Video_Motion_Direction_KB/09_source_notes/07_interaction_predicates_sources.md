# Source Notes — Topic 07: Interaction Predicates

**Sources linked:** 7

## Reading order

### 1. [S013] Behavior Markup Language 1.0 Specification

- **Authors/year:** SAIBA community (2011)
- **Authority:** `technical_standard` / `technical_specification`
- **Locator:** Behavior phases, sync points, and synchronization
- **Use:** Defines realizable behavior and synchronization; high-level intent remains outside BML.
- **URL:** https://projects.cs.ru.is/projects/behavior-markup-language/wiki

### 2. [S068] ProMPs: Probabilistic Movement Primitives

- **Authors/year:** Alexandros Paraschos et al. (2013)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Representation, conditioning, blending
- **Use:** Computational primitive model, not specific to Bartenieff.
- **URL:** https://doi.org/10.1162/NECO_a_00589
- **DOI:** `10.1162/NECO_a_00589`

### 3. [S034] HICO-DET: A Benchmark for Recognizing Human-Object Interactions in Images

- **Authors/year:** Yu-Wei Chao et al. (2018)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** WACV 2018; 600 HOI classes, 117 verbs, 80 objects
- **Use:** Useful predicate seed; lacks continuous contact and force.
- **URL:** https://www-personal.umich.edu/~ywchao/hico/

### 4. [S035] BABEL: Bodies, Action and Behavior with English Labels

- **Authors/year:** Abhinanda Punnakkal et al. (2021)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** CVPR 2021; dataset and annotation sections
- **Use:** Semantic labels over AMASS; not natively Laban annotated.
- **URL:** https://babel.is.tue.mpg.de/

### 5. [S036] Inter-X: Towards Versatile Human-Human Interaction Analysis

- **Authors/year:** Han Liang et al. (2023)
- **Authority:** `peer_reviewed_dataset` / `peer_reviewed_conference`
- **Locator:** CVPR 2023; dataset statistics and interaction annotations
- **Use:** Large two-person interaction dataset with part-level descriptions.
- **URL:** https://liangxuy.github.io/inter-x/

### 6. [S037] InterGen: Diffusion-Based Multi-Human Motion Generation Under Complex Interactions

- **Authors/year:** Han Liang et al. (2023)
- **Authority:** `peer_reviewed_open_source` / `peer_reviewed_article`
- **Locator:** Paper §§3–5 and repository documentation
- **Use:** Generation does not guarantee physical contact validity.
- **URL:** https://github.com/tr3e/InterGen

### 7. [S038] Contact-Guided Human-Object Interaction Synthesis

- **Authors/year:** CG-HOI authors (2024)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** Contact representation and synthesis sections
- **Use:** Supports contact-conditioned HOI synthesis.
- **URL:** https://arxiv.org/abs/2311.16097

## Topic-specific caution

Image-level verbs do not guarantee temporal contact topology or physics.
