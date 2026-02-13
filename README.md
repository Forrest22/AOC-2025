# AOC-2025

Trying this year in python. Of course you will want to provide your own inputs by creating the root directory `/inputs` with each relevant day's input text formated as: `day[XX].txt`. Leading zeroes area required.

## Usage

Run a specific Advent of Code day:

`python main.py <day> [part]`

- `<day>` — the day number (e.g., `3`)
- `[part]` — optional, `1` or `2`
  - If omitted, both parts run.

Run all available days in parallel:

`python main.py all`

Examples

```console
python main.py 3        # Run both parts of Day 3
python main.py 3 1      # Run only Part 1
python main.py 3 2      # Run only Part 2
python main.py all      # Run all days in parallel
```
