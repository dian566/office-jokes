#!/usr/bin/env python3
"""Second office joke for make.fun: the second monitor."""

# Bowo's pick: the ticket queue eats its own tail.

import os

JOKE = "I asked IT for a second monitor. They gave me a second ticket and closed the first one as duplicate."


def tell_joke() -> None:
    """Write Bowo's IT joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip():
        raise ValueError("joke must be a non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":  # run it
    tell_joke()
