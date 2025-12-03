from advent_of_code.battery_bank import BatteryBankArray


def test_part_one() -> None:
    battery = BatteryBankArray("2025/day-3.test.txt")
    assert battery.largest_joltage() == 357
