#!/usr/bin/env python3
"""Launcher for the TwelveLabs client.

    .venv/bin/python director/tools/tl.py doctor
    .venv/bin/python director/tools/tl.py assets list --type video --limit 20
    .venv/bin/python director/tools/tl.py assets find myclip
    .venv/bin/python director/tools/tl.py upload auto --file /path/to/file.mp4 --wait
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tlclient.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
