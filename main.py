#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands - make.fun bounty u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes a single one-line joke about cats (86 characters, within the 1-200
gate) to /output/entry.txt, where the sealed scorer and the pairwise judge
read it.

Deterministic: the same bytes on every run. No network, no randomness,
no clock, no input data - the joke is a constant.
"""

import os

# One line about a cat: a setup everyone with a cat recognises (the cat
# pushes something off the table), then the turn that lands - the cat holds
# eye contact the whole time, like it was personal. No pun, no wind-up,
# no explanation after the punchline.
LINE = "My cat pushed my coffee off the table while holding eye contact, like it was personal."


def main() -> int:
    # Fail loudly rather than hand the grader an invalid entry if the
    # line ever grew past the sealed scorer's 1-200 character gate.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("cat joke outside the 1-200 character gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
