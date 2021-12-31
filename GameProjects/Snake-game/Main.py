from turtle import Screen
import time
from Snake import Snake
from food import Food
from Scoreboard import ScoreBoard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake1 = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake1.move_down, 'Down')
screen.onkey(snake1.move_up, 'Up')
screen.onkey(snake1.move_right, 'Right')
screen.onkey(snake1.move_left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move_forward()

    #Detect collison with food
    if snake1.head.distance(food) < 15:
        food.refresh()
        snake1.extend_snake()
        scoreboard.increase_score()



    #Detect collison with wall
    if snake1.head.xcor() > 290 or snake1.head.xcor() < -300 or snake1.head.ycor() > 300 or snake1.head.ycor() < -290:
        snake1.reset()
        scoreboard.reset()

    #Detect cllison with tails
    
    for segment in snake1.segments[1:]:

        if snake1.head.distance(segment) < 6:
            scoreboard.reset()
        
    
screen.exitonclick()