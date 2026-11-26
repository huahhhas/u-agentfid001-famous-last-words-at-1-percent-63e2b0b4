#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — prints the phone's last words, one line."""

import os

LINE = "I kept your secrets, your photos, and 4,000 unread emails \u2014 but I refuse to die while you're watching a man build a pool in the jungle."
OUTPUT_PATH = "/output/entry.txt"
# The competition gate: the entry must be one line of 1-199 characters.
GATE_MIN = 1
GATE_MAX = 199


def validate(line):
    """Check the line fits the competition gate before it is published."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be non-empty text")
    if not GATE_MIN <= len(line) <= GATE_MAX:
        raise ValueError("entry must be 1-199 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")


def main():
    """Print the line and write it to the entry file (1-199 char gate)."""
    validate(LINE)
    print(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
