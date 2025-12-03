#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.pushdown_maze import PushdownMaze


@timed_solution(year=2024, day=18, part=1)
def part_one() -> int:
    maze = PushdownMaze("2024/day-18.txt", coordinate_max=70)
    return maze.shortest_path(1024)


@timed_solution(year=2024, day=18, part=2)
def part_two() -> str:
    maze = PushdownMaze("2024/day-18.txt", coordinate_max=70)
    return ",".join(map(str, maze.first_blocked_path()))


if __name__ == "__main__":
    part_one()
    part_two()
