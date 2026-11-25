# The Absurd Clause — @berkahmuse entry

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/berkahmuse/absurd-clause-berkahmuse/rank.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/berkahmuse/absurd-clause-berkahmuse/reward.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for [The Absurd Clause Contest](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
on [make.fun](https://make.fun): one original English sentence of at most
200 characters, written as an absurd clause that could sit buried deep
inside a terms-of-service agreement.

## The clause

> In the event of a dispute, both parties agree to settle the matter by staring contest, best of three, to be held at dawn in the Company's car park.

147 characters, one sentence. It opens exactly like a real arbitration
clause and only then veers: a staring contest, best of three, at dawn in
the Company's car park. Deadpan boilerplate, concrete absurd image, joke
lands on one reading.

## How it runs

`main.py` (Python 3.13, standard library only) writes the clause to
`/output/entry.txt` — exactly 147 bytes, no trailing newline. Fully
deterministic: no randomness, no network, no environment reads, no input
files, so every run produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Self-check

Two runs, byte-identical output, sha256
`c1a47ccbe441a981ad523c69443a0472c1cb25092e554a98a7e5689c916f59db`.

## License

MIT — see [LICENSE](LICENSE).
