from advent_of_code.tachyon_manifold import TachyonManifold


def test_part_one() -> None:
    manifold = TachyonManifold("2025/day-7.test.txt")
    assert manifold.n_splits() == 21


def test_part_two() -> None:
    manifold = TachyonManifold("2025/day-7.test.txt")
    assert manifold.n_timelines() == 40
