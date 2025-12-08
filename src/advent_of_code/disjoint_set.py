from collections import defaultdict
from collections.abc import Sequence
from typing import Any


class SetElement:
    def __init__(self, value: Any) -> None:  # noqa: ANN401
        self.value = value


class DisjointSet:
    """Disjoint set / union-find data structure.

    Start with each element in its own set.
    """

    def __init__(self, elements: Sequence[SetElement]) -> None:
        self.parent = {element: element for element in elements}

    def make_set(self, element: SetElement) -> None:
        """Add a new element."""
        if element not in self.parent:
            self.parent[element] = element

    def find(self, element: SetElement) -> SetElement:
        """Use path compression to find the root of the set containing element."""
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def children(self) -> dict[SetElement, list[SetElement]]:
        """Return a dict of root elements to their children."""
        children = defaultdict(list)
        for box in self.parent:
            root = self.find(box)
            children[root].append(box)
        return children

    def roots(self) -> set[SetElement]:
        """Return the set of root elements."""
        return {self.find(element) for element in self.parent}

    def union(self, element1: SetElement, element2: SetElement) -> None:
        """Join the sets containing element1 and element2."""
        root1 = self.find(element1)
        root2 = self.find(element2)
        if root1 != root2:
            self.parent[root1] = root2
