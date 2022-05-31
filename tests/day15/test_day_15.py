from typing import List
import pytest

from aoc.day15 import (
    determine_inputs,
    generate_scaled_maze,
    scaled_astar
)

@pytest.fixture
def example() -> List[int]:
    return determine_inputs("tests/resources/day15/example.txt")

@pytest.fixture
def example_scaled() -> List[int]:
    return determine_inputs("tests/resources/day15/example_scaled.txt")

@pytest.fixture
def actual() -> List[int]:
    return determine_inputs("tests/resources/day15/input.txt")


def test_generate_scaled_maze(example, example_scaled) -> None:
    example_maze, example_resolution = example
    example_scaled_maze, example_scaled_resolution = example_scaled
    assert example_scaled_maze, example_scaled_resolution == generate_scaled_maze(example_maze, example_resolution, 5)

def test_part_one_example(example) -> None:
    maze, resolution = example
    assert 40 == scaled_astar(maze, resolution, 1)


def test_part_two_example(example) -> None:
    maze, resolution = example
    scale = 5
    assert 315 == scaled_astar(maze, resolution, scale)

def test_part_one_actual(actual) -> None:
    maze, resolution = actual
    scale = 1
    assert 390 == scaled_astar(maze, resolution, scale)

def test_part_two_actual(actual) -> None:
    maze, resolution = actual
    scale = 5
    assert 2814 == scaled_astar(maze, resolution, scale)