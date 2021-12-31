import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors = colorgram.extract('image.jpg',30)
rgb_colors = []

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    color_choose = (r,g,b)
    rgb_colors.append(color_choose)

rgb_colors.pop(0)
rgb_colors.pop(0)
rgb_colors.pop(0)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for dots in range(1, number_of_dot+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
