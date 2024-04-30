"""
GC traversal benchmark.
"""

import gc
import time

N_LEVELS = 2000


def create_recursive_containers(n_levels: int):
    current_list = []

    for n in range(n_levels):
        new_list = [None] * n
        for index in range(n):
            new_list[index] = current_list
        current_list = new_list

    return current_list


def benchmark(n_levels: int, loops: int = 10):
    total_time = 0
    all_cycles = create_recursive_containers(n_levels)

    for _ in range(loops):
        gc.collect()
        # Main loop to measure
        t0 = time.perf_counter()
        collected = gc.collect()
        total_time += time.perf_counter() - t0

        assert collected is None or collected == 0

    return total_time


if __name__ == "__main__":
    benchmark(N_LEVELS)
    print("OK")
