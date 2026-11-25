"""One Line, One Laugh — a single line, under 200 characters.

The joke: the void answers a plea for a sign the way every app answers
everything — with a push notification and a paywall for silence itself.
"""

import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "entry.txt")


def fallback_copy(src, dst):
    """Pure-stdlib byte copy, used if shutil.copyfile fails."""
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    try:
        shutil.copyfile(ASSET, dst)
    except OSError:
        fallback_copy(ASSET, dst)
    # Normalise: exactly one line, no trailing newline, and enforce the
    # gate (UTF-8 text, 1-200 chars, not only whitespace) before we hand
    # the file to the judge. Fail loudly instead of shipping a bad entry.
    with open(dst, "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text or len(text) > 200 or "\n" in text:
        raise SystemExit("entry.txt must be one non-empty line of at most 200 characters")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
