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

Run the `miu.py` script to run the prover.

```bash
python miu.py
```

To see every attempted proof uncomment the logging line in `miu.py` and see `MIU.log`.

## Conclusion

There [exists a proof](https://en.wikipedia.org/wiki/MU_puzzle) for the non-existence of a `MI -> MU` proof, so this prover fails no matter how lenient the constraints.
