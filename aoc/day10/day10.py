from statistics import median

def get_brackets(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f.readlines()]
VALUES = {')': 3, '>': 25137, '}': 1197, ']': 57}
OPP = {'(':')', '[':']', '{':'}', '<':'>'}

def part_one(complete):
    total = 0
    for line in complete:
        stack = []
        for c in line:
            if c in ('(', '<', '{', '['):
                stack.append(c)
                continue
            last_opened = stack.pop()
            if c != OPP[last_opened]:
                total += VALUES[c]
    return total

def part_two(complete):
    totals = []
    for line in complete:
        corrupted = False
        stack = []
        for c in line:
            if corrupted:
                break
            if c in ('(', '<', '{', '['):
                stack.append(c)
                continue
            else:
                last_opened = stack.pop()
                if c != OPP[last_opened]:
                    total += VALUES[c]
                    corrupted = True
        if corrupted:
            continue
        total = 0
        for s in stack[::-1]:
            total *= 5
            total += list(OPP.values()).index(OPP[s]) + 1

        totals.append(total)

    return median(totals)
