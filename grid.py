from enum import Enum
from colors import Color

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def print(self):
        for x in self.grid:
            print(x)

class Cell(Enum):
    EMPTY = 0
    WALL = 1
    WAYPOINT = 2
