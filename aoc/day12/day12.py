from .cave import Cave
from .cave_system import CaveSystem


def determine_cave_system(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip().split("-") for line in file.readlines()]
    caves = []
    for line in lines:
        cave = next((cave for cave in caves if cave.name == line[0]), None)
        if not cave:
            cave = Cave(line[0])
            caves.append(cave)
        cave.add_corridor(line[1])
        cave = next((cave for cave in caves if cave.name == line[1]), None)
        if not cave:
            cave = Cave(line[1])
            caves.append(cave)
        cave.add_corridor(line[0])
    cs = CaveSystem()
    cs.add_caves(caves)
    return cs