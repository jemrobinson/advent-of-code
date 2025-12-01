from advent_of_code.towels import Towels


def test_part_one() -> None:
    towels = Towels("2024/day-19-patterns.test.txt", "2024/day-19-designs.test.txt")
    assert towels.count_possible() == 6


def test_part_two() -> None:
    towels = Towels("2024/day-19-patterns.test.txt", "2024/day-19-designs.test.txt")
    assert towels.count_combinations() == 16
