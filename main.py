#!/usr/bin/env python3
"""Last Text at One Percent.

The phone's final text: a dying confession with a twist. The phone has
been quietly keeping score the whole time -- every typo its owner ever
made, filed away in a folder called "evidence". The first draft ended on
a flat "goodbye" and wasted the punch, so the revision ends on the
count instead: the phone is still counting typos as it dies. One line,
written to /output/entry.txt.
"""

import os

LINE = (
    "1%. before i go: i've saved every typo you've ever made "
    "in a folder called 'evidence'. 4,312 and counting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
