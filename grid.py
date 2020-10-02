from enum import Enum
from colors import Color

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

class Cell(Enum):
    EMPTY = 0
    WALL = 1
    WAYPOINT = 2