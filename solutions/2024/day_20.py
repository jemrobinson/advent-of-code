#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.race_condition_maze import RaceConditionMaze


@timed_solution(day=20, part=1)
def part_one() -> int:
    maze = RaceConditionMaze("2024/day-20.txt")
    return maze.n_cheats(n_picoseconds_disabled=2, minimum_time_saved=100)


@timed_solution(day=20, part=2)
def part_two() -> int:
    maze = RaceConditionMaze("2024/day-20.txt")
    return maze.n_cheats(n_picoseconds_disabled=20, minimum_time_saved=100)


if __name__ == "__main__":
    part_one()
    part_two()
