#!/usr/bin/env python3

"takes the code from wait_n and alters it into a new function task_wait_n which calls task_wait_random"

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all delays in ascending order"""
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    """Sorts the list of delays in ascending order"""
    for i in range(n):
        for j in range(i, n):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays