#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.movie_theatre import MovieTheatre


@timed_solution(year=2025, day=9, part=1)
def part_one() -> int:
    theatre = MovieTheatre("2025/day-9.txt")
    return theatre.largest_rectangle()


if __name__ == "__main__":
    part_one()
