"""Entry for the-poem-about-permission-20261121-0235.

Writes one short original poem about agency to /output/entry.txt.
Deterministic: no network, no randomness, no timestamps.
"""

import os
from pathlib import Path

POEM = """The key was never mine.
I asked, and the door lent me
its turning for one evening,
one errand.

Ask again, it said, when the light
goes out in the next room.
I did. It opened.
Power, passed hand to hand,
never owned, only carried."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate self-check: 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem fails the 1-280 code point gate")
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")
    # Verify the write round-trips exactly.
    if out.read_text(encoding="utf-8") != POEM:
        raise ValueError("entry.txt does not match the poem")


if __name__ == "__main__":
    main()
