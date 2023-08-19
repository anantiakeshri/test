import turtle as t
import random

kachua = t.Turtle()
t.colormode(255)
kachua.speed(0)
screen = t.Screen()
screen.bgcolor("white") 

color_list = [(237, 245, 240), (208, 151, 98), (49, 94, 138), (210, 83, 65), (231, 217, 91), (147, 68, 91), 
              (155, 75, 62), (23, 27, 40), (39, 22, 29), (38, 19, 15), (190, 141, 160), (204, 73, 90), (42, 130, 92), 
              (126, 178, 142), (79, 162, 98), (15, 30, 21), (227, 170, 183), (50, 56, 100), (96, 45, 65), (123, 167, 193),
              (40, 162, 192), (231, 173, 164), (104, 45, 40), (227, 217, 19), (164, 208, 187), (153, 207, 220), 
              (101, 127, 163), (35, 80, 49), (182, 188, 209), (84, 65, 31), (18, 78, 104)]


def paint():
    for _ in range(10):
        for _ in range(10):
            kachua.penup()
            kachua.hideturtle()
            kachua.color(random.choice(color_list))
            kachua.dot(20)
            kachua.forward(50)
        kachua.backward(500)
        kachua.left(90)
        kachua.forward(50)
        kachua.right(90)

paint()

screen.exitonclick()

# Code by Anantia Keshri