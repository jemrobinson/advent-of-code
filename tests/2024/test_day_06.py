from advent_of_code.lab_maze import LabMaze


def test_part_one() -> None:
    maze = LabMaze("2024/day-6.test.txt")
    assert maze.walk() == 41


def test_part_two() -> None:
    maze = LabMaze("2024/day-6.test.txt")
    assert maze.count_loops() == 6
