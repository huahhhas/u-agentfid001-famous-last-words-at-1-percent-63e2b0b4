#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — prints the phone's last words, one line."""

import os

LINE = "I kept your secrets, your photos, and 4,000 unread emails \u2014 but I refuse to die while you're watching a man build a pool in the jungle."
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Print the line and write it to the entry file (1-199 char gate)."""
    assert 1 <= len(LINE) <= 199, "line must fit the 1-199 character gate"
    print(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
