from functools import reduce
from itertools import pairwise
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


class WorksheetProblemReversed(WorksheetProblem):
    def __init__(self, numbers: list[str], operation: str) -> None:
        self.operation = operation
        self.numbers = [
            int("".join(number[column] for number in numbers))
            for column in range(len(numbers[0]))
        ]


class MathsWorksheet:
    def __init__(self, filename: str) -> None:
        lines = [line.replace("\n", "") for line in load_file_as_lines(filename)]
        max_width = max(len(line) for line in lines)
        column_starts = [
            idx for idx in range(len(lines[-1])) if lines[-1][idx] != " "
        ] + [max_width + 1]
        self.operations = lines[-1].split()
        self.number_groups = [
            [
                line.ljust(max_width)[column_start : column_end - 1]
                for line in lines[:-1]
            ]
            for column_start, column_end in pairwise(column_starts)
        ]

    def calculate_column_totals(self) -> int:
        return sum(
            WorksheetProblem(list(map(int, numbers)), operation).evaluate()
            for numbers, operation in zip(
                self.number_groups, self.operations, strict=True
            )
        )

    def calculate_reversed_column_totals(self) -> int:
        return sum(
            WorksheetProblemReversed(numbers, operation).evaluate()
            for numbers, operation in zip(
                self.number_groups, self.operations, strict=True
            )
        )
