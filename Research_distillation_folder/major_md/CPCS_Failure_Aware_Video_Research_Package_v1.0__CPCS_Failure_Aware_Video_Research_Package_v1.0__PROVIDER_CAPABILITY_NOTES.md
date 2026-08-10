# Provider Capability and Reliability Notes

## Interpretation

`PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv` separates **documented interface capability** from **empirical reliability**. A model can officially accept first/last frames, multiple references, source video, audio, seeds, or keyframes while still failing identity, hidden state, event order, contact, or causal material response.

## Current research decisions

- Bind every claim to exact provider, model/endpoint, access surface, region, version/date, workflow, and source.
- Treat third-party adapters as separate surfaces.
- Do not infer native-provider behavior from an aggregator UI.
- Do not infer reliability from a showcase, internal benchmark, or marketing statement.
- Treat provider-side prompt enhancement/rewrite as an experimental factor.
- Preserve seed semantics exactly as documented; never equate a seed with artifact identity or compliance.
- Require one live canary and replay evidence before an executable provider profile is treated as qualified.

## Matrix scope

The matrix includes current or documented interfaces for Veo, Runway, Seedance, Kling, MiniMax/Hailuo, Wan, LTX, Wan open models, HunyuanVideo, CogVideoX, Mochi, Luma Ray, and the current unavailable status of Sora 2. Fields marked unverified must be checked against the exact authorized interface before compilation.
