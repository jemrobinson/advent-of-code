#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.lab_maze import LabMaze


@timed_solution(day=6, part=1)
def part_one() -> int:
    maze = LabMaze("2024/day-6.txt")
    return maze.walk()


@timed_solution(day=6, part=2)
def part_two() -> int:
    maze = LabMaze("2024/day-6.txt")
    return maze.count_loops()


if __name__ == "__main__":
    part_one()
    part_two()
