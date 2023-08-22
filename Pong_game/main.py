# Pong game from scratch by Anantia Keshri
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    """ Detect collision with the wall """
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    """ Detect collision with the paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_back()
    
    """ If R paddle misses the ball"""
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    """ If L paddle misses the ball"""
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        
screen.exitonclick()