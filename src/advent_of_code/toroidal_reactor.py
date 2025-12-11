from advent_of_code.data_loaders import load_file_as_lines
from advent_of_code.graph import Graph, Node


class DeviceNode(Node):
    def __init__(self, label: str) -> None:
        super().__init__(value=label)


class ToroidalReactor:
    def __init__(self, filename: str) -> None:
        self.graph = Graph()
        self.nodes: dict[str, DeviceNode] = {}
        for line in load_file_as_lines(filename):
            source = line.split(": ")[0]
            targets = line.split(": ")[1].split()
            if source not in self.nodes:
                self.nodes[source] = DeviceNode(source)
            for target in targets:
                if target not in self.nodes:
                    self.nodes[target] = DeviceNode(target)
                self.graph.add_edge(self.nodes[source], self.nodes[target], 1)

    def n_paths(self) -> int:
        return self.graph.count_paths(self.nodes["you"], self.nodes["out"])
