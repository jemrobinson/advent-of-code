from advent_of_code.reindeer_maze import ReindeerMaze


def test_part_one() -> None:
    maze_0 = ReindeerMaze("2024/day-16.test-0.txt")
    assert maze_0.shortest_path() == 7036
    maze_1 = ReindeerMaze("2024/day-16.test-1.txt")
    assert maze_1.shortest_path() == 11048


def test_part_two() -> None:
    maze_0 = ReindeerMaze("2024/day-16.test-0.txt")
    assert maze_0.best_seats() == 45
    maze_0 = ReindeerMaze("2024/day-16.test-1.txt")
    assert maze_0.best_seats() == 64
