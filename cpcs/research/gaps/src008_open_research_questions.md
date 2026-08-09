---
id: cpcs.gaps.src008_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008]
primary_route: cpcs/research/gaps/
---

# SRC-008 Open Research Questions

The frozen package provides concrete schemas, scripts, and examples. Most
questions are operational: "does the reference implementation pass its own exit
checks?" rather than empirical unknowns.

## Implementation gaps

1. Does the reference compiler pass all 4 example YAMLs through authoring
   validation, profile resolution, canonical validation, and report zero
   unresolved items? (Phase 1 exit check)
2. Does `validate_cpcs_mx_package.py` pass on the shipped package without
   warnings? (Phase 0 exit check)
3. Do the compiled JSON examples round-trip: can they be re-validated against
   the canonical schema independently? (deterministic serialization check)
4. Are the 80 source references [S001]–[S080] in the reference index all
   reachable at their listed URLs? (link rot audit)

## Cross-source questions

5. The observation record schema's 7 evidence classes match SRC-005's E1
   EXTEND to evidence_two_axis_model. Does the SRC-006 measurement_record_form
   also align with these 7 values, or does it use a different taxonomy?
6. The RAG record schema's 10 record types — should CPCS adopt these as the
   canonical RAG chunk types across all sources, or are they MX-specific?
7. The 8-profile catalog covers natural/UGC/combat/anime/superhuman. What
   additional profiles are needed for the SRC-006 reasoning scenarios or
   SRC-007 DMR runtime?
8. The compiler's `capability_report` always says
   `"dense_motion_synthesis": "not_implemented"`. When a production adapter
   is built (Phase 6), how should the report format change?

## Package completeness

9. The `director_motion_reasoning_execution_kit.zip` is a separate package.
   Should its contents be distilled as SRC-009, or is it subsumed by SRC-007?
10. The `CPCS_Failure_Aware_Video_Research_Package_v1.0.zip` is a separate
    package with failure taxonomy, records, and mitigation matrices. Should
    it be distilled as its own source?

## Governance note

- All package thresholds and example values are `authored` — they are project
  controls, not biological or scientific constants.
- The reference compiler is a **reference**, not a production system. Its exit
  codes and merge rules are testable contracts, but it does not synthesize
  motion.
