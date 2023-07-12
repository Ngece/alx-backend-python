#!/usr/bin/env python3
import asyncio
import random
"""waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
    Args:
        max_delay (int, optional): Defaults to 10.
    Returns:
        float: which is the random delay
"""

async def wait_random(max_delay: int = 10) -> float:
    """takes an integer max_delay and returns a delayed value"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay