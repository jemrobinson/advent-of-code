from advent_of_code.data_loaders import load_file_as_blocks
from advent_of_code.inclusive_range import DisjointRanges, InclusiveRange


class KitchenInventory:
    def __init__(self, filename: str) -> None:
        range_block, id_block = load_file_as_blocks(filename)
        self.ranges = DisjointRanges(
            InclusiveRange(*range_.strip().split("-"))
            for range_ in range_block.split("\n")
        )
        self.ids = [int(id_.strip()) for id_ in id_block.split("\n")]

    def n_available_fresh(self) -> int:
        return sum(1 for id_ in self.ids if self.ranges.contains(id_))

    def n_known_fresh(self) -> int:
        return len(self.ranges)
