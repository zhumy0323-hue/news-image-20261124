#!/usr/bin/env python3
"""Write the 24 Nov 2026 frontpage image for the make.fun bounty.

The entry image ships as base64 text in entry.png.b64 next to this file.
Running this script decodes it and writes the PNG to /output/entry.png,
so the picture can be viewed without any image tooling of its own.
"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png.b64"
DST = Path("/output/entry.png")


def main() -> None:
    encoded = SRC.read_text(encoding="ascii").strip()
    # Any stray newlines are removed first so the decode is strict.
    png_bytes = base64.b64decode(encoded, validate=True)
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(png_bytes)
    print(f"wrote {DST} ({len(png_bytes)} bytes)")


if __name__ == "__main__":
    main()
