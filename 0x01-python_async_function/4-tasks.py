#!/usr/bin/env python3
"""Display alter it into a new function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Return objects"""
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return objects"""
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return sorted(results)
