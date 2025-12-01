from advent_of_code_2024.lab_maze import LabMaze


def test_part_one() -> None:
    maze = LabMaze("day-6.test.txt")
    assert maze.walk() == 41


def test_part_two() -> None:
    maze = LabMaze("day-6.test.txt")
    assert maze.count_loops() == 6
