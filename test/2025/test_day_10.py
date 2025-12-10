from advent_of_code.indicator_lights import IndicatorLights


def test_part_one() -> None:
    indicators = IndicatorLights("2025/day-10.test.txt")
    assert indicators.fewest_presses_lights() == 7


def test_part_two() -> None:
    indicators = IndicatorLights("2025/day-10.test.txt")
    assert indicators.fewest_presses_joltages() == 33
