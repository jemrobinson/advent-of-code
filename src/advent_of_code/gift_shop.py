import re
from functools import partial
from itertools import chain

from advent_of_code.data_loaders import load_file_as_string
from advent_of_code.inclusive_range import InclusiveRange


class GiftShop:
    def __init__(self, filename: str) -> None:
        self.project_ids = chain.from_iterable(
            InclusiveRange(*id_range.split("-"))
            for id_range in load_file_as_string(filename).split(",")
        )

    def invalid_ids_repeat_twice(self) -> int:
        pattern = re.compile(r"^(\d+)\1$")
        return sum(filter(partial(self.is_invalid, pattern=pattern), self.project_ids))

    def invalid_ids_repeat_any(self) -> int:
        pattern = re.compile(r"^(\d+)\1+$")
        return sum(filter(partial(self.is_invalid, pattern=pattern), self.project_ids))

    def is_invalid(self, product_id: int, pattern: re.Pattern[str]) -> bool:
        return bool(pattern.match(str(product_id)))
