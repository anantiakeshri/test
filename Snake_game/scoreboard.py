from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Times New Roman', 14, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("c:/Users/anant/OneDrive/Desktop/Mini Games/Snake_game/data.txt") as data:
            self.highscore = int(data.read().strip()) 
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align = ALIGNMENT, font = FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("c:/Users/anant/OneDrive/Desktop/Mini Games/Snake_game/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()