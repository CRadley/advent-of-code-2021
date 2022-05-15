from typing import List
import pytest

from aoc.day2 import (
    part_one,
    part_two
)

from aoc.utils import file_as_list

@pytest.fixture
def example_instructions() -> List[int]:
    return file_as_list("tests/resources/day2/example.txt")


@pytest.fixture
def instructions() -> List[int]:
    return file_as_list("tests/resources/day2/input.txt")


def test_part_one_example(example_instructions: List[int]) -> None:
    assert 150 == part_one(example_instructions)

def test_part_two_example(example_instructions: List[int]) -> None:
    assert 900 == part_two(example_instructions)

def test_part_one_actual(instructions: List[int]) -> None:
    assert 1804520 == part_one(instructions)

def test_part_two_actual(instructions: List[int]) -> None:
    assert 1971095320 == part_two(instructions)
