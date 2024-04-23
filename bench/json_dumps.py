"""
Script for testing the performance of JSON parsing and serialization.

Extracted from https://github.com/python/pyperformance
    data-files/benchmarks/bm_json_dumps/run_benchmark.py
"""

import argparse
import json
import sys


EMPTY = ({}, 2000)
SIMPLE_DATA = {"key1": 0, "key2": True, "key3": "value", "key4": "foo", "key5": "string"}
SIMPLE = (SIMPLE_DATA, 1000)
NESTED_DATA = {
    "key1": 0,
    "key2": SIMPLE[0],
    "key3": "value",
    "key4": SIMPLE[0],
    "key5": SIMPLE[0],
    "key": "\u0105\u0107\u017c",
}
NESTED = (NESTED_DATA, 1000)
HUGE = ([NESTED[0]] * 1000, 1)

CASES = ["EMPTY", "SIMPLE", "NESTED", "HUGE"]


def benchmark(data):
    for obj, count_it in data:
        for _ in count_it:
            json.dumps(obj)


if __name__ == "__main__":
    # "Benchmark json.dumps()"
    cases = ", ".join(CASES)
    parser = argparse.ArgumentParser(prog="JsonDumps")
    parser.add_argument(
        "--cases",
        help="Comma separated list of cases. Available cases: %s. By default, run all cases." % cases,
    )

    args = parser.parse_args()
    if args.cases:
        cases = []
        for case in args.cases.split(","):
            case = case.strip()
            if case:
                cases.append(case)
        if not cases:
            print("ERROR: empty list of cases")
            sys.exit(1)
    else:
        cases = CASES

    data = []
    for case in cases:
        obj, count = globals()[case]
        data.append((obj, range(count)))

    benchmark(data)
    print("OK")
