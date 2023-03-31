from turtle import Turtle


class Frogger(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.setpos(0, -275)

    def jump(self):
        self.setheading(90)
        self.forward(15)

    def jump_back(self):
        self.setheading(270)
        self.forward(15)

    def go_home(self):
        self.goto(0, -275)
