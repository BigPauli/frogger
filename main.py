from turtle import Turtle, Screen
from frogger import Frogger
from car import Car
from scoreboard import Scoreboard
import time
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

frogger = Frogger()


scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(frogger.jump, 'Up')
screen.onkey(frogger.jump_back, 'Down')
all_cars = []

while game_on:
    time.sleep(0.1)
    screen.update()

    if randint(1, 4) == 1:
        new_car = Car(scoreboard.level)
        all_cars.append(new_car)
    for cars in all_cars:
        cars.drive()
        if cars.xcor() < -320:
            cars.clear()
            cars.off_screen()

    for car in all_cars:
        if frogger.distance(car) < 20 and car.xcor() in range(-20, 20):
            scoreboard.game_over()
            game_on = False

    if frogger.ycor() >= 250:
        frogger.go_home()
        scoreboard.increase_level()
        for car in all_cars:
            car.speed_up()












screen.exitonclick()