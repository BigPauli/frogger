from turtle import Turtle
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.level = 1
        self.write(f'Current Level: {self.level}', align=ALIGNMENT, font=('Courier', 20, 'bold'))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f'Current Level: {self.level}', align=ALIGNMENT, font=('Courier', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=('Courier', 30, 'bold'))

