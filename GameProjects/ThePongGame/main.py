from turtle import Turtle, Screen, clearscreen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import ScoreBoard

LEFT = -380
RIGHT = 370


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG GAME')
screen.tracer(0)

paddles = Paddle(LEFT)
paddles2 = Paddle(RIGHT)
ball = Ball()


screen.listen()
screen.onkey(paddles.move_up, "w")
screen.onkey(paddles.move_down, "s")
screen.onkey(paddles2.move_up, "Up")
screen.onkey(paddles2.move_down, "Down")
scoreboard = ScoreBoard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bound_y()

    elif ball.distance(paddles2) < 55 and ball.xcor() > 350:
        ball.bound_x()

    elif ball.distance(paddles) < 55 and ball.xcor() < -350:
        ball.bound_x()
        

    elif ball.xcor() > 390:
        time.sleep(1)
        ball.reset()
        scoreboard.r_missed()
        scoreboard.update()
        


    elif ball.xcor() < -390:
         time.sleep(1)
         ball.reset()
         scoreboard.l_missed()
         scoreboard.update()

screen.exitonclick()