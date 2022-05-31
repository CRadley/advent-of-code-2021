from typing import List
import pytest

from aoc.day5 import (
    solve,
    determine_inputs,
)

@pytest.fixture
def example_inputs() -> List[int]:
    return determine_inputs("tests/resources/day5/example.txt")


@pytest.fixture
def inputs() -> List[int]:
    return determine_inputs("tests/resources/day5/input.txt")


def test_part_one_example(example_inputs: List[int]) -> None:
    assert 5 == solve(example_inputs, True)

def test_part_two_example(example_inputs: List[int]) -> None:
    assert 12 == solve(example_inputs, False)

def test_part_one_actual(inputs: List[int]) -> None:
    assert 6572 == solve(inputs, True)

def test_part_two_actual(inputs: List[int]) -> None:
    assert 21466 == solve(inputs, False)
