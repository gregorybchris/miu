"""Proves theorems by exploring the space of theorems."""

import copy
import logging
import multiprocessing as mp
import queue

from halting_criteria import HaltingCriteria
from typing import Callable, List, Optional, Tuple


class TheoremProver:
    """
    Proves theorems by exploring the space of theorems.

    Given an axiom and a set of rules, a full search is performed
    to find a proof of the given theorem.
    """

    GIVEN = 'GIVEN'

    def __init__(self,
                 alphabet: str,
                 axioms: List[str]):
        """
        Construct TheoremProver.

        :param alphabet: The letters from which theorems are composed.
        :param axioms: The axioms that are known to be true.
        """
        self._rules = dict()
        self._alphabet = alphabet
        self._axioms = axioms

    def register_rule(self,
                      rule: Callable[[str], List[str]],
                      rule_name: str
                      ) -> None:
        """
        Register a rule with the theorem prover.

        :param rule: A function from strings to lists of strings defining
            transitions between theorems
        :param rule_name: A string to identify the rule.
        """
        self._rules[rule_name] = rule

    def prove(self,
              conjecture: str,
              halting_criteria: HaltingCriteria,
              logger: Optional[logging.Logger] = None
              ) -> Optional[List[Tuple[str, str]]]:
        """
        Prove a conjecture.

        Does a BFS to find the shortest proof that proves the conjecture.
        :param conjecture: The conjecture to be proved.
        :param halting_criteria: The method for halting the search for a proof.
        :return: A list of rule_name, theorem where the last theorem is the
            conjecture or None if there was no proof found.
        """
        if len(self._rules) == 0:
            raise ValueError("Must register a rule before proving a theorem.")

        result_queue = mp.Queue()
        process_args = (conjecture, halting_criteria, logger, result_queue)
        p = mp.Process(target=self._prove, args=process_args)
        p.start()
        timeout = halting_criteria.seconds
        try:
            result = result_queue.get(timeout=timeout)
            p.join()
        except queue.Empty:
            p.terminate()
            return None

        return result

    def _prove(self,
               conjecture: str,
               halting_criteria: HaltingCriteria,
               logger: Optional[logging.Logger],
               result_queue: mp.Queue
               ) -> None:
        """
        Prove a conjecture.

        Does a BFS to find the shortest proof that proves the conjecture.
        :param conjecture: The conjecture to be proved.
        :param halting_criteria: The method for halting the search for a proof.
        :return: A list of rule_name, theorem where the last theorem is the
            conjecture or None if there was no proof found.
        """
        proof_queue = queue.Queue()
        for axiom in self._axioms:
            init_proof = [(TheoremProver.GIVEN, axiom)]
            proof_queue.put(init_proof)

        all_theorems = set(self._axioms)

        # Iterate over all possible proofs
        while not proof_queue.empty():
            proof = proof_queue.get()
            if len(proof) > halting_criteria.proof_length:
                result_queue.put(None)
                continue
            _, theorem = proof[-1]
            # Try all rules on the current proof
            for rule_name, rule in self._rules.items():
                new_theorems = self._apply_rule(rule, theorem)
                for new_theorem in new_theorems:
                    if new_theorem not in all_theorems:
                        if len(new_theorem) < halting_criteria.theorem_length:
                            # Create a new proof with a new step
                            new_proof = self._update_proof(proof,
                                                           rule_name,
                                                           new_theorem)
                            self._log_proof(new_proof, logger)
                            if new_theorem == conjecture:
                                result_queue.put(new_proof)
                                return
                            proof_queue.put(new_proof)
                            all_theorems.add(new_theorem)
        # No proof found
        result_queue.put(None)

    def _apply_rule(self,
                    rule: Callable[[str], List[str]],
                    theorem: str
                    ) -> List[str]:
        return rule(theorem)

    def _update_proof(self, old_proof, rule_name, new_theorem):
        new_step = (rule_name, new_theorem)
        new_proof = copy.copy(old_proof)
        new_proof.append(new_step)
        return new_proof

    def _log_proof(self, proof, logger):
        if logger is not None:
            tabs = '  ' * (len(proof) - 1)
            logger.info(f'{tabs}Proof: {proof}')
