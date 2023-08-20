import turtle as t
import random

kachua = t.Turtle()
t.colormode(255)
kachua.speed("fastest")
kachua.penup()
kachua.hideturtle()
screen = t.Screen()
screen.bgcolor("white") 

color_list = [(237, 245, 240), (208, 151, 98), (49, 94, 138), (210, 83, 65), (231, 217, 91), (147, 68, 91), 
              (155, 75, 62), (23, 27, 40), (39, 22, 29), (38, 19, 15), (190, 141, 160), (204, 73, 90), (42, 130, 92), 
              (126, 178, 142), (79, 162, 98), (15, 30, 21), (227, 170, 183), (50, 56, 100), (96, 45, 65), (123, 167, 193),
              (40, 162, 192), (231, 173, 164), (104, 45, 40), (227, 217, 19), (164, 208, 187), (153, 207, 220), 
              (101, 127, 163), (35, 80, 49), (182, 188, 209), (84, 65, 31), (18, 78, 104)]
 
# this 3 line of code for setting heading for turtle so that it starts from a nice place
kachua.setheading(225)
kachua.forward(300)
kachua.setheading(0)

num_of_dots = 101

for dot_count in range(1, num_of_dots):
    kachua.dot(20, random.choice(color_list))
    kachua.forward(50)
    if dot_count % 10 == 0:
        kachua.setheading(90)
        kachua.forward(50)
        kachua.setheading(180)
        kachua.forward(500)
        kachua.setheading(0)

screen.exitonclick()

#Code with help of Miss YU. 