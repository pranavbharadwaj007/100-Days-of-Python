import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
manager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:

    scoreboard.refresh()
    manager.update()

    # Check player win
    if player.ycor() > player.y_win:

        player.reset()
        scoreboard.level += 1
        manager.next_level()

    # Check car collision
    for car in manager.cars:

        if player.distance(car) < 20:

            scoreboard.game_over()
            game_is_on = False


    screen.update()
    time.sleep(0.1)

screen.exitonclick()