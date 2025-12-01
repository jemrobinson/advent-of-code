#! /usr/bin/env python3
import time

from advent_of_code_2024.wordsearch import WordSearch, WordSearchSimple


def part_one() -> None:
    start = time.monotonic()
    wordsearch = WordSearchSimple("day-4.txt")
    print(
        "Day 4 part 1:",
        wordsearch.search("XMAS"),
        f"in {time.monotonic() - start:.3f} seconds",
    )


def part_two() -> None:
    start = time.monotonic()
    wordsearch = WordSearch("day-4.txt")
    print(
        "Day 4 part 2:",
        wordsearch.search_xmas(),
        f"in {time.monotonic() - start:.3f} seconds",
    )


if __name__ == "__main__":
    part_one()
    part_two()
