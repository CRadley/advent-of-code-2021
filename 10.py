from statistics import median

with open('inputs/10.txt', 'r') as f:
    complete = [line.strip() for line in f.readlines()]
values = {
    ')': 3,
    '>': 25137,
    '}': 1197,
    ']': 57
}
total = 0
for line in complete:
    stack = []
    for c in line:
        if c in ('(', '<', '{', '['):
            stack.append(c)
        else:
            last_opened = stack.pop()
            if last_opened == '(' and c != ')':
                total += values[c]
                break
            elif last_opened == '<' and c != '>':
                total += values[c]
                break
            elif last_opened == '{' and c != '}':
                total += values[c]
                break
            elif last_opened == '[' and c != ']':
                total += values[c]
                break
print(total)
opp = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

totals = []
for line in complete:
    corrupted = False
    stack = []
    for c in line:
        if corrupted:
            break
        if c in ('(', '<', '{', '['):
            stack.append(c)
        else:
            last_opened = stack.pop()
            if last_opened == '(' and c != ')':
                total += values[c]
                corrupted = True
            elif last_opened == '<' and c != '>':
                total += values[c]
                corrupted = True
            elif last_opened == '{' and c != '}':
                total += values[c]
                corrupted = True
            elif last_opened == '[' and c != ']':
                total += values[c]
                corrupted = True
    if corrupted:
        continue
    total = 0
    for s in stack[::-1]:
        total *= 5
        total += list(opp.values()).index(opp[s]) + 1

    totals.append(total)

print(median(totals))
