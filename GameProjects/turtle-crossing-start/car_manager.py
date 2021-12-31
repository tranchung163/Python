from turtle import Turtle 
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list =[]
        self.add_car()
        self.level = 0

    def move_forward(self):
        self.forward(STARTING_MOVE_DISTANCE)
        
    def add_car(self):
        random_chane = random.randint(1,2)
        if random_chane == 1:
            new_car = Turtle(shape='square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.penup()
            new_car_y = random.randint(-250,250)
            new_car.goto(280, new_car_y)
            new_car.setheading(180)
            self.cars_list.append(new_car)

    def level_up(self):
        pass

