from typing import List
import pytest

from aoc.day12 import determine_cave_system

@pytest.fixture
def example_cave_system() -> List[int]:
    return determine_cave_system("tests/resources/day12/example.txt")


@pytest.fixture
def cave_system() -> List[int]:
    return determine_cave_system("tests/resources/day12/input.txt")


def test_part_one_example(example_cave_system: List[int]) -> None:
    assert 10 == example_cave_system.determine_standard_paths()

def test_part_two_example(example_cave_system: List[int]) -> None:
    assert 36 == example_cave_system.determine_extended_paths()

def test_part_one_actual(cave_system: List[int]) -> None:
    assert 5874 == cave_system.determine_standard_paths()

def test_part_two_actual(cave_system: List[int]) -> None:
    assert 153592 == cave_system.determine_extended_paths()
