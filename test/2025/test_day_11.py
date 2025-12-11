from advent_of_code.toroidal_reactor import ToroidalReactor


def test_part_one() -> None:
    reactor = ToroidalReactor("2025/day-11.test-1.txt")
    assert reactor.n_paths_you() == 5


def test_part_two() -> None:
    reactor = ToroidalReactor("2025/day-11.test-2.txt")
    assert reactor.n_paths_server() == 2
