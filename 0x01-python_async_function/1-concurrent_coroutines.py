#!/usr/bin/env python3
"""
execute multiple coroutines at the same time
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    a function that spawn wait_random n times
    """
    delay = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delay
