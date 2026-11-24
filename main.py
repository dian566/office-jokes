#!/usr/bin/env python3
"""An office joke about an out-of-office reply, for make.fun."""

from pathlib import Path

# The joke is stored in two parts so each half sits on its own line;
# joining them with an em dash reproduces the drafted sentence exactly.
PARTS = (
    "My out-of-office reply said 'gone fishing for a better job'",
    "HR called it 'too honest'.",
)
SEPARATOR = " — "
OUT_FILE = Path("/output/entry.txt")


def join_parts(parts, separator):
    """Join the joke's parts with the separator between them."""
    return separator.join(parts)


def run():
    joke = join_parts(PARTS, SEPARATOR)
    if not joke:
        raise SystemExit("joke came out empty")
    if len(joke) > 200:
        raise SystemExit(f"joke is {len(joke)} chars, over the 200 limit")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(joke, encoding="utf-8")


run()
