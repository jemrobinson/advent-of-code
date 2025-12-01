#! /usr/bin/env python3
import time

from advent_of_code.data_loaders import load_csv_as_df
from advent_of_code.location_lists import distance_df, similarity_df


def part_one() -> None:
    start = time.monotonic()
    df = load_csv_as_df("2024/day-1.csv")
    print(
        "Day 1 part 1:", distance_df(df), f"in {time.monotonic() - start:.3f} seconds"
    )


def part_two() -> None:
    start = time.monotonic()
    df = load_csv_as_df("2024/day-1.csv")
    print(
        "Day 1 part 2:", similarity_df(df), f"in {time.monotonic() - start:.3f} seconds"
    )


if __name__ == "__main__":
    part_one()
    part_two()
