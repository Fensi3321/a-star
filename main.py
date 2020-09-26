import pygame as pg

w = 1080
h = 720

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

def draw_grid(surface: pg.Surface):
    surface.fill((16,16,16))

    for x in range(0, w, 54):
        pg.draw.line(surface, (64,64,64), (x, 0), (x, h), 1)
        for y in range(0, h, 54):
            pg.draw.line(surface, (64,64,64), (0, y), (w, y), 1)

    pg.display.update()

def main():
    screen = init()

    while not finished:
        handle_events()
        draw_grid(screen)

    pg.quit()

if  __name__ == "__main__":
    main()

'''
    ###    grid representation   ###
    0 - empty cell
    1 - wall
    2 - waypoint
'''