#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.christmas_tree_farm import ChristmasTreeFarm


@timed_solution(year=2025, day=12, part=1)
def part_one() -> int:
    farm = ChristmasTreeFarm("2025/day-12.txt")
    return farm.n_valid_regions()


if __name__ == "__main__":
    part_one()
