#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.plant_regions import GardenPlot


@timed_solution(year=2024, day=12, part=1)
def part_one() -> int:
    plot = GardenPlot("2024/day-12.txt")
    return plot.price()


@timed_solution(year=2024, day=12, part=2)
def part_two() -> int:
    plot_2 = GardenPlot("2024/day-12.txt")
    return plot_2.price_discounted()


if __name__ == "__main__":
    part_one()
    part_two()
