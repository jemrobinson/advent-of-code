#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.print_queue import PrintQueue


@timed_solution(year=2024, day=5, part=1)
def part_one() -> int:
    queue = PrintQueue(
        rules_file="2024/day-5.rules.csv", updates_file="2024/day-5.updates.csv"
    )
    return queue.score_ordered_updates()


@timed_solution(year=2024, day=5, part=2)
def part_two() -> int:
    queue = PrintQueue(
        rules_file="2024/day-5.rules.csv", updates_file="2024/day-5.updates.csv"
    )
    return queue.score_unordered_updates()


if __name__ == "__main__":
    part_one()
    part_two()
