#!/usr/bin/env python3
"""
adding annotations to function
"""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ gets a value safely """
    if key in dct:
        return dct[key]
    else:
        return default
