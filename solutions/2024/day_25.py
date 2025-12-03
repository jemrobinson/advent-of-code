#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.locks import LockKeyMatcher


@timed_solution(year=2024, day=25, part=1)
def part_one() -> int:
    matcher = LockKeyMatcher("2024/day-25.txt")
    return matcher.unique_pairs()


if __name__ == "__main__":
    part_one()
