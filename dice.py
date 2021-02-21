#импорт pygame и random
import pygame as pg
import random as rnd

#Кадры в секунду
FPS = 60

#Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)

#идентификация окна программы
pg.init()
screen = pg.display.set_mode((140, 140))
clock = pg.time.Clock()

#Класс, определяющий саму кость
class Dice:
#функция init, идентификация
    def __init__(self, x_circle, y_circle, dice, size_circle):
        self.x_circle = x_circle
        self.y_circle = y_circle
        self.size_circle = size_circle
        self.dice = dice
#рисование фигур для кубика, квадрат и круг
    def draw_cube(self):
        pg.draw.rect(screen, WHITE ,(20, 20, 100, 100), 0, 15)
    def draw_circle(self):
        pg.draw.circle(screen, BLACK, (self.x_circle, self.y_circle), self.size_circle)
#создание нового значения кубика
    def change(self, dice):
        self.dice = dice
        print(self.dice)      
#сторона 1
    def side_2(self):
        self.draw_cube()
        pg.draw.circle(screen, BLACK, (45, 45), 10)
        pg.draw.circle(screen, BLACK, (95, 95), 10)
#---------------------------------
    def side_1(self):
        self.draw_cube()
        pg.draw.circle(screen, BLACK, (70, 70), 10)
#---------------------------------
    def side_3(self):
        self.draw_cube()
        self.side_2()
        pg.draw.circle(screen, BLACK, (70, 70), 10)
#---------------------------------
    def side_4(self):
        self.side_2()
        pg.draw.circle(screen, BLACK, (45,95), 10)
        pg.draw.circle(screen, BLACK, (95,45), 10)
#---------------------------------
    def side_5(self):
        self.side_4()
        pg.draw.circle(screen, BLACK, (70,70), 10)
#---------------------------------
    def side_6(self):
        self.side_4()
        pg.draw.circle(screen, BLACK, (45,70), 10)
        pg.draw.circle(screen, BLACK, (95,70), 10)
#---------------------------------
            
            
        
 
# Начальная загрузка
cube = Dice(320, 240, rnd.randint(1, 6), 10)
cube.change(rnd.randint(1, 6))
    
# Бесконечный цикл
while True:
    pg.time.delay(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            FPS = 60
            for x in range(12):
                cube.change(rnd.randint(1, 6))        
                if cube.dice == 1:    
                    cube.side_1()
                elif cube.dice == 2:
                    cube.side_2()
                elif cube.dice == 3:
                    cube.side_3()
                elif cube.dice == 4:
                    cube.side_4()
                elif cube.dice == 5:
                    cube.side_5()
                elif cube.dice == 6:
                    cube.side_6()
                
                pg.time.delay(FPS)
                FPS = FPS+5
                pg.display.update()
                
