from advent_of_code.warehouse import LargeWarehouse, Warehouse


def test_part_one() -> None:
    warehouse_0 = Warehouse(
        "2024/day-15-moves.test-0.txt", "2024/day-15-warehouse.test-0.txt"
    )
    assert warehouse_0.score_gps() == 2028
    warehouse_1 = Warehouse(
        "2024/day-15-moves.test-1.txt", "2024/day-15-warehouse.test-1.txt"
    )
    assert warehouse_1.score_gps() == 10092


def test_part_two() -> None:
    warehouse_0 = LargeWarehouse(
        "2024/day-15-moves.test-0.txt", "2024/day-15-warehouse.test-0.txt"
    )
    assert warehouse_0.score_gps() == 1751
    warehouse_1 = LargeWarehouse(
        "2024/day-15-moves.test-1.txt", "2024/day-15-warehouse.test-1.txt"
    )
    assert warehouse_1.score_gps() == 9021
