#! /usr/bin/env python3
import time

from advent_of_code.rotating_dial import RotatingDial


def part_one() -> None:
    start = time.monotonic()
    dial = RotatingDial("2025/day-1.txt")
    print(
        "Day 1 part 1:",
        dial.count_zeros(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    dial = RotatingDial("2025/day-1.txt")
    print(
        "Day 1 part 2:",
        dial.count_all_zeros(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
