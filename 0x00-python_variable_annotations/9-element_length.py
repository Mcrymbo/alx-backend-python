#!/usr/bin/env python3
"""
annoting an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function for duck typing """
    return [(i, len(i)) for i in lst]
