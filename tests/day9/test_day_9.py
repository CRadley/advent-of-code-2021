from typing import List
import pytest

from aoc.day9 import (
    part_one,
    part_two,
    get_width_and_rows,
)

@pytest.fixture
def example_wr() -> List[int]:
    return get_width_and_rows("tests/resources/day9/example.txt")


@pytest.fixture
def wr() -> List[int]:
    return get_width_and_rows("tests/resources/day9/input.txt")


def test_part_one_example(example_wr: List[int]) -> None:
    width, rows = example_wr
    assert 15 == part_one(width, rows)

def test_part_two_example(example_wr: List[int]) -> None:
    width, rows = example_wr
    assert 1134 == part_two(width, rows)

def test_part_one_actual(wr: List[int]) -> None:
    width, rows = wr
    assert 585 == part_one(width, rows)

def test_part_two_actual(wr: List[int]) -> None:
    width, rows = wr
    assert 827904 == part_two(width, rows)
