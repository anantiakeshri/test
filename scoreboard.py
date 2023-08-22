from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Times New Roman', 14, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score - {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align = ALIGNMENT, font = FONT)
        
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score - {self.score}", align = ALIGNMENT, font = FONT)