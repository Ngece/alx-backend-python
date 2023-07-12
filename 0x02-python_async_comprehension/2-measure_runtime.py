#!/usr/bin/env python3
"""function measure_runtime that measures the total runtime and return it. """
import asyncio
import time
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """measure the total runtime and return it. """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start

if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))
    