from advent_of_code.topographic_map import TopographicMap


def test_part_one() -> None:
    topo_map = TopographicMap("day-10.test.txt")
    assert topo_map.score() == 36


def test_part_two() -> None:
    topo_map = TopographicMap("day-10.test.txt")
    assert topo_map.rating() == 81
