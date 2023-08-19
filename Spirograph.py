import turtle as t
import random

chadarmod = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

chadarmod.speed(0)

""" Main Spirograph which I wanted to create. """
def draw_spirograph(size_of_angle):
    for _ in range(int(360 / size_of_angle)):
        chadarmod.color(random_color())
        chadarmod.circle(100)
        chadarmod.setheading(chadarmod.heading() + size_of_angle)

draw_spirograph(5)

# """A semicircle formed inside a circle - creating a spirograph type 1"""
# for _ in range(50):
#     chadarmod.color(random_color())
#     chadarmod.circle(100)
#     chadarmod.setheading(chadarmod.heading() + 100)


# """A spirograph type 2"""
# for _ in range(100):
#     chadarmod.color(random_color())
#     chadarmod.circle(100)
#     chadarmod.forward(10)
#     chadarmod.left(10)

# """Spriograph type 3"""
# for _ in range(100):
#     chadarmod.color(random_color())
#     chadarmod.circle(100)
#     chadarmod.forward(100)
#     chadarmod.left(100)

# """ Spirograph 4 """
# for _ in range(100):
#     chadarmod.color(random_color())
#     chadarmod.circle(100)
#     chadarmod.forward(100)
#     chadarmod.left(30)


screen = t.Screen()
screen.exitonclick()
