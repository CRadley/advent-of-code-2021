from functools import lru_cache

@lru_cache(maxsize=None)
def determine_fish_generated(age, days):
    remaining = days - age
    if remaining < 0:
        return 0
    return sum([determine_fish_generated(8, day - 1) + 1 for day in range(remaining, 0, -7)])

def solve(fish, days):
    return sum([determine_fish_generated(f, days) for f in fish]) + len(fish)

def get_lanternfish(filepath):
    with open(filepath, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]
