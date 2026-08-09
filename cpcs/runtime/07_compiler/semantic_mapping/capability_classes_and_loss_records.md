---
id: cpcs.compiler.capability_classes_loss_records
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §14, §10.8, SRC-004 §22, §23]
primary_route: cpcs/runtime/07_compiler/semantic_mapping/
secondary_routes:
  - cpcs/runtime/07_compiler/loss_ledger/
  - cpcs/runtime/08_provider_negotiation/capability_matching/
interfaces: []
---

# Compiler Capability Classes and Loss Records

## Doctrine

Required compiler pipeline:

```text
research concept → retrieved evidence → director decision
→ canonical semantic field → control candidate → provider capability check
→ native / approximate / semantic / unsupported → provider representation
→ compilation-loss record
```

## Capability classes

| Class | Meaning | Example |
| --- | --- | --- |
| `native` | provider exposes a direct control | canonical `camera.pan` → provider pan control |
| `approximate` | related control, weaker semantic guarantee | focal_length=85mm → "compressed telephoto look", marked approximate |
| `semantic` | no direct control; NL describes desired effect | motion_style → NL projection |
| `unsupported` | required control cannot be safely expressed | exact_world_trajectory with no trajectory interface |
| `unknown` | capability not yet verified — research only, never treated as supported | facs_AU12 on an untested provider (SRC-002 §21) |

Do not pretend a natural-language prompt provides exact control it cannot
deliver (e.g. exact world trajectories).

## Fail-closed rule

A required exact control **fails closed** unless the caller explicitly
permits degradation. Continuity constraints follow the same negotiation and
must never be silently treated as satisfied by descriptive prose.

## Compilation-loss record

```json
{
  "loss_id": "loss_009",
  "canonical_field": "camera.optics.focal_length",
  "requested": { "value": 85, "unit": "mm" },
  "provider": "provider_x",
  "capability": "unsupported",
  "projection": "semantic",
  "replacement": "telephoto_compressed_perspective",
  "loss": { "type": "numeric_control_loss", "severity": "medium" },
  "accepted": false
}
```

## FACS-specific loss (SRC-002 §20)

A provider with `facs_AU12: semantic_only` cannot honor an ordinal
`intensity: C`. It compiles to a NL visual description and emits:

```json
{
  "control": "facs_AU12_intensity_C",
  "requested": "facs_ordinal:C",
  "compiled_as": "natural_language_visual_description",
  "loss_class": "representation_loss",
  "severity": "medium",
  "reason": "provider_has_no_native_facs_intensity_control"
}
```

The compiler must never claim exact preservation across this loss.

## Loss taxonomy (SRC-002 L2.§36.4)

`unsupported_semantic · approximation · observability_loss ·
scope_loss · temporal_loss · laterality_loss · intensity_loss ·
causal_loss · continuity_loss · interaction_loss · priority_suppression ·
provider_attention_loss`

## Compiler operations (SRC-001 §26)

resolve_defaults · normalize_units · normalize_frames · normalize_rotation ·
expand_side_semantics · resolve_phase_dependencies ·
resolve_continuity_constraints · resolve_persistence_constraints ·
resolve_causal_dependencies · validate_evidence · negotiate_capability ·
compile_native · compile_approximate · compile_semantic ·
reject_unsupported · emit_compilation_loss

## Realization statuses (SRC-004 §22)

A provider that cannot express a canonical control exactly must not be treated
as exact merely because the natural-language prompt mentions it. Realization
statuses:

```text
native_exact
native_approximate
baked_into_reference
compressed_to_text
postprocess_only
evaluation_only
dropped_with_warning
unsupported_error
```

Example: canonical `face.AU04 peak = 0.71 at 2.73s` on a prompt-only provider
compiles as `compressed_to_text` with lost: exact spline, calibrated peak,
apex tolerance. Verification: post-generation facial estimate.

## Compile loss → decision linkage (SRC-004 §23)

Compile loss is already present. ADRG links it to the decision that produced
it: `decision_id` and `loss_id` are attached to the existing compiler result.
This does not change the compiler's authority — it adds an audit trail.

## Compiler semantics additions (SRC-006 §8)

SRC-006 sharpens four rules on top of this doctrine:

1. **No prompt wording converts an unenforceable semantic request into an
   exact control.** If a provider accepts only free-form prompting with no
   event-time or trajectory control, the emitted clause is classified
   `semantic` — never `native` or `approximate` — and the loss record carries
   `loss_code: temporal_precision_unenforceable` with the requested tolerance
   and a `block_or_explicit_degrade` policy decision.
2. **Compilation loss is part of candidate feasibility.** Branches are scored
   after capability negotiation when provider realization differs, and loss
   enters Pareto comparison.
3. **`compile_key` includes capability and adapter versions.** Two
   semantically identical plans can have different `compile_key` values under
   different provider profiles; a provider-only wording alternative is a
   realization candidate under the same semantic state, not a semantic
   branch.
4. **Provider outputs never overwrite canonical intent.** Generated output
   creates observed/simulated execution records; it does not become the
   canonical target.

## Exactly-once loss accounting (SRC-007 G009)

Compilation-loss reporting is an **exactly-once accounting model** over
canonical control IDs and field paths:

```text
canonical requested control → carrier → transformation → provider field → result
```

Every field has exactly one terminal disposition per provider request:

```text
native · approximated · semantic · omitted · unsupported · unknown
```

with residual risk. Transformations may add ordered intermediate records but
may not erase or duplicate the terminal entry. Composite controls, partial
field support, conflicts, provider defaults, and information lost before
versus after request submission are all specified.

Required invariants:

```text
no requested control without a terminal disposition
no unexplained emitted provider field
no unsupported required control silently omitted
no approximation without method and residual risk
no semantic prose claim treated as native control
```

`test_every_requested_control_has_terminal_disposition`,
`test_no_unexplained_emitted_provider_field`,
`test_no_unsupported_required_control_silently_omitted`,
`test_approximation_declares_method_and_risk`,
`test_semantic_prose_not_native_control`.

## ADRG compile-loss ledger and verifier checkpoints (SRC-011 EXTEND)

> **Source:** SRC-011 §17, §19 — "Compile-loss ledger", "Compiler/verifier".

### Compile-loss ledger entry

The ADRG ledger records, per canonical control × target adapter, one of the 8
realization statuses plus retained/lost information, linked to the decision
that produced it:

```json
{
  "control_id": "face.AU04.peak",
  "decision_id": "decision.face.reaction",
  "target_adapter": "prompt_only.generic.v1",
  "realization_status": "compressed_to_text",
  "retained": ["event timing", "observable description"],
  "lost": ["exact spline", "calibrated peak", "apex tolerance"],
  "verification": ["post_generation_facial_estimate"]
}
```

This is exactly-once per terminal disposition (SRC-007 G009 above): the
ledger extends the loss record with `decision_id` linkage (already in the
tree via SRC-004 §23) and a `verification` field naming the post-hoc check.

### Three verifier roles (role separation)

The package separates three roles that must not be silently merged in one
model call: (1) **planner** — produces decisions, never declares its own
output valid; (2) **verifier** — runs external checks (parsers, schemas,
graph rules, capability checks, metrics) and never alters targets or
thresholds; (3) **repairer** — applies the smallest valid patch and
revalidates. Self-critique may refine quality; it never substitutes for
external verification (external validation over intrinsic self-critique).

### Checkpoints A–I

The verification sequence: A input schema + digest · B retrieval bundle
coverage · C graph integrity (nodes/edges/constraints) · D decision records
complete and referenced · E canonical controls map to decisions · F
realization statuses present for all controls · G target package alignment
(timebase, frame identity, hashes) · H post-generation adherence metrics · I
repair bounds respected and escalation recorded.

### Bounded repair protocol

Repair one failed artifact with the smallest valid change: base digest →
failed validator id → exact error → relevant schema/rule → object slice →
JSON Patch array only, beginning with a `test` op confirming the expected
base. No patch to unrelated paths, no weakening of hard constraints; empty
patch + `needs_escalation` when no safe patch exists. (Consistent with
`repair_strategy.md`; the package adds the empty-patch escalation form.)

## Execution-carrier decision rules R1–R4 (SRC-013 EXTEND)

> **Source:** SRC-013 (user research return, staged) — gap_answer_02
> §provider-control carrier decision matrix; evidence E8 (Veo first/last
> frame), E11 (Veo reference images), E12 (Runway Gen-4.5).

Carrier selection is a provider-surface decision, recorded per compile:

- **R1 — Endpoint authority:** when the provider exposes first/last-frame
  conditioning, boundary states compile to endpoint frames and the prompt
  carries only the in-between mechanism — endpoints are constraints, not a
  physics solver.
- **R2 — Mechanism authority:** when the provider exposes no per-event
  controls, the causal mechanism stays in the prompt as positive-language
  invariants; negative phrasing names failures, it does not encode physics.
- **R3 — One causal event per clip:** split at every causal handoff
  (unzip ≠ open); never pack two state-changing hand events into one
  unconstrained generation.
- **R4 — Carrier escalation:** escalate carriers only when a lower carrier
  demonstrably fails verification; the declared `format_policy` hierarchy
  is a request — the provider's real control surface is the ground truth
  for capability class.

## Provider control-surface matrix (SRC-014 EXTEND)

> **Source:** SRC-014 (user research return, staged) — gap_answer_03
> §Current provider-control matrix + §negative-prompt rule; evidence E8–E16
> (official provider docs, dated 2026-08-09).

Capability facts change fast; the matrix is dated, never eternal:

- **Veo 3.1:** dedicated `negativePrompt`; first/last-frame conditioning
  (first frame required when `lastFrame` is used); 4/6/8 s durations for
  that workflow.
- **Sora 2 Videos API:** no negative field documented; `input_reference`
  anchors the first frame only; API deprecated — shutdown 2026-09-24, not a
  new long-lived dependency.
- **Kling VIDEO 3.0 / 3.0 Turbo:** positive + negative share one prompt
  text; 3,072-char limit (2,500 recommended; 512/shot); Turbo is first-
  frame only; 3–15 s.
- **Runway Gen-4.5:** no negative field; positive phrasing recommended;
  `promptText` 1–1,000 UTF-16 units; keyframes app (Gen-3 retired); 2–10 s.

Negative-prompt precedence (compile rule): causal/geometric invariants in
positive language → endpoint frames for boundary states → dedicated
negative field as secondary exclusions → reject causally invalid outputs
in verification (never expect prompt syntax to guarantee physics).

## Verification

`test_semantic_mapping_records_loss_code`, `test_compile_key_has_capability_and_adapter_versions`,
`test_provider_output_never_overwrites_canonical_intent`,
`test_unsupported_required_control_fails_closed`,
`test_approximate_control_creates_loss_record`,
`test_native_control_has_no_false_loss` (SRC-001 §26),
`test_compiled_control_has_realization_status`,
`test_loss_record_required_for_non_exact_realization`,
`test_loss_linked_to_decision_id`,
`test_carrier_decision_rule_recorded`,
`test_endpoint_frames_used_when_available`,
`test_one_causal_event_per_clip`,
`test_provider_matrix_dated_and_scoped`,
`test_negative_precedence_positive_first`.
