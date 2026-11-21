# The joke about the demo

A make.fun competition entry: a Python program that writes one one-line joke
about working beside an AI coding agent to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

With `MAKEFUN_OUTPUT_DIR` unset, the program writes to `/output/entry.txt`.
Python 3.13 standard library only; no network access; the same joke on
every run.
