from collections import defaultdict

def is_diagonal(x1, y1, x2, y2):
    return x1 != x2 and y1 != y2

def detemine_points(start, end, start_, end_):
    if start == end:
        return [int(start)] * (abs(int(start_) - int(end_)) + 1)
    step = -1 if int(start) > int(end) else 1
    return list(range(int(start), int(end) + step, step))

def determine_coords(x1, y1, x2, y2):
    x_points = detemine_points(x1, x2, y1, y2)
    y_points = detemine_points(y1, y2, x1, x2)
    return zip(x_points, y_points)

def determine_endpoints(line):
    line = line.split(" -> ")
    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')
    return x1, y1, x2, y2

def solve(lines, ignore_diagonal):
    points_hit = defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = line
        if ignore_diagonal and is_diagonal(x1, y1, x2, y2):
            continue
        for x, y in determine_coords(x1, y1, x2, y2):
            points_hit[f"{x},{y}"] += 1
    return len([v for v in points_hit.values() if v > 1])

def determine_inputs(filepath):
    with open(filepath, 'r') as f:
        return [determine_endpoints(line) for line in f.read().split('\n')]
