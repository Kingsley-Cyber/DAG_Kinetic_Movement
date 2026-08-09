# Unverified, Contradictory, and Anecdotal Findings

## Purpose

This file prevents attractive but unproven claims from entering CPCS as truth. Items here are hypotheses, capability ambiguities, or version-sensitive statements that require official interface capture, controlled generation, independent reproduction, or human calibration.

## Provider capability ambiguities

- **Veo 3.1 audio and 4K behavior are endpoint/mode specific.** The current repository profile sets `sound_generation=false` and 720p/1080p. Current Google documentation contains model/preview/mode distinctions that must be captured per endpoint rather than generalized.
- **Seedance 2.0 exact native API limits were not fully verified for every access surface.** The official launch documents multimodal inputs and up to 15-second AV generation, but adapter products may expose different limits and behavior.
- **Kling 3.0 exact API schemas, prompt limits, resolutions, and region/account availability require interface capture.** Official company materials establish broad multimodal capability, not reliability.
- **Runway third-party model adapters are separate surfaces.** A Seedance, Veo, or other model accessed through Runway must not inherit native-provider assumptions without qualification.
- **Wan regional endpoints and prompt rewriting can differ.** The selected region, endpoint alias, rewrite setting, and returned metadata must be recorded.
- **LTX repository performance claims depend on checkpoint, sampler, quantization, VAE, hardware, and workflow.** Local runs must pin all of them.
- **Ray 3.2 product and API availability can differ.** This package treats the documented Ray 3.2 workflow as source-video modification, not general T2V/I2V generation.
- **Sora 2 is not represented as a current CPCS provider.** The official current status page states the consumer Sora product is unavailable as of 2026-04-26, and no current public production interface was verified in this pass.

## Unverified control claims

- XML, YAML, or JSON may improve human/compiler organization, but no universal provider-side intelligence gain is established.
- Exact timestamps, numeric coordinates, camera values, or biomechanics parameters may be semantically approximated when the provider accepts only prompt text.
- Negative prompts can reduce some unwanted concepts, but they do not prove state persistence or causal correctness and may prime the forbidden concept in some settings.
- First/last frames may improve endpoints without improving—and sometimes while worsening—the intermediate path. Effect size is provider/task dependent.
- More references can create reference conflict, identity blending, or priority dilution; a higher reference count is not automatically better.
- Same-seed comparisons reduce one source of variation where supported but do not establish byte-identical or semantically isolated outputs.
- Provider prompt enhancement may improve aesthetics while changing canonical semantics. It must be a separate arm.

## Research/benchmark uncertainty

- Several important 2026 benchmarks in the source catalog are recent preprints. Their methods, rankings, code, and conclusions may change after peer review or independent reproduction.
- Benchmark prompts and evaluated model versions age quickly relative to commercial releases.
- Automated physical and semantic judges can share blind spots with the systems they evaluate.
- Simulated counterfactual and video-prediction benchmarks inform continuity mechanisms but do not directly measure every cinematic generative-video workflow.
- Aggregate benchmark results cannot predict success for one exact CPCS scene without a matched fixture.

## Community anecdotes

No community anecdote is used as final evidence in this package. Reports such as “Kling ignores JSON,” “Seedance preserves characters better,” “Veo understands physics,” or “XML works better” should enter only as versioned experiment hypotheses with exact prompts, interfaces, outputs, and dates.

## 100% certainty boundary

The package cannot verify with 100% certainty the hidden internal mechanism of closed commercial models, current account/region availability for every provider, undocumented prompt parsing, future service changes, or provider-specific reliability without executing the sealed campaigns. All such conclusions are marked as inference, current capability documentation, or not run.
