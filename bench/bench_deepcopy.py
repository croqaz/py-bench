"""
Benchmark to measure performance of the python builtin method copy.deepcopy
Performance is tested on a nested dictionary and a dataclass
Author: Pieter Eendebak.
"""

import copy
import time
from dataclasses import dataclass


@dataclass
class A:
    string: str
    lst: list
    boolean: bool


def benchmark_reduce(loops: int):
    """Benchmark where the __reduce__ functionality is used"""

    class C(object):
        def __init__(self):
            self.a = 1
            self.b = 2

        def __reduce__(self):
            return (C, (), self.__dict__)

        def __setstate__(self, state):
            self.__dict__.update(state)

    c = C()

    t0 = time.perf_counter()
    for ii in range(loops):
        _ = copy.deepcopy(c)
    return time.perf_counter() - t0


def benchmark_memo(loops: int):
    """Benchmark where the memo functionality is used"""
    A = [1] * 100
    data = {"a": (A, A, A), "b": [A] * 100}

    t0 = time.perf_counter()
    for ii in range(loops):
        _ = copy.deepcopy(data)
    return time.perf_counter() - t0


def benchmark(loops: int):
    """Benchmark on some standard data types"""
    a = {"list": [1, 2, 3, 43], "t": (1, 2, 3), "str": "hello", "subdict": {"a": True}}
    dc = A("hello", [1, 2, 3], True)

    dt = 0
    for ii in range(loops):
        for jj in range(30):
            t0 = time.perf_counter()
            _ = copy.deepcopy(a)
            dt += time.perf_counter() - t0
        for s in ["red", "blue", "green"]:
            dc.string = s
            for kk in range(5):
                dc.lst[0] = kk
                for b in [True, False]:
                    dc.boolean = b
                    t0 = time.perf_counter()
                    _ = copy.deepcopy(dc)
                    dt += time.perf_counter() - t0
    return dt


if __name__ == "__main__":
    # "Deepcopy benchmark"
    benchmark(200)
    benchmark_reduce(200)
    benchmark_memo(200)
    print("OK")
