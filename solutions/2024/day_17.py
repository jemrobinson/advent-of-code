#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.three_bit_computer import ThreeBitComputer


@timed_solution(year=2024, day=17, part=1)
def part_one() -> str:
    computer = ThreeBitComputer("2024/day-17.txt")
    return ",".join(map(str, computer.run()))


@timed_solution(year=2024, day=17, part=2)
def part_two() -> int:
    computer = ThreeBitComputer("2024/day-17.txt")
    return computer.find_register_a()


if __name__ == "__main__":
    part_one()
    part_two()
