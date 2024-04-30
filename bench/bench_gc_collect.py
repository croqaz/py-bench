"""
GC link benchmark.
"""

import gc
import time

CYCLES = 500
LINKS = 100


class Node:

    def __init__(self):
        self.next = None
        self.prev = None

    def link_next(self, next):
        self.next = next
        self.next.prev = self


def create_cycle(node, n_links: int):
    """Create a cycle of n_links nodes, starting with node."""

    if n_links == 0:
        return

    current = node
    for i in range(n_links):
        next_node = Node()
        current.link_next(next_node)
        current = next_node

    current.link_next(node)


def create_gc_cycles(n_cycles: int, n_links: int):
    """Create n_cycles cycles n_links+1 nodes each."""
    cycles = []

    for _ in range(n_cycles):
        node = Node()
        cycles.append(node)
        create_cycle(node, n_links)

    return cycles


def benchmark(cycles: int, links: int, loops: int = 10):
    total_time = 0

    for _ in range(loops):
        gc.collect()
        all_cycles = create_gc_cycles(cycles, links)

        # Main loop to measure
        del all_cycles
        t0 = time.perf_counter()
        collected = gc.collect()
        total_time += time.perf_counter() - t0

        assert collected is None or collected >= cycles * (links + 1)

    return total_time


if __name__ == "__main__":
    benchmark(CYCLES, LINKS)
    print("OK")
