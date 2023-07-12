0-async_generator.py                    Contains a coroutine called async_generator that loops 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. 



1-async_comprehension.py                Imports async_generator from the previous task and then write a coroutine called async_comprehension that collects 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.



2-measure_runtime.py                    Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.