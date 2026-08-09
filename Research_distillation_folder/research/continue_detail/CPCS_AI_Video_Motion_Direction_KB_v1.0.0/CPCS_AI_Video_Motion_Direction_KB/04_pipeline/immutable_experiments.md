# Immutable Experiment Ledger

## Purpose

Current video models are probabilistic and product surfaces change. CPCS learns through controlled experiments while preserving exactly what was tested.

## Record requirements

- hypothesis and variable under test;
- canonical scene hash;
- compiler/adaptor/derived-weight versions;
- provider, exact model/endpoint/surface;
- full request and rendered prompt;
- reference asset URIs and SHA-256;
- seed if accepted, with no promise of determinism;
- output URIs/hashes and provider metadata;
- latency/cost/error;
- automatic metrics and human annotations;
- environment and date;
- immutable flag and supersession link.

## Experiment design

Change one factor or use a declared factorial design. Repeat enough seeds to estimate variance. Randomize presentation to evaluators. Blind model/prompt identity when practical. Maintain held-out scene families so derived weights do not memorize one choreography.

## Append-only behavior

Incorrect metadata is not edited. Add a correction record with `supersedes` and a reason. Assets are content-addressed; changing bytes creates a new hash.

## Minimum evaluation axes

intent, predicate/action, contact, identity, camera, timing/rhythm, expression, style, physics, temporal coherence, audio synchronization, and overall usefulness.
