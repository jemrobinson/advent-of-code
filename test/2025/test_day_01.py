from advent_of_code.rotating_dial import RotatingDial


def test_part_one() -> None:
    dial = RotatingDial("2025/day-1.test.txt")
    assert dial.count_zeros() == 3
