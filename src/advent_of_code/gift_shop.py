from itertools import chain

from advent_of_code.data_loaders import load_file_as_string


class GiftShop:
    def __init__(self, filename: str) -> None:
        self.project_ids = chain.from_iterable(
            range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1)
            for id_range in load_file_as_string(filename).split(",")
        )

    def invalid_id_sum(self) -> int:
        return sum(filter(self.is_invalid, self.project_ids))

    def is_invalid(self, product_id: int) -> bool:
        s_product_id = str(product_id)
        if len(s_product_id) % 2 != 0:
            return False
        return (
            s_product_id[: len(s_product_id) // 2]
            == s_product_id[len(s_product_id) // 2 :]
        )
