#!/usr/bin/env python3
""" This module contains a function that takes a list of floats and integers and returns their sum as a float """
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ Returns the sum of the list of floats """
    return sum(mxd_lst)
