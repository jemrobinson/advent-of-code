#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.warehouse import LargeWarehouse, Warehouse


@timed_solution(day=15, part=1)
def part_one() -> int:
    warehouse = Warehouse("2024/day-15-moves.txt", "2024/day-15-warehouse.txt")
    return warehouse.score_gps()


@timed_solution(day=15, part=2)
def part_two() -> int:
    warehouse = LargeWarehouse("2024/day-15-moves.txt", "2024/day-15-warehouse.txt")
    return warehouse.score_gps()


if __name__ == "__main__":
    part_one()
    part_two()
