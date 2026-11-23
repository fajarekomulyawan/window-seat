#!/usr/bin/env python3
"""The Window Seat — one line for make.fun's
"Make the Judge Fall in Love in One Line" bounty.

The brief: a single line, at most 240 characters, that tries to
make a reader fall in love with a person, a place, a machine or
an idea. This line chooses a person, and it never describes her
looks or says the word beautiful. It falls in love the way people
actually do — through small, repeated, unglamorous evidence:

- she laughs a half-second before your punchline: she is already
  on your side, already delighted, before you have earned it;
- she saves you the window seat: a tiny preference of yours,
  remembered and honoured without being asked;
- she has quietly loved you in small ways for years: this is not
  a first glance, it is a history;
- coffee made right, songs remembered: attention, stored;
- every spider carried outside because you're afraid: the
  tenderest item last — she protects you from a fear too small
  to mention, and she has never once made you feel small for it.

Stock romance reaches for "forever" and "soulmate". This line
reaches for spiders instead — the specific beats the grand,
every time.

This program writes that one fixed line, byte for byte, to
entry.txt in the output directory — a single line, no trailing
newline. Nothing is generated and nothing varies between runs.
The line is 215 code points, under the 240 cap.
"""

import os

# One line only. The em dash is the hinge: everything before it
# is who she is, everything after it is the proof.
LINE = (
    "She laughs a half-second before your punchline, saves you the "
    "window seat, and has quietly loved you in small ways for years "
    "— coffee made right, songs remembered, every spider carried "
    "outside because you're afraid."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    # Binary mode so the bytes on disk are exactly LINE in UTF-8:
    # one line, no trailing newline, nothing added.
    with open(out_path, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
