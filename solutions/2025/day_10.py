#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.indicator_lights import IndicatorLights


@timed_solution(year=2025, day=10, part=1)
def part_one() -> int:
    indicators = IndicatorLights("2025/day-10.txt")
    return indicators.fewest_presses_lights()


@timed_solution(year=2025, day=10, part=2)
def part_two() -> None:
    indicators = IndicatorLights("2025/day-10.txt")
    return indicators.fewest_presses_joltages()


if __name__ == "__main__":
    part_one()
    part_two()
