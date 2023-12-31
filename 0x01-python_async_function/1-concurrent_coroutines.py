#!/usr/bin/env python3
"""Imports wait_random from 0-basic_async_syntax and writes an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay. wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency. Imports wait_random from 0-basic_async_syntax.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    """Sorts the list of delays in ascending order"""
    for i in range(n):
        for j in range(i, n):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays
