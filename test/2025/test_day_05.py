from advent_of_code.kitchen_inventory import KitchenInventory


def test_part_one() -> None:
    inventory = KitchenInventory("2025/day-5.test.txt")
    assert inventory.n_available_fresh() == 3


def test_part_two() -> None:
    inventory = KitchenInventory("2025/day-5.test.txt")
    assert inventory.n_known_fresh() == 14
