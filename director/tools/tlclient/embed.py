"""Marengo embeddings (Embed API v2, synchronous).

Verified 2026-10-03 (docs.twelvelabs.io: create sync embeddings, migration guide 3.0 → 3.5):
with `marengo3.5` every sync request uses `input_type: "multi_input"` and
`multi_input.{input_text, media_sources[]}`; with `marengo3.0` the per-type bodies remain.
`embedding_dimension` (128, 256, 512) is Marengo 3.5 only. Embeddings from the two models are not
compatible: never mix them in one store; the model is returned with every result.
"""

from __future__ import annotations

from typing import Any, Optional, Sequence

from .common import (
    CREATE_REQUEST_OPTIONS,
    EMBED_DIMENSIONS,
    MODELS,
    build_client,
    resolve_embed_model,
    to_plain,
)

MEDIA_INPUTS = ("video", "audio", "image", "document")
MAX_MEDIA_SOURCES = 10


def build_embed_request(
    input_type: str,
    *,
    text: Optional[str] = None,
    asset_id: Optional[str] = None,
    url: Optional[str] = None,
    image_asset_ids: Optional[Sequence[str]] = None,
    model: Optional[str] = None,
    embedding_dimension: Optional[int] = None,
) -> dict:
    """Return the keyword arguments for `client.embed.v_2.create` (without request options)."""
    model_name = resolve_embed_model(model)
    modern = model_name == MODELS["embed_default"]
    if embedding_dimension is not None:
        if not modern:
            raise ValueError("embedding_dimension requires %s" % MODELS["embed_default"])
        if embedding_dimension not in EMBED_DIMENSIONS:
            raise ValueError("embedding_dimension must be one of %s" % ", ".join(map(str, EMBED_DIMENSIONS)))
    if input_type not in ("text", "multi_input") + MEDIA_INPUTS:
        raise ValueError("input_type must be text, video, audio, image, document or multi_input")
    if input_type == "document" and not modern:
        raise ValueError("document embeddings require %s" % MODELS["embed_default"])

    def media_source(kind: str) -> dict:
        if (asset_id is None) == (url is None):
            raise ValueError("%s embedding requires exactly one of asset_id or url" % kind)
        return {"asset_id": asset_id} if asset_id else {"url": url}

    kwargs: dict = {"model_name": model_name}
    if input_type == "text":
        if not text:
            raise ValueError("text embedding requires text")
        if modern:
            kwargs.update(input_type="multi_input", multi_input={"input_text": text})
        else:
            kwargs.update(input_type="text", text={"input_text": text})
    elif input_type in MEDIA_INPUTS:
        source = media_source(input_type)
        if modern:
            kwargs.update(input_type="multi_input",
                          multi_input={"media_sources": [dict(media_type=input_type, **source)]})
        else:
            kwargs.update({"input_type": input_type, input_type: {"media_source": source}})
    else:  # multi_input: text composed with images
        ids = list(image_asset_ids or [])
        if not text or not ids:
            raise ValueError("multi_input embedding requires text and image asset ids")
        if len(ids) > MAX_MEDIA_SOURCES:
            raise ValueError("multi_input supports at most %d media sources" % MAX_MEDIA_SOURCES)
        kwargs.update(input_type="multi_input", multi_input={
            "input_text": text,
            "media_sources": [{"media_type": "image", "asset_id": item} for item in ids],
        })
    if embedding_dimension is not None:
        kwargs["embedding_dimension"] = embedding_dimension
    return kwargs


def create_embedding(input_type: str, *, client: Any = None, **options: Any) -> dict:
    kwargs = build_embed_request(input_type, **options)
    active = client or build_client()
    result = to_plain(active.embed.v_2.create(request_options=CREATE_REQUEST_OPTIONS, **kwargs))
    if isinstance(result, dict):
        result["model_name"] = kwargs["model_name"]
    return result
