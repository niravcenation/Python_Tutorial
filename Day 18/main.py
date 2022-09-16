import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
popti_the_turtle = Turtle()
turtle.colormode(255)
popti_the_turtle.shape("turtle")
popti_the_turtle.color("green")

'''
#draw a square
for i in range(4):
    popti_the_turtle.right(90)
    popti_the_turtle.forward(100)
'''

'''
# draw dashed line
for i in range(15):
    popti_the_turtle.pendown()
    popti_the_turtle.forward(10)
    popti_the_turtle.penup()
    popti_the_turtle.forward(10)
'''

'''
#draw shapes : triangle, square, pentagon, hexagon, heptagon, octagone, nonagone, decagon
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
popti_the_turtle.hideturtle()
for shapes in range(3,11):
    popti_the_turtle.color(random.choice(colours))
    for i in range(shapes):
        popti_the_turtle.forward(100)
        popti_the_turtle.right(360/shapes)
'''

# random walk
direction = [0, 90, 180, 270]
popti_the_turtle.hideturtle()
popti_the_turtle.speed("fastest")
popti_the_turtle.pensize(10)
for i in range(200):
    popti_the_turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    popti_the_turtle.setheading(random.choice(direction))
    popti_the_turtle.forward(30)

screen.exitonclick()
