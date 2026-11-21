#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Writes exactly one line of UTF-8 text to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

JOKE = "I asked my agent why the demo crashed; it confidently blamed a library that doesn't exist."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    joke = JOKE
    # Gate guard: single line, 1-280 Unicode code points, not only whitespace.
    assert "\n" not in joke and "\r" not in joke, "joke must be a single line"
    assert 1 <= len(joke) <= 280, "joke must be 1-280 characters"
    assert joke.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
