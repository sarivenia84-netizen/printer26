"""The Printer Apology - make.fun one-liner bounty entry.

Writes the joke punchline to /output/entry.txt with no trailing newline.
The humor: a jam apologizing, but doing so upside down.
"""
import os


# Output directory: honour MAKEFUN_OUTPUT_DIR if set, otherwise default
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_line = "Apologies for the jam. In my defense, the jam also apologized, but it came out upside down."

# Write the entry line — deterministically, no trailing newline
# The line itself is the artifact; no trailing newline is added
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="ascii") as f:
    f.write(entry_line)  # the line itself is the artifact, no newline
# The jam's apology is upside down — literally turned round