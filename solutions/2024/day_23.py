#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.lan_party import LanParty


@timed_solution(day=23, part=1)
def part_one() -> int:
    party = LanParty("2024/day-23.txt")
    return party.count_triples_with_ts()


@timed_solution(day=23, part=2)
def part_two() -> str:
    party = LanParty("2024/day-23.txt")
    return party.find_password()


if __name__ == "__main__":
    part_one()
    part_two()
