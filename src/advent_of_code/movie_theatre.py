from itertools import combinations

from advent_of_code.data_loaders import load_file_as_lines


class MovieTheatre:
    def __init__(self, filename: str) -> None:
        self.tile_positions = [
            tuple(map(int, line.split(","))) for line in load_file_as_lines(filename)
        ]

    def largest_rectangle(self) -> int:
        max_area = 0
        for tile_1, tile_2 in combinations(self.tile_positions, 2):
            area = (abs(tile_2[0] - tile_1[0]) + 1) * (abs(tile_2[1] - tile_1[1]) + 1)
            max_area = max(max_area, area)
        return max_area
