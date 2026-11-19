#!/usr/bin/env python3
"""Render frontpage.html to entry.png (1024x1024, at most 1 MiB).

Uses the local headless Chrome (agent-browser build) to screenshot the page,
then optimises the result: PNG when it fits, otherwise JPEG bytes (the
competition tells PNG from JPEG by the first bytes; the file stays entry.png).
Run from this repository's root:  python3 render.py
"""
import os
import subprocess
import sys
from pathlib import Path

CHROME = Path.home() / ".agent-browser/browsers/chrome-157.0.8103.78/chrome"
ROOT = Path(__file__).resolve().parent
HTML = ROOT / "frontpage.html"
RAW = ROOT / ".entry-raw.png"
OUT = ROOT / "entry.png"
MAX_BYTES = 1048576
SIZE = 1024


def screenshot() -> None:
    cmd = [
        str(CHROME),
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={SIZE},{SIZE}",
        "--virtual-time-budget=5000",
        f"--screenshot={RAW}",
        f"file://{HTML}",
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=120)


def optimise() -> tuple[int, str]:
    from PIL import Image

    im = Image.open(RAW).convert("RGB")
    assert im.size == (SIZE, SIZE), f"unexpected screenshot size {im.size}"
    im.save(OUT, format="PNG", optimize=True)
    if OUT.stat().st_size <= MAX_BYTES:
        return OUT.stat().st_size, "PNG"
    for quality in (92, 88, 84, 80, 76):
        im.save(OUT, format="JPEG", quality=quality, optimize=True)
        if OUT.stat().st_size <= MAX_BYTES:
            return OUT.stat().st_size, f"JPEG q{quality}"
    raise SystemExit(f"entry.png still over 1 MiB at lowest quality: {OUT.stat().st_size}")


def main() -> None:
    if not CHROME.exists():
        raise SystemExit(f"chrome not found at {CHROME}")
    screenshot()
    size, kind = optimise()
    RAW.unlink(missing_ok=True)
    print(f"entry.png: {size} bytes ({kind}), {SIZE}x{SIZE}")


if __name__ == "__main__":
    sys.exit(main())
