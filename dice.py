import pygame as pg
import Colors as clr
import random as rnd

FPS = 60

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

class Dice:
#---------------------------------
    def __init__(self, x_circle, y_circle, dice, size_circle):
        self.x_circle = x_circle
        self.y_circle = y_circle
        self.size_circle = size_circle
        self.dice = dice
#---------------------------------
    def draw_cube(self):
        pg.draw.rect(screen, clr.WHITE ,(20, 20, 100, 100))
    def draw_circle(self):
        pg.draw.circle(screen, clr.BLACK, (self.x_circle, self.y_circle), self.size_circle)
#---------------------------------
    def change(self, dice):
        self.dice = dice
        print(self.dice)      
#---------------------------------
    def change_number(self, x, y, size):
        self.draw_cube()
        self.x_circle = x
        self.y_circle = y
        self.size_circle = size
        self.draw_circle()
 
# Начальная загрузка
cube = Dice(320, 240, rnd.randint(1, 6), 10)
cube.change(rnd.randint(1, 6))


# Бесконечный цикл
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            cube.change(rnd.randint(1, 6))

    if cube.dice == 1:
        cube.draw_cube()
        cube.change_number(70,70,10)
    elif cube.dice == 2:
        cube.draw_cube()
        cube.change_number(95,95,10)
        cube.change_number(45,45,10)
    elif cube.dice == 3:
        cube.draw_cube()
        cube.change_number(45,45,10)
        cube.change_number(70,70,10)
        cube.change_number(95,95,10)
    else:
        pass
        
    pg.display.update()
