# The famous Snake Game. Code by Anantia Keshri
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The famous Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

""" 3 - Control of Snake"""
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

is_game_on = True
""" 2 - Move the snake """
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()    
    
    """ Detect collision with food """
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.increase_score()
     
    """ Detect collision with wall """   
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        
    """Detect collision with tail"""
    for segment in snake.segments:
        #if head collides with any segment in the tail then GAME OVER
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()