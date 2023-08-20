# Etch a sketch game by Anantia Keshri
"""This game is for drawing a sketch using Turtle
    W to move forward
    A to turn left
    S to move backwards
    D to move right
    C to clear screen
    and W + A to make curves"""
    
from turtle import Turtle, Screen

kachua = Turtle()
my_screen = Screen()
kachua.speed(10)

def move_forward():
    kachua.forward(20)
    
def move_backward():
    kachua.backward(20)
    
def counter_clockwise():
    kachua.left(10)

def clockwise():
    kachua.right(10)
    
def clear_screen():
    kachua.clear()
    kachua.penup()
    kachua.home()
    kachua.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=counter_clockwise)
my_screen.onkey(key="d", fun=clockwise)
my_screen.onkey(key="c", fun=clear_screen)



my_screen.exitonclick()