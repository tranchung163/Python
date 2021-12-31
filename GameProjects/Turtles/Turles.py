import turtle
import random

color_list = ["white", "yellow", "blue", "deep sky blue", "sky blue", "sea green", "peru", "orange"]
angle_list = [0,90,180,270,360]
window = turtle.Screen()
turtle.colormode(255)
geoff = turtle.Turtle()

# geoff.shape("turtle")
# geoff.color("red")
# geoff.pensize(15)
# geoff.speed("fastest")

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_colors = (r,b,g)
    return random_colors

def draw(side):
    degree = 360/side
    for _ in range(side):
        geoff.forward(80)
        geoff.left(degree)

def draw_wall():
    degree = random.choice(angle_list)
    color = random.choice(color_list)
    geoff.color(color)
    geoff.left(degree)
    geoff.forward(30)


geoff.speed("fastest")

def draw_spinograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        geoff.color(random_color())
        geoff.circle(100)
        geoff.setheading(geoff.heading() + size_of_gap)
        
draw_spinograph(10)
window.exitonclick()

