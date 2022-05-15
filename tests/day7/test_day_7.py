from typing import List
import pytest

from aoc.day7 import (
    part_one,
    part_two,
    get_crabs,
)

@pytest.fixture
def example_crabs() -> List[int]:
    return get_crabs("tests/resources/day7/example.txt")


@pytest.fixture
def crabs() -> List[int]:
    return get_crabs("tests/resources/day7/input.txt")


def test_part_one_example(example_crabs: List[int]) -> None:
    assert 37 == part_one(example_crabs)

def test_part_two_example(example_crabs: List[int]) -> None:
    assert 168 == part_two(example_crabs)

def test_part_one_actual(crabs: List[int]) -> None:
    assert 323647 == part_one(crabs)

def test_part_two_actual(crabs: List[int]) -> None:
    # This one takes a while
    assert 87640209 == part_two(crabs)
