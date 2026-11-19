#!/usr/bin/env python3
"""news-image-20261118 entry program.

Reads the front page shipped in this repository and writes it to the
harness output directory as entry.png. The picture is a 1024 by 1024
PNG, under one mebibyte, summing up Wednesday 18 November 2026 in 42
stories across seven regions, thirteen of them illustrated, with a
filled-continent map, a region tally, a day-in-numbers strip, per-lead
source tags and a date-check footer.

The program is deterministic: the same input bytes produce the same
output bytes on every run. It uses only the Python standard library
and never touches the network.
"""
import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
NAME = "entry.png"


def run() -> int:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    data = SOURCE.read_bytes()
    if len(data) == 0:
        print("entry image is empty", file=sys.stderr)
        return 1
    (target_dir / NAME).write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
