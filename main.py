"""One-sentence absurd invention pitch.

Writes a single sentence pitching a ridiculous invention that fixes
a tiny everyday annoyance to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network, reads nothing outside the repo.
"""

import os

ENTRY = (
    "The Sock Lighthouse sews a miniature lighthouse into every sock, "
    "so the one that vanishes in the wash can flash SOS and guide its "
    "lonely partner home before the spin cycle eats it."
)


def main():
    # The gate allows 1-220 characters; fail loudly instead of
    # writing an entry the grader would reject.
    if not (1 <= len(ENTRY) <= 220):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-220")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
