from advent_of_code_2024.pushdown_maze import PushdownMaze


def test_part_one() -> None:
    maze = PushdownMaze("day-18.test.txt", coordinate_max=6)
    assert maze.shortest_path(12) == 22


def test_part_two() -> None:
    maze = PushdownMaze("day-18.test.txt", coordinate_max=6)
    assert maze.first_blocked_path() == (6, 1)
