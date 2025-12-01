from advent_of_code.print_queue import PrintQueue


def test_part_one() -> None:
    queue = PrintQueue(
        rules_file="day-5.rules.test.csv", updates_file="day-5.updates.test.csv"
    )
    assert queue.score_ordered_updates() == 143


def test_part_two() -> None:
    queue = PrintQueue(
        rules_file="day-5.rules.test.csv", updates_file="day-5.updates.test.csv"
    )
    assert queue.score_unordered_updates() == 123
