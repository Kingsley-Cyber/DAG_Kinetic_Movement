---
id: cpcs.gaps.src001_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §26]
primary_route: cpcs/research/gaps/
---

# SRC-001 Open Research Questions

All fourteen questions below are stated by the source itself as unresolved.
None carries an answer in SRC-001; each must be settled by CPCS experiments,
provider evaluations, or curation before any runtime policy depends on it.
The "Priority hook" column is a CPCS-side assignment (INFERENCE from the
governance priority policy), not a source statement.

| # | Question | Linked object | Priority hook |
|---|----------|---------------|---------------|
| 1 | What phase boundaries are sufficiently reproducible across annotators to become canonical? | phase grammar | P0 fixture: punch/reach |
| 2 | Which motion quantities improve provider adherence enough to justify their schema complexity? | kernel schema | P0 |
| 3 | Which kinematic controls survive provider compilation reliably? | capability classes | P1 |
| 4 | Which camera controls are actually native versus merely prompt-sensitive for each provider/model/version? | provider capability cards | P1 |
| 5 | Can complexity features predict generation failures sufficiently well to become routing policy? | complexity feature vector | P2 |
| 6 | Does structured carrier choice materially change motion adherence when semantic content is held constant? | carrier experiment design | P2 |
| 7 | What is the minimum useful style invariant vocabulary? | style constraint model | P1 |
| 8 | Which force/dynamics estimates are reliable enough for VOG evidence rather than research-only annotations? | fail-closed dynamics | P1 |
| 9 | What calibration is required before a scalar complexity score can be used for production decisions? | complexity feature vector | P2 |
| 10 | How should CPCS represent uncertainty when multiple 3D pose hypotheses are equally plausible? | monocular ambiguity | P1 |
| 11 | Which continuity constraints measurably reduce identity/teleport/pose-reset failures across providers? | continuity objects | P0 |
| 12 | Which occlusion types require explicit visibility bridges versus ordinary persistence constraints? | visibility-not-existence | P1 |
| 13 | Can causal-event constraints improve generation outcomes without over-constraining creative variation? | causal event semantics | P2 |
| 14 | Which continuity failures are best addressed by compiler decomposition rather than stronger prompting? | compiler pipeline | P2 |

## Governance note

- Q6 is operationalized by
  `research/sources/experiments/carrier_effect_experiment_design.md`.
- Q4 must be answered **per provider/model/version** — provider cards in
  `providers/` must carry version stamps, never timeless capability claims.
- Q10–Q12 touch PROJECT_DERIVED continuity objects; promotion of those
  objects is blocked until these questions have empirical answers.
