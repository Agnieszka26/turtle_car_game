from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(x=-250, y=250)
        self.color("black")
        self.write(f"Level: {self.level}", font = FONT, align="left")


