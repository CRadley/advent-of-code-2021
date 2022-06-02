from typing import List
import pytest

from aoc.day16 import (
    determine_input_binary,
    hex_to_binary,
    calculate_version_sum,
)

@pytest.fixture
def example_binary_1() -> List[int]:
    return hex_to_binary("8A004A801A8002F478")

@pytest.fixture
def example_binary_2() -> List[int]:
    return hex_to_binary("620080001611562C8802118E34")

@pytest.fixture
def example_binary_3() -> List[int]:
    return hex_to_binary("C0015000016115A2E0802F182340")

@pytest.fixture
def example_binary_4() -> List[int]:
    return hex_to_binary("A0016C880162017C3686B18A3D4780")


def test_example_binary_1_part_one(example_binary_1) -> List[int]:
    assert 16 == calculate_version_sum(example_binary_1)

def test_example_binary_2_part_one(example_binary_2) -> List[int]:
    assert 12 == calculate_version_sum(example_binary_2)

def test_example_binary_3_part_one(example_binary_3) -> List[int]:
    assert 13 == calculate_version_sum(example_binary_3)

def test_example_binary_4_part_one(example_binary_4) -> List[int]:
    assert 31 == calculate_version_sum(example_binary_4)