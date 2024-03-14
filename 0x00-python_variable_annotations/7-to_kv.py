#!/usr/bin/env python3
"""
module for complex types-string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    type-annoted function for str and int/float
    """
    return (k, v ** 2)
