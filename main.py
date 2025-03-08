import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()
game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
#detect the collision with car
    for car in car_manager.cars:
        if player.distance(car) <25:
            game_is_on=False

#detect reach FINISH_LINE
    if player.ycor() >= FINISH_LINE:
        scoreboard.update_scoreboard()
        player.reset_position()
        car_manager.speed_car += 2

screen.exitonclick()