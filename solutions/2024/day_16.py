#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.reindeer_maze import ReindeerMaze


@timed_solution(year=2024, day=16, part=1)
def part_one() -> int:
    maze = ReindeerMaze("2024/day-16.txt")
    return maze.shortest_path()


@timed_solution(year=2024, day=16, part=2)
def part_two() -> int:
    maze = ReindeerMaze("2024/day-16.txt")
    return maze.best_seats()


if __name__ == "__main__":
    part_one()
    part_two()
