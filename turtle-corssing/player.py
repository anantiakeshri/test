from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_pos()
        # self.setheading(90)
        self.move()
       
    def starting_pos(self):
        self.goto(STARTING_POSITION)
       
        
    def move(self): 
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
        
    def finishing_line(self):
        # self.goto(0, FINISH_LINE_Y)
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False