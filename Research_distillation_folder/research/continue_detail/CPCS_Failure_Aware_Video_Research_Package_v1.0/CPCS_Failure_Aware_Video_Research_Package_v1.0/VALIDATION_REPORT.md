# Validation Report

**Status:** `passed`  
**Validated:** 2026-08-05  
**Repository revision:** `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Live render campaign:** `not_run`

## Counts

| Catalog | Count |
| --- | --- |
| failure_records | 96 |
| families | 16 |
| metrics | 60 |
| providers | 21 |
| sources | 81 |
| claims | 35 |
| experiments | 8 |
| engineering_failure_records | 71 |
| engineering_metrics | 34 |
| contract_examples | 5 |

## Checks

| Check | Status | Details |
| --- | --- | --- |
| schema_meta_validation | passed | {"count": 10} |
| failure_records | passed | {"count": 96} |
| evaluation_metrics | passed | {"count": 60} |
| engineering_catalogs | passed | {"failure_records": 71, "metrics": 34} |
| experiments | passed | {"count": 8} |
| contract_examples | passed | {"count": 5} |
| source_traceability | passed | {"sources": 81, "claims": 35, "providers": 21} |
| identity_and_ordinal_integrity | passed | {} |
| required_outputs | passed | {"count": 31} |

## Limitations

- No authorized provider renders or human rating panel were executed.
- Provider reliability remains unmeasured by CPCS.
- Recent preprints and official provider claims retain the limitations recorded in SOURCE_CATALOG.csv.
