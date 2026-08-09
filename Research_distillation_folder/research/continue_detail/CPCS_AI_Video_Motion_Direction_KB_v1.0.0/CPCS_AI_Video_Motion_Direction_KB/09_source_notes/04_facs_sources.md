# Source Notes — Topic 04: FACS

**Sources linked:** 9

## Reading order

### 1. [S017] Facial Action Coding System, 2nd ed.

- **Authors/year:** Paul Ekman; Wallace V. Friesen; Joseph C. Hager (2002)
- **Authority:** `definitive_manual` / `manual`
- **Locator:** AU chapters; intensity scoring; head/eye sections; proprietary pagination
- **Use:** Package does not reproduce proprietary scoring criteria.
- **URL:** https://www.paulekman.com/facial-action-coding-system/

### 2. [S018] Recognizing Action Units for Facial Expression Analysis

- **Authors/year:** Ying-li Tian; Takeo Kanade; Jeffrey F. Cohn (2001)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Public AU table and discussion of 44 FACS action units/intensity
- **Use:** Publicly accessible consolidation; code grouping/counting varies across implementations.
- **URL:** https://www.cs.cmu.edu/~face/Papers/Tian_face03.pdf

### 3. [S020] Automatic Recognition of Facial Actions in Spontaneous Expressions

- **Authors/year:** Marian Stewart Bartlett et al. (2006)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** pp.22–35; p.23 spontaneous-versus-posed dynamics
- **Use:** Dynamic cues are probabilistic; not a deception detector.
- **URL:** https://mplab.ucsd.edu/46/media/Bartlett_JMM06.pdf

### 4. [S022] The Face of Pain: Evidence for a Core Configuration

- **Authors/year:** Kenneth M. Prkachin; Patricia E. Solomon (2008)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** Pain 134(1–2), pp.82–97; PSPI formulation
- **Use:** Validated in pain-expression contexts, not a general diagnosis.
- **URL:** https://doi.org/10.1016/j.pain.2007.09.010
- **DOI:** `10.1016/j.pain.2007.09.010`

### 5. [S023] Pain Recognition Based on Joint Feature Selection and Nonlinear Modeling of Facial Expressions

- **Authors/year:** Steffen Kaltwang; Ognjen Rudovic; Maja Pantic (2012)
- **Authority:** `peer_reviewed` / `peer_reviewed_conference`
- **Locator:** p.370, Eq.1: AU4 + max(AU6,AU7) + max(AU9,AU10) + AU43
- **Use:** Displays the standard PSPI formula and UNBC conventions.
- **URL:** https://ibug.doc.ic.ac.uk/media/uploads/documents/74320368.pdf

### 6. [S021] Compound Facial Expressions of Emotion

- **Authors/year:** Shichuan Du; Yong Tao; Aleix M. Martinez (2014)
- **Authority:** `peer_reviewed` / `peer_reviewed_article`
- **Locator:** PNAS 111(15), E1454–E1462; tables and supplementary AU prototypes
- **Use:** Expression prototypes are statistical patterns, not deterministic inner-state labels.
- **URL:** https://doi.org/10.1073/pnas.1322355111
- **DOI:** `10.1073/pnas.1322355111`

### 7. [S070] Video-Based Facial Micro-Expression Analysis: A Survey of Datasets, Features and Algorithms

- **Authors/year:** Xianye Ben et al. (2022)
- **Authority:** `peer_reviewed` / `peer_reviewed_review`
- **Locator:** IEEE TPAMI 44(9), pp.5826–5846
- **Use:** Dataset thresholds vary; micro-expressions are not deterministic deception evidence.
- **URL:** https://doi.org/10.1109/TPAMI.2021.3067464
- **DOI:** `10.1109/TPAMI.2021.3067464`

### 8. [S019] OpenFace Action Units Documentation

- **Authors/year:** OpenFace project; Tadas Baltrušaitis et al. (2026)
- **Authority:** `official_open_source` / `official_open_source_documentation`
- **Locator:** Supported AUs; presence and 0–5 intensity outputs
- **Use:** Automatic detector covers only a subset of FACS; presence and intensity models are distinct.
- **URL:** https://github.com/TadasBaltrusaitis/OpenFace/wiki/Action-Units

### 9. [S069] MagicFace: High-Fidelity Facial Expression Editing with Action-Unit Control

- **Authors/year:** MagicFace authors (2025)
- **Authority:** `academic_preprint` / `academic_preprint`
- **Locator:** §II-A historical AU convention; §III relative AU variation
- **Use:** Relative continuous AU-conditioned generation; not a FACS manual replacement.
- **URL:** https://arxiv.org/abs/2501.02260

## Topic-specific caution

FACS codes visible movement; do not infer hidden emotion, pain diagnosis, or deception.
