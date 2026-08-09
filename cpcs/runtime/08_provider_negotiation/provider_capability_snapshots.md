---
id: cpcs.runtime.provider_capability_snapshots
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G007, G008, G021]
primary_route: cpcs/runtime/08_provider_negotiation/
secondary_routes:
  - cpcs/runtime/07_compiler/semantic_mapping/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.compiler.capability_classes_loss_records
  - cpcs.runtime.state_equivalence_keys
  - cpcs.runtime.sceneplan_authority_projection
---

# Provider Capability Snapshots

> **Source:** SRC-007 G007/G008 — "Provider contracts and adapters", G021 —
> "Provider lifecycle"

## Principle

Represent each provider contract as a **versioned, dated capability
snapshot**, never as code constants or prose. Do not treat an old provider
snapshot as current truth. Never claim a current capability without official
documentation or a dated experiment.

## Snapshot fields

```text
native controls · reference/control media · duration · fps · camera controls
image conditioning · motion conditioning · pose controls · negative prompting
structured input · carrier support · API version · limits · unknowns
evidence date · expiry/reprobe condition
```

## Evidence kinds

```text
documented capability      (official documentation)
experimentally observed    (dated experiment)
adapter support            (realized through an adapter)
unverified assumption      (never treated as supported)
```

A snapshot also records: capability identity/granularity, evidence locator
and retrieval date, model/API version and scope, native parameter domain,
approximation strategy, prohibited transformations, expiry, smoke test,
drift signal, and reprobe trigger — plus the exact pre-compilation
negotiation rule.

## Provider lifecycle

```text
unverified → verified → stale → reprobe_due → invalidated
```

Compilation may proceed in each state only per explicit policy. A smoke test
establishes what it can establish; anything else requires official
documentation. Changed behavior is quarantined without rewriting historical
evidence.

## Demonstration requirement

For one canonical scene, two providers must produce different
`RepresentationPlan` and loss ledgers while preserving canonical meaning.

## Verification

`test_snapshot_versioned_and_dated`,
`test_snapshot_evidence_kind_declared`,
`test_old_snapshot_not_treated_as_current`,
`test_stale_snapshot_blocks_or_requires_reprobe`,
`test_two_providers_different_plans_same_meaning`.

## KB control-surface snapshot (SRC-012 EXTEND)

> **Source:** SRC-012 topic 14 — "AI Video Model Capabilities and Control
> Surfaces" (dated snapshot verified 2026-07-30, not a permanent ranking)

### Capability status vocabulary (7 values)

```text
native · reference_conditioned · prompt_only · postprocess · unsupported · unknown · legacy
```

CPCS never upgrades a prompt phrase to `native` just because the prompt
sometimes works (same rule as the "unverified assumption" evidence kind
above).

### Model matrix (verified 2026-07-30)

| Provider | Model/surface | Native controls / limits |
|---|---|---|
| Google | Veo 3.1 | duration [4, 6, 8] s · 16:9/9:16 · 720p/1080p/4k model-dependent · seed · native audio |
| Kling AI | VIDEO 3.0 / Omni | 3–15 s · multi-shot · shot-level duration · native audio · element voice (Omni) |
| Runway | Gen-4.5 | 2–10 s · 24/25 fps |
| Runway | Act-Two | 3–30 s · gesture control via character image mode |
| Luma AI | Ray 3.2 Modify Video | motion/structure Off or 1–9 · Poses vs Blocking |
| Adobe | Firefly Video | camera-motion reference 5–10 s < 200 MB (first 5 s used) |
| OpenAI | Sora 2 | **legacy** — web ended 2026-04-26, API scheduled end 2026-09-24; no new primary adapter without a migration plan |

**Surface parity rule:** store `surface=web|api|partner_wrapper`; UI and API
capabilities are probed separately and never assumed equal.

### Canonical downcasting (preferred → fallback; loss risk)

| Canonical control | Preferred surface | Fallback | Loss risk |
|---|---|---|---|
| actor_identity | element/reference image or video, character asset | descriptive prompt + seed | high without reference |
| motion_trajectory | source/performance video, motion control, keyframes | prompt prose | high |
| camera_track | camera-motion reference, shot-level camera controls | camera prompt phrases | medium-high |
| phase_timing | shot duration/keyframes/performance video | ordered prompt with time markers | high |
| FACS | driving performance/reference face | visible feature prose, not AU codes alone | high |
| BESS | performance/motion reference | natural-language descriptors | medium-high |
| audio/dialogue | native audio + speaker/voice controls | postproduction | model dependent |

### Adapter contract fields

`provider · model_id · surface · verified_at · documentation_snapshot ·
native_capabilities · prompt_only · validation_rules · ttl_days`. Worked
example: Veo 3.1 adapter with `validation_rules: ["reference_images=>duration=8",
"resolution=4k=>duration=8"]`, `ttl_days: 30`. Invalid combinations are a
**schema error before submission**; if documentation and live schema
conflict, the adapter stays blocked until the discrepancy is resolved and
documented.

### Loss report

A compiled request returns: preserved natively / represented by reference /
translated to prose / deferred to postprocess / unsupported-unknown /
expected failure risks / experiment IDs supporting prompt choices. A model
output can succeed artistically while the adapter truthfully reports that
phase timing and FACS were prompt approximations rather than native controls.

## Verification

`test_status_native_not_upgraded_from_prompt`,
`test_surface_parity_probed_separately`,
`test_invalid_combination_schema_error_before_submit`,
`test_legacy_adapter_requires_migration_plan`.
