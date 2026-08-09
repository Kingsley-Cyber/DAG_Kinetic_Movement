---
id: cpcs.gaps.src002_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §31, L2.§56]
primary_route: cpcs/research/gaps/
---

# SRC-002 Open Research Questions

SRC-002 states two open-question sets (§31 Layer 1, L2.§56 Layer 2). None
carries a closed answer in the source; all must remain `unknown` or
`experimental` until experiments/evidence close them.

## Layer 1 — semantic/measurement (SRC-002 §31)

1. Which FACS AU subset should CPCS support natively vs via semantic projection?
2. Which provider models actually honor AU identifiers?
3. Which providers preserve bilateral/asymmetric instructions?
4. What is the provider-specific response to ordinal vs NL intensity?
5. Can Laban proxy features predict CMA labels across subjects?
6. Which Bartenieff patterns are reliably detectable from monocular video?
7. How should breath be estimated when audio is absent?
8. Which temporal carrier yields the highest provider adherence?
9. How much combined FACS/Laban/Bartenieff structure improves output vs a simpler semantic instruction?
10. What are the minimum controls required for each CPCS provider profile?

## Layer 2 — operational (SRC-002 L2.§56)

1. Which FACS temporal tolerance windows suit CPCS verification across frame rates/protocols?
2. Which automatic AU detectors are sufficiently calibrated for project-level verification?
3. Can project-normalized FACS intensity be calibrated across subjects/cameras without becoming misleading?
4. Which Laban qualities have reliable measurable proxies under controlled video conditions?
5. Which Laban-to-kinematic mappings generalize across action classes?
6. Which Bartenieff connectivity patterns are reliably classified from pose sequences?
7. Which cross-framework interactions are published research vs useful CPCS engineering hypotheses?
8. How much provider adherence improves when realization primitives are inserted between semantic controls and NL?
9. How much semantic compression can occur before provider adherence degrades?
10. What attention budget maximizes provider adherence for each target model?
11. Which shot-scale observability heuristics generalize across providers?
12. Can generated-video verification reliably detect qualitative Laban adherence, or must human/expert judgment remain in the loop?
13. Which continuity constraints can be measured automatically from the VOG?
14. Which actor-to-actor temporal dependencies are best causal vs authored narrative relations?
15. How should stylized/anime performance modify realization without corrupting the underlying semantic framework?

## Governance note

- Frozen-package reconciliation (`CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip`)
  is itself an open item — package-specific claims cannot be certified until
  the ZIP is supplied.
- Q8/Q9 (Layer 1) and Q8/Q9 (Layer 2) overlap and are operationalized by the
  SRC-002 model-conditioning experiments (see `src002_operational_experiments.md`).
