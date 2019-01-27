"""Pretty printing for proofs."""

from dataclasses import dataclass
from typing import Callable, List, Optional, Tuple


@dataclass
class _COLOR:
    RED: str = '\x1b[31m'
    GREEN: str = '\x1b[32m'
    YELLOW: str = '\x1b[33m'
    BLUE: str = '\x1b[34m'
    RESET: str = '\x1b[39m'


def _color_print(message: str, color: str):
    print(color + message + _COLOR.RESET)


def print_proof(proof: Optional[List[Tuple[str, str]]]):
    """
    Pretty print proof with colors.

    :param proof: The proof to print.
    """
    if proof is None:
        _color_print("No proof was found", _COLOR.RED)
    else:
        rule_names, theorems = zip(*proof[1:])
        rule_names, theorems = list(rule_names), list(theorems)

        print("Theorems:")
        for theorem in theorems:
            _color_print(theorem, _COLOR.GREEN)

        print("\nRules:")
        for rule_name in rule_names:
            _color_print(rule_name, _COLOR.GREEN)
