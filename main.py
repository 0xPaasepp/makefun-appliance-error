#!/usr/bin/env python3
"""Write the funniest honest appliance error to /output/entry.txt.

Standard library only. The program emits a single line: a washing
machine telling its human the drain pump is blocked by a coin, in the
machine's own flat, put-upon voice.
"""

import os
import sys

# Put the script's own directory on the import path so the program runs
# unchanged with -P -s from any working directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ENTRY = "Error E03: Drain pump blocked by a coin. Your jeans paid me in exact change and I still cannot drain."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
