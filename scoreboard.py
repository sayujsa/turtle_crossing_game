import turtle
FONT = ("arial", 18, "bold")


class Scoreboard(turtle.Turtle):

    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"LEVEL : {level}", font=FONT)

    def refresh(self, level):
        self.clear()
        self.write(f"LEVEL : {level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 28, "bold"))