from advent_of_code.stones import StoneLine


def test_part_one() -> None:
    stone_line = StoneLine("2024/day-11.test.txt")
    assert stone_line.score(25) == 55312
