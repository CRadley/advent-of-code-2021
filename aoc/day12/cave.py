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
