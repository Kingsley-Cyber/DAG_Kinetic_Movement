---
distillation_id: DIST-014
source_id: SRC-014
status: complete
coverage: core
---

# Distillation Ledger — SRC-014

User research return (gap_answer_03, 2026-08-09): causal video-generation
reliability cheat sheet — provider-control matrix (Veo 3.1, Sora 2, Kling
3.0/3.0 Turbo, Runway Gen-4.5), negative-prompt precedence, endpoint
conditioning limits, STRIPS-vs-contract clarification, one-causal-event
rule (evidence E1–E16) → CPCS knowledge tree. Distilled 2026-08-09.
Coverage: core (1 EXTEND + corroboration). Provider facts and numeric
limits stay staged.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-014_video_generation_reliability_cheatsheet.md`.
Epistemic class: research_package (staged — "not curated repository truth").
BLUF: generators produce plausible sequences, not guaranteed mechanical
state transitions; stack = typed action operator → one causal event per
clip → endpoint anchors → provider compiler → causal verifier → chaining.

## PASS 1 — Structural map

- BLUF + 6 findings (pin state/contact/order; planning-inspired not STRIPS;
  endpoints ≠ physics solver; one handoff per generation; negative-prompt
  assumption corrected per product; camera vocabulary recognized)
- Provider-control matrix (4 providers × grammar/endpoints/negative/
  limits/duration/notes)
- Practical negative-prompt precedence rule (4 steps)
- Why models break: world-simulator hypothesis, benchmark evidence
  (VideoPhy, PhyGenBench), mechanism failure taxonomy
- Planning operators: STRIPS mapping + minimal systematic recipe + sling-bag
  state variables + example durative operator + full causal chain

## PASS 2 — Placement (D2)

| Unit | Route | Action |
| --- | --- | --- |
| Provider control-surface matrix + negative-prompt precedence | `runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md` | EXTEND (SRC-014) |
| Corroboration of SRC-013 R1–R3 (endpoint authority, mechanism authority, one causal event per clip) | — | SUPPORT (no new object) |
| Identity + ledger + gap-register closure note supplement | `research/source_registry/identities/`, `research/gaps/understanding_gap_register.md` | CREATE (this batch) |

## PASS 3 — Staged facts (NOT canonical)

Provider durations/limits (Veo 4/6/8 s; Kling 3,072-char / 512-shot; Runway
1–1,000 UTF-16; 2–15 s ranges) and Sora 2 shutdown 2026-09-24 are recorded
as SRC-014 evidence dated 2026-08-09; re-verify per provider update before
any promotion (promotion_rules).

## Housekeeping

DIRECTORY.md regenerated; checker 0 deviations; control plane reference
§2/§8/§9/§14 synced; doctrine register D-2026-08-09-11.
