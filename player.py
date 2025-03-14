from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.reset_position()

    def move(self):
        x = self.xcor()
        y= self.ycor() + MOVE_DISTANCE
        self.goto(x, y)

    def reset_position(self):
        self.goto(STARTING_POSITION)