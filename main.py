#!/usr/bin/env python3
"""Cat Reviews Its Human: a one-star review, written by the cat.

Writes one single line to /output/entry.txt. Pure standard library,
deterministic, no network.
"""

import os

LINE = (
    "One star. He feeds me seven minutes late, shuts every door I just "
    "opened with my face, and calls the laptop on my lap 'his spot.' "
    "I live here. He is staff."
)


def main() -> None:
    assert 0 < len(LINE) <= 200, "entry line must be 1-200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
