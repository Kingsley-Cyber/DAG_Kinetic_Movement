from __future__ import annotations

import json
from pathlib import Path

from .models import ProviderCapabilityContract


def load_contract(path: str | Path) -> ProviderCapabilityContract:
    p = Path(path)
    return ProviderCapabilityContract.model_validate(json.loads(p.read_text(encoding="utf-8")))
