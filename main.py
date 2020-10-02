import pygame as pg
import drawing
from colors import Color

w = 1081
h = 757

finished = False

def init():
    pg.init()
    pg.display.set_caption("A-star")

    screen = pg.display.set_mode((w, h))

    return screen

def handle_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.display.update()

def main():
    screen = init()
    drawing.draw_board(screen, (10,10), Color.BACKGROUND)

    while not finished:
        handle_events()

    pg.quit()

if  __name__ == "__main__":
    main()

'''
    ###    grid representation   ###
    0 - empty cell
    1 - wall
    2 - waypoint
'''