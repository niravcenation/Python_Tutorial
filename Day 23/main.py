import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

plr = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(plr.go_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars.move_speed)
    cars.create_car()
    cars.move_cars()
    screen.update()

    # Car detection with turtle
    for car in cars.all_cars:
        if car.distance(plr) < 25:
            score.game_over()
            game_is_on = False

    # Turtle has reached to finish line
    if plr.is_at_finish_line():
        cars.increase_move_speed()
        plr.go_to_start_line()
        score.update_level()


screen.exitonclick()
