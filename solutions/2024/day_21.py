#! /usr/bin/env python3
import time

from advent_of_code.keypad import KeypadSolver


def part_one() -> None:
    start = time.monotonic()
    solver = KeypadSolver("day-21.txt", num_directional=2)
    print(
        "Day 21 part 1:",
        solver.total_complexity(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    solver = KeypadSolver("day-21.txt", num_directional=25)
    print(
        "Day 21 part 2:",
        solver.total_complexity(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
