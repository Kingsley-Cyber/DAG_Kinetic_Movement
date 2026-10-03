# Queue

Execute top to bottom. Status: `todo` · `doing` · `done` · `blocked`. A GATE stops execution
until the owner acts (see `OWNER_ACTIONS.md`).

| # | Work order | Plan task | Depends on | Status |
|---|---|---|---|---|
| WO-01 | Relative prompting: anchors in the IR, comparisons in the emitter, magnitude lint | T16 | — | todo |
| WO-02 | Physics causal events (minimal): schema, validators, emission | T35 (first slice) | WO-01 | todo |
| WO-03 | Passes connect: `reads`, beat-scoped controls, coupling checks | T17 | WO-02 | todo |
| WO-04 | Run 002: product handling with two hands (handoff test) | T12 | WO-03 | todo |
| WO-05 | Run 003: thrown into the pool (world reactions) | T12, T30 (as needed) | WO-04 | todo |
| WO-06 | First ingest: DMR package; run 004 glass fixture; camera move validator | T36, T38 | WO-05 | todo |
| WO-07 | Run 005: camera-only | T12 | WO-06 | todo |
| WO-08 | Experiment arms: absolute vs relative, wording rungs (emit flags + one run) | T18 | WO-06 | todo |
| **GATE A** | **Owner confirms the model route, renders E1 (runs 001–005) and E2/E3 arms, fills verdicts** | T13 | WO-07, WO-08 | blocked on owner |
| WO-09 | Kill check and effects: read the ledger, write the result in STATUS, update treatment `## Effects` | T14 | GATE A | todo |
| — | After WO-09: Phase 3 work orders (T20–T29, T39) are written only if the kill check passes | | | not written |

Notes:
- The order follows the external review's remediation order: enforce existing contracts, one
  working dialect mapping (done in T09), handoff test, then renders, then breadth.
- WO-04 is the handoff test: record every point where you had to guess in `plan/STATUS.md`.
- Work orders for Phase 3 and later are deliberately not written yet (evidence before machinery).
