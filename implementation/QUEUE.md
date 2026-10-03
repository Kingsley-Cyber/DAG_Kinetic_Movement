# Queue

Execute top to bottom. Status: `todo` · `doing` · `done` · `blocked`. A GATE stops execution
until the owner acts (see `OWNER_ACTIONS.md`).

| # | Work order | Plan task | Depends on | Status |
|---|---|---|---|---|
| WO-01 | Relative prompting: anchors in the IR, comparisons in the emitter, magnitude and vague-word lint | T16 | — | done 2026-10-03 (11 tests; run 001 prompt unchanged; tool split into dircheck.py, diremit.py, director.py) |
| WO-02 | Physics causal events (minimal): schema, validators, emission | T35 (first slice) | WO-01 | done 2026-10-03 (8 tests; run 001 prompt unchanged) |
| WO-03 | Passes connect: `reads`, beat-scoped controls, coupling checks | T17 | WO-02 | done 2026-10-03 (6 tests; run 001 prompt unchanged) |
| WO-03b | Shared scratchpad: `pack <pass>`, `check --pass`, `open.jsonl`, saved `check_report.json`; beat spacing and the constant-motion warning | T33 (first slice) | WO-03 | done 2026-10-03 (8 tests; run 001 prompt unchanged) |
| WO-04 | Run 002: product handling with two hands (handoff test) | T12 | WO-03b | done 2026-10-03 (check GREEN/TIGHT 0.9; prompt 1,987/2,000; read-back MATCH by a Haiku subagent; 3 new treatments; 83 tests unchanged; 24 guesses in STATUS; owner renders pending) |
| WO-05 | Run 003: thrown into the pool (world reactions) | T12, T30 (as needed) | WO-04 | done 2026-10-02 (check GREEN/FITS 0.7; prompt 1,967/2,000; read-back MATCH by a Haiku subagent; 2 new treatments; 87 tests unchanged; 15 guesses in STATUS; owner renders pending) |
| WO-06 | First ingest: DMR package (triage already written in `plan/ingest/DMR_triage.md`); typed outcomes, camera move validator, profile lifecycle, CI workflow; run 004 glass fixture | T36, T38 | WO-05 | done 2026-10-02 (97 tests, 10 new in IngestDMR; runs 001–003 prompts byte-identical; run 004 check GREEN/FITS 0.675, prompt 1,997/2,000, read-back MATCH by a Haiku subagent; 1 new treatment world.glass_break; c_latency unsupported; owner renders pending) |
| WO-07 | Run 005: camera-only | T12 | WO-06 | todo |
| WO-08 | Experiment arms: absolute vs relative, wording rungs (emit flags + one run) | T18 | WO-06 | todo |
| **GATE A** | **Owner confirms the model route, renders E1 (runs 001–005) and E2/E3 arms, fills verdicts** | T13 | WO-07, WO-08 | blocked on owner |
| WO-09 | Kill check and effects: read the ledger, write the result in STATUS, update treatment `## Effects` | T14 | GATE A | todo |
| — | After WO-09: Phase 3 work orders (T20–T29, T39) are written only if the kill check passes | | | not written |
| WO-10 | TwelveLabs client refresh (models, request bodies, asset library listing, image and video uploads incl. multipart) | — | — | done 2026-10-03 (code, 24 tests, live doctor/list/find); live uploads wait for the owner's two files |

Notes:
- The order follows the external review's remediation order: enforce existing contracts, one
  working dialect mapping (done in T09), handoff test, then renders, then breadth.
- WO-04 is the handoff test: record every point where you had to guess in `plan/STATUS.md`.
- Work orders for Phase 3 and later are deliberately not written yet (evidence before machinery).
