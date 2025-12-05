from collections.abc import Iterable, Iterator


class InclusiveRange:
    def __init__(self, start: float | str, end: float | str) -> None:
        self.start = int(start)
        self.end = int(end)
        self._range = range(self.start, self.end + 1)

    def __add__(self, other: "InclusiveRange") -> "InclusiveRange":
        """Combine two ranges if they overlap."""
        if not self.overlaps(other):
            raise ValueError
        return InclusiveRange(min(self.start, other.start), max(self.end, other.end))

    def __iter__(self) -> Iterator[int]:
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

    def overlaps(self, other: "InclusiveRange") -> bool:
        """Return True if ranges overlap."""
        return (self.contains(other.start) or self.contains(other.end)) or (
            other.contains(self.start) or other.contains(self.end)
        )


class DisjointRanges:
    def __init__(self, *ranges: InclusiveRange) -> None:
        self.ranges = self.simplify(ranges)

    def simplify(self, ranges: Iterable[InclusiveRange]) -> list[InclusiveRange]:
        simplified_ranges: list[InclusiveRange] = []
        for range_ in sorted(ranges, key=lambda r: r.start):
            if simplified_ranges and range_.overlaps(simplified_ranges[-1]):
                simplified_ranges[-1] = range_ + simplified_ranges[-1]
            else:
                simplified_ranges.append(range_)
        return simplified_ranges

    def __len__(self) -> int:
        """Return total number of distinct entries across all ranges."""
        return sum(len(r) for r in self.ranges)

    def contains(self, number: int) -> bool:
        return any(r.contains(number) for r in self.ranges)
