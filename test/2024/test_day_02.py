from advent_of_code.report import load_reports, load_reports_with_dampener


def test_part_one() -> None:
    reports = load_reports("2024/day-2.test.csv")
    assert sum([report.is_safe() for report in reports]) == 2


def test_part_two() -> None:
    reports = load_reports_with_dampener("2024/day-2.test.csv")
    assert sum([report.is_safe() for report in reports]) == 4
