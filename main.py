"""The Printer Apology — make.fun bounty entry.

Deterministic Python stdlib only: writes the exact one-liner to
/output/entry.txt (mkdir /output first, respects MAKEFUN_OUTPUT_DIR).
"""

import os

# The final one-liner (max 120 chars):
#   Apologies for the jam. In my defense, the jam also apologized, but it came out upside down.
LINE = "Apologies for the jam. In my defense, the jam also apologized, but it came out upside down."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline


if __name__ == "__main__":
    main()