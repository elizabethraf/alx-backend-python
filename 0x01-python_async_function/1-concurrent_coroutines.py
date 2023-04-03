#!/usr/bin/env python3
"""Display  async routine called wait_n"""
import asyncio
import random
from typing import List


async def wait_random(max_delay=10):
    """Return  the list of all the delays (float values)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [wait_random(max_delay=max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
