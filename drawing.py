import pygame
import grid
from colors import Color

def draw_board(surface: pygame.Surface, color: Color, grid):
    surface.fill(color.value)
    draw_grid(surface, grid)

    draw_square(surface, get_grid_snapped_mouse_pos(pygame.mouse.get_pos(), grid), Color.CURSOR, grid)

    xlen = len(grid.grid)
    ylen = len(grid.grid[0])

    for x in range(xlen):
        for y in range(ylen):
            if grid.grid[x][y] == 1:
                draw_square(surface, (y * grid.cell_size, x * grid.cell_size), Color.WALL, grid)



def draw_grid(surface: pygame.Surface, grid):
    # magic numbers are cool        
    for x in range(0, 1081, grid.cell_size):
        pygame.draw.line(surface, Color.LINE.value, (x, 0), (x, grid.height * grid.cell_size), 1)
        for y in range(0, 757, grid.cell_size):
           pygame.draw.line(surface, Color.LINE.value, (0, y), (grid.width * grid.cell_size, y), 1)


def draw_square(surface: pygame.Surface, pos: tuple, color, grid):
    pygame.draw.rect(surface, color.value, pygame.Rect(pos, (grid.cell_size, grid.cell_size)))


def get_grid_snapped_mouse_pos(pos, grid):
    square_center = (pos[0] - (grid.cell_size // 2), pos[1] - grid.cell_size // 2)
    
    squareX = round(square_center[0] / grid.cell_size) * grid.cell_size
    squareY = round(square_center[1] / grid.cell_size) * grid.cell_size

    snapped = (squareX, squareY)

    return snapped


def get_grid_pos(pos, grid):
    temp = get_grid_snapped_mouse_pos(pos, grid)

    return (temp[0] // grid.cell_size, temp[1] // grid.cell_size)
