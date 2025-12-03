#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.paper_forklift import PaperForklift


@timed_solution(year=2025, day=4, part=1)
def part_one() -> int:
    forklift = PaperForklift("2025/day-4.txt")
    return forklift.accessible_rolls()


if __name__ == "__main__":
    part_one()
