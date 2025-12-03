from advent_of_code.data_loaders import load_file_as_lines


class BatteryBankArray:
    def __init__(self, filename: str) -> None:
        self.banks = [BatteryBank(line) for line in load_file_as_lines(filename)]

    def largest_joltage(self) -> int:
        return sum(bank.largest_joltage() for bank in self.banks)


class BatteryBank:
    def __init__(self, digits: str) -> None:
        self.digits = [int(d) for d in digits.strip()]

    def largest_joltage(self) -> int:
        joltage = ""
        start, end = 0, len(self.digits) - 1
        for _ in range(2):
            idx, value = self.indexed_maximum(start, end)
            joltage += str(value)
            start, end = idx + 1, end + 1
        return int(joltage)

    def indexed_maximum(self, start: int, end: int) -> tuple[int, int]:
        largest_digit = max(self.digits[start:end])
        for idx in range(start, end):
            if self.digits[idx] == largest_digit:
                return (idx, largest_digit)
        raise ValueError
