from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,280)
        self.color('white')
        self.penup()
        self.write(f'Score:{self.score} ',move=False,align='center',font=('Arial',24,'normal'))
        self.hideturtle()
    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f'Score:{self.score} ', move=False, align='center', font=('Arial', 24, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', move=False, align='center', font=('Arial', 24, 'normal'))



