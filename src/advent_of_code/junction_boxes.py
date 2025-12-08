from functools import reduce
from operator import mul

from advent_of_code.data_loaders import load_file_as_lines
from advent_of_code.disjoint_set import DisjointSet, SetElement


class JunctionBoxElement(SetElement):
    def __init__(self, position: tuple[int, int, int]) -> None:
        super().__init__(position)

    def distance(self, other: "JunctionBoxElement") -> int:
        return sum(abs(self.value[idx] - other.value[idx]) ** 2 for idx in range(3))


class JunctionBoxes:
    def __init__(self, filename: str) -> None:
        box_positions = [
            list(map(int, line.split(","))) for line in load_file_as_lines(filename)
        ]
        self.boxes = [
            JunctionBoxElement(box_position) for box_position in box_positions
        ]
        distances = {
            (box_i, box_j): box_i.distance(box_j)
            for idx, box_i in enumerate(self.boxes)
            for box_j in self.boxes[idx + 1 :]
        }
        self.closest_pairs = [
            boxes for boxes, _ in sorted(distances.items(), key=lambda item: item[1])
        ]
        self.box_set = DisjointSet(self.boxes)

    def fully_connected(self) -> int:
        for box_i, box_j in self.closest_pairs:
            self.box_set.union(box_i, box_j)
            if len(self.box_set.roots()) == 1:
                return box_i.value[0] * box_j.value[0]
        raise RuntimeError

    def largest_circuits(self, n_connections: int = 10) -> int:
        for box_i, box_j in self.closest_pairs[:n_connections]:
            self.box_set.union(box_i, box_j)
        circuit_sizes = [len(children) for children in self.box_set.children().values()]
        return reduce(mul, sorted(circuit_sizes, reverse=True)[:3], 1)
