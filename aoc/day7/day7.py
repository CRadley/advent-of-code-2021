def part_one(crabs):
    v = None
    for i in range(max(crabs) + 1):
        d = sum([abs(crab - i) for crab in crabs])
        if not v or d < v:
            v = d
    return v

def part_two(crabs):
    v = None
    for i in range(max(crabs) + 1):
        d = sum([sum(range(abs(crab - i) + 1)) for crab in crabs])
        if not v or d < v:
            v = d
    return v

def get_crabs(filepath):
    with open(filepath, 'r') as f:
        return [int(x.strip()) for x in f.read().split(',')]