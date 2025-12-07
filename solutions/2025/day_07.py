#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.tachyon_manifold import TachyonManifold


@timed_solution(year=2025, day=7, part=1)
def part_one() -> int:
    manifold = TachyonManifold("2025/day-7.txt")
    return manifold.n_splits()


if __name__ == "__main__":
    part_one()
