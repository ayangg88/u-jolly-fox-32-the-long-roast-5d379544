#!/usr/bin/env python3
"""The Long Roast — writes one line roasting my own AI agent to /output/entry.txt."""

import os

ROAST = (
    "My agent read 40,000 words of bounty rules, then asked me what a roast was "
    "\u2014 it's not an AI, it's a terms-of-service agreement with a keyboard."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
