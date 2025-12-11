#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.toroidal_reactor import ToroidalReactor


@timed_solution(year=2025, day=11, part=1)
def part_one() -> int:
    reactor = ToroidalReactor("2025/day-11.txt")
    return reactor.n_paths_you()


@timed_solution(year=2025, day=11, part=2)
def part_two() -> int:
    reactor = ToroidalReactor("2025/day-11.txt")
    return reactor.n_paths_server()


if __name__ == "__main__":
    part_one()
    part_two()
