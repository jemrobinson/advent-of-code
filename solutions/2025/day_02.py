#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.gift_shop import GiftShop


@timed_solution(year=2025, day=2, part=1)
def part_one() -> int:
    shop = GiftShop("2025/day-2.txt")
    return shop.invalid_ids_repeat_twice()


@timed_solution(year=2025, day=2, part=2)
def part_two() -> int:
    shop = GiftShop("2025/day-2.txt")
    return shop.invalid_ids_repeat_any()


if __name__ == "__main__":
    part_one()
    part_two()
