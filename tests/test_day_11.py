from advent_of_code_2024.stones import StoneLine


def test_part_one() -> None:
    stone_line = StoneLine("day-11.test.txt")
    assert stone_line.score(25) == 55312
