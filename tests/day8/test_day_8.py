from typing import List
import pytest

from aoc.day8 import (
    part_one,
    part_two,
    get_display_outputs,
)

@pytest.fixture
def example_display_outputs() -> List[int]:
    return get_display_outputs("tests/resources/day8/example.txt")


@pytest.fixture
def display_outputs() -> List[int]:
    return get_display_outputs("tests/resources/day8/input.txt")


def test_part_one_example(example_display_outputs: List[int]) -> None:
    assert 26 == part_one(example_display_outputs)

def test_part_two_example(example_display_outputs: List[int]) -> None:
    assert 61229 == part_two(example_display_outputs)

def test_part_one_actual(display_outputs: List[int]) -> None:
    assert 321 == part_one(display_outputs)

def test_part_two_actual(display_outputs: List[int]) -> None:
    # This one takes a while
    assert 1028926 == part_two(display_outputs)
