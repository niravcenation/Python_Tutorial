from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.score = 0
        self.new_score()

    def new_score(self):
        self.goto(x=0, y=270)
        self.write(f" Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER !!! ☺", align=ALIGNMENT, font=FONT)

    def updated_score(self):
        self.clear()
        self.score += 1
        self.new_score()
