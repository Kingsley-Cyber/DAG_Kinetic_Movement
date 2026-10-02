# Control layer — checkable requirements

The control layer emits and validates; it never decides. Each requirement has an id so tests can
cite it. The reference implementation of R-01…R-20 is `director/tools/director.py` with tests in
`director/tools/tests/test_director.py`; the rest are to build. Vocabulary is the research's own
(see `ARCHITECTURE.md` §3 and §12 for sources).

## A. Controls and dispositions

| Id | Requirement | Status |
|---|---|---|
| R-01 | A control has `id, pass, field, value, importance 0..1, lock, origin, capability, disposition`, optional `treatment, exactness, expected_visual_effect, check, clause` (`ir.schema.json`) | done |
| R-02 | `field` has exactly one owner pass (`passes.yaml → owns`); a control written by another pass fails | done |
| R-03 | `capability` ∈ native, approximate, semantic, unsupported, unknown; `disposition` ∈ native, approximated, semantic, omitted, unsupported, unknown; the pair must be consistent | done |
| R-04 | A locked control is never omitted; a locked `exactness: exact` request on a semantic/unknown/unsupported capability blocks with a reason | done |
| R-05 | `native` applies only to fields the model profile lists as `native_fields`; native controls become settings, not prose, unless a treatment gives wording | done |
| R-06 | A Style- or Render-tier pass may not write `beats`, `pathways` or `hands` | done |
| R-07 | Camera grammar is mandatory: at least one camera control covering motion and one covering framing or optics | done |
| R-08 | A phrase is never upgraded to native because it sometimes works (no code path may promote capability from evidence alone) | done by construction |

## B. Validators over the IR (never over the ask)

| Id | Requirement | Status |
|---|---|---|
| R-09 | Hand ledger: one state per (actor, hand, beat); a stage needing N hands lists N hands that are `free` or holding the pathway's object or parts; a `camera` hand cannot be used | done |
| R-10 | Action pathway: stages in causal order; at least anticipation, one action stage, one aftermath stage; last stage ends in `end_state`; any state change after contact needs prior contact and transfer (no magic jump) | done |
| R-11 | Every `effect` stage has a non-empty stated `reaction`; every `contact` has a later effect with a reaction (impact-and-physics language) | done |
| R-12 | Beats: order 1..n; `after` and `caused_by` point to earlier beats; a reaction cannot precede its cause | done |
| R-13 | Fit: `load = Σ min_s`; `load ÷ duration` → FITS ≤ 0.85, TIGHT ≤ 1.0, OVERLOADED > 1.0 with options (cut lowest importance, overlap non-causal pairs, split, lengthen); no duration → UNDERSPECIFIED, no seconds invented | done |
| R-14 | Speech capacity: words ≤ duration × 190 / 60 for any `audio.dialogue` control | done |
| R-15 | Anti-arcade detectors on power actions: plane transition present; anticipation present; weight-transfer path recorded; Flow alternates | to build (phase 3) |
| R-16 | Relative prompting: flag two absolute magnitude words for one quality in one clause; require an anchor before an escalation | to build (phase 3) |

## C. Emitter

| Id | Requirement | Status |
|---|---|---|
| R-17 | `emit` runs `check` first and is blocked by any error | done |
| R-18 | Assembly order is the profile's `clause_order` (default `[SHOT] [SUBJECT AND ACTION] [PERFORMANCE] [TIMING] [CAMERA] [NEGATIVES]`); entities first, then beats in order, then controls by importance | done |
| R-19 | Budget: compress to `short` wording (lowest importance first), then drop unlocked lines (lowest importance first), then block with options including "one clip per causal event" when more than one pathway changes state; locked content is never squeezed | done |
| R-20 | Receipt: every prompt line → source (entity, beat, or control + treatment) with origin; `prompt_sha256`; `emit_report.json` with chars, limit, settings, dispositions, drops, compressions, four validity levels | done |
| R-21 | Loss record per non-exact realization with the research fields (`loss_id, canonical_field, requested, provider, capability, projection, replacement, loss{type, severity}, accepted`) and `loss_code` where applicable | done |
| R-22 | Same inputs and profile → byte-identical prompt | done |
| R-23 | Dialects: a treatment's `dialect=<model>` block overrides `core` for that model; dialect changes wording only, never order | parsing done; profile rules to build (phase 6) |
| R-24 | Negatives: positive-language invariants first; a dedicated negative field when the profile has one, otherwise one short "Avoid:" line | done |
| R-25 | Suppression reason codes on anything not emitted: `low_observability · provider_unsupported · redundant · conflicting · lower_priority · already_encoded_by_stronger_control · token_budget` | token_budget done; others to build (phase 3) |
| R-26 | Redundancy: a control whose wording is already carried by beats or a stronger control is suppressed with `already_encoded_by_stronger_control` | to build (phase 3; run 001 read-back found the duplication) |
| R-27 | Strength-scaled emission: profile `strength: strong | weak`; weak → minimal core (3–5 highest-leverage lines) + camera/continuity compensation | to build (phase 5) |
| R-28 | Structured carriers (YAML/JSON/XML/hybrid) from the same IR, each with a loss report; promoted only on render evidence | to build (phase 7) |

## D. Model profiles

| Id | Requirement | Status |
|---|---|---|
| R-29 | `director/profiles/<model>.yaml`: every fact tagged `documented | documented_thirdparty | measured | guess | unknown` with source and date | done (seedance) |
| R-30 | Profiles for Kling, Hailuo, Veo, Wan from the tree's provider findings plus current docs | to build (phase 9) |

## E. Records

| Id | Requirement | Status |
|---|---|---|
| R-31 | `decisions.jsonl` per run: bridge chain + DecisionRecord subset; `selected ∈ alternatives` | written by the LLM; validator to build (phase 4) |
| R-32 | `director/gaps.jsonl`: every INFERENCE decision appended | written by the LLM; validator to build (phase 4) |
| R-33 | `director/runs/ledger.jsonl`: one line per render verdict; treatments' `## Effects` updated from it | to build (phase 2) |

## IR schema

`director/ir.schema.json` is the contract. Rule: a field exists only if a check or the emitter
reads it. Current top-level keys: `schema_version, run_id, ask, model, clip, pass_plan, entities,
hands, pathways, beats, controls, notes`. Example instance: `director/runs/001_bottle_selfie/ir.json`.
