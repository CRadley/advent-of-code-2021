import re

def in_area(x, y, a_x1, a_y1, a_x2, a_y2):
    return (a_x1 <= x and x <= a_x2) and (a_y1 <= y and y <= a_y2)

def missed_area(x, y, a_x2, a_y1):
    return x > a_x2 or y < a_y1


def is_correct_initial(x_vel, y_vel, a_x1, a_y1, a_x2, a_y2):
    x = 0
    y = 0
    while True:
        x += x_vel
        y += y_vel
        if in_area(x, y, a_x1, a_y1, a_x2, a_y2):
            return True
        if missed_area(x, y, a_x2, a_y1):
            return False
        y_vel -= 1
        if x_vel > 0:
            x_vel -= 1

def part_one(y1, y2):
    y = min(y1, y2)
    return sum(range(0, abs(y)))


def part_two(x1, y1, x2, y2):
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    z = set([(x, y) for x in range(x_max + 1) for y in range(abs(y_min) + 1, y_min -1, -1) if is_correct_initial(x, y, x1, y1, x2, y2)])
    return len(z)

def determine_inputs(filepath):
    with open(filepath, "r") as input_file:
        search = re.search(r"target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)", input_file.read())
        return map(int, search.groups())
