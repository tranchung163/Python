from turtle import Turtle
ALIGNTMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file='new_file.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}     Max Score: {self.high_score}', align = ALIGNTMENT, font = FONT )
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='new_file.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align = 'center', font = ("Arial", 50, 'normal'))

