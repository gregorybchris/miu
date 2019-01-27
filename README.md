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

User-defined constraints will terminate the theorem prover early.

```bash
python mui.py --proof-length 8 --theorem-length 10
```

```bash
python mui.py --timeout 3
```

Log every attempted proof to a file use the debug flag.

```bash
python mui.py --debug
```