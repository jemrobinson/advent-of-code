from advent_of_code.data_loaders import load_file_as_lines


class BatteryBankArray:
    def __init__(self, filename: str) -> None:
        self.banks = [BatteryBank(line) for line in load_file_as_lines(filename)]

    def largest_joltage(self, n_batteries: int) -> int:
        return sum(bank.largest_joltage(n_batteries) for bank in self.banks)


class BatteryBank:
    def __init__(self, digits: str) -> None:
        self.digits = [int(d) for d in digits.strip()]

    def largest_joltage(self, n_batteries: int) -> int:
        joltage = 0
        start, end = 0, len(self.digits) + 1 - n_batteries
        for _ in range(n_batteries):
            idx, value = self.indexed_maximum(start, end)
            joltage = 10 * joltage + value
            start, end = idx + 1, end + 1
        return joltage

    def indexed_maximum(self, start: int, end: int) -> tuple[int, int]:
        idx_max = max(range(start, end), key=self.digits.__getitem__)
        return (idx_max, self.digits[idx_max])
