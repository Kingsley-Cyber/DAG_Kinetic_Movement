"""Pegasus 1.5 synchronous analysis.

Request body verified 2026-10-03 (docs.twelvelabs.io: sync analysis): `model_name` pegasus1.5;
`video` with exactly one source (`asset_id`, `url` or `base64_string`); `prompt` or `prompt_v2`
(structured prompt whose text refers to named image sources as `<@name>`); `temperature`
(API default 0.2); `max_tokens` (API default 4096); `response_format` json_schema; `start_time`,
`end_time`. This project's defaults are temperature 0.0 and max_tokens 8192: a project choice for
repeatable structured output, not the API default.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .common import CREATE_REQUEST_OPTIONS, MODELS, TwelveLabsError, build_client, to_plain


def analyze_video(
    prompt: str,
    *,
    asset_id: Optional[str] = None,
    video_url: Optional[str] = None,
    output_schema: Optional[dict] = None,
    images: Optional[Mapping[str, str]] = None,
    start_s: Optional[float] = None,
    end_s: Optional[float] = None,
    temperature: float = 0.0,
    max_tokens: int = 8192,
    client: Any = None,
) -> dict:
    if not prompt.strip():
        raise ValueError("prompt must be non-empty")
    if (asset_id is None) == (video_url is None):
        raise ValueError("provide exactly one of asset_id or video_url")
    if (start_s is None) != (end_s is None):
        raise ValueError("start_s and end_s must be supplied together")
    if start_s is not None and (start_s < 0 or end_s is None or end_s - start_s < 4):
        raise ValueError("clipped analysis requires an interval of at least 4 seconds")
    video = {"type": "asset_id", "asset_id": asset_id} if asset_id else {"type": "url", "url": video_url}
    kwargs: dict = {
        "model_name": MODELS["analyze"],
        "video": video,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "request_options": CREATE_REQUEST_OPTIONS,
    }
    if images:
        for name in images:
            if "<@%s>" % name not in prompt:
                raise ValueError("prompt must reference image '%s' as <@%s>" % (name, name))
        kwargs["prompt_v_2"] = {
            "input_text": prompt,
            "media_sources": [
                {"name": name, "media_type": "image", "asset_id": image_id}
                for name, image_id in images.items()
            ],
        }
    else:
        kwargs["prompt"] = prompt
    if output_schema is not None:
        kwargs["response_format"] = {"type": "json_schema", "json_schema": output_schema}
    if start_s is not None:
        kwargs["start_time"] = start_s
        kwargs["end_time"] = end_s
    active = client or build_client()
    response = to_plain(active.analyze(**kwargs))  # `analyze` is the non-streaming call in the SDK
    if response.get("finish_reason") not in ("stop", None):
        raise TwelveLabsError("analysis did not finish cleanly: %s" % response.get("finish_reason"))
    if not isinstance(response.get("data"), (str, dict)):
        raise TwelveLabsError("analysis returned no data")
    response["model_name"] = MODELS["analyze"]
    return response
