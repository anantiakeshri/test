import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    """ Detect collision with the car_manager """
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    """ Detect when turtle reaches other sides"""
    if player.finishing_line():
        player.starting_pos()
        car_manager.level_up()
        """ Updating the level"""
        scoreboard.game_up()

screen.exitonclick()

# Code from scratch by Anantia Keshri