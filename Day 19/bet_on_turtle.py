import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtle_y_axis = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []
is_true = False

for turtle_index in range(0, 7):
    pointer = Turtle()
    pointer.shape("turtle")
    pointer.color(turtle_colors[turtle_index])
    pointer.penup()
    pointer.goto(x=-230, y=turtle_y_axis[turtle_index])
    all_turtles.append(pointer)

if user_bet:
    is_true = True

while is_true:
    for turtle_no in all_turtles:
        if turtle_no.xcor() > 230:
            is_true = False
            winning_color = turtle_no.pencolor()
            if winning_color == user_bet:
                print(f"You have won the bet. The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost the bet. The {winning_color} turtle is the winner.")
            break
        random_distance = random.randint(0, 10)
        turtle_no.forward(random_distance)

# screen.exitonclick()
