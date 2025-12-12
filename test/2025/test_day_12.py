import pytest

from advent_of_code.christmas_tree_farm import ChristmasTreeFarm


def test_part_one() -> None:
    farm = ChristmasTreeFarm("2025/day-12.test.txt")
    with pytest.raises(
        ValueError, match=r"Found 0 valid regions, but 3 regions remain."
    ):
        farm.n_valid_regions()
