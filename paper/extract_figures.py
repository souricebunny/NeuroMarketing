#!/usr/bin/env python3
"""Extract the embedded brain-response figures from the project notebooks.

The TRIBE v2 runs in this repository were executed on Google Colab and the
predicted activity arrays (shape T x 20484) were never written to disk. The
only surviving artefacts of each run are the rendered cortical-surface figures
embedded as base64 PNGs in the notebook ``outputs``. This script recovers those
PNGs so they can be used as manuscript figures, and records their provenance.

Usage:
    python paper/extract_figures.py

It writes into ``paper/figures/`` and is safe to re-run (idempotent overwrite).
"""

from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

# Repo root = parent of this file's directory (paper/ -> repo root).
REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = Path(__file__).resolve().parent / "figures"

# (notebook, cell_index, output_filename, human description)
# Cell indices verified against the committed notebooks.
FIGURES = [
    ("tribe_demo.ipynb", 11, "fig_sintel_reference.png",
     "Reference reproduction: Sintel trailer (video+audio), first 15 TRs."),
    ("LaysAD.ipynb", 7, "fig_lays.png",
     "Lay's 'More smiles per mile' ad (25.09 s), first 15 TRs."),
    ("colgatead.ipynb", 5, "fig_colgate.png",
     "Colgate Visible White (Hindi) ad (20.13 s), first 15 TRs."),
    ("surfexcelad.ipynb", 7, "fig_surfexcel.png",
     "Surf Excel Rs.10 'Primary Colours' ad (33.01 s), first 15 TRs."),
]


def extract_png_from_cell(nb_path: Path, cell_index: int) -> bytes:
    """Return the decoded bytes of the first image/png output in a code cell."""
    with nb_path.open(encoding="utf-8") as fh:
        nb = json.load(fh)
    cells = nb["cells"]
    if cell_index >= len(cells):
        raise IndexError(f"{nb_path.name}: cell {cell_index} out of range "
                         f"({len(cells)} cells)")
    cell = cells[cell_index]
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        if "image/png" in data:
            payload = data["image/png"]
            if isinstance(payload, list):
                payload = "".join(payload)
            return base64.b64decode(payload)
    raise ValueError(f"{nb_path.name}: no image/png output in cell {cell_index}")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ok = True
    for nb_name, cell_index, out_name, desc in FIGURES:
        nb_path = REPO_ROOT / nb_name
        try:
            png_bytes = extract_png_from_cell(nb_path, cell_index)
        except (OSError, IndexError, ValueError) as exc:
            print(f"[FAIL] {nb_name} -> {out_name}: {exc}", file=sys.stderr)
            ok = False
            continue
        out_path = OUT_DIR / out_name
        out_path.write_bytes(png_bytes)
        print(f"[OK]   {out_name:28s} {len(png_bytes):>8d} bytes  ({desc})")
    if not ok:
        print("One or more figures could not be extracted.", file=sys.stderr)
        return 1
    print(f"\nWrote figures to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
