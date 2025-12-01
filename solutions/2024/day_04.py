#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.wordsearch import WordSearch, WordSearchSimple


@timed_solution(day=4, part=1)
def part_one() -> int:
    wordsearch = WordSearchSimple("2024/day-4.txt")
    return wordsearch.search("XMAS")


@timed_solution(day=4, part=2)
def part_two() -> int:
    wordsearch = WordSearch("2024/day-4.txt")
    return wordsearch.search_xmas()


if __name__ == "__main__":
    part_one()
    part_two()
