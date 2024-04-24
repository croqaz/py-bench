"""
List sort performance test.

Options:

    * `benchmark` name to run
    * `--rnd-seed` to set random seed
    * `--size` to set the sorted list size

Based on https://github.com/python/cpython/blob/963904335e579bfe39101adf3fd6a0cf705975ff/Lib/test/sortperf.py

Later from https://github.com/python/cpython/blob/3.12/Tools/scripts/sortperf.py
"""

from __future__ import annotations

import argparse
import time
import random


# ===============
# Data generation
# ===============


def _random_data(size: int, rand: random.Random) -> list[float]:
    result = [rand.random() for _ in range(size)]
    # Shuffle it a bit...
    for i in range(10):
        i = rand.randrange(size)
        temp = result[:i]
        del result[:i]
        temp.reverse()
        result.extend(temp)
        del temp
    assert len(result) == size
    return result


def list_sort(size: int, rand: random.Random) -> list[float]:
    return _random_data(size, rand)


def list_sort_descending(size: int, rand: random.Random) -> list[float]:
    return list(reversed(list_sort_ascending(size, rand)))


def list_sort_ascending(size: int, rand: random.Random) -> list[float]:
    return sorted(_random_data(size, rand))


def list_sort_ascending_exchanged(size: int, rand: random.Random) -> list[float]:
    result = list_sort_ascending(size, rand)
    # Do 3 random exchanges.
    for _ in range(3):
        i1 = rand.randrange(size)
        i2 = rand.randrange(size)
        result[i1], result[i2] = result[i2], result[i1]
    return result


def list_sort_ascending_random(size: int, rand: random.Random) -> list[float]:
    assert size >= 10, "This benchmark requires size to be >= 10"
    result = list_sort_ascending(size, rand)
    # Replace the last 10 with random floats.
    result[-10:] = [rand.random() for _ in range(10)]
    return result


def list_sort_ascending_one_percent(size: int, rand: random.Random) -> list[float]:
    result = list_sort_ascending(size, rand)
    # Replace 1% of the elements at random.
    for _ in range(size // 100):
        result[rand.randrange(size)] = rand.random()
    return result


def list_sort_duplicates(size: int, rand: random.Random) -> list[float]:
    assert size >= 4
    result = list_sort_ascending(4, rand)
    # Arrange for lots of duplicates.
    result = result * (size // 4)
    # Force the elements to be distinct objects, else timings can be
    # artificially low.
    return list(map(abs, result))


def list_sort_equal(size: int, rand: random.Random) -> list[float]:
    # All equal.  Again, force the elements to be distinct objects.
    return list(map(abs, [-0.519012] * size))


def list_sort_worst_case(size: int, rand: random.Random) -> list[float]:
    # This one looks like [3, 2, 1, 0, 0, 1, 2, 3].  It was a bad case
    # for an older implementation of quicksort, which used the median
    # of the first, last and middle elements as the pivot.
    half = size // 2
    result = list(range(half - 1, -1, -1))
    result.extend(range(half))
    # Force to float, so that the timings are comparable.  This is
    # significantly faster if we leave them as ints.
    return list(map(float, result))


# =========
# Benchmark
# =========


class Benchmark:
    def __init__(self, name: str, size: int, seed: int) -> None:
        self._name = name
        self._size = size
        self._seed = seed
        self._random = random.Random(self._seed)

    def run(self, loops: int = 100) -> float:
        all_data = self._prepare_data(loops)
        start = time.perf_counter()

        for data in all_data:
            data.sort()  # Benching this method!

        return time.perf_counter() - start

    def _prepare_data(self, loops: int) -> list[float]:
        bench = BENCHMARKS[self._name]
        data = bench(self._size, self._random)
        return [data.copy() for _ in range(loops)]


DEFAULT_SIZE = 1 << 14
DEFAULT_RANDOM_SEED = 0
BENCHMARKS = {
    "list_sort": list_sort,
    "list_sort_descending": list_sort_descending,
    "list_sort_ascending": list_sort_ascending,
    "list_sort_ascending_exchanged": list_sort_ascending_exchanged,
    "list_sort_ascending_random": list_sort_ascending_random,
    "list_sort_ascending_one_percent": list_sort_ascending_one_percent,
    "list_sort_duplicates": list_sort_duplicates,
    "list_sort_equal": list_sort_equal,
    "list_sort_worst_case": list_sort_worst_case,
}

if __name__ == "__main__":
    # "Test `list.sort()` with different data"
    parser = argparse.ArgumentParser(prog="ListSort")
    parser.add_argument(
        "benchmark",
        choices=BENCHMARKS,
        nargs="?",
        help="Can be any of: {0}".format(", ".join(BENCHMARKS)),
    )
    parser.add_argument(
        "--size",
        type=int,
        default=DEFAULT_SIZE,
        help=f"Size of the lists to sort (default: {DEFAULT_SIZE})",
    )
    parser.add_argument(
        "--rng-seed",
        type=int,
        default=DEFAULT_RANDOM_SEED,
        help=f"Random number generator seed (default: {DEFAULT_RANDOM_SEED})",
    )
    args = parser.parse_args()
    if args.benchmark:
        benchmarks = (args.benchmark,)
    else:
        benchmarks = sorted(BENCHMARKS)
    for bench in benchmarks:
        benchmark = Benchmark(bench, args.size, args.rng_seed)
        benchmark.run()
    print("OK")
