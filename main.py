"""The Absurd Clause Contest -- entry program (account @berkahmuse).

Writes one original English sentence (<=200 characters), phrased as a
clause buried deep inside a terms-of-service agreement: deadpan legal
boilerplate that quietly turns absurd, to /output/entry.txt.

Design: the clause opens exactly like a real arbitration clause ("In the
event of a dispute, both parties agree to settle the matter...") and only
then veers -- staring contest, best of three, at dawn in the Company's
car park. The joke lands on one reading, needs no setup, and the absurd
image is concrete. The program is fully deterministic: no randomness, no
network, no environment reads, no input files; it always writes the same
147 bytes.
"""

import os

CLAUSE = (
    "In the event of a dispute, both parties agree to settle the matter "
    "by staring contest, best of three, to be held at dawn in the "
    "Company's car park."
)


def main() -> None:
    assert 1 <= len(CLAUSE) <= 200, "clause must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
