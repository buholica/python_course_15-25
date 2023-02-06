import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collision with the top edge of the screen
    if player.ycor() > 270:
        player.reset_position()
        cars.increase_speed()
        scoreboard.increase_score()

    # Detect collision with a car
    for car in cars.all_cars:
        if player.distance(car) < 35:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
