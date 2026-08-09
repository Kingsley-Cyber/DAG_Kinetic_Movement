# Implementation Roadmap

## Phase 0 — Repository and invariants

- adopt schemas, source IDs, provenance classes, units, and graph tiers;
- run package validator in CI;
- define content-addressed asset storage and immutable experiment IDs.

**Exit check:** all included examples validate; no missing source IDs; adapter dates are visible.

## Phase 1 — Canonical scene compiler

- intent/beat/Affect planner;
- BESS, connectivity, primitive, phase, interaction, rhythm, camera, style records;
- JSON/YAML/XML/prose exports;
- semantic validation and loss reports.

**Exit check:** five examples compile deterministically and round-trip without losing IDs/times.

## Phase 2 — First adapters

Implement two complementary targets: one reference/performance-oriented surface and one text/image-to-video surface. Probe live schemas, encode combination rules, and build request renderers.

**Exit check:** adapter requests pass dry-run/live validation and the loss report matches actual payload fields.

## Phase 3 — Evaluation harness

- pose/contact/camera/identity automatic metrics;
- human annotation UI/protocol;
- immutable record writer;
- content hashes and provenance.

**Exit check:** repeated generations create complete append-only records with output hashes and blinded evaluations.

## Phase 4 — Computational Laban MVP

Start with observable heads: reach, path directness, timing/suddenness, Shape axes, initiation/sequence, and contact/support. Add expert annotation and calibration. Keep Weight/Flow assisted.

**Exit check:** actor/camera-disjoint metrics and calibrated confidence meet predeclared thresholds.

## Phase 5 — Derived learning

Train adapter-specific prompt/risk weights, reranking, and failure predictors from immutable experiments.

**Exit check:** held-out improvement over curated baseline with no source-definition mutation.

## Phase 6 — Production hardening

- rights/security review;
- adapter freshness job;
- schema migrations;
- performance/queue observability;
- regression suite by model/scene family;
- disaster recovery and artifact retention.

**Exit check:** reproducible release manifest, passing regression suite, and documented rollback.
