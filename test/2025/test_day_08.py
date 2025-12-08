from advent_of_code.junction_boxes import JunctionBoxes


def test_part_one() -> None:
    boxes = JunctionBoxes("2025/day-8.test.txt")
    assert boxes.largest_circuits(10) == 40
