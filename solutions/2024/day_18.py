#! /usr/bin/env python3
import time

from advent_of_code.pushdown_maze import PushdownMaze


def part_one() -> None:
    start = time.monotonic()
    maze = PushdownMaze("day-18.txt", coordinate_max=70)
    print(
        "Day 18 part 1:",
        maze.shortest_path(1024),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    maze = PushdownMaze("day-18.txt", coordinate_max=70)
    print(
        "Day 18 part 2:",
        maze.first_blocked_path(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
