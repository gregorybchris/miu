"""Runs the theorem prover for the MIU problem."""

import miu_logging

import theorem_prover
import miu_rules
import halting_criteria


if __name__ == '__main__':
    language = 'MIU'
    axioms = ['MI']
    prover = theorem_prover.TheoremProver(language, axioms)
    for name, rule in miu_rules.rules.items():
        prover.register_rule(rule, name)

    conjecture = 'MU'
    # conjecture = 'MIUIIIIU'
    halt = halting_criteria.HaltingCriteria()

    # logger = miu_logging.get_logger('MIU.log')
    logger = None
    proof = prover.prove(conjecture, halt, logger=logger)

    if proof is None:
        print("No proof was found")
    else:
        rules, theorems = zip(*proof[1:])
        print(f"Theorems: {theorems}")
        print(f"Rules: {rules}")
