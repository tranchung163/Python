import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Crossing Tutrle')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()


screen.listen()
screen.onkey(player.move_up, 'Up')


game_is_on = True
speed = 0.5
while game_is_on:
    cars.add_car()

    for each_car in cars.cars_list:
        each_car.forward(30)
        
    time.sleep(speed)
    screen.update()
    for each_car in cars.cars_list:
        if each_car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        speed *= 0.5
        player.goto(STARTING_POSITION)
        scoreboard.score += 1
        scoreboard.update_scoreboard()


screen.exitonclick()