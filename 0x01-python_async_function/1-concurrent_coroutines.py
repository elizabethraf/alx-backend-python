#!/usr/bin/env python3
"""Display  async routine called wait_n"""
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return float"""
    coroutines = [wait_random(max_delay=max_delay) for _ in range(n)]
    delay = await asyncio.gather(*coroutines)
    return sorted(delay)

async def wait_random(max_delay: int = 10) -> float:
    """Return the list of all the delays"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
