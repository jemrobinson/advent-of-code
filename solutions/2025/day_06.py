#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.maths_worksheet import MathsWorksheet


@timed_solution(year=2025, day=6, part=1)
def part_one() -> int:
    worksheet = MathsWorksheet("2025/day-6.txt")
    return worksheet.calculate_column_totals()


if __name__ == "__main__":
    part_one()
