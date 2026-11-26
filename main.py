"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs
-----------
Run ``python3 main.py`` from the repository root. The program creates
``/output`` if needed and writes the tip as a single line of UTF-8 text
with no trailing newline. It prints nothing to stdout.

Verification notes
------------------
Verified 2026-11-25: ``python3 main.py`` writes 109 characters to
``/output/entry.txt`` — one line, valid UTF-8, no trailing newline, inside
the competition's 1–200 character gate. Re-running after a docstring-only
edit produces byte-identical output (same sha256 of /output/entry.txt and
of stdout).
"""

import os

TEXT = "Tip: your agent read the entire codebase in four seconds and still has no idea what you meant by 'quick fix'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one line, 109 characters, one sentence; a loading-screen tip
# that speaks to the stressed developer and the AI agent at once — the agent
# did the impossible homework and still can't decode "quick fix".
