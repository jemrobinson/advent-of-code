from advent_of_code.file_system import FileSystem


def test_part_one() -> None:
    file_system = FileSystem("day-9.test.txt")
    assert file_system.checksum() == 1928


def test_part_two() -> None:
    file_system = FileSystem("day-9.test.txt")
    assert file_system.checksum(strategy="conservative") == 2858
