#!/usr/bin/env python3
"""imprts wait_random from 0-basic_async_syntax and uses task_wait_random that takes in an integer n and returns a asyncio.Task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))