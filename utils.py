from typing import List

def file_as_int_list(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        return [int(line) for line in f.readlines()]

def display_solutions(solution_one: int, solution_two: int) -> None:
    print(f'Solution 1: {solution_one}\nSolution 2: {solution_two}')