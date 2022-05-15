from dataclasses import dataclass, field
from typing import List



@dataclass
class Cave:
    name: str
    corridors: List[str] = field(default_factory=lambda: [])

    @property
    def is_large(self) -> bool:
        return self.name.isupper()

    def add_corridor(self, corridor: str) -> None:
        self.corridors.append(corridor)

@dataclass
class CaveSystem:
    caves: List[Cave] = field(default_factory=lambda: [])
    solver_path: List[str] = field(default_factory=lambda: [])
    paths: List[str] = field(default_factory=lambda: [])

    def _solve(self, cave: Cave, extended: bool):
        if cave.name == "end":
            self.solver_path.append(cave.name)
            self.paths.append(",".join(self.solver_path))
            self.solver_path.pop()
            return
        
        if extended:
            if not cave.is_large and cave.name in self.solver_path and self.small_cave_visited_twice():
                return
        else:
            if not cave.is_large and cave.name in self.solver_path and cave.name != "start":
                return
        if self.solver_path.count("start") == 1 and cave.name == "start":
            return

        self.solver_path.append(cave.name)

        for c in cave.corridors:
            cd = next((cave for cave in self.caves if cave.name == c), None)
            self._solve(cd, extended)
        self.solver_path.pop()

    def determine_paths(self) -> List[str]:
        start = next((cave for cave in self.caves if cave.name == "start"), None)
        self.paths = []
        self._solve(start, False)
        print(f"Part 1: {len(self.paths)}")
        self.paths = []
        self._solve(start, True)
        print(f"Part 2: {len(self.paths)}")

    def add_caves(self, caves):
        for cave in caves:
            self.caves.append(cave)

    def small_cave_visited_twice(self) -> bool:
        small_caves = [c for c in self.solver_path if c.islower() and len(c) < 3]
        return len(small_caves) != len(set(small_caves))
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

cave_system = determine_cave_system("day12.txt")
cave_system.determine_paths()