"""Runs the theorem prover for the MIU problem."""

import argparse

import halting_criteria
import miu_logging
import miu_rules
import proof_printer
import theorem_prover


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--conjecture', default='MU',
                        type=str, help='Conjecture to prove.')
    parser.add_argument('-p', '--proof-length', default=1000,
                        type=int, help='Max proof length.')
    parser.add_argument('-l', '--theorem-length', default=25,
                        type=int, help='Max theorem length.')
    parser.add_argument('-t', '--timeout', default=5,
                        type=int, help='Timeout in seconds.')
    parser.add_argument('-d', '--debug', default=False, action='store_true',
                        help='Turn debug on with a logger.')

    args = parser.parse_args()

    language = 'MIU'
    axioms = ['MI']
    prover = theorem_prover.TheoremProver(language, axioms)
    for name, rule in miu_rules.rules.items():
        prover.register_rule(rule, name)

    halt = halting_criteria.HaltingCriteria(args.proof_length,
                                            args.theorem_length,
                                            args.timeout)

    logger = miu_logging.get_logger('MIU.log') if args.debug else None

    proof = prover.prove(args.conjecture, halt, logger=logger)
    proof_printer.print_proof(proof)
