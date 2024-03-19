#!/usr/bin/env python3
"""
measures runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measures runtime """
    start_t = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    total_time = end_time - start_t
    return total_time
