#!/usr/bin/env python3
"""
coroutines to collect 10 random numbers
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    collect 10 random numbers
    """
    numbers = [numb async for numb in async_generator()]
    return numbers
