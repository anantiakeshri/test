# The famous Snake Game. Code by Anantia Keshri
from turtle import Screen
from Snake_game.snake import Snake
from Snake_game.food import Food
from Snake_game.scoreboard import Scoreboard
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
        is_game_on = False
        score.game_over()
        
    """Detect collision with tail"""
    for segment in snake.segments[1:]:
    #if head collides with any segment in the tail then GAME OVER
        if snake.head.distance < 10:
            is_game_on = False
            score.game_over() 
    

    

screen.exitonclick()