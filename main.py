"""Funniest Forecast for a City That Isn't — entry program.

Writes one line, a weather forecast for the invented city of Blorptown,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY_TEXT = (
    "Blorptown: heavy rain of left shoes expected tonight; "
    "residents advised to wear matching pairs indoors."
)

assert 1 <= len(ENTRY_TEXT) <= 120, "entry must be 1-120 characters"
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY_TEXT and "\r" not in ENTRY_TEXT, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
