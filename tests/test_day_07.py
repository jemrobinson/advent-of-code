from advent_of_code.calibration import CalibrationFull, CalibrationSimple
from advent_of_code.data_loaders import load_file_as_lines


def test_part_one() -> None:
    calibrations = [
        CalibrationSimple(line) for line in load_file_as_lines("day-7.test.txt")
    ]
    assert (
        sum(
            [
                calibration.output
                for calibration in calibrations
                if calibration.is_valid()
            ]
        )
        == 3749
    )


def test_part_two() -> None:
    calibrations = [
        CalibrationFull(line) for line in load_file_as_lines("day-7.test.txt")
    ]
    assert (
        sum(
            [
                calibration.output
                for calibration in calibrations
                if calibration.is_valid()
            ]
        )
        == 11387
    )
