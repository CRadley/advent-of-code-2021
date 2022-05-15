from utils import display_solutions

def determine_points(start, end, start_, end_):
    return range(int(start), int(end) - 1 if int(start) > int(end) else int(end) if start == end else int(end) + 1, -1 if int(start) > int(end) else 1) or [int(start)] * (abs(int(start_) - int(end_)) + 1) 

def solve(points, diagonal):
    points_hit = {}
    for point in points:
        x1, y1 = point[0].split(',')
        x2, y2 = point[1].split(',')
        if not diagonal and (x1 != x2 and y1 != y2):
            continue
        y_r = determine_points(y1, y2, x1, x2)
        x_r = determine_points(x1, x2, y1, y2)
        for x, y in zip(x_r, y_r):
            if f'{x},{y}' not in points_hit:
                points_hit[f'{x},{y}'] = 0
            points_hit[f'{x},{y}'] += 1
    return len([v for v in points_hit.values() if v > 1])

def main():
    with open('./inputs/5.txt', 'r') as f:
        points = [line.split(' -> ') for line in f.read().split('\n')]
    display_solutions(solve(points, False), solve(points, True))

if __name__ == '__main__':
    main()