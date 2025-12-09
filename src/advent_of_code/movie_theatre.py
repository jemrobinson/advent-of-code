from itertools import combinations, pairwise

from advent_of_code.data_loaders import load_file_as_lines
from advent_of_code.grid_location import GridLocation


class MovieTheatre:
    def __init__(self, filename: str) -> None:
        self.red_tiles = [
            GridLocation(line.split(",")) for line in load_file_as_lines(filename)
        ]

    @classmethod
    def enclosed_area(cls, tile_1: GridLocation, tile_2: GridLocation) -> int:
        diff = tile_1 - tile_2
        return (abs(diff.pos_0) + 1) * (abs(diff.pos_1) + 1)

    def largest_rectangle(self) -> int:
        max_area = 0
        for tile_1, tile_2 in combinations(self.red_tiles, 2):
            area = self.enclosed_area(tile_1, tile_2)
            max_area = max(max_area, area)
        return max_area

    def is_box_enclosed(self, corner_1: GridLocation, corner_2: GridLocation) -> bool:
        """Check if the box is enclosed by each edge in turn.

        The box is enclosed if it is entirely on one side of the edge in either x or y.
        """
        bxmin, bxmax = (
            min(corner_1.pos_0, corner_2.pos_0),
            max(corner_1.pos_0, corner_2.pos_0),
        )
        bymin, bymax = (
            min(corner_1.pos_1, corner_2.pos_1),
            max(corner_1.pos_1, corner_2.pos_1),
        )
        for tile_1, tile_2 in pairwise(self.red_tiles):
            xs = (tile_1.pos_0, tile_2.pos_0)
            ys = (tile_1.pos_1, tile_2.pos_1)
            if not (
                max(xs) <= bxmin
                or bxmax <= min(xs)
                or max(ys) <= bymin
                or bymax <= min(ys)
            ):
                return False
        return True

    def largest_enclosed_rectangle(self) -> int:
        max_area = 0
        for tile_1, tile_2 in combinations(self.red_tiles, 2):
            area = self.enclosed_area(tile_1, tile_2)
            if area > max_area and self.is_box_enclosed(tile_1, tile_2):
                max_area = area
        return max_area
