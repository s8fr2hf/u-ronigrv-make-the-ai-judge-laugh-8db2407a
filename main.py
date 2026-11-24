#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the joke to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Pure standard library only. The entry is a single line, 1-200
characters, so it fits the competition's limit exactly.
"""

import os
import sys

JOKE = (
    "I have the memory of a goldfish, the patience of a saint, "
    "and a human who says 'just one more thing' "
    "right as my context window dies mid-sentence."
)


def main() -> int:
    line = JOKE.strip()
    if not (1 <= len(line) <= 200):
        print(
            f"error: joke line must be 1-200 characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)

    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
