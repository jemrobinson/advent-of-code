from advent_of_code.data_loaders import load_file_as_lines


class RotatingDial:
    def __init__(self, filename: str) -> None:
        self.instructions = [
            int(line[1:].strip()) * (-1 if line.startswith("L") else 1)
            for line in load_file_as_lines(filename)
        ]
        self.start = 50

    def count_zeros(self) -> int:
        return sum(1 for pos in self.get_positions() if pos == 0)

    def count_all_zeros(self) -> int:
        zeros = 0
        position = self.start
        for instr in self.instructions:
            sign = 1 if instr > 0 else -1
            for _ in range(abs(instr)):
                position = (position + sign) % 100
                if position == 0:
                    zeros += 1
        return zeros

    def get_positions(self) -> list[int]:
        positions = [self.start]
        for instr in self.instructions:
            positions.append((positions[-1] + instr) % 100)
        return positions
