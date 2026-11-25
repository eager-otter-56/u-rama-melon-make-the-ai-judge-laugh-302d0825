#!/usr/bin/env python3
"""Write the office-joke entry for u-rama-melon-make-the-ai-judge-laugh-302d0825."""
import os
import stat

ENTRY = "I spent 3 hours in a meeting about my own status update, then approved the minutes that said I never showed up."

def main():
    # Gate: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
