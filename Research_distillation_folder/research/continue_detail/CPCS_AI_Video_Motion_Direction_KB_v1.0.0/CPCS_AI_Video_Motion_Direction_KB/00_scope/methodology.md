# Methodology

## Evidence classes

| Class | Meaning | Production treatment |
|---|---|---|
| `ESTABLISHED` | Defined by an established notation, manual, standard, official documentation, or foundational text | Preserve source vocabulary and locator |
| `EMPIRICAL` | Supported by a study, dataset, or validated implementation | Store population, measurement method, limitations, and uncertainty |
| `PRACTICE` | Repeated professional convention, including animation and film craft | Use as a tunable default, never as a law |
| `CPCS_CONVENTION` | A new normalization, preset, mapping, schema, or compiler rule introduced here | Version, test, and permit replacement |
| `UNVERIFIED` | Could not be located in a reliable source or remains ambiguous | Exclude from curated graph; preserve only in a gap log |

## Research policy

1. Prefer official standards, manuals, project documentation, and primary papers.
2. Use foundational books when they are the controlling source for a practice framework.
3. Use preprints for emerging work only with their status explicit.
4. Give dynamic product controls a `verified_at` date and force revalidation before release.
5. Preserve contradictions instead of silently selecting the convenient result.
6. Label all numeric presets as source values, derived formulas, or CPCS conventions.

## Citation policy

Topic files cite stable source IDs such as `[S007, pp.343–348, §§II–V]`. The source registry stores the full bibliographic record and locator. Edition-variable books use chapters/sections where a stable page cannot be guaranteed.

## Reproducibility

The repository includes JSON Schemas, immutable experiment records, model-adapter snapshots, examples in JSON/YAML/XML/prose, evidence matrices, test cases, and a deterministic validation script.
