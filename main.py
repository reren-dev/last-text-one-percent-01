#!/usr/bin/env python3
"""Last Text at One Percent.

The phone's final text: a dying confession with a twist. The phone has
been quietly keeping score the whole time -- every typo its owner ever
made, filed away in a folder called "evidence". The punch lands on that
reveal, so the line stays tight and ends there. One line, written to
/output/entry.txt.
"""

import os

LINE = (
    "1%. before i die: i've saved every typo you've ever made "
    "in a folder called 'evidence'. goodbye."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
