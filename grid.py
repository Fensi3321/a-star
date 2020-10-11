from enum import Enum
from colors import Color

class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.width //= self.cell_size
        self.height //= self.cell_size

        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print(self):
        for x in self.grid:
            print(x)


class Cell(Enum):
    EMPTY       = 0
    WALL        = 1
    WAYPOINT    = 2
