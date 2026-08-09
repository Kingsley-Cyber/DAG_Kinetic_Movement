---
id: cpcs.gaps.src005_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §30, §24.6, §27.4, §30.5]
primary_route: cpcs/research/gaps/
---

# SRC-005 Open Research Questions

SRC-005 identifies ten research questions that remain genuinely empirical.
None should be filled with invented constants. Each should have a fixture and
measurable outcome before becoming a hard CPCS rule.

1. Does explicit phase and contact coding improve temporal compliance over
   text-only prompting? (§30.1 Q1)
2. Do Laban and mannerism layers improve perceived performance specificity
   without reducing action correctness? (§30.1 Q2)
3. Does separating anatomical motion from stylized deformation reduce rig
   failures in superhuman clips? (§30.1 Q3)
4. Do dense pose controls outperform key poses for fight-scene contact
   timing? (§30.1 Q4)
5. Does a canonical score improve transfer of choreography across characters
   and morphologies? (§30.1 Q5)
6. Does re-extraction enable targeted correction with fewer full
   regenerations? (§30.1 Q6)
7. Which fields remain unsupported by current generation adapters? (§30.1 Q7)
8. Which ambiguity-resolution strategy — targeted director questions versus
   named batch defaults — produces the best balance of author control and
   throughput? (§24.6)
9. What phase-labeled smoothness thresholds distinguish intended discontinuity
   (impact, strike, stumble) from artifact across style profiles? (§27.4)
10. What calibration procedure produces Laban proxy profiles that are
    predictive without collapsing distinct concepts? (§30.5)

## Governance note

- These questions are operationalized by the CPCS-MX experimental program
  (`cpcs.research.cpcs_mx_experiments`) with ablation conditions A–G.
- Q1/Q2/Q4 relate to the ablation ladder (text → action graph → phase/contact
  → root/joint → Laban/mannerism/face → style → dense control).
- Q3 relates to the three joint-limit domains (`cpcs.body.skeleton_topology`)
  and the superhuman transform (`cpcs.body.superhuman_transform`).
- Q7 relates to capability coverage matrices (`cpcs.runtime.constraint_compilation`).
- Q9 relates to phase-labeled smoothness evaluation (`cpcs.verification.verification_layers`).
- Q10 relates to Laban numeric calibration
  (`cpcs.mx.laban_numeric_calibration_contract`).
- All thresholds remain `EXPERIMENTAL` / `null` until calibrated.
