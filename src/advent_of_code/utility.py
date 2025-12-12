from collections.abc import Callable, Sequence


def as_int(input_string: str) -> int:
    return int("".join([char for char in input_string if char.isdigit()]))


def count(substring: str, string: str) -> int:
    return sum(
        [
            1 if string[idx:].startswith(substring) else 0
            for idx in range(len(string) - len(substring) + 1)
        ]
    )


def partition[T](
    predicate: Callable[[T], bool], iterable: Sequence[T]
) -> tuple[list[T], list[T]]:
    """Partition `iterable` into (list-of-false, list-of-true) according to `predicate`."""
    results: tuple[list[T], list[T]] = ([], [])
    for item in iterable:
        results[predicate(item)].append(item)
    return results
