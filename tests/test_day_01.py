from advent_of_code.data_loaders import load_csv_as_df
from advent_of_code.location_lists import distance_df, similarity_df


def test_part_one() -> None:
    df = load_csv_as_df("day-1.test.csv")
    assert distance_df(df) == 11


def test_part_two() -> None:
    df = load_csv_as_df("day-1.test.csv")
    assert similarity_df(df) == 31
