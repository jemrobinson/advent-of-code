from advent_of_code.kitchen_inventory import KitchenInventory


def test_part_one() -> None:
    inventory = KitchenInventory("2025/day-5.test.txt")
    assert inventory.n_fresh_ingredients() == 3
