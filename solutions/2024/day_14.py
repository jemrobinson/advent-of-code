#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.robots import RobotGrid


@timed_solution(day=14, part=1)
def part_one() -> int:
    grid = RobotGrid("2024/day-14.txt", width=101, height=103)
    return grid.safety_factor(100)


@timed_solution(day=14, part=2)
def part_two() -> int:
    grid = RobotGrid("2024/day-14.txt", width=101, height=103)
    return grid.christmas_tree()


@timed_solution(day=14, part=2)
def part_two_adjacency() -> int:
    grid = RobotGrid("2024/day-14.txt", width=101, height=103)
    return grid.christmas_tree_adjacency(500)


@timed_solution(day=14, part=2)
def part_two_non_adjacency() -> int:
    grid = RobotGrid("2024/day-14.txt", width=101, height=103)
    return grid.christmas_tree_non_adjacency(1000)


if __name__ == "__main__":
    part_one()
    part_two()
    part_two_adjacency()
    part_two_non_adjacency()
