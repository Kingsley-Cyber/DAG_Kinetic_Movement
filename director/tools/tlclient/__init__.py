"""TwelveLabs client for the director tools: asset library, uploads, analysis, embeddings.

Transport only. No knowledge authority, no video harvest pipeline (that stays parked; see
plan/DECISIONS.md). Run through the launcher: `python director/tools/tl.py doctor`.
"""

from .analyze import analyze_video
from .assets import (
    find_assets,
    guess_media_type,
    list_assets,
    upload_asset,
    upload_asset_multipart,
    wait_for_asset,
)
from .common import MODELS, TwelveLabsError, build_client, doctor, resolve_embed_model
from .embed import build_embed_request, create_embedding

__all__ = [
    "MODELS", "TwelveLabsError", "analyze_video", "build_client", "build_embed_request",
    "create_embedding", "doctor", "find_assets", "guess_media_type", "list_assets",
    "resolve_embed_model", "upload_asset", "upload_asset_multipart", "wait_for_asset",
]
