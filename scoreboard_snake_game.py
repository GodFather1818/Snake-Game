from turtle import *
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        with open('snake_data.txt', mode='r') as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} HIGH SCORE : {self.highscore}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('snake_data.txt', mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

