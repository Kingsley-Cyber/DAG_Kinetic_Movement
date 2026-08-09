# Repository Integration Checklist

## Before copying code

- Pin repository commit `3db5dcef5f4902ac7343b79a3d9bdae7dc17fc7e` as the audit baseline.
- Confirm no newer branch or commit changes the canonical schemas, lab rules, or provider assets.
- Preserve `research/` byte-for-byte.

## Structural integration

- [ ] `lab/runtime/models/scene.py` owns the authoritative runtime object.
- [ ] Existing CPCS-MX fields are mapped rather than duplicated under new names.
- [ ] YAML and XML are generated/editable views, not competing authorities.
- [ ] Every time value records clock and units.
- [ ] Every coordinate value records coordinate frame and units.
- [ ] Authored, solved, detected, measured, inferred, and interpreted values remain distinguishable.

## Deterministic gates

- [ ] STN unit tests pass.
- [ ] Seeded contradictory timelines fail with responsible constraint IDs.
- [ ] Underconstrained points are reported.
- [ ] State/resource contradiction tests pass.
- [ ] Every requested control is represented in the compilation loss report.
- [ ] Required unsupported/unknown controls fail closed.
- [ ] Provider contracts validate against JSON Schema.
- [ ] Contract documentation access date and exact model/API surface are recorded.

## Repository gates

```bash
python3 -m pytest lab/tests/runtime -q
python3 lab/scripts/sync_repo.py --fix
python3 lab/scripts/validate_repo.py
```

Only the final command’s exit code is authoritative for repository integrity. Runtime quality still requires DMR benchmark acceptance tests; the existing integrity gate explicitly does not measure output quality.
