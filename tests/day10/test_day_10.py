from typing import List
import pytest

from aoc.day10 import (
    part_one,
    part_two,
    get_brackets,
)

@pytest.fixture
def example_brackets() -> List[int]:
    return get_brackets("tests/resources/day10/example.txt")


@pytest.fixture
def brackets() -> List[int]:
    return get_brackets("tests/resources/day10/input.txt")


def test_part_one_example(example_brackets: List[int]) -> None:
    assert 26397 == part_one(example_brackets)

def test_part_two_example(example_brackets: List[int]) -> None:
    assert 288957 == part_two(example_brackets)

def test_part_one_actual(brackets: List[int]) -> None:
    assert 436497 == part_one(brackets)

def test_part_two_actual(brackets: List[int]) -> None:
    assert 2377613374 == part_two(brackets)
