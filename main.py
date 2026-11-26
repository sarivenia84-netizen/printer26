"""The Printer Apology - make.fun one-liner bounty entry.

Writes the apology sentence to /output/entry.txt without a trailing newline.
The humor: a jar of jam apologizes, but — being upside down — its
apology is literally turned round (upside down), making the words
appear back-to-front as if read in a mirror.
"""
import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_line = "Apologies for the jam. In my defense, the jam also apologized, but it came out upside down."

# Write the entry line to /output/entry.txt deterministically. The
# file is the deliverable; no trailing newline is added so the output
# is a single clean line suitable for character-count verification.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="ascii") as f:
    f.write(entry_line)

# The jam's apology is upside down — literally turned round, so the
# mirrored text reads back-to-front like words in a mirror. The
# humor is in the absurdity of a jar of jam offering an apology that
# is itself inverted.

