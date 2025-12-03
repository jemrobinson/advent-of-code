#! /usr/bin/env python3
from functools import reduce

from advent_of_code.antennae import load_antenna_sets
from advent_of_code.aoc_solution import timed_solution


@timed_solution(year=2024, day=8, part=1)
def part_one() -> int:
    antennae = load_antenna_sets("2024/day-8.txt")
    antinodes = reduce(set.union, [a.antinodes() for a in antennae])
    return len(antinodes)


@timed_solution(year=2024, day=8, part=2)
def part_two() -> int:
    antennae = load_antenna_sets("2024/day-8.txt")
    antinodes = reduce(
        set.union, [a.antinodes(first_harmonic=0, last_harmonic=999) for a in antennae]
    )
    return len(antinodes)


if __name__ == "__main__":
    part_one()
    part_two()
