#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.battery_bank import BatteryBankArray


@timed_solution(year=2025, day=3, part=1)
def part_one() -> int:
    battery = BatteryBankArray("2025/day-3.txt")
    return battery.largest_joltage(2)


@timed_solution(year=2025, day=3, part=2)
def part_two() -> int:
    battery = BatteryBankArray("2025/day-3.txt")
    return battery.largest_joltage(12)


if __name__ == "__main__":
    part_one()
    part_two()
