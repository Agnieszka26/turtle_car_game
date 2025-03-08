from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(x=-250, y=250)
        self.write(f"Level: {self.level}", font = FONT, align="left")

    def handle_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align="center")
