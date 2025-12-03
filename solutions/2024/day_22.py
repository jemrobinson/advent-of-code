#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.banana_market import BananaMarket


@timed_solution(year=2024, day=22, part=1)
def part_one() -> int:
    market = BananaMarket("2024/day-22.txt")
    return market.sum_buyer_secrets()


@timed_solution(year=2024, day=22, part=2)
def part_two() -> int:
    market = BananaMarket("2024/day-22.txt")
    return market.most_bananas()


if __name__ == "__main__":
    part_one()
    part_two()
