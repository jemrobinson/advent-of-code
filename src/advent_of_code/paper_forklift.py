from advent_of_code.data_loaders import load_file_as_array
from advent_of_code.grid_location import GridLocation
from advent_of_code.matrix import StrMatrix


class PaperForklift:
    def __init__(self, filename: str) -> None:
        self.grid = StrMatrix(load_file_as_array(filename))

    def is_accessible(self, location: GridLocation, max_adjacent: int) -> bool:
        adjacent_paper = [
            self.grid.get(neighbour) == "@"
            for neighbour in location.neighbours_all()
            if self.grid.contains(neighbour)
        ]
        return sum(adjacent_paper) < max_adjacent

    def accessible_rolls(self) -> int:
        return sum(self.is_accessible(location, 4) for location in self.grid.find("@"))

    def accessible_rolls_with_removal(self) -> int:
        accessed = 0
        while True:
            accessed_this_pass = 0
            for location in self.grid.find("@"):
                if self.is_accessible(location, 4):
                    accessed_this_pass += 1
                    self.grid.set(location, ".")
            if accessed_this_pass:
                accessed += accessed_this_pass
            else:
                break
        return accessed
