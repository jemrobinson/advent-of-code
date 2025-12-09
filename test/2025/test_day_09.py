from advent_of_code.movie_theatre import MovieTheatre


def test_part_one() -> None:
    theatre = MovieTheatre("2025/day-9.test.txt")
    assert theatre.largest_rectangle() == 50
