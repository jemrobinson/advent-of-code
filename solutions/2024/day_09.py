#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.file_system import FileSystem


@timed_solution(year=2024, day=9, part=1)
def part_one() -> int:
    file_system = FileSystem("2024/day-9.txt")
    return file_system.checksum()


@timed_solution(year=2024, day=9, part=2)
def part_two() -> int:
    file_system = FileSystem("2024/day-9.txt")
    return file_system.checksum(strategy="conservative")


if __name__ == "__main__":
    part_one()
    part_two()
