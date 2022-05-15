from typing import Tuple


def read_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        dots = []
        instructions = []
        for line in file.readlines():
            if line.startswith("fold"):
                instructions.append((line.split("=")[0][-1], int(line.split("=")[-1])))
            elif len(line) > 1:
                dots.append(tuple(map(int, line.strip().split(","))))
        return dots, instructions



dots, instructions = read_file("day13.txt")

for i in instructions:
    new_dots = []
    for dot in dots:
        if i[0] == "y" and dot[1] > i[1]:
            new_dots.append((dot[0], i[1] - (dot[1] - i[1])))
        elif i[0] == "x" and dot[0] > i[1]:
            new_dots.append((i[1] - (dot[0] - i[1]),dot[1]))
        else:
            new_dots.append(dot)

    dots = [d for d in list(set(new_dots))]

def display(dots):
    max_x = max(map(lambda x: x[0], dots))
    max_y = max(map(lambda x: x[1], dots))
    for y in range(max_y + 1):
        buffer = ""
        for x in range(max_x + 1):
            if (x, y) in dots:
                buffer += "#"
            else:
                buffer += "."
        print(buffer)
        
display(dots)