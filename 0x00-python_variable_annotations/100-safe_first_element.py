#!/usr/bin/env python3
"""
Duck-typed annotations
The types of the elements of the input are not known
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ annotes elements with unknown type """
    if lst:
        return lst[0]
    else:
        return None
