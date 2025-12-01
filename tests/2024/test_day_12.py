from advent_of_code.plant_regions import GardenPlot


def test_part_one() -> None:
    plot_0 = GardenPlot("2024/day-12.test-0.txt")
    assert plot_0.price() == 140
    plot_1 = GardenPlot("2024/day-12.test-1.txt")
    assert plot_1.price() == 772
    plot_2 = GardenPlot("2024/day-12.test-2.txt")
    assert plot_2.price() == 1930


def test_part_two() -> None:
    plot_0 = GardenPlot("2024/day-12.test-0.txt")
    assert plot_0.price_discounted() == 80
    plot_1 = GardenPlot("2024/day-12.test-1.txt")
    assert plot_1.price_discounted() == 436
    plot_2 = GardenPlot("2024/day-12.test-2.txt")
    assert plot_2.price_discounted() == 1206
    plot_3 = GardenPlot("2024/day-12.test-3.txt")
    assert plot_3.price_discounted() == 236
    plot_4 = GardenPlot("2024/day-12.test-4.txt")
    assert plot_4.price_discounted() == 368
