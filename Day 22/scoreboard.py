from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_updated_score(self):
        self.l_score += 1
        self.updated_scoreboard()

    def r_updated_score(self):
        self.r_score += 1
        self.updated_scoreboard()

    def l_winner(self):
        self.goto(0, 0)
        self.write(f"Player 1 is winner", align=ALIGNMENT, font=FONT)

    def r_winner(self):
        self.goto(0, 0)
        self.write(f"Player 2 is winner", align=ALIGNMENT, font=FONT)
