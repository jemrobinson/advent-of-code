from advent_of_code.data_loaders import load_file_as_lines


class RotatingDial:
    def __init__(self, filename: str) -> None:
        self.instructions = [
            int(line[1:].strip()) * (-1 if line.startswith("L") else 1)
            for line in load_file_as_lines(filename)
        ]

    def count_zeros(self) -> int:
        return sum(1 for pos in self.get_positions() if pos == 0)

    def get_positions(self) -> list[int]:
        positions = [50]
        for instr in self.instructions:
            positions.append((positions[-1] + instr) % 100)
        return positions
