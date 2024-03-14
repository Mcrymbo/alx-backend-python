#!/usr/bin/env python3
"""
adding mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums integer and float """
    return sum(mxd_lst)
