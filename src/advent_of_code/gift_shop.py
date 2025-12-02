from functools import partial
from itertools import chain

from advent_of_code.data_loaders import load_file_as_string


class GiftShop:
    def __init__(self, filename: str) -> None:
        self.project_ids = chain.from_iterable(
            range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1)
            for id_range in load_file_as_string(filename).split(",")
        )

    def invalid_ids_repeat_twice(self) -> int:
        return sum(filter(partial(self.is_invalid, n_repeats=2), self.project_ids))

    def invalid_ids_repeat_any(self) -> int:
        return sum(filter(self.is_invalid, self.project_ids))

    def is_invalid(self, product_id: int, n_repeats: int = -1) -> bool:
        s_product_id = str(product_id)
        s_product_id_length = len(s_product_id)
        for substring_length in range(1, s_product_id_length // 2 + 1):
            substring = s_product_id[:substring_length]
            if s_product_id_length % substring_length != 0:
                continue
            repeats = s_product_id_length // substring_length
            if n_repeats in (-1, repeats) and (substring * repeats == s_product_id):
                return True
        return False
