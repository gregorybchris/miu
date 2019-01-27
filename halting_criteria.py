"""Halting criteria for the theorem prover."""

from dataclasses import dataclass


@dataclass
class HaltingCriteria:
    """Criteria to decide when to halt a TheoremProver."""

    proof_length: int = 1000
    theorem_length: int = 25
    seconds: int = 5
