from advent_of_code.gift_shop import GiftShop


def test_part_one() -> None:
    shop = GiftShop("2025/day-2.test.txt")
    assert shop.invalid_ids_repeat_twice() == 1227775554


def test_part_two() -> None:
    shop = GiftShop("2025/day-2.test.txt")
    assert shop.invalid_ids_repeat_any() == 4174379265
