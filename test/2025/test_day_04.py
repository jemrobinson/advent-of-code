from advent_of_code.paper_forklift import PaperForklift


def test_part_one() -> None:
    forklift = PaperForklift("2025/day-4.test.txt")
    assert forklift.accessible_rolls() == 13


def test_part_two() -> None:
    forklift = PaperForklift("2025/day-4.test.txt")
    assert forklift.accessible_rolls_with_removal() == 43
