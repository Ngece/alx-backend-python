#!/usr/bin/env python3
""" This module contains a function with annotations """

from typing import Union, Tuple

def safely_get_value(dct: dict, key: str, default: Union[None, Tuple[None, None]]) -> Union[None, int, float, str, Tuple[None, None]]:
    """ Returns the value of a key safely """
    if key in dct:
        return dct[key]
    else:
        return default