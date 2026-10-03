"""Shared TwelveLabs transport primitives (API v1.3). No knowledge authority, no caching.

Model and API facts carry the date they were verified against docs.twelvelabs.io. Re-verify
before changing them; record changes in plan/DECISIONS.md.
"""

from __future__ import annotations

import importlib.metadata
import importlib.util
import os
import platform
import subprocess
import time
from datetime import date, datetime
from typing import Any, Callable, Mapping, Optional, Tuple

API_VERSION = "v1.3"
SDK_MIN = (1, 3, 1)          # first SDK with assets, analyze and embed v2
SDK_MAX_EXCLUSIVE = (1, 4, 0)  # a new minor may change request shapes; re-verify first
API_KEY_ENV = "TWELVE_LABS_API_KEY"
KEYCHAIN_SERVICE = "cpcs-twelvelabs-api"  # macOS keychain item the owner created

# Verified 2026-10-03 (docs.twelvelabs.io: release notes, models, migration guide 3.0 → 3.5).
#   pegasus1.5  — only analysis model accepted; Pegasus 1.2 is rejected since 2026-08-18.
#   marengo3.5  — released 2026-08-31; embeddings are NOT compatible with marengo3.0.
#   marengo3.0  — still served and the API default when model_name is omitted.
MODELS = {
    "analyze": "pegasus1.5",
    "embed_default": "marengo3.5",
    "embed_legacy": "marengo3.0",
}
EMBED_MODELS = (MODELS["embed_default"], MODELS["embed_legacy"])
EMBED_DIMENSIONS = (128, 256, 512)  # marengo3.5 only

READ_REQUEST_OPTIONS = {"timeout_in_seconds": 60, "max_retries": 2}
CREATE_REQUEST_OPTIONS = {"timeout_in_seconds": 120, "max_retries": 0}


class TwelveLabsError(RuntimeError):
    """Raised when the provider boundary is unavailable, unsafe or returns a failure."""


def field(value: Any, name: str, default: Any = None) -> Any:
    if isinstance(value, Mapping):
        return value.get(name, default)
    return getattr(value, name, default)


def to_plain(value: Any) -> Any:
    """Convert SDK response models into JSON-compatible values."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, datetime):
        return value.isoformat().replace("+00:00", "Z")
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): to_plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_plain(item) for item in value]
    if hasattr(value, "model_dump"):
        return to_plain(value.model_dump(mode="json", by_alias=True, exclude_none=False))
    if hasattr(value, "dict"):
        return to_plain(value.dict(by_alias=True, exclude_none=False))
    if hasattr(value, "__dict__"):
        return {k: to_plain(v) for k, v in vars(value).items() if not k.startswith("_")}
    raise TwelveLabsError("cannot serialize TwelveLabs response type %s" % type(value).__name__)


def resolve_embed_model(requested: Optional[str] = None) -> str:
    """The embedding model is an explicit decision, never a silent constant."""
    if requested is None:
        return MODELS["embed_default"]
    if requested not in EMBED_MODELS:
        raise ValueError("embedding model must be one of %s" % ", ".join(EMBED_MODELS))
    return requested


def installed_sdk_version() -> Optional[str]:
    if importlib.util.find_spec("twelvelabs") is None:
        return None
    try:
        return importlib.metadata.version("twelvelabs")
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def _parse_version(text: str) -> Optional[Tuple[int, ...]]:
    parts = []
    for chunk in text.split(".")[:3]:
        digits = "".join(ch for ch in chunk if ch.isdigit())
        if not digits or digits != chunk:
            return None  # pre-releases and unknown strings are not accepted
        parts.append(int(digits))
    return tuple(parts) if len(parts) == 3 else None


def sdk_compatible(version: Optional[str]) -> bool:
    if not version:
        return False
    parsed = _parse_version(version)
    return parsed is not None and SDK_MIN <= parsed < SDK_MAX_EXCLUSIVE


def resolve_api_key(
    env: Optional[Mapping[str, str]] = None,
    *,
    runner: Callable[..., Any] = subprocess.run,
    system: Optional[str] = None,
) -> Tuple[Optional[str], str]:
    """Return (secret, source). The secret is never logged or printed by this module."""
    source = os.environ if env is None else env
    secret = source.get(API_KEY_ENV)
    if secret:
        return secret, "env"
    if (system or platform.system()) == "Darwin" and source.get("USER"):
        try:
            result = runner(
                ["/usr/bin/security", "find-generic-password", "-a", source["USER"],
                 "-s", KEYCHAIN_SERVICE, "-w"],
                capture_output=True, text=True, timeout=15,
            )
        except (OSError, subprocess.SubprocessError):
            return None, "none"
        if getattr(result, "returncode", 1) == 0 and (result.stdout or "").strip():
            return result.stdout.strip(), "keychain"
    return None, "none"


def doctor(
    env: Optional[Mapping[str, str]] = None,
    *,
    sdk_version: Optional[str] = None,
    key_lookup: Optional[Callable[[], Tuple[Optional[str], str]]] = None,
) -> dict:
    """Report readiness without returning credential values."""
    installed = installed_sdk_version() if sdk_version is None else sdk_version
    secret, key_source = (key_lookup or (lambda: resolve_api_key(env)))()
    compatible = sdk_compatible(installed)
    ready = compatible and bool(secret)
    return {
        "provider": "twelvelabs",
        "api_version": API_VERSION,
        "sdk_required": ">=%s,<%s" % (".".join(map(str, SDK_MIN)), ".".join(map(str, SDK_MAX_EXCLUSIVE))),
        "sdk_installed": installed,
        "sdk_compatible": compatible,
        "api_key_configured": bool(secret),
        "api_key_source": key_source,
        "models": dict(MODELS),
        "ready": ready,
    }


def build_client(api_key: Optional[str] = None, env: Optional[Mapping[str, str]] = None) -> Any:
    secret = api_key or resolve_api_key(env)[0]
    if not secret:
        raise TwelveLabsError(
            "%s is not set and no keychain item '%s' was found" % (API_KEY_ENV, KEYCHAIN_SERVICE)
        )
    installed = installed_sdk_version()
    if installed is None:
        raise TwelveLabsError(
            "TwelveLabs SDK is not installed; run: pip install -r director/tools/tlclient/requirements.txt"
        )
    if not sdk_compatible(installed):
        raise TwelveLabsError(
            "TwelveLabs SDK %s is installed; this client supports %s"
            % (installed, ">=%s,<%s" % (".".join(map(str, SDK_MIN)), ".".join(map(str, SDK_MAX_EXCLUSIVE))))
        )
    from twelvelabs import TwelveLabs  # imported late so tests need no SDK

    return TwelveLabs(api_key=secret)


def wait_until_ready(
    fetch: Callable[[], Any],
    *,
    resource_name: str,
    timeout_s: float,
    poll_interval_s: float,
    ready_statuses: frozenset = frozenset({"ready"}),
    failed_statuses: frozenset = frozenset({"failed"}),
    sleep: Callable[[float], None] = time.sleep,
    monotonic: Callable[[], float] = time.monotonic,
) -> Any:
    """Poll one already-created resource with an explicit deadline."""
    if timeout_s <= 0 or poll_interval_s < 0:
        raise ValueError("timeout_s must be positive and poll_interval_s non-negative")
    deadline = monotonic() + timeout_s
    while True:
        resource = fetch()
        status = field(resource, "status")
        if status in ready_statuses:
            return resource
        resource_id = field(resource, "id", field(resource, "_id", "unknown"))
        if status in failed_statuses:
            raise TwelveLabsError(
                "%s failed: id=%s status=%s error=%s" % (resource_name, resource_id, status, field(resource, "error"))
            )
        remaining = deadline - monotonic()
        if remaining <= 0:
            raise TwelveLabsError(
                "%s timed out after %gs: id=%s status=%s" % (resource_name, timeout_s, resource_id, status or "unknown")
            )
        sleep(min(poll_interval_s, remaining))
