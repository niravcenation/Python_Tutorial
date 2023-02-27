from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.updated_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over 😔", align="center", font=FONT)
