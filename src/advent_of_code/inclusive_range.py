from collections.abc import Sequence


class InclusiveRange:
    def __init__(self, start: float | str, end: float | str) -> None:
        self.start = int(start)
        self.end = int(end)
        self._range = range(self.start, self.end + 1)

    def __iter__(self) -> "InclusiveRange":
        """Return iterator over range."""
        return iter(self._range)

    def __len__(self) -> int:
        """Return length of range."""
        return self.end - self.start + 1

    def __next__(self) -> int:
        """Return next value in range."""
        return next(self)

    def __str__(self) -> str:
        """Return string representation."""
        return f"InclusiveRange({self.start}, {self.end})"

    def contains(self, number: int) -> bool:
        return self.start <= number <= self.end


class DisjointRanges:
    def __init__(self, ranges: Sequence[InclusiveRange]) -> None:
        self.ranges = list(ranges)

    def contains(self, number: int) -> bool:
        return any(r.contains(number) for r in self.ranges)
