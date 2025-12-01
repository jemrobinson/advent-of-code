"""Reusable decorators."""

import time
from collections.abc import Callable


def timed_solution[**P, R](
    day: int, part: int
) -> Callable[[Callable[P, R]], Callable[P, None]]:
    """Decorate solution with execution time."""

    def decorator(func: Callable[P, R]) -> Callable[P, None]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
            start = time.monotonic()
            result = func(*args, **kwargs)
            elapsed = time.monotonic() - start
            print(
                f"Day {day:02d} part {part}: {result} "
                f"completed in {elapsed:.3f} seconds.",
            )

        return wrapper

    return decorator
