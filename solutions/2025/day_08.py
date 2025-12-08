#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.junction_boxes import JunctionBoxes


@timed_solution(year=2025, day=8, part=1)
def part_one() -> int:
    boxes = JunctionBoxes("2025/day-8.txt")
    return boxes.largest_circuits(1000)


if __name__ == "__main__":
    part_one()
