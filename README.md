# MIU Theorem Prover

## Background

This program is based on a puzzle in the book [Gödel, Escher, Bach: An Eternal Golden Braid](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach).

In the puzzle you are given a string and a set of rules for transforming the string. You have to provide the steps (a proof) to transform the input to some specified output string using only the rules given.

## Puzzle

Input: `MI`

Rules:
- `xI => xIU`
- `Mx => Mxx`
- `xIIIy => xUy`
- `xUUy => xy`

Output: `MU`

## Running the Theorem Prover

**Note:** [Python 3.7](https://www.python.org/downloads/) is required.

Run the `miu.py` script to test the theorem prover.

```bash
python miu.py
```

## Conclusion

There is [provably](https://en.wikipedia.org/wiki/MU_puzzle) no `MI -> MU` proof. Without constraints the prover would never halt.

## Settings

Run the theorem prover with other conjectures.

```bash
python miu.py --conjecture MIU
```

User-defined constraints terminate the theorem prover early.

```bash
python miu.py --proof-length 8 --theorem-length 10
```

```bash
python miu.py --timeout 3
```

Log every attempted proof to a file using the debug flag.

```bash
python miu.py --debug
```

## Goals of the Project

Although this is a silly little project, it's over-engineered in order to bring together much of what I've learned about Python and software engineering over the past 7 months.

Heres a list of some of the topics I covered:

- Debug logging
- Multiprocessing
- Python [data classes](https://docs.python.org/3/library/dataclasses.html)
- Type hints and [Pyre](https://pyre-check.org/) type check
- Software [design patterns](https://sourcemaking.com/design_patterns)
- Python [regular expressions](https://regex101.com/#python)
- [Argument parsing](https://docs.python.org/3/library/argparse.html)
- Printing with color
- Unit testing with [data driven tests](https://ddt.readthedocs.io/en/latest/example.html)
- Programming with args and kwargs
- Document and code styles