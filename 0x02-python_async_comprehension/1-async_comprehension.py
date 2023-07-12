#!/usr/bin/env python3
"""function async_comprehension that takes no arguments and returns a list of the 10 random numbers """
import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """return the 10 random numbers. """
    return [i async for i in async_generator()]

async def main() -> None:
    """the coroutine async_comprehension and print the 10 random numbers. """
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
