#!/usr/bin/env python3
import asyncio

"""Async Generator"""

async def async_generator():
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield i

async def main():
    """Main"""
    async for i in async_generator():
        print(i, end=' ')
    print(i)

if __name__ == '__main__':
    asyncio.run(main())