# WO-10 — TwelveLabs client refresh: models, request bodies, asset library, uploads

> **Status 2026-10-03: implemented.** Owner chose the director repo (D1) and read-only plus test
> uploads (D3). Code: `director/tools/tlclient/` (`common`, `assets`, `analyze`, `embed`, `cli`),
> launcher `director/tools/tl.py`, tests `director/tools/tests/test_tlclient.py` (24 tests, fake
> clients), SDK 1.3.5 in `.venv/` (gitignored; `director/tools/tlclient/requirements.txt`).
> Live, verified: `doctor` ready (key from the keychain, value never printed); `assets list`
> returned the library (1 video, `x_video2.mp4`); `assets find x_video` found it. Remaining: live
> steps 4–6 below wait for the owner to name one image and one short video.
> The package is named `tlclient` because a local package called `twelvelabs` would shadow the SDK.
> Knowledge stores and Jockey were not ported: no consumer in this repo yet.
> Run: `.venv/bin/python director/tools/tl.py <command>`.

## Goal

A working, current TwelveLabs client the agent can use to (1) find assets already in the owner's
library, (2) upload images and videos of any practical size, (3) analyze with Pegasus and embed
with Marengo using current request bodies and an explicit model decision.

## Diagnosis (verified 2026-10-03)

Existing client: `/Users/king/ai-video-movement-prompt-system/lab/second_brain/src/providers/twelvelabs/`
(10 modules, about 890 lines; SDK-based; tests use fake clients).

| # | Stale or missing | Evidence in the code | Current fact (source) |
|---|---|---|---|
| 1 | SDK pin blocks every newer SDK | `common.py:13` `SDK_VERSION = "1.3.1"`; `build_client` raises unless `installed == SDK_VERSION`; pinned `twelvelabs==1.3.1` in `lab/second_brain/requirements.txt`, `setup.cfg`, `requirements-providers.lock` | latest SDK is **1.3.5** (PyPI); the SDK is installed only in the old `New project` venv, not for the clean checkout or system Python |
| 2 | Embedding model decision | `common.py:16` `MARENGO_MODEL = "marengo3.0"` as a constant | **Marengo 3.5** released 2026-08-31; identifier `marengo3.5`; 3.0 still works and is the default when `model_name` is omitted; **3.5 embeddings are not compatible with 3.0** (regenerate to migrate) |
| 3 | Embed request body | `marengo.py` sends per-type bodies (`{"image": {"media_source": {"asset_id": …}}}`) | for 3.5, sync calls use `input_type: "multi_input"` with `multi_input.media_sources[{media_type, asset_id | url | base64_string, name?}]` and optional `input_text` (composed queries, up to 10 sources); new options `embedding_dimension` (128, 256, 512), `embedding_uncertainty`, `auto_truncate` |
| 4 | Analysis model | `common.py:14` `PEGASUS_MODEL = "pegasus1.5"` | correct: Pegasus 1.2 is rejected since 2026-08-18; `pegasus1.5` is the only allowed value |
| 5 | Analyze body options | `pegasus_analyze.py` sends `video: {type: asset_id}`, `prompt`, `temperature`, `max_tokens`, `response_format`, `start_time`/`end_time` | still valid. Not used: `prompt_v2` (structured prompt with `<@name>` image placeholders), video sources `url` and `base64_string` (≤ 30 MB), `stream` (API default `true`); defaults are temperature 0.2 and max_tokens 4096 |
| 6 | **No way to find assets in the library** | `assets.py` has create, wait, store-item functions only; no list or search by name | `GET /v1.3/assets` — `client.assets.list(page, page_limit ≤ 50, asset_ids, asset_types ∈ image, video, audio, document, filename)`; `filename` is case-insensitive partial match; returns a pager of `AssetDetail` (`id`, `method`, `status`, `filename`, `file_type`, `size`, `duration`, `created_at`) |
| 7 | Upload limits | `assets.py:66` refuses local files over 200 MB (32 MB for images); no multipart | direct: video/audio ≤ 200 MB local or ≤ 4 GB by URL, images ≤ 32 MB, documents ≤ 200 MB local; **multipart: video/audio up to 10 GB** via `client.multipart_upload.create(filename, type, total_size)` → presigned chunk URLs → `report_chunk_batch` → `get_status` |
| 8 | Upload options | not passed | `user_metadata` (JSON string), `enable_hls`, `enable_thumbnail`; documents (PDF, text, Markdown) are a fourth asset type |
| 9 | Key and entry point | the key is only in the macOS keychain item `cpcs-twelvelabs-api`; the only wrapper that reads it (`bin/cpcs-twelvelabs`) is an untracked file in the old `New project` checkout and launches `pegasus`, not the provider CLI | `TWELVE_LABS_API_KEY` env var is not set in a normal shell, so `doctor` reports not ready |
| 10 | Knowledge stores and Jockey | used by `assets.py`, `jockey.py`, `knowledge_store_search.py` | still documented (knowledge stores, items, search; Jockey under "agents"); keep, not changed here |

Sources: docs.twelvelabs.io (v1.3) release notes, models, upload methods, API reference for
assets, analyze, embed v2, migration guide Marengo 3.0 → 3.5, Python SDK reference; PyPI.

## Decisions for the owner (defaults in brackets)

- **D1 Location.** [Port the client into this repo as `director/tools/twelvelabs/` and refresh it
  there; the old repo stays frozen.] Alternative: patch the provider in the prompt-system repo on a
  branch and pass its 18-step gate, which also fixes it for agents still using the old CPCS tools.
- **D2 Embedding default.** [`marengo3.5` for new work; `marengo3.0` selectable for stores already
  embedded with 3.0. The model is a parameter recorded in every result, never a silent constant.]
- **D3 Live calls.** Listing assets is read-only. Uploads write to the owner's TwelveLabs account
  and may incur cost: each live upload needs the owner's go and the file path.

## Changes (location per D1)

1. `common.py`
   - SDK compatibility: accept `>= 1.3.1, < 1.4` (compare parsed versions); record the installed
     version in `doctor`. Pin `twelvelabs>=1.3.5,<1.4` in the requirements file used.
   - `MODELS = {"analyze": "pegasus1.5", "embed_default": "marengo3.5", "embed_legacy": "marengo3.0"}`
     plus `resolve_embed_model(requested: Optional[str]) -> str` (allowed: the two Marengo ids;
     anything else raises). Each entry carries `verified_on` and the doc URL in a comment.
   - `resolve_api_key(env)`: `TWELVE_LABS_API_KEY`, else on macOS the keychain item
     `cpcs-twelvelabs-api` via `/usr/bin/security find-generic-password -a $USER -s … -w`. Never
     print or log the value; `doctor` reports only `api_key_source: env | keychain | none`.
2. `assets.py`
   - `list_assets(asset_types=None, filename=None, asset_ids=None, limit=200) -> list[dict]`:
     iterate the SDK pager (`page_limit=50`), stop at `limit`, return plain dicts sorted by
     `created_at` descending.
   - `find_assets(query, asset_type=None)`: `list_assets(filename=query, …)`; exact filename
     matches first.
   - `upload_asset(...)`: add `user_metadata: dict | None` (JSON-encode), `enable_hls`,
     `enable_thumbnail`; add `"document"` to media types; when a local video or audio file is over
     200 MB, route to `upload_asset_multipart`; images over 32 MB are refused with the limit named.
   - `upload_asset_multipart(file_path, media_type)`: `multipart_upload.create` → PUT each chunk to
     its presigned URL (stdlib `urllib.request`, read `chunk_size` bytes at a time) → collect ETags
     → `report_chunk_batch` (batches of ≤ 50) → request more URLs with
     `get_additional_presigned_urls` when `total_chunks` exceeds those returned → `get_status` →
     return the asset; refuse files over 10 GB.
3. `marengo.py`
   - `create_embedding(..., model=None, embedding_dimension=None)`: with `marengo3.5` send
     `input_type="multi_input"` and `media_sources` (text-only → `multi_input.input_text`); with
     `marengo3.0` keep today's per-type body. Reject `embedding_dimension` unless the model is 3.5
     and the value is 128, 256 or 512. The result includes `model_name`.
4. `pegasus_analyze.py`
   - accept a `video_url` alternative to `asset_id` (exactly one), and `images: dict[name, asset_id]`
     that switches to `prompt_v2` with `<@name>` placeholders. Pass `stream=False` explicitly.
     Keep temperature 0.0 and max_tokens 8192 as this project's defaults, stated in a comment as a
     project choice (API defaults are 0.2 and 4096).
5. CLI `python3 -m … twelvelabs`:
   `doctor` · `assets list [--type image|video|audio|document] [--name TEXT] [--limit N]` ·
   `assets find TEXT` · `upload <video|image|audio|document> (--file PATH | --url URL)
   [--metadata KEY=VALUE …] [--wait]` · `embed … [--model marengo3.5|marengo3.0] [--dim 512]` ·
   `analyze --asset-id ID | --url URL --prompt TEXT --schema FILE`.
6. Tests (fake client, no network): pager iteration and limit; filename filter passed through;
   exact-match-first ordering; SDK range check (1.3.1, 1.3.5 accepted; 1.2.9 and 1.4.0 refused);
   key source reported without the value; multipart routing above 200 MB and chunk reporting with
   a fake HTTP PUT; 3.5 body shape vs 3.0 body shape; `embedding_dimension` validation;
   `prompt_v2` body when images are given; `stream=False` passed.

## Live verification (after tests are green; each step needs the owner's go)

1. `doctor` → ready, `api_key_source: keychain`.
2. `assets list --limit 20` → the owner's library appears (read-only).
3. `assets find <a filename the owner names>` → found.
4. `upload image --file <owner's file> --wait` → status `ready`; then `assets find` shows it.
5. `upload video --file <owner's file> --wait` → status `ready`.
6. One `analyze` on the uploaded video with a three-field schema; one `embed` with `marengo3.5`.

## Acceptance

Unit tests green; steps 1–3 pass live; steps 4–6 pass when the owner approves them; no key value
appears in any output, log or file.

## Records

`plan/DECISIONS.md` (D1–D3 outcome; video harvest stays parked; this is transport only) ·
`plan/STATUS.md` · `implementation/QUEUE.md`.
