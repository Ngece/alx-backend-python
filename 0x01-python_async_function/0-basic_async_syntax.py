#!/usr/bin/env python3
import asyncio
import random
"""function wait_random that takes an integer max_delay and waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it."""

async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        float: which is the random delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay