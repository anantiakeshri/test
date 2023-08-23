from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.clear()
        self.goto(-270, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", False, align="left", font = FONT)
        
        
    def game_up(self):
        self.level += 1
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align="center", font = FONT)