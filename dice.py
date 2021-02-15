import pygame as pg

FPS = 60

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

pg.display.update()

WHITE = (255,255,255)
BG_COLOR = (0,0,0)
X_circle = 0


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()