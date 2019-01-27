"""Tests for the MIU prover."""

import numpy as np
import unittest

from ddt import ddt, data, unpack
from miu_rules import rule_1, rule_2, rule_3, rule_4

rule_tests = [
    {
        'rule': rule_1,
        'name': 'rule 1',
        'in_theorem': 'MI',
        'out_theorems': ['MIU']
    },
    {
        'rule': rule_2,
        'name': 'rule 2',
        'in_theorem': 'MI',
        'out_theorems': ['MII']
    },
    {
        'rule': rule_3,
        'name': 'rule 3',
        'in_theorem': 'MIIII',
        'out_theorems': ['MUI', 'MIU']
    },
    {
        'rule': rule_4,
        'name': 'rule 4',
        'in_theorem': 'MI',
        'out_theorems': []
    },
    {
        'rule': rule_4,
        'name': 'rule 4',
        'in_theorem': 'MUU',
        'out_theorems': ['M']
    }
]


def all_equal(list_a, list_b):
    """Return True when the lists are equal."""
    if len(list_a) != len(list_b):
        return False
    a, b = np.array(list_a), np.array(list_b)
    return all(a == b)


@ddt
class MIUTests(unittest.TestCase):
    """Tests for the MIU prover."""

    @data(*rule_tests)
    @unpack
    def test_rule(self, rule, name, in_theorem, out_theorems):
        """Tests the rules."""
        out = rule(in_theorem)
        self.assertTrue(all_equal(out, out_theorems))


if __name__ == '__main__':
    unittest.main()
