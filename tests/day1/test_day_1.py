from typing import List
import pytest

from aoc.day1 import (
    part_one,
    part_two
)

from aoc.utils import file_as_int_list

@pytest.fixture
def example_depths() -> List[int]:
    return file_as_int_list("tests/resources/day1/example.txt")


@pytest.fixture
def depths() -> List[int]:
    return file_as_int_list("tests/resources/day1/input.txt")


def test_part_one_example(example_depths: List[int]) -> None:
    assert 7 == part_one(example_depths)

def test_part_two_example(example_depths: List[int]) -> None:
    assert 5 == part_two(example_depths)

def test_part_one_actual(depths: List[int]) -> None:
    assert 1754 == part_one(depths)

def test_part_two_actual(depths: List[int]) -> None:
    assert 1789 == part_two(depths)
