import pygame
import grid
from colors import Color

cell_size = 108
grid = grid.Grid(1081 // cell_size, 757 // cell_size)

def draw_board(surface: pygame.Surface, size: tuple, color: Color):
    surface.fill(color.value)
    draw_grid(surface)

def draw_grid(surface: pygame.Surface):
    # magic numbers are cool        
    for x in range(0, 1081, cell_size):
        pygame.draw.line(surface, Color.LINE.value, (x, 0), (x, grid.height * cell_size), 1)
        for y in range(0, 757, cell_size):
           pygame.draw.line(surface, Color.LINE.value, (0, y), (grid.width * cell_size, y), 1)