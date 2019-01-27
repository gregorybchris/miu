"""Rules for the MIU problem."""

import re
from typing import Optional, Callable, List


def rule_1(theorem: str) -> List[str]:
    """
    If the last letter is I, add a U to the end.

    xI => xIU
    """
    matches = re.findall("^.*I$", theorem)
    return [f'{m}U' for m in matches]


def rule_2(theorem: str) -> List[str]:
    """
    Double the tail of a theorem beginning with an M.

    Mx => Mxx
    """
    matches = re.findall("^M(.*)$", theorem)
    return [f'M{m}{m}' for m in matches]


def rule_3(theorem: str) -> List[str]:
    """
    Replace a triple I with a U.

    xIIIy => xUy
    """
    if len(theorem) < 3:
        return []

    results = []
    for i in range(len(theorem) - 2):
        if theorem[i:i + 3] == 'III':
            results.append(theorem[:i] + 'U' + theorem[i + 3:])

    return results


def rule_4(theorem: str) -> List[str]:
    """
    Remove a double U.

    xUUy => xy
    """
    if len(theorem) < 2:
        return []

    results = []
    for i in range(len(theorem) - 1):
        if theorem[i:i + 2] == 'UU':
            results.append(theorem[:i] + theorem[i + 2:])

    return results


rules = {
    'Append-U': rule_1,
    'Double-Tail': rule_2,
    'Replace-III': rule_3,
    'Remove-UU': rule_4
}
