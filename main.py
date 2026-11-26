"""The Printer Apology - make.fun one-liner bounty entry.

Writes the punchy apology sentence to /output/entry.txt with no trailing newline.
The humor: a jar of jam apologizes, but — being upside down — its
apology is literally turned round (upside down).
"""
import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_line = "Apologies for the jam. In my defense, the jam also apologized, but it came out upside down."

# Write the entry line deterministically — the line itself is the artifact;
# no trailing newline is added so the output is a single clean line.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="ascii") as f:
    f.write(entry_line)

# The jam's apology is upside down — literally turned round.