#!/usr/bin/env python3
""" This module contains a type-annotated function that takes a list input_list of floats as argument and returns their sum as a float. """

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element of a list """
    if lst:
        return lst[0]
    else:
        return None