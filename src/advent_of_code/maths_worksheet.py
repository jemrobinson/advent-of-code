from functools import reduce
from operator import mul

from advent_of_code.data_loaders import load_file_as_lines


class WorksheetProblem:
    def __init__(self, numbers: list[int], operation: str) -> None:
        self.numbers = numbers
        self.operation = operation

    def evaluate(self) -> int:
        if self.operation == "+":
            return sum(self.numbers)
        if self.operation == "*":
            return reduce(mul, self.numbers, 1)
        raise ValueError


class MathsWorksheet:
    def __init__(self, filename: str) -> None:
        lines = [line.strip() for line in load_file_as_lines(filename)]
        operations = lines[-1].split()
        numbers = [int(num) for line in lines[:-1] for num in line.split()]
        number_groups = [[] for _ in range(len(operations))]
        for idx, num in enumerate(numbers):
            number_groups[idx % len(operations)].append(num)
        self.problems = [
            WorksheetProblem(numbers, operation)
            for numbers, operation in zip(number_groups, operations, strict=True)
        ]

    def calculate_column_totals(self) -> int:
        return sum(problem.evaluate() for problem in self.problems)
