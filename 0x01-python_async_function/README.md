0-basic_async_syntax.py                 Coantains an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.



1-concurrent_coroutines.py              Import wait_random from the previous python file that I've written and writes an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay.



2-measure_runtime.py                    From the previous file, imports wait_n into 2-measure_runtime.py and Create sa measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. 



3-tasks.py                              Import wait_random from 0-basic_async_syntax. and a function task_wait_random that takes an integer max_delay and returns a asyncio.Task.



4-tasks.py                              Takes the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
