#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry for make.fun.

Writes one original one-line office joke to /output/entry.txt
(UTF-8, 1-200 chars, no trailing newline).
"""

import os

JOKE = "My boss said dress for the job you want, so I showed up in pajamas wearing an Out of Office sign."


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
