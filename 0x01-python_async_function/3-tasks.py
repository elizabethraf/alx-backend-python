#!/usr/bin/env python3
"""Display  the regular function"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Return  a asyncio.Task"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay):
    """Return a asyncia.taks"""
    return asyncio.create_task(wait_random(max_delay=max_delay))
