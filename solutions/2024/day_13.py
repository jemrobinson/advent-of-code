#! /usr/bin/env python3
from advent_of_code.aoc_solution import timed_solution
from advent_of_code.claw_machine import get_claw_machines


@timed_solution(day=13, part=1)
def part_one() -> int:
    machines = get_claw_machines("2024/day-13.txt")
    solutions = [machine.solve(use_brute_force=True) for machine in machines]
    prizes = list(filter(None, solutions))
    return sum([prize[2] for prize in prizes])


@timed_solution(day=13, part=2)
def part_two() -> int:
    machines = get_claw_machines("2024/day-13.txt", offset=10000000000000)
    solutions = [machine.solve() for machine in machines]
    prizes = list(filter(None, solutions))
    return sum([prize[2] for prize in prizes])


if __name__ == "__main__":
    part_one()
    part_two()
