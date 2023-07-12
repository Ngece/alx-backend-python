#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

"""function async_generator that takes no arguments and returns a generator. """
async def async_generator() -> Generator[float, None, None]:
    """loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def main() -> None:
    """the coroutine async_generator and print each random number. """
    async for i in async_generator():
        print(i)

if __name__ == "__main__":
    asyncio.run(main())