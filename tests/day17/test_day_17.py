from typing import List
import pytest

from aoc.day17 import (
    part_one,
    part_two,
    determine_inputs,
)

@pytest.fixture
def example_area() -> List[int]:
    return determine_inputs("tests/resources/day17/example.txt")


@pytest.fixture
def area() -> List[int]:
    return determine_inputs("tests/resources/day17/input.txt")


def test_part_one_example(example_area) -> None:
    _, _, y1, y2 = example_area
    assert 45 == part_one(y1, y2)

def test_part_two_example(example_area: List[int]) -> None:
    x1, x2, y1, y2 = example_area
    assert 112 == part_two(x1, y1, x2, y2)

def test_part_one_actual(area) -> None:
    _, _, y1, y2 = area
    assert 6441 == part_one(y1, y2)

def test_part_two_actual(area) -> None:
    x1, x2, y1, y2 = area
    assert 3186 == part_two(x1, y1, x2, y2)
