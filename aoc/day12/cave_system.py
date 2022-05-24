from dataclasses import dataclass, field
from typing import List
from .cave import Cave


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

    def determine_standard_paths(self) -> List[str]:
        start = next((cave for cave in self.caves if cave.name == "start"), None)
        self.paths = []
        self._solve(start, False)
        return len(self.paths)

    def determine_extended_paths(self):
        start = next((cave for cave in self.caves if cave.name == "start"), None)
        self.paths = []
        self._solve(start, True)
        return len(self.paths)

    def add_caves(self, caves):
        for cave in caves:
            self.caves.append(cave)

    def small_cave_visited_twice(self) -> bool:
        small_caves = [c for c in self.solver_path if c.islower() and len(c) < 3]
        return len(small_caves) != len(set(small_caves))
