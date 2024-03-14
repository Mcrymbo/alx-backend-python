#!/usr/bin/env python3
"""
function multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function that returns function multiplier """
    return (lambda x: multiplier * x)
