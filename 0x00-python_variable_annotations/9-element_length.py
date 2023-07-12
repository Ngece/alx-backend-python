#!/usr/bin/env python3
""" This module contains a function that returns the length of a string or list """

from typing import Union, Sequence, Iterable, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples containing the length of each element in the list """
    return [(i, len(i)) for i in lst]