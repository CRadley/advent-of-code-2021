from typing import List
import pytest

from aoc.day6 import (
    solve,
    get_lanternfish,
)

@pytest.fixture
def example_lanternfish() -> List[int]:
    return get_lanternfish("tests/resources/day6/example.txt")


@pytest.fixture
def lanternfish() -> List[int]:
    return get_lanternfish("tests/resources/day6/input.txt")


def test_part_one_example(example_lanternfish: List[int]) -> None:
    assert 5934 == solve(example_lanternfish, 80)

def test_part_two_example(example_lanternfish: List[int]) -> None:
    assert 26984457539 == solve(example_lanternfish, 256)

def test_part_one_actual(lanternfish: List[int]) -> None:
    assert 362666 == solve(lanternfish, 80)

def test_part_two_actual(lanternfish: List[int]) -> None:
    assert 1640526601595 == solve(lanternfish, 256)
