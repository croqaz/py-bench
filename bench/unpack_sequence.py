"""
Microbenchmark for Python's sequence unpacking.

Extracted from https://github.com/python/pyperformance
    data-files/benchmarks/bm_unpack_sequence/run_benchmark.py
"""

import argparse
import time


def do_unpacking(loops, to_unpack):
    range_it = range(loops)
    t0 = time.perf_counter()

    for _ in range_it:
        # 400 unpackings
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack

    return time.perf_counter() - t0


def bench_tuple_unpacking(loops):
    x = tuple(range(10))
    return do_unpacking(loops, x)


def bench_list_unpacking(loops):
    x = list(range(10))
    return do_unpacking(loops, x)


def bench_all(loops):
    dt1 = bench_tuple_unpacking(loops)
    dt2 = bench_list_unpacking(loops)
    return dt1 + dt2


if __name__ == "__main__":
    # "Microbenchmark for Python's sequence unpacking."
    benchmarks = {"tuple": bench_tuple_unpacking, "list": bench_list_unpacking}

    parser = argparse.ArgumentParser(prog="UnpackSeq")
    parser.add_argument("benchmark", nargs="?", choices=sorted(benchmarks))
    parser.add_argument("--loops", type=int, default=1000, help="Number of loops.")

    args = parser.parse_args()
    if args.benchmark:
        benchmark = benchmarks[args.benchmark]
    else:
        benchmark = bench_all

    benchmark(args.loops)
    print("OK")
