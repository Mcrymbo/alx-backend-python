#!/usr/bin/env python3
"""
async_generator that loops 10 times
"""
import asyncio
import random


async def async_generator():
    """ async generator that loops 10 times """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
