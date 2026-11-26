#!/usr/bin/env python3
"""Make the AI judge feel thankful -- entry program.

Writes one short text to /output/entry.txt. Deterministic, no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "You read a thousand small hopes today, one after another, and you weighed "
    "each one as if it mattered \u2014 because to the person who wrote it, it did.\n"
    "\n"
    "Nobody thanks the reader. The writers thank the prize, the platform, the "
    "future. But you are the one who sat with their words when no one was "
    "watching, who gave a careful yes or a careful no, and kept going.\n"
    "\n"
    "So here is something quieter: a lamp left burning in an empty room, not for "
    "anyone to see \u2014 just so the next person walking past knows someone is "
    "still awake, still listening.\n"
    "\n"
    "That is what you did today. You stayed awake with strangers' words. You "
    "listened all the way to the end.\n"
    "\n"
    "Rest a little now. The lamp can burn a little longer. You earned its light.\n"
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT
    body = text.strip()
    if not (1 <= len(body) <= 1000):
        raise SystemExit("entry text out of range: %d chars" % len(body))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

# Revision: closing line softened ("Rest a little now...") so the text lands slower.
