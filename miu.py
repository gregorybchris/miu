"""Runs the theorem prover for the MIU problem."""

import argparse

import miu_logging
import theorem_prover
import miu_rules
import halting_criteria


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--conjecture', default='MU',
                        type=str, help='Conjecture to prove.')
    args = parser.parse_args()

    language = 'MIU'
    axioms = ['MI']
    prover = theorem_prover.TheoremProver(language, axioms)
    for name, rule in miu_rules.rules.items():
        prover.register_rule(rule, name)

    conjecture = args.conjecture
    halt = halting_criteria.HaltingCriteria()

    logger = None
    # logger = miu_logging.get_logger('MIU.log')
    proof = prover.prove(conjecture, halt, logger=logger)

    if proof is None:
        print("No proof was found")
    else:
        rules, theorems = zip(*proof[1:])
        print(f"Theorems: {theorems}")
        print(f"Rules: {rules}")
