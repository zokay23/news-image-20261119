#!/usr/bin/env python3
"""news-image-20261119 entry: write the poster to /output/entry.png.

The finished poster lives in this repo as entry.png (drawn with PIL by
build_poster.py). This program copies it byte-for-byte, so it is fully
deterministic: every run writes the exact same bytes, with no network
and no generation at runtime.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
