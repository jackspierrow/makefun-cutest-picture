"""make.fun entry: Make the cutest picture.

The program writes one picture to /output/entry.png.
It copies the bundled image byte-for-byte: no network, no
randomness, so two runs always produce identical bytes.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# Verify the copy: size and content must match the bundled image.
if os.path.getsize(DST) != os.path.getsize(SRC) or _sha256(DST) != _sha256(SRC):
    raise RuntimeError("output does not match bundled entry.png")
print(f"Wrote {DST} ({os.path.getsize(DST)} bytes, sha256 {_sha256(DST)[:16]}... verified)")
