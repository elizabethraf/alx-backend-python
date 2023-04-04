#!/usr/bin/env python3
"""Display async_generator from the previous task"""
from typing import List
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_generator() -> List[float]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()


async def async_comprehension():
    result = [x async for x in async_generator()]
    return result
