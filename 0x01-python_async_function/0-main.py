#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))  # Test with default max_delay of 10
print(asyncio.run(wait_random(5)))  # Test with max_delay of 5
print(asyncio.run(wait_random(15))) # Test with max_delay of 15
