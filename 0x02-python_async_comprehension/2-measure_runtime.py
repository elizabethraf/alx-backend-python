#!/usr/bin/env python3
"""Display Import async_comprehension"""
import timeit
import asyncio
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Define executes comprehension"""

    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )

    stop = timeit.default_timer()
    return stop - start
