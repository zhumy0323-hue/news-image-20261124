"""Decode the front-page image for the 24 November 2026 news-image entry.

The repository ships the image as base64 text (entry.png.b64) so the
entrypoint can reproduce the exact 1024x1024 PNG without any binary
blob in the source tree. Running this script writes the decoded image
to /output/entry.png.
"""

import base64
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
DST = "/output/entry.png"


def main() -> None:
    with open(SRC, "r", encoding="ascii") as handle:
        encoded = handle.read().strip()
    raw = base64.b64decode(encoded, validate=True)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as handle:
        handle.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    # One line of confirmation: path, size, and hash, so a runner can
    # check the decoded image byte for byte against the entry.
    print(f"wrote {DST} ({len(raw)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
