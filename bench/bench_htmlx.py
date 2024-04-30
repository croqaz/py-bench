"""
Benchmark different HTML parsers.

Adapted from: https://github.com/kovidgoyal/HTML5-parser
    benchmark.py

Requires external libraries:
- html5_parser
- html5lib
- bs4 BeautifulSoup
"""

from functools import partial
import argparse
import os
import time


try:
    import html5_parser
except Exception:
    print("html5_parser not available!")

    class html5_parser:
        def parse(self):
            pass


try:
    import html5lib
except Exception:
    print("html5lib not available!")

    class html5lib:
        def parse(self):
            pass


try:
    from bs4 import BeautifulSoup
except Exception:
    print("BeautifulSoup not available!")
    BeautifulSoup = lambda: 0


def timeit(name: str, parser_func):
    t0 = time.perf_counter()
    try:
        root = parser_func()
        # I really wanted to select some random element from the tree here,
        # but the API is super different for all the builders returned by
        # the parser...
    except Exception as err:
        print(f"{name} crashed: {err}")
        return
    t1 = time.perf_counter()
    print(f"{name} {t1-t0:.4f} sec")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Benchmark HTML5 parsers")
    p.add_argument("--num", "-n", type=int, default=1, help="Number of repetitions")
    args = p.parse_args()

    DIR = os.path.split(__file__)[0]
    raw = open(DIR + "/data/HTML-Standard.html", "rb").read()

    for i in range(args.num):
        timeit("html5_parser-LXML", partial(html5_parser.parse, raw, transport_encoding="utf-8", treebuilder="lxml"))
        timeit("html5_parser-etree", partial(html5_parser.parse, raw, transport_encoding="utf-8", treebuilder="etree"))
        timeit("html5_parser-soup", partial(html5_parser.parse, raw, transport_encoding="utf-8", treebuilder="soup"))

        timeit("html5lib-LXML", partial(html5lib.parse, raw, transport_encoding="utf-8", treebuilder="lxml"))
        timeit("html5lib-etree", partial(html5lib.parse, raw, transport_encoding="utf-8", treebuilder="etree"))
        timeit("html5lib-dom", partial(html5lib.parse, raw, transport_encoding="utf-8", treebuilder="dom"))

        timeit("BeautifulSoup-LXML", partial(BeautifulSoup, raw, "lxml"))
        # timeit("BeautifulSoup-html.parser", partial(BeautifulSoup, raw, "html.parser")) # 4x slower!
