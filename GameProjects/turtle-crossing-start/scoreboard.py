from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-290,260)
        self.write(f'Game Level: 0', align='left', font=FONT)
        self.score = 0

    def game_over(self):
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-90,0)
        self.write(f'GAME OVER', align='left', font=("Courier", 40, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.color('black')
        self.penup()
        self.goto(-290,260)
        self.write(f'Game Level: {self.score}', align='left', font=FONT)

