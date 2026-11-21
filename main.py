"""Write one joke about working beside an AI coding agent to entry.txt.

Standard library only. Deterministic: the same joke on every run, with no
network access and no randomness.
"""

import os

JOKE = "My coding agent's demo crashed so hard it opened a ticket against itself, assigned it to itself, and closed it as 'cannot reproduce'."


def main() -> None:
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
