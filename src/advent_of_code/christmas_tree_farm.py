from collections.abc import Sequence

import numpy as np

from advent_of_code.data_loaders import load_file_as_blocks
from advent_of_code.matrix import StrMatrix
from advent_of_code.utility import partition


class Present:
    def __init__(self, block: str) -> None:
        lines = block.splitlines()[1:]
        self.shape = StrMatrix(np.array([list(line) for line in lines]))
        self.n_filled = len(self.shape.find("#"))


class Region:
    def __init__(self, line: str) -> None:
        parts = line.split(": ")
        self.width, self.height = map(int, parts[0].split("x"))
        self.present_types = list(map(int, parts[1].split()))

    def easy_fit_possible(self) -> bool:
        """Check whether each present fits in its own 3x3 square."""
        return sum(self.present_types) <= (self.width // 3) * (self.height // 3)

    def no_fit_possible(self, presents: Sequence[Present]) -> bool:
        """Check whether the required area exceeds available area for this region."""
        required_area = sum(
            present.n_filled * number
            for present, number in zip(presents, self.present_types, strict=True)
        )
        return required_area > self.width * self.height


class ChristmasTreeFarm:
    def __init__(self, filename: str) -> None:
        blocks = load_file_as_blocks(filename)
        self.presents = [Present(block) for block in blocks[:-1]]
        self.regions = [Region(line) for line in blocks[-1].splitlines()]

    def n_valid_regions(self) -> int:
        """Use a simple heuristic to identify definitely valid/invalid regions."""
        unsure, _ = partition(lambda r: r.no_fit_possible(self.presents), self.regions)
        unsure, valid = partition(lambda r: r.easy_fit_possible(), unsure)
        if not unsure:
            return len(valid)
        msg = f"Found {len(valid)} valid regions, but {len(unsure)} regions remain."
        raise ValueError(msg)
