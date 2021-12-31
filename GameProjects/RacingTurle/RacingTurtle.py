from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600,height= 600)
user_bet = screen.textinput(title="Make a bet", prompt="Which turle would you like to choose? ")
color_list = ["red", "blue", "yellow", "orange", "purple", "black"]
y_position = [-250,-150,-50,50,150,250]
turtle_list = []

for i in range(len(color_list)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_position[i])
    turtle_list.append(new_turtle)

stop = False
while not stop:
    for turles_ in turtle_list:
    
        turles_.forward(random.randint(0,10))
        
        if turles_.xcor() > 280:

            if turles_.pencolor() == user_bet:
                print("you win")
            else:
                print(f"you lose, the winner turle is {turles_.pencolor()}")
            stop = True

screen.exitonclick()