from advent_of_code.indicator_lights import IndicatorLights


def test_part_one() -> None:
    indicators = IndicatorLights("2025/day-10.test.txt")
    assert indicators.fewest_presses() == 7
