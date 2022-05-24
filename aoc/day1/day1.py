from typing import List
from ..utils import file_as_int_list, display_solutions

def part_one(depths: List[int]) -> int:
    return len([i for i, y in enumerate(depths) if y > depths[i-1] and i])

def part_two(depths: List[int]) -> int:
    return part_one([sum(depths[i:i+3]) for i, _ in enumerate(depths) if i < len(depths) - 2])
