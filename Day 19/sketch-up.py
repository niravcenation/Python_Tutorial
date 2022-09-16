from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()
pointer.speed("fastest")


def move_forwards():
    pointer.forward(10)


def move_backwards():
    pointer.backward(10)


def move_right():
    pointer.setheading(pointer.heading() - 10)


def move_left():
    pointer.setheading(pointer.heading() + 10)


def clear_screen():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()
