#! /usr/bin/env python3
import time

from advent_of_code.towels import Towels


def part_one() -> None:
    start = time.monotonic()
    towels = Towels("2024/day-19-patterns.txt", "2024/day-19-designs.txt")
    print(
        "Day 19 part 1:",
        towels.count_possible(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    towels = Towels("2024/day-19-patterns.txt", "2024/day-19-designs.txt")
    print(
        "Day 19 part 2:",
        towels.count_combinations(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
