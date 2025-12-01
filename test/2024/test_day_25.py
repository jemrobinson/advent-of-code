from advent_of_code.locks import LockKeyMatcher


def test_part_one() -> None:
    matcher = LockKeyMatcher("2024/day-25.test.txt")
    assert matcher.unique_pairs() == 3
