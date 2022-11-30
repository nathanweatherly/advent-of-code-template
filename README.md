# Advent of Code Template

If you're like me, you'll spend just as much time writing simple I/O as you will actually doing the fun stuff!

Here's some simple I/O for solving [Advent of Code](https://adventofcode.com) puzzles effectively. 

**Note:** This uses Python 3. If you want to solve the puzzles in another language, you're out of luck. Sorry about that.

## Pre-reqs

Python 3

If you want to use the `make pretty` command, first run `make deps`

## Puzzle Prep

### Copy the `day_temp` directory.

```bash
make copy YEAR=<y> DAY=<d>
```

... where `<y>` and `<d>` are integers.

Example:

```bash
make copy YEAR=2022 DAY=1
```

### Provide puzzle inputs

Copy the example input into `/2022/day_<d>/test_input.txt` file.

Copy the puzzle input into the day's `/2022/day_<d>/input.txt` file.

## Solving the puzzle

Open `/<y>/day_<d>/solution.py`.

Implement the functions `part_one` and `part_two` (make sure to `return` the solution).

To run your solution(s) against the test input:

```bash
make test YEAR=<y> DAY=<d>
```

To run your solution(s) against the puzzle input:

```bash 
make run YEAR=<y> DAY=<d>
```

## Helpful hints

By default, `YEAR` is set to `2022`.

If you don't want to constantly provide the day:

```bash
export DAY=<d>
```

## Example

The solution to 2021's Day 1 puzzle is included. See `/2021/day_1/solution.py` for the code.

```bash
$ export YEAR=2021
$ export DAY=1
$ make test
Part 1: 7
Part 2: 5
$ make run
Part 1: 1676
Part 2: 1706
```

Notice that the test results aren't compared to the example solutions provided. This could be added, but I'm lazy :) 

---

## Good Luck!