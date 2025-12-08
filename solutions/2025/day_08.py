#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.junction_boxes import JunctionBoxes


@timed_solution(year=2025, day=8, part=1)
def part_one() -> int:
    boxes = JunctionBoxes("2025/day-8.txt")
    return boxes.largest_circuits(1000)


@timed_solution(year=2025, day=8, part=2)
def part_two() -> int:
    boxes = JunctionBoxes("2025/day-8.txt")
    return boxes.fully_connected()


if __name__ == "__main__":
    part_one()
    part_two()
