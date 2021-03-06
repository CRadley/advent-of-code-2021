from aoc.utils import file_as_list, display_solutions
from typing import List

def part_one(moves: List[str]) -> int:
    h = 0
    d = 0
    for move in moves:
        direction, value = move.split(' ')
        value = int(value)
        if direction == "forward":
            h += value
        elif direction == "up":
            d -= value
        else:
            d += value
    return h * d

def part_two(moves: List[str]) -> int:
    h = 0
    d = 0
    a = 0
    for move in moves:
        direction, value = move.split(' ')
        value = int(value)
        if direction == "forward":
            h += value
            d += a * value
        elif direction == "up":
            a -= value
        else:
            a += value
    return h * d
