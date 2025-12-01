#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.logic_gates import Computer


@timed_solution(day=24, part=1)
def part_one() -> int:
    computer = Computer("2024/day-24.txt")
    return computer.output()


@timed_solution(day=24, part=2)
def part_two() -> str:
    computer = Computer("2024/day-24.txt")
    return computer.calculate_swaps()


if __name__ == "__main__":
    part_one()
    part_two()
