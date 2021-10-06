import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def in_play_bounds(self):
        if self.ycor() <= FINISH_LINE_Y:
            return True
        else:
            return False

    def move(self):
        self.forward(20)
