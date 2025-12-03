#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.topographic_map import TopographicMap


@timed_solution(year=2024, day=10, part=1)
def part_one() -> int:
    topo_map = TopographicMap("2024/day-10.txt")
    return topo_map.score()


@timed_solution(year=2024, day=10, part=2)
def part_two() -> int:
    topo_map = TopographicMap("2024/day-10.txt")
    return topo_map.rating()


if __name__ == "__main__":
    part_one()
    part_two()
