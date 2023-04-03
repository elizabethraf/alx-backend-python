#!/usr/bin/env python3
"""Display function with integers n"""
import asyncio
import random
from typing import List
import time


async def wait_random(max_delay=10):
    """Return a float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a float"""
    coroutines = [wait_random(max_delay=max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """Return a float"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
