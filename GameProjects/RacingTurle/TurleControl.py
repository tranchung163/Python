from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

    

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(turn_left, "a")
screen.onkey(clear, "l")

screen.exitonclick()