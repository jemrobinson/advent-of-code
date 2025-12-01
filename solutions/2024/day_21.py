#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.keypad import KeypadSolver


@timed_solution(day=21, part=1)
def part_one() -> int:
    solver = KeypadSolver("2024/day-21.txt", num_directional=2)
    return solver.total_complexity()


@timed_solution(day=21, part=2)
def part_two() -> int:
    solver = KeypadSolver("2024/day-21.txt", num_directional=25)
    return solver.total_complexity()


if __name__ == "__main__":
    part_one()
    part_two()
