#!/usr/bin/env python3
""" This module contains a function that returns a function that multiplies a float by a given number """

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by a given number using lamda expression"""
    return lambda x: x * multiplier
