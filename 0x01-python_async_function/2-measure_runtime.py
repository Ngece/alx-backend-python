#!/usr/bin/env python3
"""imports wait_n from 1-concurrent_coroutines.py and uses measure_time function with integers n and max_delay as arguments"""

import asyncio
import random
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """returns time it takes to execute wait_n"""
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    total_time = end - start
    
    return total_time / n