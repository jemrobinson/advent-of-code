from advent_of_code.toroidal_reactor import ToroidalReactor


def test_part_one() -> None:
    reactor = ToroidalReactor("2025/day-11.test.txt")
    assert reactor.n_paths() == 5
