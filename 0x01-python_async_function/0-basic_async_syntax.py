#!/usr/bin/env python3
"""
This module contains a single function, wait_random, which asynchronously 
waits for a random delay between 0 and max_delay seconds and returns the actual wait time.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay, in seconds. Default is 10.

    Returns:
        float: The random delay time.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
