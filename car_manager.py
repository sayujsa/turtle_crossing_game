import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
slots = [x for x in range(-230, 261, 30)]


def reset_slots():
    global slots
    slots = [x for x in range(-230, 261, 30)]


class CarManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color("white")
        # self.color(random.choice(COLORS))
        slot_choice = random.choice(slots)
        self.goto(random.choice([310, 324, 333, 348, 354, 358, 370]), slot_choice)
        slots.remove(slot_choice)
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

