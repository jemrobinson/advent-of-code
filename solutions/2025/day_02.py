#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.gift_shop import GiftShop


@timed_solution(day=1, part=1)
def part_one() -> int:
    shop = GiftShop("2025/day-2.txt")
    return shop.invalid_id_sum()


def part_two() -> int:
    pass


if __name__ == "__main__":
    part_one()
    part_two()
