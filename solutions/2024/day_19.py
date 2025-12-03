#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.towels import Towels


@timed_solution(year=2024, day=19, part=1)
def part_one() -> int:
    towels = Towels("2024/day-19-patterns.txt", "2024/day-19-designs.txt")
    return towels.count_possible()


@timed_solution(year=2024, day=19, part=2)
def part_two() -> int:
    towels = Towels("2024/day-19-patterns.txt", "2024/day-19-designs.txt")
    return towels.count_combinations()


if __name__ == "__main__":
    part_one()
    part_two()
