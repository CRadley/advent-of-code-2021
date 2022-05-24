from typing import List
import pytest

from aoc.day11 import (
    part_one,
    part_two,
    get_octopi,
)

@pytest.fixture
def example_octopi() -> List[int]:
    return get_octopi("tests/resources/day11/example.txt")


@pytest.fixture
def octopi() -> List[int]:
    return get_octopi("tests/resources/day11/input.txt")


def test_part_one_example(example_octopi: List[int]) -> None:
    assert 1656 == part_one(example_octopi)

def test_part_two_example(example_octopi: List[int]) -> None:
    assert 195 == part_two(example_octopi)

def test_part_one_actual(octopi: List[int]) -> None:
    assert 1608 == part_one(octopi)

def test_part_two_actual(octopi: List[int]) -> None:
    assert 214 == part_two(octopi)
