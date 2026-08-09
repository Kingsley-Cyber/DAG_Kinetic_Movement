---
id: cpcs.gaps.src009_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009]
primary_route: cpcs/research/gaps/
---

# SRC-009 Open Research Questions

SRC-009 provides the complete CPCS paper v1.2 (8,731 lines), extraction guide
v1.2 (1,378 lines), Pegasus paper v1.0 (2,782 lines), and v1.2 package (33
files). Most questions are operational: "does the pipeline pass its own
acceptance checks?" rather than empirical unknowns.

## Implementation gaps

1. Does the reference pipeline (`video_to_cpcs_reference_pipeline.py`) pass
   all 4 commands (probe, prepare, init-record, validate) on a test video
   without errors? (Phase 0 exit check)
2. Does `validate_video_observation_graph.py` pass on the shipped example
   graph without warnings? (schema + semantic validation)
3. Does `merge_video_observations.py` produce a structurally valid VOG from
   the example observations, with zero unresolved conflicts?
4. Are the 92 source references [S001]–[S092] in the reference index all
   reachable at their listed URLs? (link rot audit)
5. Does the RAG corpus (179 JSONL records) pass line-level schema validation
   with unique record_ids and correct sha256 hashes?

## Cross-source questions

6. The VOG schema's 5 evidence classes (measured, detected, inferred,
   interpreted, authored) are a subset of the observation record's 7 classes
   (adding `defaulted`, `derived`). Should the VOG schema be extended to
   include all 7, or is the 5-class set intentional for the graph layer?
7. The pipeline config defines 7 capability statuses; the paper defines 8
   (adding `native_exact`). Should the pipeline config be updated, or is
   `native_exact` intentionally merged with `native_approximate`?
8. The extraction guide's 12 failure modes are a subset of the paper's 15.
   Which 3 are omitted, and does this matter for the MVP?
9. The Pegasus paper's fight layers include 3 new layers (anime VFX,
   camera/edit causality, interaction) not in SRC-005's combat coding.
   Should the combat coding card be extended with these layers?
10. The paper's 10 style domains (Appendix G) vs the extraction guide's 11
    tracking dimensions — are these aligned or is there a gap?

## Empirical unknowns

11. The 6 hypotheses (H1-H6) are stated but not tested. What is the minimum
    viable experiment for H3 (Laban variation produces perceptually distinct
    motion)?
12. The similarity budget defaults (temporal_structure 0.80, identity 0.00,
    etc.) are authored, not calibrated. What calibration protocol is needed?
13. The round-trip verification's 10 metrics have no established thresholds
    beyond the hard gates. What are reasonable soft thresholds?
14. The 4-tier MVP defines minimum capability but provides no benchmark
    results. What is the expected extraction quality at each tier?
15. The confidence fusion precedence chains are proposed, not empirically
    validated. Does calibrated geometry actually outrank semantic inference
    for camera motion type?

## Governance notes

- All threshold values, similarity budgets, and acceptance gates in SRC-009
  are `authored` — they are project controls, not scientific constants.
- The paper explicitly states CPCS is "a proposal, not a validated standard."
- The reference pipeline is a **reference implementation**, not a production
  system. Its scripts demonstrate the contract but do not constitute a
  complete extraction pipeline.
- The Pegasus paper's fight analysis is a worked example, not a validated
  fight-detection system.
