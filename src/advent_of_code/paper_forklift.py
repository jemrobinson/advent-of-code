from advent_of_code.data_loaders import load_file_as_array
from advent_of_code.grid_location import GridLocation
from advent_of_code.matrix import StrMatrix


class PaperForklift:
    def __init__(self, filename: str) -> None:
        self.grid = StrMatrix(load_file_as_array(filename))

    def is_accessible(self, location: GridLocation, max_adjacent: int) -> bool:
        if not self.grid.contains(location):
            return False
        if self.grid.get(location) != "@":
            return False
        adjacent_paper = [
            self.grid.get(neighbour) == "@"
            for neighbour in location.neighbours_all()
            if self.grid.contains(neighbour)
        ]
        return sum(adjacent_paper) < max_adjacent

    def accessible_rolls(self) -> int:
        return sum(
            self.is_accessible(location, 4) for location in self.grid.locations()
        )

    def accessible_rolls_with_removal(self) -> int:
        accessed, accessible = 0, []
        while True:
            accessible = [
                location
                for location in self.grid.locations()
                if self.is_accessible(location, 4)
            ]
            if accessible:
                accessed += len(accessible)
                for location in accessible:
                    self.grid.set(location, ".")
            else:
                return accessed
