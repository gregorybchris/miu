"""Halting criteria for the theorem prover."""

from dataclasses import dataclass


@dataclass
class HaltingCriteria:
    """Criteria to decide when to halt a TheoremProver."""

    depth: int = 1000
    theorem_length = 15
