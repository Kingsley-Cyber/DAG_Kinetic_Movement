"""Asset library: list, find, upload (direct, URL, multipart), wait.

Limits verified 2026-10-03 (docs.twelvelabs.io: upload methods, create an asset, multipart):
direct local video/audio and documents ≤ 200 MB, images ≤ 32 MB; URL video/audio ≤ 4 GB;
multipart local video/audio ≤ 10 GB. Assets process asynchronously: poll until `ready`.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Callable, List, Optional, Sequence
from urllib.parse import urlparse

from .common import (
    CREATE_REQUEST_OPTIONS,
    READ_REQUEST_OPTIONS,
    TwelveLabsError,
    build_client,
    field,
    to_plain,
    wait_until_ready,
)

MB = 1024 * 1024
GB = 1024 * MB
MEDIA_TYPES = ("video", "image", "audio", "document")
DIRECT_LIMIT = {"video": 200 * MB, "audio": 200 * MB, "document": 200 * MB, "image": 32 * MB}
MULTIPART_LIMIT = 10 * GB
MULTIPART_TYPES = ("video", "audio")
PAGE_LIMIT = 50  # API maximum

EXTENSIONS = {
    "image": (".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tif", ".tiff"),
    "video": (".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi", ".m3u8"),
    "audio": (".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"),
    "document": (".pdf", ".txt", ".md"),
}


def guess_media_type(name: str) -> Optional[str]:
    """Routing convenience from the file extension; the platform validates the real format."""
    suffix = Path(urlparse(name).path).suffix.lower()
    for media_type, suffixes in EXTENSIONS.items():
        if suffix in suffixes:
            return media_type
    return None


def _asset_dict(asset: Any) -> dict:
    created = field(asset, "created_at")
    plain = to_plain(created) if created is not None else None
    return {
        "id": field(asset, "id") or field(asset, "_id"),
        "filename": field(asset, "filename"),
        "status": field(asset, "status"),
        "file_type": field(asset, "file_type"),
        "method": field(asset, "method"),
        "size": field(asset, "size"),
        "duration": field(asset, "duration"),
        "created_at": plain,
        "error": field(asset, "error"),
    }


def list_assets(
    *,
    asset_types: Optional[Sequence[str]] = None,
    filename: Optional[str] = None,
    asset_ids: Optional[Sequence[str]] = None,
    limit: int = 200,
    client: Any = None,
) -> List[dict]:
    """Return up to `limit` assets from the library, newest first."""
    if limit <= 0:
        raise ValueError("limit must be positive")
    if asset_types:
        unknown = [t for t in asset_types if t not in MEDIA_TYPES]
        if unknown:
            raise ValueError("asset_types must be among %s" % ", ".join(MEDIA_TYPES))
    active = client or build_client()
    kwargs: dict = {"page_limit": min(PAGE_LIMIT, limit), "request_options": READ_REQUEST_OPTIONS}
    if asset_types:
        kwargs["asset_types"] = list(asset_types)
    if filename:
        kwargs["filename"] = filename
    if asset_ids:
        kwargs["asset_ids"] = list(asset_ids)
    out: List[dict] = []
    for asset in active.assets.list(**kwargs):  # the SDK pager fetches further pages on demand
        out.append(_asset_dict(asset))
        if len(out) >= limit:
            break
    out.sort(key=lambda a: a.get("created_at") or "", reverse=True)
    return out


def find_assets(query: str, *, asset_type: Optional[str] = None, limit: int = 50, client: Any = None) -> List[dict]:
    """Find assets by (partial, case-insensitive) filename; exact filename matches first."""
    if not query.strip():
        raise ValueError("query must be non-empty")
    found = list_assets(
        asset_types=[asset_type] if asset_type else None, filename=query, limit=limit, client=client
    )
    wanted = query.strip().lower()
    return sorted(found, key=lambda a: 0 if (a.get("filename") or "").lower() == wanted else 1)


def upload_asset(
    *,
    media_type: str,
    url: Optional[str] = None,
    file_path: Optional[Path] = None,
    user_metadata: Optional[dict] = None,
    enable_hls: Optional[bool] = None,
    enable_thumbnail: Optional[bool] = None,
    client: Any = None,
) -> dict:
    """Upload one image, video, audio file or document. Returns the created asset (processing)."""
    if media_type not in MEDIA_TYPES:
        raise ValueError("media_type must be one of %s" % ", ".join(MEDIA_TYPES))
    if (url is None) == (file_path is None):
        raise ValueError("provide exactly one of url or file_path")
    active = client or build_client()
    extra: dict = {}
    if user_metadata is not None:
        extra["user_metadata"] = json.dumps(user_metadata, sort_keys=True)
    if enable_hls is not None:
        extra["enable_hls"] = enable_hls
    if enable_thumbnail is not None:
        extra["enable_thumbnail"] = enable_thumbnail

    if url is not None:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise ValueError("url must be a direct HTTP(S) media URL")
        asset = active.assets.create(method="url", url=url, request_options=CREATE_REQUEST_OPTIONS, **extra)
    else:
        path = Path(file_path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(str(path))
        size = path.stat().st_size
        if size > DIRECT_LIMIT[media_type]:
            if media_type in MULTIPART_TYPES:
                return upload_asset_multipart(path, media_type=media_type, client=active)
            raise ValueError(
                "local %s is %d MB; the limit is %d MB" % (media_type, size // MB, DIRECT_LIMIT[media_type] // MB)
            )
        with path.open("rb") as handle:
            asset = active.assets.create(
                method="direct", file=handle, filename=path.name,
                request_options=CREATE_REQUEST_OPTIONS, **extra
            )
    result = _asset_dict(asset)
    if not result["id"]:
        raise TwelveLabsError("asset creation returned no id")
    return result


def upload_asset_multipart(file_path: Path, *, media_type: str = "video", client: Any = None) -> dict:
    """Upload a large local video or audio file in chunks (up to 10 GB) with the SDK helper."""
    if media_type not in MULTIPART_TYPES:
        raise ValueError("multipart upload supports video and audio")
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(str(path))
    size = path.stat().st_size
    if size > MULTIPART_LIMIT:
        raise ValueError("local %s is %d GB; the multipart limit is 10 GB" % (media_type, size // GB))
    active = client or build_client()
    session = active.multipart_upload.upload_file(file_path=str(path), filename=path.name, file_type=media_type)
    asset_id = field(session, "asset_id")
    upload_id = field(session, "upload_id")
    if not asset_id and upload_id:
        done = active.multipart_upload.wait_for_upload_completion(upload_id)
        asset_id = field(done, "asset_id")
    if not asset_id:
        raise TwelveLabsError("multipart upload returned no asset id")
    return {"id": asset_id, "filename": path.name, "status": "processing", "file_type": None,
            "method": "multipart", "size": size, "duration": None, "created_at": None, "error": None}


def wait_for_asset(
    asset_id: str,
    *,
    client: Any = None,
    timeout_s: float = 1800,
    poll_interval_s: float = 5,
    sleep: Callable[[float], None] = time.sleep,
    monotonic: Callable[[], float] = time.monotonic,
) -> dict:
    active = client or build_client()
    result = wait_until_ready(
        lambda: active.assets.retrieve(asset_id, request_options=READ_REQUEST_OPTIONS),
        resource_name="asset processing",
        timeout_s=timeout_s,
        poll_interval_s=poll_interval_s,
        sleep=sleep,
        monotonic=monotonic,
    )
    return _asset_dict(result)
