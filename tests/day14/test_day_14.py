from typing import List
import pytest

from aoc.day14 import (
    determine_polymer,
    read_file,
    optimised_determine_polymer
)

@pytest.fixture
def example_di() -> List[int]:
    return read_file("tests/resources/day14/example.txt")


@pytest.fixture
def di() -> List[int]:
    return read_file("tests/resources/day14/input.txt")


def test_determine_polymer_10_steps_example(example_di) -> None:
    polymer_template, insertertion_rules = example_di
    assert 1588 == determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_10_steps_example(example_di) -> None:
    polymer_template, insertertion_rules = example_di
    assert 1588 == optimised_determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_40_steps_example(example_di) -> None:
    polymer_template, insertertion_rules = example_di
    assert 2188189693529 == optimised_determine_polymer(polymer_template, insertertion_rules, 40)


def test_determine_polymer_10_steps(di) -> None:
    polymer_template, insertertion_rules = di
    assert 2435 == determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_10_steps(di) -> None:
    polymer_template, insertertion_rules = di
    assert 2435 == optimised_determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_40_steps(di) -> None:
    polymer_template, insertertion_rules = di
    assert 2587447599164 == optimised_determine_polymer(polymer_template, insertertion_rules, 40)