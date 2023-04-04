#!/usr/bin/env python3
"""Display async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Definen loops 10 times"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()
