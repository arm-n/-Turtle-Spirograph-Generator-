import turtle
import random


tom = turtle.Turtle()
tom.shape('turtle')
tom.pensize(3)
tom.speed('fast')
turtle.colormode(255)
# tom.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(17)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()