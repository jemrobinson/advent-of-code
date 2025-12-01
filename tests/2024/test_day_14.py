from advent_of_code.robots import RobotGrid


def test_part_one() -> None:
    grid = RobotGrid("2024/day-14.test.txt", width=11, height=7)
    assert grid.safety_factor(100) == 12
