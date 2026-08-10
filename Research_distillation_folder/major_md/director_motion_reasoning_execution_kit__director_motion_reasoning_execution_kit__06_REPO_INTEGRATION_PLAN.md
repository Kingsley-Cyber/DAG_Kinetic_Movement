# Repository Integration Plan

## Objective

Extend `Kingsley-Cyber/ai-video-movement-prompt-system` without duplicating its frozen research packages or breaking its control plane.

## Phase 0 — reproducible baseline

Run and save output:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
python3 lab/scripts/validate_repo.py
python3 lab/scripts/sync_repo.py
python3 lab/scripts/concepts.py stats
```

Acceptance: baseline state, branch, SHA, gate status, and any pre-existing warnings are recorded before edits.

## Phase 1 — requirement-to-owner map

Generate a matrix for every requested concept with one status:

```text
existing_complete | existing_partial | missing | conflicting | obsolete
```

For each non-missing item, name its owning file/schema/script. A new file is prohibited when an existing owner can absorb the change cleanly.

Recommended active owners:

| Concern | Owner |
|---|---|
| Retrieval concepts | `lab/concepts.jsonl` |
| Full research-space status | `lab/CONCEPT_INDEX.md` |
| Active control channels | `lab/CONTROL_SURFACE.md` |
| Format responsibility | `lab/FORMAT_CONTROL_MAP.md` |
| Cross-domain canonical skeleton | `lab/UNIVERSAL_MOTION_SKELETON.md` |
| Composition blocks | `lab/blocks.yaml` |
| Routing/workflows | `lab/AGENTS.md` + one routed `RUNBOOK_*.md` when necessary |
| Active schemas | `lab/schema/` or a clearly routed active implementation area |
| Active utilities | `lab/scripts/` |
| Derived knowledge graph | `lab/graph.json`, regenerated only |

## Phase 2 — source delta research

Research only the missing/partial claims. Minimum new evidence clusters:

1. Bartenieff six connectivity patterns and terminology.
2. BML/SAIBA architecture, modalities, sync points, and conformance status.
3. Domain-specific phase models proving that no universal seven-phase model is established.
4. EmotionML dimensional/trace/confidence interoperability.
5. ISB coordinate-system and reporting recommendations.
6. Empirical format/structured-output effects, including contradictory results.
7. PROV-O, SHACL, and temporal ontology alignment.

Every source record must include stable ID, exact supported concepts, source type, primary/secondary status, peer-review status, access date, rights note, and files that cite it.

## Phase 3 — ontology and schema delta

Add backward-compatible modules rather than a second canonical root:

```text
body_connectivity[]
  pattern_id
  canonical_name
  aliases[]
  interval
  initiation_region
  propagation_path[]
  direction
  phase_lag[]
  joint_chain[]
  support_effect
  com_effect
  observed_proxies[]
  evidence[]
  confidence
  knowledge_type

behavior_sync[]
  behavior_id
  modality
  bml_mapping
  sync_points{}
  canonical_event_refs[]
  conformance_level
  provenance

phase_profile
  profile_id: dmr.normalized-seven.v1
  knowledge_type: project_specific_synthesis
  phases[]
  domain_mapping{}
  optionality{}
  merge_rules[]
  interruption_rules[]
```

Rules:

- No numerical proxy without `proxy_method`, `units`, `normalization`, and `uncertainty`.
- No BML compliance claim without a verified profile and validation result.
- No phase marked universal.
- One authority per quantity.
- Every new ID is stable and namespaced.

## Phase 4 — serializers and semantic equivalence

Canonical JSON is authoritative. Generate:

```text
canonical JSON
  -> YAML authoring/readable projection
  -> XML event envelope/BML-aligned projection
  -> JSONL atomic evidence/event records
  -> Markdown/CNL documentation projection
```

For every projection record:

- source canonical hash;
- serializer version;
- fields preserved;
- fields transformed;
- fields omitted;
- reason and severity of each loss.

Round-trip tests compare normalized typed objects and semantic hashes, not whitespace or object-key order.

## Phase 5 — fixtures

Build a compact fixture matrix from shared canonical inputs:

1. cautious room entry and greeting;
2. conversational gesture/affect transition;
3. walk-stop-turn;
4. staged screen action;
5. original shonen-style transform;
6. live-action VFX transform;
7. product-size demonstration;
8. structural transfer to a different product;
9. dialogue performance with face/body/camera/audio.

Avoid nine hand-maintained copies. Store canonical fixtures once and generate the five projections.

## Phase 6 — verification

Required checks:

```bash
python3 lab/scripts/concepts.py validate
python3 lab/scripts/build_graph.py
python3 lab/scripts/sync_repo.py
python3 lab/scripts/validate_repo.py
pytest -q
git diff --check
```

Additional checks to add:

- Bartenieff canonical IDs and aliases;
- BML namespace/sync-point integrity;
- phase profile classification and domain mapping;
- JSON Schema Draft 2020-12 validation;
- YAML safe parsing and type preservation;
- XML well-formedness/XSD and XXE rejection;
- JSONL line validation, revision/supersedes integrity;
- semantic-hash equality across lossless projections;
- loss report for intentionally lossy projections;
- temporal interval consistency;
- provenance/source-ID coverage;
- internal link and citation checks;
- source URL checks where network policy permits.

## Phase 7 — controlled integration

1. Update `lab/registry.yaml` pointers only for new active artifacts.
2. Add concept cards with at least three natural-language triggers.
3. Update `CONCEPT_INDEX.md` and relevant control maps.
4. Add a routing row for every new runbook.
5. Regenerate `lab/graph.json` last.
6. Append one `CHANGELOG.md` line in the same commit.
7. Run the full root gate after every final edit.
8. Commit on `agent/director-motion-reasoning` with the repository's owner identity and co-author line.
9. Push and verify that remote SHA equals local SHA.

## Completion report

Return exact paths, source counts by class, claim coverage, schemas/utilities/tests added, command outputs, unresolved claims, limitations, diff summary, commit SHA, remote branch, and the next implementation step. Never claim success from planned commands.
