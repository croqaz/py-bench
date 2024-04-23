# Python benchmark

From https://github.com/python/pyperformance and other places.

## Why

These tests are designed to be run without Pyperformance. You can use whichever benchmarking tool you want.

## Running

Using [GNU time](https://gnu.org/software/time/) command. Example:

```
/usr/bin/time -f "Time result \ncmd: %C \nreal: %es \nuser: %Us \nsys: %Ss \nMax mem: %MKB \nCPU: %P" python bench/pystone.py

  Time result
  cmd: python bench/pystone.py
  real: 0.34s
  user: 0.34s
  sys: 0.00s
  Max mem: 8448KB
  CPU: 100%
```

Using [Hyperfine](https://github.com/sharkdp/hyperfine) app. Example:

```
hyperfine --warmup=3 --runs=3 -n=Python 'python bench/pystone.py'

Benchmark 1: Python
  Time (mean ± σ):     309.5 ms ±   2.3 ms    [User: 307.8 ms, System: 2.0 ms]
  Range (min … max):   307.2 ms … 313.9 ms    10 runs
```

Using [Pyperf](https://github.com/psf/pyperf) Python library and app. Example:

```
python -m pip install pyperf
python -m pyperf command -- python bench/pystone.py

  .....................
  command: Mean +- std dev: 318 ms +- 10 ms
```
