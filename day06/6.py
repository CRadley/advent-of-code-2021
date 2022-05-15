from functools import lru_cache
from utils import display_solutions

@lru_cache(maxsize=None)
def determine_fish_generated(age, days):
    remaining = days - age
    if remaining < 0:
        return 0
    return sum([determine_fish_generated(8, day - 1) + 1 for day in range(remaining, 0, -7)])

def solve(fish, days):
    return sum([determine_fish_generated(f, days) for f in fish]) + len(fish)

def main():
    with open('./inputs/6.txt', 'r') as f:
        lanternfish = [int(x) for x in f.read().split(',')]
    display_solutions(solve(lanternfish, 80), solve(lanternfish, 256))

if __name__ == "__main__":
    main()