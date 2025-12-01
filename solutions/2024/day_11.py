#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.stones import StoneLine


@timed_solution(day=11, part=1)
def part_one() -> int:
    stone_line = StoneLine("2024/day-11.txt")
    return stone_line.score(25)


@timed_solution(day=11, part=2)
def part_two() -> int:
    stone_line = StoneLine("2024/day-11.txt")
    return stone_line.score(75)


if __name__ == "__main__":
    part_one()
    part_two()
