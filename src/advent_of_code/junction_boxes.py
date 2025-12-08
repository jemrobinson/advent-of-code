from collections.abc import Iterator
from functools import reduce
from operator import mul

from advent_of_code.data_loaders import load_file_as_lines
from advent_of_code.disjoint_set import DisjointSet, SetElement


class JunctionBoxElement(SetElement):
    def __init__(self, position: Iterator[int]) -> None:
        super().__init__((next(position), next(position), next(position)))

    def distance(self, other: "JunctionBoxElement") -> int:
        return sum(abs(self.value[idx] - other.value[idx]) ** 2 for idx in range(3))


class JunctionBoxes:
    def __init__(self, filename: str) -> None:
        self.boxes = [
            JunctionBoxElement(map(int, line.split(",")))
            for line in load_file_as_lines(filename)
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
        """Use a modified Kruskal's algorithm, terminating when all boxes are connected.

        Note that this is slower than the original implementation since we check the
        number of roots at each iteration.
        """
        for box_i, box_j in self.closest_pairs:
            self.box_set.union(box_i, box_j)
            if len(self.box_set.roots()) == 1:
                return int(box_i.value[0]) * int(box_j.value[0])
        raise RuntimeError

    def largest_circuits(self, n_connections: int = 10) -> int:
        for box_i, box_j in self.closest_pairs[:n_connections]:
            self.box_set.union(box_i, box_j)
        circuit_sizes = [len(children) for children in self.box_set.children().values()]
        return reduce(mul, sorted(circuit_sizes, reverse=True)[:3], 1)
