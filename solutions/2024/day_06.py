#! /usr/bin/env python3
import time

from advent_of_code.lab_maze import LabMaze


def part_one() -> None:
    start = time.monotonic()
    maze = LabMaze("2024/day-6.txt")
    print("Day 6 part 1:", maze.walk(), f"in {time.monotonic() - start:.3f} seconds")


def part_two() -> None:
    start = time.monotonic()
    maze = LabMaze("2024/day-6.txt")
    print(
        "Day 6 part 2:",
        maze.count_loops(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
