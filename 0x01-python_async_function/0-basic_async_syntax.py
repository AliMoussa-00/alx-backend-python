#!/usr/bin/env python3
'''The basics of async'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronously generates a random float value within range [0, max_delay].

    Parameters:
    max_delay (int): The maximum delay value. Defaults to 10.

    Returns:
    float: A random float value within the range [0, max_delay].
    '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
