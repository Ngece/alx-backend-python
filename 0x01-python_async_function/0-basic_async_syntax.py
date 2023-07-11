#!/usr/bin/env python3
import asyncio
"""imports wait_random from the previous python file"""
wait_random = __import__('0-basic_async_syntax').wait_random


"""declares wait_random parameterized coroutine that waits for a random delay"""
async def wait_random(max_delay: int = 10) -> float:
    """[summary]"""
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


"""imports wait_random from the previous python file"""
def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        asyncio.Task: [description]
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task