#! /usr/bin/env python3
import time

from advent_of_code.lan_party import LanParty


def part_one() -> None:
    start = time.monotonic()
    party = LanParty("2024/day-23.txt")
    print(
        "Day 23 part 1:",
        party.count_triples_with_ts(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    party = LanParty("2024/day-23.txt")
    print(
        "Day 23 part 2:",
        party.find_password(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
