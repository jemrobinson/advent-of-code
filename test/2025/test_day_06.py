from advent_of_code.maths_worksheet import MathsWorksheet


def test_part_one() -> None:
    worksheet = MathsWorksheet("2025/day-6.test.txt")
    assert worksheet.calculate_column_totals() == 4277556
