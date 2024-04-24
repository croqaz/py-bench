"""
Benchmark for recursive coroutines.
Author: Kumar Aditya.
"""

import time


async def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return await fibonacci(n - 1) + await fibonacci(n - 2)


def benchmark(loops: int = 10) -> float:
    range_it = range(loops)
    t0 = time.perf_counter()
    for _ in range_it:
        coro = fibonacci(25)
        try:
            while True:
                coro.send(None)
        except StopIteration:
            pass
    return time.perf_counter() - t0


if __name__ == "__main__":
    # "Benchmark coroutines"
    benchmark()
    print("OK")
