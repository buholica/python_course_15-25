import colorgram
from turtle import Turtle, Screen
import random

# Extracting colors from the picture
colors = colorgram.extract("image.jpg", 20)
color_palette = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.width(16)
timmy.speed("fastest")

# Changing the turtle's position to start drawing
timmy.up()
timmy.backward(300)
timmy.right(90)
timmy.forward(150)
timmy.left(90)


# Creating a row
def rows():
    for _ in range(10):
        timmy.penup()
        timmy.forward(30)
        timmy.pencolor(random.choice(color_palette))
        timmy.pendown()
        timmy.forward(0.4)
        timmy.penup()
        timmy.forward(30)
        timmy.pencolor(random.choice(color_palette))
        timmy.pendown()


# Creating columns
for _ in range(5):
    rows()
    timmy.left(90)
    timmy.up()
    timmy.forward(30)
    timmy.left(90)
    rows()
    timmy.right(90)
    timmy.up()
    timmy.forward(30)
    timmy.right(90)


screen.exitonclick()