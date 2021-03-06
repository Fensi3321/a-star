import pygame as pg
import drawing
import grid
from colors import Color

w = 1081
h = 757
cell_size = 56

finished = False

grid = grid.Grid(w, h, cell_size)

def init():
    pg.init()

    pg.display.set_caption("A-star")
    screen = pg.display.set_mode((w, h))

    return screen

def handle_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            selected_cell = drawing.get_grid_pos(event.pos, grid)
            if event.button == 1: # 1 == Left Mouse Button
                grid.grid[selected_cell[1]][selected_cell[0]] = 1
            if event.button == 2: # 2 == Middle Mouse Button
                grid.grid[selected_cell[1]][selected_cell[0]] = 0
            if event.button == 3: # 3 == Right Mouse Button
                grid.grid[selected_cell[1]][selected_cell[0]] = 2


    pg.display.update()

def main():
    screen = init()

    while not finished:
        handle_events()
        drawing.draw_board(screen, Color.BACKGROUND, grid)

        print("Grid")
        grid.print()


    pg.quit()

if  __name__ == "__main__":
    main()

'''
    ###    grid representation   ###
    0 - empty cell
    1 - wall
    2 - waypoint
'''