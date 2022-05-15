from typing import List
import pytest

from aoc.day4 import (
    part_one,
    part_two,
    determine_inputs,
)

@pytest.fixture
def example_inputs() -> List[int]:
    return determine_inputs("tests/resources/day4/example.txt")


@pytest.fixture
def inputs() -> List[int]:
    return determine_inputs("tests/resources/day4/input.txt")


def test_part_one_example(example_inputs: List[int]) -> None:
    draws, boards = example_inputs
    assert 4512 == part_one(draws, boards)

def test_part_two_example(example_inputs: List[int]) -> None:
    draws, boards = example_inputs
    assert 1924 == part_two(draws, boards)

def test_part_one_actual(inputs: List[int]) -> None:
    draws, boards = inputs
    assert 54275 == part_one(draws, boards)

def test_part_two_actual(inputs: List[int]) -> None:
    draws, boards = inputs
    assert 13158 == part_two(draws, boards)
