"""Command line access to the TwelveLabs client. Prints JSON. Never prints credentials."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from .analyze import analyze_video
from .assets import MEDIA_TYPES, find_assets, guess_media_type, list_assets, upload_asset, wait_for_asset
from .common import EMBED_DIMENSIONS, EMBED_MODELS, TwelveLabsError, doctor
from .embed import create_embedding


def _metadata(pairs: List[str]) -> Optional[dict]:
    if not pairs:
        return None
    out = {}
    for pair in pairs:
        if "=" not in pair:
            raise ValueError("--metadata expects KEY=VALUE, got %r" % pair)
        key, value = pair.split("=", 1)
        out[key.strip()] = value
    return out


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tl", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor", help="readiness: SDK, key source, models")

    assets = sub.add_parser("assets", help="look in your asset library")
    asub = assets.add_subparsers(dest="assets_command", required=True)
    lst = asub.add_parser("list", help="list assets, newest first")
    lst.add_argument("--type", choices=MEDIA_TYPES, action="append", default=[])
    lst.add_argument("--name", help="filename filter (partial, case-insensitive)")
    lst.add_argument("--limit", type=int, default=50)
    fnd = asub.add_parser("find", help="find assets by filename")
    fnd.add_argument("query")
    fnd.add_argument("--type", choices=MEDIA_TYPES)

    up = sub.add_parser("upload", help="upload an image, video, audio file or document")
    up.add_argument("media_type", choices=MEDIA_TYPES + ("auto",))
    src = up.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", type=Path)
    src.add_argument("--url")
    up.add_argument("--metadata", action="append", default=[], metavar="KEY=VALUE")
    up.add_argument("--wait", action="store_true", help="poll until the asset is ready")

    emb = sub.add_parser("embed", help="create a Marengo embedding")
    emb.add_argument("input_type", choices=("text", "video", "audio", "image", "document", "multi_input"))
    emb.add_argument("--text")
    emb.add_argument("--asset-id")
    emb.add_argument("--url")
    emb.add_argument("--image-asset-id", action="append", default=[])
    emb.add_argument("--model", choices=EMBED_MODELS)
    emb.add_argument("--dim", type=int, choices=EMBED_DIMENSIONS)

    ana = sub.add_parser("analyze", help="analyze a video with Pegasus")
    vid = ana.add_mutually_exclusive_group(required=True)
    vid.add_argument("--asset-id")
    vid.add_argument("--url")
    ana.add_argument("--prompt", required=True)
    ana.add_argument("--schema", type=Path, help="JSON schema file for structured output")
    ana.add_argument("--start", type=float)
    ana.add_argument("--end", type=float)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "doctor":
            result = doctor()
        elif args.command == "assets" and args.assets_command == "list":
            result = list_assets(asset_types=args.type or None, filename=args.name, limit=args.limit)
        elif args.command == "assets":
            result = find_assets(args.query, asset_type=args.type)
        elif args.command == "upload":
            media_type = args.media_type
            if media_type == "auto":
                media_type = guess_media_type(str(args.file or args.url))
                if media_type is None:
                    raise ValueError("cannot tell the media type from the name; pass video, image, audio or document")
            result = upload_asset(media_type=media_type, url=args.url, file_path=args.file,
                                  user_metadata=_metadata(args.metadata))
            if args.wait:
                result = wait_for_asset(result["id"])
        elif args.command == "embed":
            result = create_embedding(
                args.input_type, text=args.text, asset_id=args.asset_id, url=args.url,
                image_asset_ids=args.image_asset_id or None, model=args.model, embedding_dimension=args.dim,
            )
        else:
            schema = json.loads(args.schema.read_text(encoding="utf-8")) if args.schema else None
            result = analyze_video(args.prompt, asset_id=args.asset_id, video_url=args.url,
                                   output_schema=schema, start_s=args.start, end_s=args.end)
    except (TwelveLabsError, ValueError, FileNotFoundError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
