#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.data_loaders import load_csv_as_df
from advent_of_code.location_lists import distance_df, similarity_df


@timed_solution(year=2024, day=1, part=1)
def part_one() -> int:
    df = load_csv_as_df("2024/day-1.csv")
    return distance_df(df)


@timed_solution(year=2024, day=1, part=2)
def part_two() -> int:
    df = load_csv_as_df("2024/day-1.csv")
    return similarity_df(df)


if __name__ == "__main__":
    part_one()
    part_two()
