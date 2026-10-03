# DMR gap register — triage for the text-only compiler

Source: `Research_distillation_folder/research/continue_detail/director_motion_reasoning_complete_package/director_motion_reasoning_gap_report.md`
§3 "Gap register" (22 gaps, DMR-G001…G022), read in full 2026-10-03. The report audited the
prompt-system repo at `3db5dce` (2026-07-20); research access date 2026-07-31.

Statuses: closed · implementable_now · requires_experiment · unknown · deferred · rejected.
"Reduced" means the text-only compiler takes the part of the gap that has a consumer here.

| Gap | What the register asks for | Priority there | Status here | Lands as |
|---|---|---|---|---|
| G001 Authoritative runtime object | one executable ScenePlan separating authored, solved, observed values | P0 | implementable_now (reduced) | the IR is the execution projection; every value carries an origin tag; R-50 (IR is never a second semantic authority) |
| G002 Deterministic temporal solver | Allen-to-endpoint compiler + STN, negative-cycle explanation, underconstraint detection | P0 | requires_experiment for a solver; closed for the arithmetic part | R-12, R-13 (order, cause before reaction, fit verdict, UNDERSPECIFIED without a duration). A solver is added only if runs show order conflicts the checks miss |
| G003 Hierarchical action/state semantics | preconditions, effects, resource locks; same-hand conflicts, ownership discontinuities | P0 | closed for hands and object states; implementable_now for more | hand ledger R-09, pathways R-10, state chain (T09); extend stage kinds only when a run needs them |
| G004 Persistent scene state | state snapshots across beats and shots, invariants, shot handoff | P0 | implementable_now (reduced) | continuity locks and pathway end states; shot handoff = `connection.start_end_states` (camera) when multi-shot work starts |
| G005 First-class contact graph | typed lifecycle: actor, target, sites, start/end, confidence, visibility, support, normal, reaction link, cheat policy | P0 | implementable_now | `physics_events` (WO-02) with `contact_state` incl. occluded and editorial; "cheat policy" = the degradation rules (R-43) |
| G006 Feasibility validator | pass / warn / fail / unknown checks for support, reach, joint limits, penetration; never claim exact forces from video | P1 | implementable_now (reduced) | typed outcomes R-51 (the deep-research prompt's five outcomes are a superset: pass, fail, indeterminate, not_applicable, unobservable; "warn" stays the warnings list). Reach, joint limits and penetration need geometry → deferred |
| G007 Versioned provider capability contracts | contracts pinned to exact model/API/version/region; six-way classification; stale or unknown contract blocks execution | P0 | implementable_now, with one recorded deviation | profile facts with tag, source, date and lifecycle (R-52, R-54). Deviation: this compiler emits text for manual rendering and makes no API calls, so an `unverified` profile emits with a flag instead of blocking |
| G008 Provider adapters | compile canonical fields into exact request parameters and conditioning assets | P0 | deferred | text prompt + recommended settings only; no API adapter until the owner wants unattended rendering |
| G009 Complete compilation-loss report | exactly-once field accounting, fail closed | P0 | closed | R-03, R-19…R-21, route resolution (T09) |
| G010 Reproducible generation runner | GenerationManifest: exact model, API version, request/response digests, seeds, output links | P0 | implementable_now (reduced) | `ledger.jsonl` fields: model, route, version, seed, prompt hash, IR hash, output filename (R-45, WO-09). The runner itself is deferred with G008 |
| G011 Calibrated extraction stack | tracking, 3D reconstruction, camera solve, hand/face/gaze, optical flow | P1 | deferred | out of text-only scope; verification is the owner or a VLM answering yes/no questions |
| G012 Camera–body motion disentanglement | background/camera solve, world-root reconstruction | P1 | deferred | same |
| G013 Structured evaluator | target/observed alignment with confidence | P1 | requires_experiment (reduced) | verdict tables per adherence dimension and three yes/no per event; no automatic scorer |
| G014 Failure taxonomy and causal diagnosis | typed failure labels, earliest responsible layer | P1 | implementable_now (reduced) | `failures.jsonl` classes (vocabulary gap, ceiling, unknown) and `depends_on` for upstream repair (R-46) |
| G015 Minimal repair engine | JSON Patch plans, protected invariants, dependency-aware re-check | P1 | implementable_now as procedure | repair mode in the protocol: smallest IR change, locks protected, `check` and `emit` re-run. No patch engine |
| G016 Benchmark and annotation protocol | fourteen-category benchmark with gold graphs and human ratings | P0 | requires_experiment | golden asks (runs 001–005) and `EXPERIMENTS.md` are the first slice |
| G017 Statistical experiment harness | repeated-condition A/B, effect sizes | P0 | implementable_now (reduced) | paired seeds, ≥ 3 per arm, decision rules recorded as conventions (`EXPERIMENTS.md`) |
| G018 Reasoning-grade hybrid retrieval | lexical + dense + typed graph retrieval, contradiction retrieval, reranking | P2 | deferred | pass packs and the trigger test set (T33, T34). Graph retrieval is adopted only if query logs show a failure the router cannot fix |
| G019 Format doctrine validation | semantic-equivalence serializer and controlled format experiments | P0 | requires_experiment | T60 structured carriers; no format has a universal role |
| G020 FACS/Laban/Bartenieff calibration | reliability and provider-adherence evidence for every numeric scale | P3 | requires_experiment | numeric rungs are experiments only (E3); ordinal stays ordinal (R-35) |
| G021 Provider lifecycle monitoring | scheduled doc/API diff, contract expiry, smoke tests | P1 | implementable_now (reduced) | lifecycle state and dates on profile facts (R-52); no scheduler |
| G022 Runtime CI and maturity evidence | unit, property, golden and integration tests wired into CI | P0 | implementable_now | a GitHub Actions workflow running `python3 -m unittest discover -s director/tools/tests` on push and pull request (WO-06 Part B) |

## What reading the register changed

1. **G010, G018 and G022 are now defined** (they were unnamed in the deep-research prompt):
   generation runner, hybrid retrieval, runtime CI.
2. **Seedance has documented facts in the owner's research.** §6 of the report (evidence E05,
   BytePlus ModelArk Video Generation API, accessed 2026-07-31) classifies **BytePlus Seedance
   2.0**: text prompt native; duration native, 4–15 s; aspect ratio and resolution native; seed
   native; native audio; first and last frame and multi-reference media-conditioned; camera
   trajectory semantic "except a `camera_fixed` parameter"; exact event timestamps unsupported;
   contact constraints, FACS and Laban numeric tracks semantic only; negative prompt and masks
   unknown; multi-shot semantic or unknown. "Legacy parameters embedded in prompt text must not be
   treated as equivalent to top-level API parameters." Capabilities of Seedance routed through
   Runway must not be inherited. These are now in `director/profiles/seedance.yaml`.
3. **The register's classification has six classes:** native, media-conditioned,
   semantic-text-only, approximated, unsupported, unknown. Here `media-conditioned` is recorded
   only as an exclusion (text-only) and `semantic-text-only` is `semantic`.
4. **The report's own priority logic supports the plan's order:** "This ordering deliberately
   resists the temptation to perfect FACS/Laban/Bartenieff numeric controls before the system can
   even prove that a reaction occurs after contact." P3 for calibration; contact, state, time and
   loss accounting first.
5. **Its "low-value or premature work" list is adopted as a guardrail:** expanding terminology
   without executable consumers; universal claims for JSON/YAML/XML; more provider templates
   without a contract and tests; a physics simulator before support/contact/state checks; numeric
   Bartenieff or Laban controls before reliability and adherence tests; learned graph retrievers
   before a retrieval benchmark; multi-agent orchestration before each agent has deterministic
   interfaces and acceptance gates.
6. **Other dated provider facts** (for later profiles): Veo 3.1 on Google Cloud has no sound while
   the Gemini API preview surface has audio, so the surface must be pinned; Kling VIDEO 3.0 Omni
   is a product profile (multi-shot, up to 15 s, shot-level camera semantics), not a verified API;
   Sora 2 is discontinued (no adapter).

## Not taken from the package

The `dmr_runtime_starter` code (Pydantic models, STN solver, compiler) stays reference reading
(admission ledger). The benchmark's fourteen categories, the extraction stack and the adapters
are deferred with the evidence each would need: a route with an API, a chosen detector, and
render results showing the text-only path has hit its ceiling.
