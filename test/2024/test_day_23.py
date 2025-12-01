from advent_of_code.lan_party import LanParty


def test_part_one() -> None:
    party = LanParty("2024/day-23.test.txt")
    assert party.count_triples_with_ts() == 7


def test_part_two() -> None:
    party = LanParty("2024/day-23.test.txt")
    assert party.find_password() == "co,de,ka,ta"
