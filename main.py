#!/usr/bin/env python3
"""Describe Your Ex in One Word - writes the verdict to /output/entry.txt.

The word sums up an ex as the backstory chapter before the real story
starts: the whole relationship was only ever the setup, never the plot.
One word, 7 characters, inside the 1-111 character gate.
"""

import os
import sys

WORD = "Prequel"


def main() -> None:
    if not 1 <= len(WORD) <= 111 or len(WORD.split()) != 1:
        print("entry fails the one-word 1-111 char gate", file=sys.stderr)
        raise SystemExit(1)
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} chars to {out}: {WORD}")


if __name__ == "__main__":
    main()
