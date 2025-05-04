import asyncio 


class AsyncCounter:
    def __init___(self,start,end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > self.end:
            raise StopAsyncIteration
        self.current += 1
        return self.current - 1


async def main():
    async for number in AsyncCounter(1,5):
        print(number)


asyncio.run(main())

