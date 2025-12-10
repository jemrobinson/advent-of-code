import re
from collections import deque

from advent_of_code.data_loaders import load_file_as_lines


class IndicatorLightMachine:
    def __init__(self, config: str) -> None:
        self.target = {m.start() - 1 for m in re.finditer("#", config)}
        self.buttons = tuple(
            {int(d) for d in group[1:-1].split(",")}
            for group in config.split(" ")[1:-1]
        )
        self.joltages = tuple(
            {int(d) for d in config.strip().split(" ")[-1][1:-1].split(",")}
        )

    def fewest_presses(self) -> int:
        queue: deque[tuple[set[int], int]] = deque()
        queue.append((frozenset(set()), 0))
        seen: set[frozenset[int]] = set()
        while queue:
            state, n_presses = queue.popleft()
            if state == self.target:
                return n_presses
            for button in self.buttons:
                new_state = frozenset(button.symmetric_difference(state))
                if new_state not in seen:
                    seen.add(new_state)
                    queue.append((new_state, n_presses + 1))
        raise RuntimeError


class IndicatorLights:
    def __init__(self, filename: str) -> None:
        lines = load_file_as_lines(filename)
        self.machines = [IndicatorLightMachine(line) for line in lines]

    def fewest_presses(self) -> int:
        return sum(machine.fewest_presses() for machine in self.machines)
