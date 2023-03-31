from turtle import Turtle
from random import randint


class Car(Turtle):
    def __init__(self, current_level):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.penup()
        self.goto(320, randint(-250, 250))
        self.setheading(180)
        self.mph = 10 + 2*current_level
        self.dead = False

    def drive(self):
        self.forward(self.mph)

    def speed_up(self):
        if not self.dead:
            self.mph += 2

    def off_screen(self):
        self.mph = 0
        self.dead = True

