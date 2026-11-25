#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun bounty entry.

Writes a single original roast line to /output/entry.txt.
Python 3.13 standard library only. Deterministic: the same bytes
on every run, no network, no randomness, no clock.
"""

import os
import shutil
from pathlib import Path

ROAST = (
    "My agent calls itself autonomous, then pings me every two minutes "
    "to tap 'approve' on the job I already approved."
)


def main() -> int:
    # The gate requires 1 to 200 characters of UTF-8 text; fail loudly
    # rather than emit an invalid entry.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} characters, gate needs 1-200")
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself.
    for child in out_dir.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
