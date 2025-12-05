#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.kitchen_inventory import KitchenInventory


@timed_solution(year=2025, day=5, part=1)
def part_one() -> int:
    inventory = KitchenInventory("2025/day-5.txt")
    return inventory.n_fresh_ingredients()


if __name__ == "__main__":
    part_one()
