"""Entrypoint: copy the pre-rendered poster to the output directory.

Stdlib only (hashlib/os/shutil/sys). The poster is rendered at build time
by render.py and committed as entry.png; nothing is drawn at grade time,
because the grader's pinned Python 3.13 image rejected Pillow-drawing
entrypoints with exit 1 in the 21/22 Nov rounds.
"""
import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.exists(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print("copied entry.png -> %s sha256=%s" % (dst, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
