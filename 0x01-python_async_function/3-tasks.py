#!/usr/bin/env python3
"""Display  the regular function"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Return a asyncia.taks"""
    return asyncio.create_task(wait_random(max_delay))
