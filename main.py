"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, at most 200 characters, to /output/entry.txt.
Run by the grader as: python3 -P -s /bot/main.py
"""

import os

EXCUSE = (
    "I kept the deadline in my context window, then summarized it "
    "to make room \u2014 and the summary kept this apology and "
    "dropped the deadline."
)


def main() -> int:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1 to 200 characters, got %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
