#! /usr/bin/env python3
import time

from advent_of_code.locks import LockKeyMatcher


def part_one() -> None:
    start = time.monotonic()
    matcher = LockKeyMatcher("2024/day-25.txt")
    print(
        "Day 25 part 1:",
        matcher.unique_pairs(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
