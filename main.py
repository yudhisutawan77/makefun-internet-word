"""The Internet in One Word — entry program.

Writes a single word describing the whole internet to the output file
the grader reads (/output/entry.txt). Stdlib only, no network, fully
deterministic: every run produces byte-identical output.
"""

import os
import sys
from pathlib import Path

# Bootstrap: make sure the directory holding this file is importable,
# so the program works no matter which working directory it is run from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

# The entry: one word for the whole internet.
# Feral — wild, untamed, nobody in charge, and it bites.
# Funny on its own, true of the internet as a whole, and not the first
# obvious word anyone reaches for.
WORD = "Feral"


def resolve_output_path() -> Path:
    """Pick where the entry text goes.

    Priority, first set wins:
    1. ENTRY_OUT — a file path, or a directory (then entry.txt inside it).
    2. MAKEFUN_OUTPUT_DIR — a directory; entry.txt goes inside it.
    3. /output/entry.txt — the grader's default location.
    4. ./entry.txt in the current working directory — last resort.
    """
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if entry_out:
        candidate = Path(entry_out)
        if candidate.is_dir() or entry_out.endswith(os.sep):
            return candidate / "entry.txt"
        return candidate

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if output_dir:
        return Path(output_dir) / "entry.txt"

    default = Path("/output/entry.txt")
    if default.parent.is_dir():
        return default

    return Path.cwd() / "entry.txt"


def write_entry(path: Path) -> None:
    """Write the word to *path*, creating parent directories as needed.

    The file holds the word and nothing else — no trailing newline, no
    extra whitespace — so the sealed gate sees exactly one word.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(WORD, encoding="utf-8")


def main() -> int:
    """Resolve the output location and write the entry word there."""
    write_entry(resolve_output_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
