import turtle as t
import random

t.colormode(255)
screen = t.Screen()
pointer = t.Turtle()


# other_pointer = t.Turtle()
def draw_graph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        pointer.hideturtle()
        pointer.speed("fastest")
        pointer.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pointer.circle(100)
        pointer.setheading(pointer.heading() + size_of_gap)


draw_graph(20)
screen.exitonclick()
