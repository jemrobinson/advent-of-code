#! /usr/bin/env python3
import logging

from advent_of_code.aoc_solution import timed_solution
from advent_of_code.data_loaders import load_file_as_string
from advent_of_code.parser import MemoryParser, parse_memory_string


@timed_solution(year=2024, day=3, part=1)
def part_one() -> int:
    memory = load_file_as_string("2024/day-3.txt")
    instructions = parse_memory_string(memory)
    return sum([x * y for x, y in instructions])


@timed_solution(year=2024, day=3, part=2)
def part_two() -> int:
    memory = load_file_as_string("2024/day-3.txt")
    parser = MemoryParser()
    return parser.parse(memory)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format=r"[%(levelname)8s] %(message)s")
    part_one()
    part_two()
