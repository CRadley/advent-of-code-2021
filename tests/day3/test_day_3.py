from typing import List
import pytest

from aoc.day3 import (
    part_one,
    part_two
)

from aoc.utils import file_as_list

@pytest.fixture
def example_binaries() -> List[int]:
    return file_as_list("tests/resources/day3/example.txt")


@pytest.fixture
def binaries() -> List[int]:
    return file_as_list("tests/resources/day3/input.txt")


def test_part_one_example(example_binaries: List[int]) -> None:
    assert 198 == part_one(example_binaries)

def test_part_two_example(example_binaries: List[int]) -> None:
    assert 230 == part_two(example_binaries)

def test_part_one_actual(binaries: List[int]) -> None:
    assert 3320834 == part_one(binaries)

def test_part_two_actual(binaries: List[int]) -> None:
    assert 4481199 == part_two(binaries)
