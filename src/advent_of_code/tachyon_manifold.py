from collections import defaultdict

from advent_of_code.data_loaders import load_file_as_array
from advent_of_code.grid_location import GridLocation
from advent_of_code.matrix import StrMatrix


class TachyonBeam:
    def __init__(self, location: GridLocation) -> None:
        self.location = location

    def __eq__(self, other: object) -> bool:
        """Equality operator for comparing two TachyonBeams."""
        if not isinstance(other, TachyonBeam):
            return False
        return bool(self.location == other.location)

    def __hash__(self) -> int:
        """Define hash of the TachyonBeam."""
        return hash(self.location)

    def move(self, grid: StrMatrix) -> list["TachyonBeam"]:
        if grid.get(self.location.south()) == "^":
            return [
                TachyonBeam(self.location.southeast()),
                TachyonBeam(self.location.southwest()),
            ]
        return [TachyonBeam(self.location.south())]


class TachyonManifold:
    def __init__(self, filename: str) -> None:
        self.grid = StrMatrix(load_file_as_array(filename))
        self.start = self.grid.find("S")[0]
        self.beams = {TachyonBeam(self.start): 1}

    def n_splits(self) -> int:
        n_splits = 0
        for _ in range(self.start.pos_0, self.grid.bounds()[0]):
            beams = [beam.move(self.grid) for beam in self.beams]
            splits = sum([len(beam_list) > 1 for beam_list in beams])
            self.beams = {beam: 1 for beam_list in beams for beam in beam_list}
            n_splits += splits
        return n_splits

    def n_timelines(self) -> int:
        for _ in range(self.start.pos_0, self.grid.bounds()[0]):
            new_beams: dict[TachyonBeam, int] = defaultdict(int)
            for beam, count in self.beams.items():
                for new_beam in beam.move(self.grid):
                    new_beams[new_beam] += count
            self.beams = new_beams
        return sum(self.beams.values())
