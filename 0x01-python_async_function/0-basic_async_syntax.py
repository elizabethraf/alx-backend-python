#!/usr/bin/env python3
"""Display integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns the value"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)

    return delay
