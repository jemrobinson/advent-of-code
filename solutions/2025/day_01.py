#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.rotating_dial import RotatingDial


@timed_solution(day=1, part=1)
def part_one() -> None:
    dial = RotatingDial("2025/day-1.txt")
    return dial.count_zeros()


@timed_solution(day=1, part=2)
def part_two() -> None:
    dial = RotatingDial("2025/day-1.txt")
    return dial.count_all_zeros()


if __name__ == "__main__":
    part_one()
    part_two()
