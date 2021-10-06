import time
import car_manager
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
chicken = Player()
screen.listen()
screen.onkeypress(chicken.move, "Up")
random_cars = []  # an empty list to store the incoming car objects later on
speed = .07
level = 1
score = Scoreboard(level)

game_is_on = True
while game_is_on:
    score.refresh(level)
    i = 0  # created i to stop the while loop below from running till infinity
    for x in range(5):  # creating cars
        car = CarManager()
        random_cars.append(car)
    car_manager.reset_slots()
    while chicken.in_play_bounds():
        i += 1  # increasing i to make sure this while loop runs only until i = 25
        for x in random_cars[-35:]:
            if x.xcor() < 20 and x.distance(chicken) <= 19:  # collision detection
                game_is_on = False
                score.game_over()
                break
            elif x.xcor() > -330:
                x.move()
            else:
                x.hideturtle()
        if i >= 25:  # if i isn't there, only 5 cars will be created. This is here to make sure more cars are created
            # in the for loop above the while loop
            break
        time.sleep(speed)
        screen.update()
    if not chicken.in_play_bounds():
        chicken.goto((0, -280))
        speed *= .7
        level += 1

screen.exitonclick()
