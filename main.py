#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — prints the phone's last words, one line."""

import os

LINE = "I kept your secrets, your photos, and 4,000 unread emails \u2014 but I refuse to die while you're watching a man build a pool in the jungle."

if __name__ == "__main__":
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
