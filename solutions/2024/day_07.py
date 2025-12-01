#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.calibration import CalibrationFull, CalibrationSimple
from advent_of_code.data_loaders import load_file_as_lines


@timed_solution(day=7, part=1)
def part_one() -> int:
    calibrations = [
        CalibrationSimple(line) for line in load_file_as_lines("2024/day-7.txt")
    ]
    return sum(
        [calibration.output for calibration in calibrations if calibration.is_valid()]
    )


@timed_solution(day=7, part=2)
def part_two() -> int:
    calibrations = [
        CalibrationFull(line) for line in load_file_as_lines("2024/day-7.txt")
    ]
    return sum(
        [calibration.output for calibration in calibrations if calibration.is_valid()]
    )


if __name__ == "__main__":
    part_one()
    part_two()
