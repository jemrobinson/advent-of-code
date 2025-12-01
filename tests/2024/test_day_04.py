from advent_of_code.wordsearch import WordSearch, WordSearchSimple


def test_part_one() -> None:
    wordsearch = WordSearchSimple("2024/day-4.test.txt")
    assert wordsearch.search("XMAS") == 18


def test_part_two() -> None:
    wordsearch = WordSearch("2024/day-4.test.txt")
    assert wordsearch.search_xmas() == 9
