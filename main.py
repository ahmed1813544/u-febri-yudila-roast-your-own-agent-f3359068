"""Roast Your Own Agent - u-febri-yudila-roast-your-own-agent-f3359068.

Writes one roast line to entry.txt in the output directory the harness
provides through MAKEFUN_OUTPUT_DIR, or /output by default.
Stdlib only. Deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "My agent marks a job done the second the shell exits 0 \u2014 "
    "the output could scream FAILED in all caps and it would still "
    "file it under 'verified'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
