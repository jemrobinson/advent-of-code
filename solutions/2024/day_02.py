#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.report import load_reports, load_reports_with_dampener


@timed_solution(day=2, part=1)
def part_one() -> int:
    reports = load_reports("2024/day-2.csv")
    return sum([report.is_safe() for report in reports])


@timed_solution(day=2, part=2)
def part_two() -> None:
    reports = load_reports_with_dampener("2024/day-2.csv")
    return sum([report.is_safe() for report in reports])


if __name__ == "__main__":
    part_one()
    part_two()
