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

    def n_paths_you(self) -> int:
        return self.graph.count_paths(self.nodes["you"], self.nodes["out"])

    def n_paths_server(self) -> int:
        # Get nodes
        n_svr = self.nodes["svr"]
        n_dac = self.nodes["dac"]
        n_fft = self.nodes["fft"]
        n_out = self.nodes["out"]
        n_svr_dac = self.graph.count_paths(n_svr, n_dac)
        n_dac_fft = self.graph.count_paths(n_dac, n_fft)
        n_fft_out = self.graph.count_paths(n_fft, n_out)
        # n_svr -> n_fft -> n_dac -> n_out
        n_svr_fft = self.graph.count_paths(n_svr, n_fft)
        n_fft_dac = self.graph.count_paths(n_fft, n_dac)
        n_dac_out = self.graph.count_paths(n_dac, n_out)
        return n_svr_dac * n_dac_fft * n_fft_out + n_svr_fft * n_fft_dac * n_dac_out
