#!/usr/bin/env python3
"""news-image-20261118 entry: copy the front-page image to /output/entry.png.

The image (entry.png, 1024x1024, under 1 MiB) is a dense newspaper front
page summing up the world news of Wednesday 18 November 2026: 42 stories
across 7 regions, 13 illustrated, with a filled-continent world map and a
briefs list. It was built from frontpage.html (rendered with headless
Chrome; see render.py) and is shipped in this repository.

The front page follows the winning formula of the sibling boards: 3 big
illustrated leads (Xi greets Trump on the trilateral eve, Iran drones at
Kuwait, the EU EUR 45bn loan for Ukraine), 10 more illustrated cards with
data graphics (Voyager 1 at one light-day, COP31 split, Bangladesh
factories shut, the 141/126 drone tally, the Hoekstra petition, UK and
euro-area inflation, the 251-11 Jeffries vote, Cyclone Akvan, Gaza hunger,
Wall Street steadying), a region tally bar, a day-in-numbers strip,
per-lead source tags, and a date-check footer naming the 17 November
stories deliberately left out.

The program is deterministic: it copies the same bytes on every run,
uses only the standard library, and needs no network.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    if not IMAGE.is_file():
        print(f"missing image: {IMAGE}", file=sys.stderr)
        return 1
    shutil.copyfile(IMAGE, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
