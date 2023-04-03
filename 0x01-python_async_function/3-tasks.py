#!/usr/bin/env python3
"""Display  the regular function"""
import asyncio
import random


def task_wait_random(max_delay):
    """Return a asyncia.taks"""
    return asyncio.create_task(wait_random(max_delay=max_delay))
